value_to_num = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
    "K": 13, "A": 14
}
num_to_value = {v: k for k, v in value_to_num.items()}
suits = {"P", "D", "T", "C"}

# Todas las escaleras posibles (14 = A)
all_straights = [list(range(start, start + 5)) for start in range(10, 0, -1)]

def parse_cards(tokens):
    cards = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]

        # Caso 1: "10P" "JP" "QC"
        if len(tok) >= 2 and tok[-1] in suits:
            val = tok[:-1]
            suit = tok[-1]
            i += 1
        else:
            # Caso 2: "10 P", "J C"
            val = tok
            suit = tokens[i + 1]
            i += 2

        if val not in value_to_num or suit not in suits:
            raise ValueError("Carta inválida")

        cards.append((value_to_num[val], suit))

    return cards


while True:
    line = input().strip()
    if not line:
        continue
    tokens = line.split()

    if tokens[0] == "0":
        break

    try:
        cards = parse_cards(tokens)
        if len(cards) != 4:
            print("NADA")
            continue
    except:
        print("NADA")
        continue

    # Agrupar cartas por palo
    by_suit = {}
    for v, s in cards:
        by_suit.setdefault(s, []).append(v)

    best_missing = None
    best_value = -1
    best_suit = None

    # Para cada palo, buscar escaleras posibles
    for palo, valores in by_suit.items():
        set_vals = set(valores)

        for esc in all_straights:
            missing = [x for x in esc if x not in set_vals]

            if len(missing) == 1:
                m = missing[0]
                if m > best_value:
                    best_value = m
                    best_missing = num_to_value[m]
                    best_suit = palo

    if best_missing is None:
        print("NADA")
    else:
        print(f"{best_missing}{best_suit}")
