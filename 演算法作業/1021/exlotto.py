# -*- coding: utf-8 -*-
"""exlotto.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FciMe48BVQFAqKR-t44YD-J6QQkuA-ew
"""

import random
def lotto(n,m):
  list=random.sample(range(1,n+1),m)
  return list
