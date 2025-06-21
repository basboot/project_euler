coins = [1, 2, 5, 10, 20, 50, 100, 200]

VALUE = 200

def try_coin(value, coin, config, n_configs):
    global configs
    # check if possible to add this coin (or any higher coin), and there still are coins
    if coin == len(coins):
        return n_configs

    # add maximum coins
    max_coins = (VALUE - value) // coins[coin]
    config[coin] = max_coins
    value += coins[coin] * max_coins

    # config found?
    if value == VALUE:
        n_configs += 1
        # print(config)

    # remove coins 1 by 1 and try next
    while config[coin] > 0:
        config[coin] -= 1
        value -= coins[coin]
        n_configs = try_coin(value, coin + 1, config, n_configs)

    # if coin not used, still try next (just in case...)
    if max_coins == 0:
        n_configs = try_coin(value, coin + 1, config, n_configs)

    return n_configs

print(try_coin(0, 0, [0, 0, 0, 0, 0, 0, 0, 0], 0))
