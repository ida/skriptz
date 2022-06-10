def merge_dicts():
    x = {'a':1, 'b': 2}
    y = {'b':10, 'c': 11}
    z = dict(x.items() + y.items())
    print z
    # 'b' gets the value of lastly added dict (here: y, so val is 10)
