#!/usr/bin/python

import unittest
import change

class TestChange(unittest.TestCase):

  def test_changeslow(self):

    # Test single coin change
    print "Doing the really simple ones..."
    self.assertEqual(change.changeslow([1], 1), [1])
    self.assertEqual(change.changeslow([1, 5], 5), [0, 1])
    self.assertEqual(change.changeslow([1, 5, 10], 10), [0, 0, 1])
    self.assertEqual(change.changeslow([1, 5, 10, 25], 25), [0, 0, 0, 1])

    # Test 1 cent change
    print "Doing the still really simple ones..."
    self.assertEqual(change.changeslow([1], 2), [2])
    self.assertEqual(change.changeslow([1], 3), [3])
    self.assertEqual(change.changeslow([1], 4), [4])

    # Test Nickel and Penny
    print "Do the knickel and penny tests..."
    self.assertEqual(change.changeslow([1, 5], 1), [1, 0])
    self.assertEqual(change.changeslow([1, 5], 2), [2, 0])
    self.assertEqual(change.changeslow([1, 5], 3), [3, 0])
    self.assertEqual(change.changeslow([1, 5], 4), [4, 0])
    self.assertEqual(change.changeslow([1, 5], 5), [0, 1])
    self.assertEqual(change.changeslow([1, 5], 6), [1, 1])
    self.assertEqual(change.changeslow([1, 5], 7), [2, 1])
    self.assertEqual(change.changeslow([1, 5], 8), [3, 1])
    self.assertEqual(change.changeslow([1, 5], 9), [4, 1])
    self.assertEqual(change.changeslow([1, 5], 10), [0, 2])
    self.assertEqual(change.changeslow([1, 5], 11), [1, 2])
    

    print "Doing the harder ones..."
    self.assertEqual(change.changeslow([1, 3, 7], 1), [1, 0, 0])
    self.assertEqual(change.changeslow([1, 3, 7], 2), [2, 0, 0])
    self.assertEqual(change.changeslow([1, 3, 7], 3), [0, 1, 0])
    self.assertEqual(change.changeslow([1, 3, 7], 4), [1, 1, 0])
    self.assertEqual(change.changeslow([1, 3, 7], 6), [0, 2, 0])
    self.assertEqual(change.changeslow([1, 3, 7], 7), [0, 0, 1])
    self.assertEqual(change.changeslow([1, 3, 7], 8), [1, 0, 1])
    self.assertEqual(change.changeslow([1, 3, 7], 9), [2, 0, 1])
    self.assertEqual(change.changeslow([1, 3, 7], 10), [0, 1, 1])

    #print "Doing the slow ones..."
    #self.assertEqual(change.changeslow([1, 3, 7], 15), [1, 0, 2])

    # This one takes forever... does it ever finish?
    # Yes it does. It just really does take forever.
    #self.assertEqual(change.changeslow([1, 3, 7, 26], 22), [1, 0, 3, 0])

    # Misc examples from assignment
    print "Doing misc examples..."
    self.assertEqual(change.changeslow([1, 2, 5], 10), [0, 0, 2])

    

if __name__ == '__main__':
  unittest.main()
