import asyncio
import time


async def start_strongman(name, power):
    print(f"Силачь {name} начал соревнования.")
    self_time = 5 / power
    for i in range(5):
        await asyncio.sleep(self_time)
        print(f"Силачь {name} поднял шар номер {i + 1}")
    print(f"Силачь {name} закончил соревнование")


async def main():
    all_man = [('Pasha', 3), ('Denis', 4), ('Apollon', 5)]
    task_strongman = [asyncio.create_task(start_strongman(*man)) for man in all_man]
    for man in task_strongman:
        await man


asyncio.run(main())
