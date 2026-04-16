import asyncio

from client import APIClient, get_users_async


def main():
    api = APIClient()

    print("\n--- GET normal ---")
    users = api.get_users()
    print(users)

    print("\n--- GET con retry ---")
    users_retry = api.get_users_with_retry()
    print(users_retry)

    print("\n--- Streaming a archivo ---")
    api.download_users_stream("users.json")

    api.close()


async def main_async():
    print("\n--- Async HTTP/2 ---")
    users = await get_users_async()
    print(users)


if __name__ == "__main__":
    main()
    asyncio.run(main_async())
