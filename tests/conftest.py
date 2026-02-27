import pytest
import os
from datetime import datetime


@pytest.fixture(scope="function")
def page(page):
    """Инжектим заглушку gtag чтобы onclick не падал на stage"""
    page.add_init_script("""
        window.gtag = window.gtag || function() {};
        window.dataLayer = window.dataLayer || [];
    """)
    yield page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Этот блок выполняется после каждого этапа теста (setup, call, teardown)
    outcome = yield
    rep = outcome.get_result()
    
    # Мы проверяем, что это этап самого теста ("call") и он завершился неудачей
    if rep.when == "call" and rep.failed:
        # Пытаемся достать фикстуру 'page' из теста
        page_fixture = item.funcargs.get("page")
        if page_fixture:
            # Создаем папку, если её нет (дублируем логику для надежности)
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            # Формируем имя: название_теста.png
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = f"screenshots/FAILED_{item.name}_{timestamp}.png"
            page_fixture.screenshot(path=file_path)