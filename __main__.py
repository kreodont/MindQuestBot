import asyncio
import os

from telethon import Client


async def connect(*, phone: str, code: str, password: str, session_name: str, api_id: int, api_hash: str) -> Client:
    async with Client(session_name, api_id, api_hash) as client:
        if not await client.is_authorized():
            print(f'Authorizing with phone "{phone}"')
            login_token = await client.request_login_code(phone)
            code = input('code: ')
            password_token = await client.sign_in(login_token, code)
            await client.check_password(password_token, password)
            return client
        else:
            print('Client already authorized')
            return client


async def main():
    client = await connect(
        phone=os.getenv('phone'),
        code=os.getenv('!code'),
        password=os.getenv('password'),
        session_name=os.getenv('session_name'),
        api_id=int(os.getenv('api_id')),
        api_hash=os.getenv('api_hash')
    )
    await client.connect()
    print('Connected')
    await client.send_message(chat='MindQuestBot', text='/inv_other')


if __name__ == '__main__':
    asyncio.run(main())
