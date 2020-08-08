def time_converter(time):
    h = int(time[:2])
    m = time[3:]
    apm = 'p.m.'
    if h < 12:
        apm = 'a.m.'
        if h < 10:
            h = int(time[1:2])
        else:
            h = int(time[:2])
        return f'{h}:{m} {apm}'
    return f'{h - 12 if h!= 12 else 12}:{m} {apm}'

if __name__ == '__main__':
    print("Example:")
    print(time_converter('00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")