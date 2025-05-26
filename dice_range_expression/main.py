import ast

# Bemenet beolvasása
with open('./input.txt', 'r') as f:
    input = f.read().split()

print(input)

# Dobókockák oldalainak listája
dice_faces = [20, 10, 8, 6, 4, 3, 2]

# A bemenetek párokban jönnek (min_val, max_val)
for i in range(0, len(input), 2):
    min_val = int(input[i])
    max_val = int(input[i+1])
    target_range = max_val - min_val + 1

    best_expression = None
    min_dice_count = float('inf')

    # 1 kocka esetén
    for face in dice_faces:
        if 1 <= target_range <= face:
            offset = min_val - 1
            expr = f"1d{face}"
            if offset > 0:
                expr += f"+{offset}"
            elif offset < 0:
                expr += f"{offset}"
            best_expression = expr
            min_dice_count = 1
            break

    # 2 kocka kombináció (ha 1 nem elég)
    if not best_expression:
        for face1 in dice_faces:
            for face2 in dice_faces:
                min_sum = 2
                max_sum = face1 + face2
                if max_sum - min_sum + 1 == target_range:
                    offset = min_val - min_sum
                    expr = f"1d{face1}+1d{face2}"
                    if offset > 0:
                        expr += f"+{offset}"
                    elif offset < 0:
                        expr += f"{offset}"
                    if 2 < min_dice_count:
                        best_expression = expr
                        min_dice_count = 2

    # Ha nem talált semmit
    if not best_expression:
        best_expression = "Nem található megfelelő kombináció"

    print(best_expression)

