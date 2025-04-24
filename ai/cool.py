import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense
import numpy as np

# Parameters
alphabet = 'abcdefghijklmnopqrstuvwxyz'
char_to_idx = {char: idx for idx, char in enumerate(alphabet)}
idx_to_char = {idx: char for char, idx in char_to_idx.items()}
vocab_size = len(alphabet)
max_len = 10  # Maximum length of cipher strings

# Helper Functions
def generate_data(num_samples=10000):
    """Generate synthetic cipher data."""
    inputs, targets = [], []
    for _ in range(num_samples):
        plain = ''.join(np.random.choice(list(alphabet), size=max_len))
        shuffled = ''.join(np.random.permutation(list(plain)))
        inputs.append(shuffled)
        targets.append(plain)
    return inputs, targets

def encode_data(data, max_len):
    """Convert strings to one-hot encoded tensors."""
    encoded = np.zeros((len(data), max_len, vocab_size), dtype='float32')
    for i, seq in enumerate(data):
        for t, char in enumerate(seq):
            encoded[i, t, char_to_idx[char]] = 1
    return encoded

# Generate Data
num_samples = 20000
inputs, targets = generate_data(num_samples)
input_data = encode_data(inputs, max_len)
target_data = encode_data(targets, max_len)

# Model Architecture
encoder_inputs = Input(shape=(max_len, vocab_size))
encoder = LSTM(128, return_state=True)
encoder_outputs, state_h, state_c = encoder(encoder_inputs)
encoder_states = [state_h, state_c]

decoder_inputs = Input(shape=(max_len, vocab_size))
decoder_lstm = LSTM(128, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = Dense(vocab_size, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Define the Model
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Training
decoder_input_data = np.zeros_like(input_data)  # Shifted inputs for teacher forcing
for i in range(num_samples):
    decoder_input_data[i, 1:] = target_data[i, :-1]

epochs = 10
batch_size = 64
model.fit([input_data, decoder_input_data], target_data, batch_size=batch_size, epochs=epochs, validation_split=0.2)

# Testing
def decode_sequence(input_seq):
    """Decode a cipher sequence."""
    states_value = encoder.predict(input_seq)
    target_seq = np.zeros((1, 1, vocab_size))
    decoded_sentence = ''

    for _ in range(max_len):
        output_tokens, h, c = decoder_lstm.predict([target_seq] + states_value)
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = idx_to_char[sampled_token_index]
        decoded_sentence += sampled_char

        target_seq = np.zeros((1, 1, vocab_size))
        target_seq[0, 0, sampled_token_index] = 1
        states_value = [h, c]

    return decoded_sentence

# Example
sample_input = inputs[0]
encoded_input = encode_data([sample_input], max_len)
predicted_output = decode_sequence(encoded_input)

print(f"Cipher: {sample_input}")
print(f"Decoded: {predicted_output}")
