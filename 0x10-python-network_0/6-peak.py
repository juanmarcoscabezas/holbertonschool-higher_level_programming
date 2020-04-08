#!/usr/bin/python3

"""Technical interview
"""


def find_peak(list_of_integers):
   """"Finds a peak in a list"""
   if list_of_integers:
      peak = list_of_integers[0]

      for i, num in enumerate(list_of_integers):
          if i > 0 and i < len(list_of_integers) - 1:
              if list_of_integers[i - 1] < num and list_of_integers[i + 1] < num:
                  peak = num
                  continue
          if num > peak:
              peak = num
      return peak
   else:
      return None
