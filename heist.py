def maximum_value(max_weight, items):

    items_len = len(items)
    weights = [i['weight'] if type(i['weight']) == int and i['weight']>0 else None for i in items]
    values = [i['value'] if type(i['value'])==int and i['value']>0 else None for i in items]

    if None in weights or None in values:
        raise Exception("Negative value given in items! Only positive values allowed.")

    dp = [[0 for i in range(max_weight+1)] for _ in range(items_len+1)]

    for item in range(items_len+1):
        for weight in range(max_weight+1):

            if item == 0 or weight == 0:
                dp[item][weight] = 0

            elif weights[item-1] <= weight:
                dp[item][weight] = max(dp[item-1][weight-weights[item-1]]+values[item-1],dp[item-1][weight])

            else:
                dp[item][weight] = dp[item-1][weight]

    return dp[items_len][max_weight]
