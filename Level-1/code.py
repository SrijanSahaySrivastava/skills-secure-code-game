'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal('0')
    
    max_amt = 100000
    max_qty = 100
    max_len = 1e6

    for item in order.items:
        if item.type == 'payment':
            if item.amount > -1*max_amt and item.amount < max_amt:
                net += Decimal(str(item.amount))
        elif item.type == 'product':
            if item.quantity > 0 and item.quantity <= max_qty and item.amount > 0 and item.amount <= max_amt:
                net -= Decimal(str(item.amount)) * item.quantity
            if net > max_len or net < -1*max_len:
                return("Amount exceeds maximum length")
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
