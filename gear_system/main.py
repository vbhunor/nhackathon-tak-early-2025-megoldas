import ast
from collections import deque

# ----- Beolvassuk az inputot -----
with open('./input.txt', 'r') as f:
    raw_input = f.read()

print(raw_input)

# ----- Segedfuggveny az input sor feldolgozasahoz -----
def parse_line(line):
    line = line.strip().replace('(', '').replace(')', '')
    parts = line.split(']')
    try:
        target = ast.literal_eval(parts[0] + ']')
        steps = int(parts[1].strip()) if len(parts) > 1 and parts[1].strip() else 8
        return (target, steps)
    except:
        return None

# ----- Feldolgozzuk az osszes inputot -----
input_data = []
for line in raw_input.strip().splitlines():
    if not line.strip():
        continue
    parsed = parse_line(line)
    if parsed is None:
        print("Hibás input formátum.")
        exit()
    input_data.append(parsed)

# ----- Fogaskerekek modellje -----
left_lever = [1, 1, 0]
right_lever = [0, 1, 1]

# ----- Alapvető állapot -----
def rotate(state, lever):
    return [((state[i] + lever[i] - 1) % 3) + 1 for i in range(3)]

def solve(target, max_steps):
    start = (3, 3, 3)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if list(current) == target:
            return ' '.join(path)

        if len(path) >= max_steps:
            continue

        # bal kar
        new_state = tuple(rotate(current, left_lever))
        if new_state not in visited:
            visited.add(new_state)
            queue.append((new_state, path + ['left']))

        # jobb kar
        new_state = tuple(rotate(current, right_lever))
        if new_state not in visited:
            visited.add(new_state)
            queue.append((new_state, path + ['right']))

    return "Megoldhatatlan"

# ----- Minden feladat megoldasa -----
for target, limit in input_data:
    print(solve(target, limit))
