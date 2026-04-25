from .core import convert_from_10_base

def generate_encoding_map() -> dict:
    encoding_map = {}
    nums = [i for i in range(10)]
    upper_case = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    lower_case = [chr(i) for i in range(ord("a"), ord("z") + 1)]

    characters = nums +  lower_case + upper_case

    for i, v in enumerate(characters):
        encoding_map[i] = str(v)

    return encoding_map

def generate_coding_maps() -> tuple[dict, dict]:
    encoding_map = {}
    decoding_map = {}
    nums = [i for i in range(10)]
    upper_case = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    lower_case = [chr(i) for i in range(ord("a"), ord("z") + 1)]

    characters = nums +  lower_case + upper_case

    for i, v in enumerate(characters):
        encoding_map[i] = str(v)
        decoding_map[str(v)] = i

    return encoding_map, decoding_map

ENCODING_MAP, DECODING_MAP = generate_coding_maps()
BASE = 62

def encode(number: int) -> str:
    encoded_value = ""
    converted_digits=convert_from_10_base(number, BASE)
    for digit in converted_digits:
        encoded_value += ENCODING_MAP.get(digit)

    return encoded_value

def decode(encoded_value: str) -> int:
    decoded_value = 0
    place = len(encoded_value) - 1
    for i, encoded_digit in enumerate(encoded_value):
        decoded_value += DECODING_MAP.get(encoded_digit) * BASE**(place - i)

    return decoded_value
