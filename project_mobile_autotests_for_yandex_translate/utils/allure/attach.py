import allure
from selene.support.shared import browser

from project_mobile_autotests_for_yandex_translate.utils.utils import get_video_url


def screenshot(*, name='Screenshot'):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


def screen_xml_dump(*, name='Page_XML_dump'):
    allure.attach(
        browser.driver.page_source,
        name=name,
        attachment_type=allure.attachment_type.XML,
    )


def video_from_browserstack(session_id: str):
    name = f'Screencast_{session_id}'
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + get_video_url(session_id) \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, name, allure.attachment_type.HTML, '.html')
