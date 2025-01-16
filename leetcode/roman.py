
def romanToInt(s: str) -> int:
    count = 0
    last: str = ''

    for letter in s:
        match letter:
            case 'I':
                count += 1
            case 'V':
                if last == 'I':
                    count += 3
                else:
                    count += 5
            case 'X':
                if last == 'I':
                    count += 8
                else:
                    count += 10
            case 'L':
                if last == 'X':
                    count += 30
                else:
                    count += 50
            case 'C':
                if last == 'X':
                    count += 80
                else:
                    count += 100
            case 'D':
                if last == 'C':
                    count += 300
                else:
                    count += 500
            case 'M':
                if last == 'C':
                    count += 800
                else:
                    count += 1000
            case _: 
                print("crap")
        last = letter
    return count

print(romanToInt("MMMDCCXXIV"))