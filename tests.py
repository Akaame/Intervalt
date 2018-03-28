
from interval import *
import unittest

class IntervalTests(unittest.TestCase):
    def test_create_interval(self):
        i = Interval(4,5)
        self.assertLess(i.left, i.right)

    def test_create_interval_invalid(self):
        self.assertRaises(InvalidInterval, lambda: Interval(5,4))

    def test_check_overlap(self):
        i1 = Interval(3,6)
        i2 = Interval(4,5)
        self.assertTrue(i1.check_overlap(i2))
        
    def test_check_do_not_overlap(self):
        i1 = Interval(3,3.5)
        i2 = Interval(4,5)
        self.assertTrue(i1.check_overlap(i2))

class NodeTests(unittest.TestCase):
    def test_create_node(self):
        i = Interval(4,5)
        n = Node(i)
        self.assertEqual(i, n.interval)

    def test_add_get_left(self):
        i1 = Interval(4,5)
        n1 = Node(i1)
        i2 = Interval(3,6)
        n2 = Node(i2)
        n1.right_node = n2
        self.assertEqual(n1.right_node.interval, i2)
        self.assertEqual(n1.maxval, i2.right)
        self.assertEqual(n2.parent, n1)

    def test_add_get_right(self):
        i1 = Interval(4,5)
        n1 = Node(i1)
        i2 = Interval(3,6)
        n2 = Node(i2)
        n1.right_node = n2 
        self.assertEqual(n1.right_node.interval, i2)
        self.assertEqual(n1.maxval, i2.right)
        self.assertEqual(n2.parent, n1)
        
class IntervalTreeTests(unittest.TestCase):
    def test_create_interval_tree(self):
        tree = IntervalTree()
        i1 = Interval(3,4)
        n1 = Node(i1)
        tree.root = n1
        self.assertEqual(tree.root.interval, i1)

class IntervalBSTreeTests(unittest.TestCase):
    def test_create_bs_interval_tree(self):
        tree = IntervalBSTree()
        i1 = Interval(3,4)
        n1 = Node(i1)
        tree.root = n1
        self.assertEqual(tree.root.interval, i1)

    def test_add_interval_node(self):
        tree = IntervalBSTree()
        i1 = Interval(3,4)
        n1 = Node(i1)
        i2 = Interval(4,5)
        n2 = Node(i2)
        tree.root = n1
        tree.add(n2)
        self.assertEqual(tree.root.right_node, n2)

    def test_remove_interval_node_right(self):
        tree = IntervalBSTree()
        i1 = Interval(3,4)
        n1 = Node(i1)
        i2 = Interval(4,5)
        n2 = Node(i2)
        tree.root = n1
        tree.add(n2)
        self.assertEqual(tree.root.right_node, n2)
        tree.remove(n2)
        self.assertIsNone(tree.root.right_node)

    def test_remove_interval_node(self):
        tree = IntervalBSTree()
        i1 = Interval(3,4)
        n1 = Node(i1)
        i2 = Interval(2,5)
        n2 = Node(i2)
        tree.root = n1
        tree.add(n2)
        self.assertEqual(tree.root.left_node, n2)
        tree.remove(n2)
        self.assertIsNone(tree.root.left_node)

    def test_remove_interval_node_root(self):
        tree = IntervalBSTree()
        i1 = Interval(3,4)
        n1 = Node(i1)
        i2 = Interval(2,5)
        n2 = Node(i2)
        tree.root = n1
        tree.add(n2)
        self.assertEqual(tree.root.left_node, n2)
        tree.remove(n2)
        self.assertIsNone(tree.root.left_node)

    def test_overlapping(self):
        pass

class IntervalAVLTreeTests(unittest.TestCase):
    NotImplemented
    
class IntervalRBTreeTests(unittest.TestCase):
    NotImplemented
    
if __name__ == "__main__":
    unittest.main()