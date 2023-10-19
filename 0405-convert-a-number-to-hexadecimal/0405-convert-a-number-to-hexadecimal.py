class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            # Convert the two's complement representation
            num &= 0xFFFFFFFF  # Ensure 32-bit representation
        hex_str = ""
        while num > 0:
            hex_digit = num % 16
            if hex_digit < 10:
                hex_str = str(hex_digit) + hex_str
            else:
                hex_str = chr(ord('a') + hex_digit - 10) + hex_str
            num //= 16
        return "0" if hex_str == "" else hex_str
