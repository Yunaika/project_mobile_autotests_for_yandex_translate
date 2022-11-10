import os

import requests

import config


def humanify(name: str):
    import re
    return ' '.join(re.split('_+', name)).capitalize()


def humanify_class(name: str):
    new_name = [name[0]]
    for i in range(1, len(name)):
        if name[i].isupper():
            new_name.append(' ' + name[i].lower())
        else:
            new_name.append(name[i])
    return ''.join(new_name)


def get_video_url(session_id: str):
    # session = requests.Session()
    # session.auth = (os.getenv('browserstackUser'), os.getenv('browserstackKey'))
    # response = session.get(f'https://api.browserstack.com/app-automate/sessions/{session_id}.json')
    # return response.json().get('automation_session').get('video_url')
    session_info = requests.get(f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
                                auth=(config.settings.browserstackUser, config.settings.browserstackKey),
                                ).json()

    return session_info['automation_session']['video_url']
