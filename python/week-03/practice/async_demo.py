"""Completed scheduling experiment. No network; sleeps simulate waiting."""

import asyncio
import sys
import time


async def task(name: str, blocking: bool) -> None:
    print(f"{name} start")
    if blocking:
        time.sleep(0.05)
    else:
        await asyncio.sleep(0.05)
    print(f"{name} end")


async def main(blocking: bool) -> None:
    await asyncio.gather(task("A", blocking), task("B", blocking))


if __name__ == "__main__":
    asyncio.run(main("--blocking" in sys.argv))
