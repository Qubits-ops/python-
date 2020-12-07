"""
calcul premier terme sur suite reccurente.
"""
terme = 2
suite = 2 * terme - 1
print(suite)
for i in range(10):
    suite = 2 * terme - 1
    terme = suite
    print(suite)
