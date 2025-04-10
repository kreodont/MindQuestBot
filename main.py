import asyncio
import os
from typing import Optional
from telethon import Client


async def connect(*, session_name: str, api_id: int, api_hash: str) -> Optional[Client]:
    async with Client(session_name, api_id, api_hash) as client:
        if not await client.is_authorized():
            print('First run init_session.py to create a session file')
        else:
            return client


async def main():
    client = await connect(
        session_name='kreodont',
        api_id=int(os.getenv('api_id')),
        api_hash=os.getenv('api_hash')
    )
    if not client:
        print('Run init_session.py first to create a correct session file')
        return

    await client.connect()
    print('Connected')
    await client.send_message(chat='MindQuestBot', text='/inv_other')


if __name__ == '__main__':
    asyncio.run(main())
