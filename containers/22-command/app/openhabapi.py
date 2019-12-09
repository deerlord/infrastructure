from openhab import OpenHAB

hab = OpenHAB('http://openhab:8080/rest')

ITEM_ACTIONS = [
    'on',
    'off',
    'increase',
    'decrease',
    'up',
    'down',
    'stop',
]

EXTERNAL_COMMANDS = [
    'play',
]


class ExternalCommands:
    def play(request):
        return True


def __handle_command(item, command):
    cmd = getattr(item, 'command')
    return cmd(command)


def request(data):
    if data['command'] in EXTERNAL_COMMANDS:
        cmd = getattr(ExternalCommands, data['command'])
        cmd(data['item'])
    elif data['commmand'] in ITEM_ACTIONS:
        # get item
        cmd = getattr(item, data['command'])
        cmd()

def request(data):
    if data['action'] in EXTERNAL_COMMANDS:
        cmd = getattr(ExternalCommands, data['action'])
        result = cmd(data['item']))
    elif data['action'] in ITEM_ACTIONS:
        if data['group']:
            pass
        else:
            items = [hab.get_items(data['item']),]
        if (
            isinstance(data['action'], dict) and
            data['action'].has_key('command')
        ):
            action = 'command'
            args = [data['item'],]
        else:
            action = data['action']
            args = []
        result = all([
            getattr(item, action)(*args)
            for item in items
        ])
    return result
