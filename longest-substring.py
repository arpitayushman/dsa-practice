def longest_substring(s: str) -> str:
    if not s:
        return ""
    left = 0
    max_len = 0
    start = 0
    char_map = {}
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            start = left
    return s[start:start+max_len]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abcabcbb", "abc"),
        ("bbbbb", "b"),
        ("pwwkew", "wke"),
        ("", ""),
        ("a", "a"),
        ("ab", "ab"),
        ("aab", "ab"),
        ("dvdf", "vdf"),
        ("tmmzuxt", "mzuxt"),
    ]
    
    for i, (input_str, expected) in enumerate(test_cases):
        result = longest_substring(input_str)
        print(f"Test {i+1}: longest_substring('{input_str}') = '{result}'")
        assert result == expected, f"Expected '{expected}', got '{result}'"
        print(f"✓ Passed")
    
    print("\nAll tests passed!")