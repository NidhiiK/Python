# Tupls: Tuples are similar to lists, so we can use them to store a list of items. But unlike lists we cannot
#        modify them, we cannot add new items, we cannot remove existing items. Therfore, Tuples are immutable.
#        Only 2 methods are applicable : count and index.

numbers = (1, 2, 3, 4, 3, 6, 3)
x = numbers.count(3)
print(x)
