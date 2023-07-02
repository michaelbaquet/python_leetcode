def is_valid_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    s = s.strip()

    if len(s) < 1 or s is None:
        return False

    while l < r:
        if not is_alpha_num(s[l]):
            l += 1
        elif not is_alpha_num(s[r]):
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1

    return True


def is_alpha_num(character) -> bool:
    return (
            ord("A") <= ord(character) <= ord("Z")
            or ord("a") <= ord(character) <= ord("z")
            or ord("0") <= ord(character) <= ord("9")
    )
