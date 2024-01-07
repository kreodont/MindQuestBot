import asyncio
from telethon import Client
from telethon.types import PasswordToken


async def new_session(*, api_id: int, api_hash: str) -> None:
    # api_id and api_hash can be got at https://my.telegram.org/ -> API development tools
    session_name = input("Session name: ")
    async with Client(session_name, api_id, api_hash) as client:
        if await client.is_authorized():
            print(f'Session {session_name} already authorized. Run __main__ to work with it. For new session, provide '
                  f'an unique name')
            return
        phone = input("Enter a phone number: ")
        login_token = await client.request_login_code(phone)
        code = input('Code: ')
        password_token = await client.sign_in(login_token, code)

        if isinstance(password_token, PasswordToken):
            password = input('Password: ')
            print(f'"{password}"')
            await client.check_password(password_token, password)

        print(f'New session "{session_name}" created')

if __name__ == '__main__':
    asyncio.run(new_session(api_id=int(input('App api_id: ')), api_hash=input('App api_hash: ')))
