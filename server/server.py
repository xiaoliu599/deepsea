import tornado.web
import asyncio
from handlers import ConnectHandler


async def makeApp():
    app = tornado.web.Application([
        (r"/connect", ConnectHandler)
    ])
    app.listen(8000)
    print("=====> SERVER START && PORT 8000")
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(makeApp())