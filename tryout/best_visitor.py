visitors = [0, 2, 3, 2, 0, 4, 1, 1, 2]
entries_by_visitor = [0] * 5
best_visitor = 0

print(f'Entries by visitor start: {entries_by_visitor}')

for visitor in visitors:
    entries_by_visitor[visitor] += 1
    print(f'Entries by visitor on step: {entries_by_visitor}')
    if entries_by_visitor[visitor] > entries_by_visitor[best_visitor]:
        best_visitor = visitor

print(best_visitor)
