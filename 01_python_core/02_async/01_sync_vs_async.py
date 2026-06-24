# 01_sync_vs_async.py
# 학습일: 2026-06-25
# 개념: 동기 vs 비동기 - 시간 차이 직접 확인

import time
import asyncio

# 동기함수
def sync_task(name: str, seconds: int):
    print(f"{name} 시작")
    time.sleep(seconds)
    print(f"{name} 종료")

# 비동기 함수
async def async_task(name: str, seconds: int):
    print(f"{name} 시작")
    await asyncio.sleep(seconds)
    print(f"{name} 종료")

# ========================
# 동기 실행 — 순서대로 실행
# ========================
print("=== 동기 실행 ===")
start = time.time()
sync_task("작업1", 2)
sync_task("작업2", 2)
print(f"동기 총 시간: {time.time() - start:.1f}초")  # 4.0초

# ========================
# 비동기 실행 — 동시에 실행
# ========================
print("\n=== 비동기 실행 ===")
start = time.time()

async def main():
    await asyncio.gather(
        async_task("작업1", 2),
        async_task("작업2", 2)
    )

asyncio.run(main())
print(f"비동기 총 시간: {time.time() - start:.1f}초")  # 2.0초
