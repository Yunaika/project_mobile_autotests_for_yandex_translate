"""
An example of extending Selene with custom commands, specific to mobile context by Iakiv Kramarenko
"""
from selene.core.entity import Element
from project_mobile_autotests_for_yandex_translate.utils.python import monkey


@monkey.patch_method_in(Element)
def tap(self: Element) -> Element:
    return self.click()
