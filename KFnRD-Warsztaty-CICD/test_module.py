def plural(
        i: int,
        singular: str,
        plural_nominative: str,
        plural_genitive: str) -> str:
    if i == 1:
        return singular
    elif i >= 11 and i <= 20 or i % 10 in [1, 5, 6, 7, 8, 9, 0]: 
        return plural_genitive
    else:
        return plural_nominative
    
assert plural(1, "s", "p_n", "p_g") == "s"
assert plural(20, "s", "p_n", "p_g") == "p_g"
assert plural(22, "s", "p_n", "p_g") == "p_n"
assert plural(91, "s", "p_n", "p_g") == "p_g"