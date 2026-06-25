# 02_async_basic.py
# 학습일: 2026-06-25
# 개념: async/await 기초 - async def, await, asyncio.run()

import asyncio  

async def fetch_user(name, delay):
    await asyncio.sleep(delay)
    return f"유저: {name}"

async def fetch_order(name, delay):
    await asyncio.sleep(delay)
    return f"주문 {name}"

async def main():
    user = await fetch_user("김철수", 2)
    print(user)                            # 유저: 김철수

    order = await fetch_order("001", 1)
    print(order)                           # 주문: 001

asyncio.run(main())