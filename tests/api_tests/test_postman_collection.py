import os

def test_postman_collection():
    # Spustíme Postman kolekci pomocí příkazu `newman run`
    # Místo "my_collection.json" použijte název vaší kolekce
    result = os.system('newman run api_tests/my_collection.json')

    # Kontrola výsledku, pokud byl příkaz úspěšný, vrátí 0
    assert result == 0, "API testy neproběhly úspěšně!"
