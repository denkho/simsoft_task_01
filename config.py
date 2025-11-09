# config.py

class Config:
    """
    Глобальная конфигурация проекта.
    """

    # URLs
    BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
    MANAGER_PAGE = BASE_URL + "#/manager"

    # selenium таймауты
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 10

    # Настройки браузера (options)
    HEADLESS = True
    START_MAXIMIZED = True
    INCOGNITO = True
