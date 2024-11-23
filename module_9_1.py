def apply_all_func(int_list, *func):
    results = {}
    for usable in func:
        i = usable(int_list)
        results.setdefault(usable.__name__, i)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))