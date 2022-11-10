from selene import be
from selene.support.shared import browser

from project_mobile_autotests_for_yandex_translate.model.components.main_screen import MainScreen
from project_mobile_autotests_for_yandex_translate.utils.allure.report import step

main_screen = MainScreen()

@step
def given_opened():
    if browser.element('#design_bottom_sheet').matching(be.visible):
        browser.element('.android.widget.Button').tap()
