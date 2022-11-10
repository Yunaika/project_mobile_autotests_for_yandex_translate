import requests
import config


def video_url(session_id: str):
    session_info = requests.get(f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
                                auth=(config.settings.browserstackUser, config.settings.browserstackKey),
                                ).json()

    return session_info['automation_session']['video_url']
