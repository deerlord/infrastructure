from openhab import OpenHAB

hab = OpenHAB('http://openhab:8080/rest')


class ExternalCommands:
    def play(request):
        pass



class Commands:
    def _get_item(name):
        return hab.get_item(name)

    def on(name):
        item = Commands._get_item(name)
        return item.on() if hasattr(item, 'on') else None

    def off(name):
        item = Commands._get_item(name)
        return item.off() if hasattr(item, 'off') else None

    def increase(name):
        item = Commands._get_item(name)
        return item.increase() if hasattr(item, 'increase') else None

    def decrease(name):
        item = Commands._get_item(name)
        return item.decrease() if hasattr(item, 'decrease') else None

    def up(name):
        item = Commands._get_item(name)
        return item.up() if hasattr(item, 'up') else None

    def down(name):
        item = Commands._get_item(name)
        return item.down() if hasattr(item, 'down') else None

    def stop(name):
        item = Commands._get_item(name)
        return item.stop() if hasattr(item, 'stop') else None

    def command(name, command):
        item = Commands._get_item(name)
        return item.command(command) if hasattr(item, 'command') else None


COMMANDS = {
    'on': Commands.on,
    'off': Commands.off,
    'increase': Commands.increase,
    'decrease': Commands.decrease,
    'up': Commands.up,
    'down': Commands.down,
    'stop': Commands.stop,
    'play': ExternalCommands.play,
}


def request(data):
    verb = data['verb']
    subj = data['subject']
    if verb in COMMANDS:
        result = COMMANDS[verb](subj)
    else:
        try:
            result = Commands['command'](subj, verb)
        except:
            result = None
    return result
