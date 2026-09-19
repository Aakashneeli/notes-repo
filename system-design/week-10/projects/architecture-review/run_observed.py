"""Supplied local integration runner; expected unfinished-starter failure initially."""
import asyncio
import json
from uuid import uuid4
from fixture import query
from instrumentation import observe


async def main():
    for fail in (False, True):
        request_id = str(uuid4())
        try:
            await observe(lambda: query(fail=fail),
                          lambda event: print(json.dumps(event, sort_keys=True)),
                          request_id, "fixture-model", {"input": 2.0, "output": 6.0})
        except TimeoutError:
            pass  # Expected second case. NotImplementedError is not swallowed.


if __name__ == "__main__":
    asyncio.run(main())
