import datetime
from datetime import date

import pydantic
from appium.options.android import UiAutomator2Options
from typing import Literal, Optional

from dotenv import load_dotenv

from project_mobile_autotests_for_yandex_translate import utils

from pathlib import Path

EnvContext = Literal['local', 'browserstack']


class Settings(pydantic.BaseSettings):
    context: EnvContext = 'browserstack'

    # --- Appium Capabilities ---
    platformName: str = None
    platformVersion: str = None
    deviceName: str = None
    app: Optional[str] = None
    appName: Optional[str] = None
    appWaitActivity: Optional[str] = None
    newCommandTimeout: Optional[int] = 60

    # --- > BrowserStack Capabilities ---
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    browserstackSessionName: Optional[str] = None
    # --- > > BrowserStack credentials---
    browserstackUser: Optional[str] = None
    browserstackKey: Optional[str] = None
    udid: Optional[str] = None

    # --- Remote Driver ---
    remote_url: str = 'http://127.0.0.1:4723/wd/hub'  # default appium server url

    # --- Selene ---
    timeout: float = 6.0

    @property
    def run_on_browserstack(self):
        return 'hub.browserstack.com/wd/hub' in self.remote_url

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        if self.deviceName:
            options.device_name = self.deviceName
        if self.platformName:
            options.platform_name = self.platformName
        options.app = (
            utils.file.abs_path_from_project(self.app)
            if self.app.startswith('./') or self.app.startswith('../')
            else self.app
        )
        options.new_command_timeout = self.newCommandTimeout
        if self.udid:
            options.udid = self.udid
        if self.appWaitActivity:
            options.app_wait_activity = self.appWaitActivity
        if self.run_on_browserstack:
            options.load_capabilities(
                {
                    'platformVersion': self.platformVersion,
                    # BrowserStack capabilities
                    'bstack:options': {
                        'projectName': self.projectName,
                        'buildName': f'{self.buildName}_{date.today()}',
                        'sessionName': f'{self.browserstackSessionName}_{datetime.datetime.now().time()}',
                        # Access credentials
                        'userName': self.browserstackUser,
                        'accessKey': self.browserstackKey,
                    },
                }
            )

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        """
        factory method to init Settings with values from corresponding .env file
        """
        asked_or_current = env or cls().context
        # env_file = Path(f'config.{asked_or_current}.env');
        # load_dotenv(env_file)
        return cls(
            _env_file=utils.file.abs_path_from_project(f'config.{asked_or_current}.env')
        )


settings = Settings.in_context()
