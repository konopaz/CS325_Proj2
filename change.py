def changeslow(coins, amount, change = None):

  if change == None:
    change = []
    for i in range(0, len(coins)):
      change.append(0)

  try:

    idx = coins.index(amount)
    change[idx] = change[idx] + 1

  except ValueError:

    tmpCoins = None

    for i in range(1, amount):

        iChange = changeslow(coins, i)
        kMinusIChange = changeslow(coins, amount - i)

        tmpCoins2 = 0
        tmpChange = []

        for i in range(0, len(iChange)):
          tmpCoins2 = tmpCoins2 + iChange[i]
          tmpCoins2 = tmpCoins2 + kMinusIChange[i]
          tmpChange.append(iChange[i] + kMinusIChange[i])

        if tmpCoins == None or tmpCoins2 < tmpCoins:
          tmpCoins = tmpCoins2
          change = tmpChange

  return change

def changegreedy(coins, amount):

  change = []
  for i in range(0, len(coins)):
    change.append(0)

  coinIdx = len(coins) - 1;

  while amount > 0:

    while coins[coinIdx] > amount:
      coinIdx = coinIdx - 1

    amount = amount - coins[coinIdx]
    change[coinIdx] = change[coinIdx] + 1

  return change

def changedp(coins, amount, change = None, table = None):

  if change == None:
    change = []
    for i in range(0, len(coins)):
      change.append(0)

  if table == None:
    table = {}
    table[0] = []
    for i in range(0, len(coins)):
      table[0].append(0)

  if table.has_key(amount):
    return table[amount]

  try:

    idx = coins.index(amount)
    change[idx] = change[idx] + 1

  except ValueError:

    tmpCoins = None

    for i in range(1, amount):

        iChange = changedp(coins, i, None, table)
        kMinusIChange = changedp(coins, amount - i, None, table)

        tmpCoins2 = 0
        tmpChange = []

        for i in range(0, len(iChange)):
          tmpCoins2 = tmpCoins2 + iChange[i]
          tmpCoins2 = tmpCoins2 + kMinusIChange[i]
          tmpChange.append(iChange[i] + kMinusIChange[i])

        if tmpCoins == None or tmpCoins2 < tmpCoins:
          tmpCoins = tmpCoins2
          change = tmpChange

  table[amount] = change
  return change
