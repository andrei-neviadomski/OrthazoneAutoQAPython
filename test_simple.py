from playwright.sync_api import Page, expect

def test_example_site(page: Page):
    # Переходим на сайт
    page.goto("https://orthazone.com")

    # Проверяем заголовок
    expect(page).to_have_title("Orthodontic Supplies Store, Orthodontic Products & Instruments at Orthazone")
