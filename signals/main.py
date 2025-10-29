import ast
from collections import defaultdict
from typing import Dict, List, Tuple

def decode_signals(data: List[Tuple[List[str], List[str]]]) -> Dict[str, str]:
    # Lehetséges események halmaza kódonként
    possible = defaultdict(set)
    all_codes = set()

    # Egyes napok adatai alapján szűkítjük a kódokhoz tartozó eseményeket
    for codes, events in data:
        for code in codes:
            if code not in possible:
                possible[code] = set(events)
            else:
                possible[code] &= set(events)
        all_codes.update(codes)

    decoded: Dict[str, str] = {}
    max_iter = 1000
    iter_count = 0

    # Kódok megfejtése addig, amíg van változás vagy el nem fogy a lehetőség
    while len(decoded) < len(all_codes) and iter_count < max_iter:
        progress = False
        for code, events_set in possible.items():
            if code in decoded:
                continue
            # Kiszűrjük már kiosztott eseményeket
            events_set -= set(decoded.values())
            if len(events_set) == 1:
                decoded[code] = events_set.pop()
                progress = True
        if not progress:
            break
        iter_count += 1

    return decoded


if __name__ == "__main__":
    # Bemeneti fájl beolvasása
    with open('./input.txt', 'r') as f:
        raw_input = f.read()

    # Az eredeti bemenet kiírása
    print(raw_input)

    # Bemenet Python adattípussá alakítása
    input_data = ast.literal_eval(raw_input)

    # Kódok megfejtése
    decoded = decode_signals(input_data)

    # Az eredmény formázott kiírása
    print("{")
    for i, (code, event) in enumerate(decoded.items()):
        comma = "," if i < len(decoded) - 1 else ""
        print(f'    "{code}": "{event}"{comma}')
    print("}")

