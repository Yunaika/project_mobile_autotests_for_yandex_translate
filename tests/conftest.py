import allure
import allure_commons
import pytest
import config
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from selene.support.shared import browser
from selene import support
from appium import webdriver
from project_mobile_autotests_for_yandex_translate import utils


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with allure.step('Set up app session'):
        browser.config.driver = webdriver.Remote(
            config.settings.remote_url, options=config.settings.driver_options
        )

    yield

    session_id = browser.driver.session_id

    if config.settings.run_on_browserstack:
        utils.allure.attach.screenshot(name=f'Last screenshot_{session_id}')
        utils.allure.attach.screen_xml_dump(name=f'XML_dump_{session_id}')

    allure.step('Close app session')(browser.quit)()

    if config.settings.run_on_browserstack:
        utils.allure.attach.video_from_browserstack(session_id)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):  # noqa
    # execute all other hooks to obtain the report object
    outcome = yield
    result_of_ = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, 'result_of_' + result_of_.when, result_of_)
