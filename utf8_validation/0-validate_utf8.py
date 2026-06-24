#!/usr/bin/python3
"""UTF-8 validation - determine if data is valid UTF-8 encoding."""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else False."""
    byte_count = 0

    for num in data:
        if num < 0 or num > 255:
            return False

        if byte_count == 0:
            if num >> 7 == 0:
                continue
            elif num >> 5 == 0b110:
                byte_count = 1
            elif num >> 4 == 0b1110:
                byte_count = 2
            elif num >> 3 == 0b11110:
                byte_count = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            byte_count -= 1

    return byte_count == 0
