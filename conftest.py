import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import project_mobile_autotests_for_yandex_translate.utils.selene.patch_selector_strategy  # noqa
    import project_mobile_autotests_for_yandex_translate.utils.selene.patch_element_mobile_commands  # noqa
