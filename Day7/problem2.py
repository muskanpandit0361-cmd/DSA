# Choose two cards so the product of their values is maximum.
# Print the winning amount as the sum of the two card values.


def max_product_sum(cards):
    if len(cards) < 2:
        return 0

    max_product = None
    best_sum = 0

    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            product = cards[i] * cards[j]
            if max_product is None or product > max_product:
                max_product = product
                best_sum = cards[i] + cards[j]

    return best_sum


if __name__ == "__main__":
    values = input().strip().split()
    cards = [int(x) for x in values]
    print(max_product_sum(cards))


#output:: 1 53 2 8 3 -10
#61  (53+8)



