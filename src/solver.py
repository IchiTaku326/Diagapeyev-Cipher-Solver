"""
Diagapeyev Cipher Solver
This script performs decryption of the Diagapeyev Cipher using a 6x6 
Straddling Checkerboard system.
"""

def decrypt_diagapeyev(cipher_text, key1=30, key2=40):
    # Flatten the text and convert to pairs
    raw_digits = "".join(cipher_text.strip().split())
    pairs = [int(raw_digits[i:i+2]) for i in range(0, len(raw_digits) - 1, 2)]
    
    # Perform decryption by subtracting keys (Cycle of 2)
    decrypted_nums = []
    for i, x in enumerate(pairs):
        k = key1 if i % 2 == 0 else key2
        decrypted_nums.append(x - k)
    return decrypted_nums

def to_keypad_text(decrypted_nums):
    # Pattern B: Convert to keypad-like letters (Toggle/Flick input style)
    keypad = {
        2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ"
    }
    result = []
    for num in decrypted_nums:
        button = num // 10
        times = num % 10
        if button in keypad:
            letters = keypad[button]
            idx = (times - 1) % len(letters)
            result.append(letters[idx])
        else:
            result.append(f"[{num}]")
    return "".join(result)

if __name__ == "__main__":
    # Target ciphertext for analysis
    cipher_text = """
    75628 28591 62916 48164 91748 58464 74748 28483 81638 18174
    74826 26475 83828 49175 74658 37575 75936 36565 81638 17585
    75756 46282 92857 46382 75748 38165 81848 56485 64858 56382
    72628 36281 81728 16463 75828 16483 63828 58163 63630 47481
    91918 46385 84656 48565 62946 26285 91859 17491 72756 46575
    71658 36264 74818 28462 82649 18193 65626 48484 91838 57491
    81657 27483 83858 28364 62726 26562 83759 27263 82827 27283
    82858 47582 81837 28462 82837 58164 75748 58162 92000
    """

    # Run decryption
    nums = decrypt_diagapeyev(cipher_text)
    
    print("=== Decryption Process Started ===")
    print(f"Decrypted Numbers (First 20): {nums[:20]}...")
    
    # Output the result
    decrypted_text = to_keypad_text(nums)
    print("\n=== Decrypted Text (Keypad Pattern) ===")
    print(decrypted_text)
