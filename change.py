def changeslow(coins, amount, change = None):

  #print amount

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

        #print str(i) + ": " + str(amount)
        #print iChange
        #print kMinusIChange

        tmpCoins2 = 0
        tmpChange = []

        for i in range(0, len(iChange)):
          tmpCoins2 = tmpCoins2 + iChange[i]
          tmpCoins2 = tmpCoins2 + kMinusIChange[i]
          tmpChange.append(iChange[i] + kMinusIChange[i])

        if tmpCoins == None or tmpCoins2 < tmpCoins:
          tmpCoins = tmpCoins2
          change = tmpChange
          #print change



  return change
