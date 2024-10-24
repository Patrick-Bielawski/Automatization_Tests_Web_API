from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://pokeapi.co/docs/v2")
        assert page.title() == "Documentation - PokéAPI"
        browser.close()