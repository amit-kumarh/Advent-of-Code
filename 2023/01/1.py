from aocd import get_data
import re

content = [line.strip() for line in get_data(day=1, year=2023).split("\n")]
d = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
ans = 0
for line in content:
    m = re.findall(r"one|two|three|four|five|six|seven|eight|nine|\d", line)
    first = d.get(m[0], m[0])
    second = d.get(m[-1], m[-1])
    ans += int(first + second)

print(ans)
