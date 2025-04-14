def longest_substring_without_repeating_characters(s: str) -> int:
    # Dictionnaire pour stocker l'index de chaque caractère
    char_index_map = {}
    # Variables pour la longueur maximale et le début de la fenêtre
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        # Si le caractère est déjà dans la fenêtre, on déplace le début de la fenêtre
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        
        # Met à jour l'index du caractère dans le dictionnaire
        char_index_map[s[end]] = end
        # Calcule la longueur de la fenêtre actuelle
        max_length = max(max_length, end - start + 1)
    
    return max_length







def run_tests():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdef", 6),
    ]
    
    for i, (s, expected) in enumerate(test_cases, 1):
        try:
            result = longest_substring_without_repeating_characters(s)
            assert result == expected, f"Test {i} échoué : '{s}' → attendu {expected}, obtenu {result}"
            print(f"✅ Test {i} OK")
        except AssertionError as e:
            print("❌", e)
        except Exception as e:
            print(f"⚠️ Erreur inattendue dans le test {i} :", e)
run_tests()