from openhab import OpenHAB

hab = OpenHAB('http://openhab:8080/rest')

ACTIONS = [
    'on',
    'off',
    'increase',
    'decrease',
    'up',
    'down',
    'stop',
]

def request(command):
    action = command['action'].lower()
    if action not in ACTIONS:
        return None
    if command['plural']:
        retval = __action_to_group(command['name'], action)
    else:
        item = hab.get_item(command['name'])
        retval = __take_action(item, action)
    return retval


def __take_action(item, action):
    return getattr(item, action)() if hasattr(item, action) else None


def __action_to_group(type_, action):
    return all([
        __take_action(item, action)
        for item in hab.fetch_all_items()
        if item.type == type_
    ])
