from constants import RPC
from pypresence.types import ActivityType
from time import sleep


RPC.connect()

RPC.update(
    activity_type=ActivityType.LISTENING,
    details='Ого рпс рабитает',
    state='Работаю над проектом',
    state_url="https://github.com/Xibsy/MyDiscordRpc",
    end=60000
)

while True:
    sleep(15)
