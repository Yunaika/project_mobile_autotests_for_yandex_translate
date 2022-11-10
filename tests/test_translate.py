import allure
from allure_commons.types import Severity
from project_mobile_autotests_for_yandex_translate.model import app


@allure.tag("ui", "mobile")
@allure.label('owner', 'juliamur')
@allure.feature('UI')
@allure.story('Text translation')
class TestsTranslateText:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Translation text from English to Russian')
    def test_translation_text_from_English_to_Russian(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.translate_source_lang_should_be('ENGLISH')\
                       .translate_target_lang_should_be('RUSSIAN')\
                       .set_text_to_translate("I'm a robot")

        # THEN
        app.main_screen.should_be_translated_text('Я робот')

    @allure.severity(Severity.NORMAL)
    @allure.title('Switch language by button')
    def test_switch_language_by_button(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.translate_source_lang_should_be('ENGLISH')\
                       .set_text_to_translate('Milk')\
                       .translate_target_lang_should_be('RUSSIAN')\
                       .tap_switch_language()

        # THEN
        app.main_screen.translate_source_lang_should_be('RUSSIAN')\
                       .translate_target_lang_should_be('ENGLISH')\
                       .should_be_translated_text('Milk')

@allure.tag("ui", "mobile")
@allure.label('owner', 'juliamur')
@allure.feature('UI')
@allure.story('Translation area')
class TestsTranslationArea:
    @allure.severity(Severity.NORMAL)
    @allure.title('Clear input field by click on the cross icon')
    def test_clear_input_field_by_click_on_the_cross_icon(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.set_text_to_translate('Hello, world!')\
                       .tap_cross_icon()

        # THEN
        app.main_screen.should_be_text_to_translate('Type text or a site address')

    @allure.severity(Severity.NORMAL)
    @allure.title('Open translated text in full screen')
    def test_open_translated_text_in_full_screen(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.set_text_to_translate('Python is one of the most popular programming languages')\
                       .tap_fullscreen_icon()

        # THEN
        app.main_screen.fullscreen_popup.should_be_visible()\
                                        .should_have_text('Python - один из самых популярных языков программирования')\
                                        .tap_close_button()

    @allure.severity(Severity.BLOCKER)
    @allure.title('Button Translate site should be visible')
    def test_button__translate_site__should_be_visible(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.set_text_to_translate('appium.io')

        # THEN
        app.main_screen.should_be_visible_translate_site_button()
