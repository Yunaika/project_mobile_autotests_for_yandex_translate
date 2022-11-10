from project_mobile_autotests_for_yandex_translate.model import app


class TestsTranslateText:
    def test_translation_text_from_English_to_Russian(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.translate_source_lang_should_be('ENGLISH')\
                       .translate_target_lang_should_be('RUSSIAN')\
                       .set_text_to_translate("I'm a robot")

        # THEN
        app.main_screen.should_be_translated_text('Я робот')

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


class TestsTranslationArea:
    def test_clear_input_field_by_clicking_on_the_cross_icon(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.set_text_to_translate('Hello, world!')\
                       .tap_cross_icon()

        # THEN
        app.main_screen.should_be_text_to_translate('Type text or a site address')

    def test_open_fullscreen_translated_text(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.set_text_to_translate('Python is one of the most popular programming languages')\
                       .tap_fullscreen_icon()

        # THEN
        app.main_screen.fullscreen_popup.should_be_visible()\
                                        .should_have_text('Python - один из самых популярных языков программирования')\
                                        .tap_close_button()


    def test_button_translate_site_should_be_visible(self):
        # PRECONDITION
        app.given_opened()

        # WHEN
        app.main_screen.set_text_to_translate('appium.io')

        # THEN
        app.main_screen.should_be_visible_translate_site_button()
