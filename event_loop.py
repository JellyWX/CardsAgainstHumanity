import time
import asyncio
from globalvars import client

async def event_loop():
  await client.wait_until_ready()
  last_update = time.time()
  while not client.is_closed:

    try:
      this_update = time.time()
      if this_update - last_update > 12.5:
        print('bot ticking too slowly. skipping a tick')
        continue

      ## RUN CODE HERE:

      ## STOP RUNNING CODE HERE ^

      last_update = this_update

    except:
      print('skipping loop due to errors.')
      continue

    await asyncio.sleep(1.2)
