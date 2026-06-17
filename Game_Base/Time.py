import asyncio
import curses
class THE_TIME:
    async def passage_of_time(self):
        await asyncio.sleep(120)
    async def passage_of_min(self):
        await asyncio.sleep(2)
    async def game(self, stdscr):
        min = 1
        count = 1
        stdscr.addstr(f"0{count}:0{min}")
        while True:
            stdscr.clear()
            while min < 60:
                await self.passage_of_min()
                min += 1
                if len(str(min)) != 2:
                    print(f"0{count}:0{min}")
                else:
                    stdscr.addstr(f"0{count}:0{min}")
            while count < 6:
                await self.passage_of_time()
                count += 1
    async def main(self, stdscr):
        pass





curses.wrapper(asyncio.run(THE_TIME().game()))

