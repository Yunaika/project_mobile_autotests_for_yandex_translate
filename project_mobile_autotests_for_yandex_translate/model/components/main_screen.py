from selene import have, be
from selene.support.shared import browser
from project_mobile_autotests_for_yandex_translate.utils.allure.report import step


class FullscreenPopup:
    @step
    def should_be_visible(self):
        browser.element('#tvFullscreen').should(be.visible)
        return self

    @step
    def should_have_text(self, value):
        browser.element('#tvFullscreen').should(have.exact_text(value))
        return self

    @step
    def tap_close_button(self):
        browser.element('#closeButton').tap()
        return self


class MainScreen:
    @step
    def set_text_to_translate(self, value):
        browser.with_(timeout=15).element('#et_input_field').set_value(value)
        return self

    @step
    def should_be_text_to_translate(self, value):
        browser.element('#et_input_field').should(have.exact_text(value))
        return self

    @step
    def should_be_translated_text(self, value):
        browser.element('#tv_translation').wait_until(have.exact_text(value))
        return self

    @step
    def should_be_visible_translate_site_button(self):
        browser.element('#btnTrUrl').should(be.visible)
        return self

    @step
    def translate_source_lang_should_be(self, value):
        browser.element('#tv_translate_source_lang').should(have.exact_text(value))
        return self

    @step
    def translate_target_lang_should_be(self, value):
        browser.element('#tv_translate_target_lang').should(have.exact_text(value))
        return self

    @step
    def tap_cross_icon(self):
        browser.element('#clearButton').tap()
        return self

    @step
    def tap_switch_language(self):
        browser.element('#ib_translate_switch_langs').tap()
        return self

    @step
    def tap_fullscreen_icon(self):
        browser.element('#ib_fullscreen_tr').tap()
        return self

    fullscreen_popup = FullscreenPopup()
