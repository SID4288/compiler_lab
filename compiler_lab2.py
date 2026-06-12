def verify_string(input_string):
    state = 0
    
    for char in input_string:
        if state == 0:
            if char == 'b': state = 1
            elif char == 'a': state = 0
            else: return False  # Reject invalid character
            
        elif state == 1:
            if char == 'b': state = 1
            elif char == 'a': state = 2
            else: return False
            
        elif state == 2:
            if char == 'b': state = 3
            elif char == 'a': state = 0
            else: return False
            
        elif state == 3:
            if char == 'b': state = 1
            elif char == 'a': state = 2
            else: return False
            
    return state == 3

if __name__ == "__main__":
    # Test cases demonstrating various suffixes over alphabet {a,b}
    test_strings = ["abababab", "babab", "bbaab", "bab", "baba"]
    
    for s in test_strings:
        if verify_string(s):
            print(f"'{s}' is VALID")
        else:
            print(f"'{s}' is INVALID")