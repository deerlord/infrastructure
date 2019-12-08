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
    if data['action'] in EXTERNAL_COMMANDS:
        cmd = getattr(ExternalCommands, data['action'])
        result = cmd(data['item'])
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
        else:
            action = data['action']
        for item in items:
            cmd = getattr(item, action)
            result = all(
                cmd(data['action']['command'])
                if action == 'command'
                else cmd()
            )
    return result
