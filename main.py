from pypresence import Presence
from pypresence.types import ActivityType
from pypresence.exceptions import DiscordNotFound
from time import sleep, time


client_id = '1442081639436914709'
RPC = Presence(client_id)
LISTENING_BUTTONS = [
    {
        'label': 'My GitHub',
        'url': 'https://github.com/Xibsy'
    },
    {
        'label': 'Telegram',
        'url': 'https://t.me/Xibsy'
    }]

RPC.connect()  # Start the handshake loop

while True:
    try:
        RPC.update(
            activity_type=ActivityType.WATCHING,
            details="Хай Я Xibsy",
            state="https://guns.lol/Xibsy",
            name="на move.move",
            start=time(),
            large_image='non-active',
            buttons=LISTENING_BUTTONS,

        )
    except DiscordNotFound:
            print('биля')
    # The presence will stay on as long as the program is running
    sleep(15)
