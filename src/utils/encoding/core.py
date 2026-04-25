def convert_from_10_base(number: int, new_base: int) -> list[int]:
    divisor = new_base
    res = []
    current = number
    while True:
        quotient = current//divisor
        if quotient == 0:
            res.append(current)
            break

        res.append(current%divisor)
        current = quotient

    return res[::-1]