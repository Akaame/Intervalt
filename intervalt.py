"""
========
Intervalt

Interval tree implementation in Python.

Interval trees hold intervals in tree structure 
so that overlaps can be observed faster.

"""
import sys
ver = sys.version_info.major 
# If 2 change property logic TODO

class InvalidInterval(Exception):
    pass

class Interval(object):
    """ Interval class for holding interval boundaries """
    def __init__(self, l, r):
        if l > r:
            raise InvalidInterval
        self._l = l
        self._r = r

    @property
    def left(self):
        return self._l

    @property
    def right(self):
        return self._r

    def check_overlap(self, other):
        if self.right > other.left or self.left < other.right:
            return True
        return False

    def __repr__(self):
        return "Interval[" +str(self.left) + ", "+str(self.right)+"]"

class Node(object):
    """ Node structure holds an interval """
    def __init__(self, interval):
        self._interval = interval
        self._parent = None
        self._left_node = None
        self._right_node = None
        self._maxval = interval.right

    @property
    def interval(self):
        """ Interval getter """
        return self._interval

    @property
    def parent(self):
        """ Parent node getter """
        return self._parent

    @property
    def left_node(self):
        """ Left node getter """
        return self._left_node

    @property
    def right_node(self):
        """ Right node getter """
        return self._right_node

    @property
    def maxval(self):
        """ Max value in subtree getter """
        return self._maxval

    @parent.setter
    def parent(self, value):
        """ Parent node setter """
        self._parent = value

    @left_node.setter
    def left_node(self, value):
        """ Left node setter """
        self._left_node = value
        if value != None:
            value.parent = self
            self.maxval = max(self.maxval, value.maxval)
        
    @right_node.setter
    def right_node(self, value):
        """ Right node setter """
        self._right_node = value
        if value != None:
            value.parent = self
            self.maxval = max(self.maxval, value.maxval)
    
    @right_node.deleter
    def right_node(self):
        """ Right node deleter """
        self._right_node = None
    
    @left_node.deleter
    def left_node(self):
        """ Left node deleter """
        self._left_node = None

    @maxval.setter
    def maxval(self, value):
        """ Max value in subtree setter """
        self._maxval = value

    def __repr__(self):
        st = "Node holding " + repr(self.interval) 
        if self.left_node != None:
            st += " Has left child "
        if self.right_node != None:
            st += " Has right child "
        return st

class IntervalTree(object):
    """
    Generic abstract tree structure.
    """
    
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        """ Tree root getter """
        return self._root
    
    @root.setter
    def root(self, val):
        """ Tree root setter """
        self._root = val
    
    def add(self, node):
        """ Tree add rule """
        pass
    
    def remove(self, node):
        """ Tree remove rule """
        pass

    def check_overlap(self, node):
        """ Check if node overlaps """
        pass

    def __repr__(self):
        return "Interval tree with root: " + repr(self.root)

class IntervalBSTree(IntervalTree):
    """ 
    Interval tree structure that uses simple 
    Binary Search Tree as underlying tree.

    Supports adding, removing and checking overlaps.
    """
    def add(self, node):
        """ 
        BST Tree add rule 
        Add according to left value of interval
        """
        self._add(self.root, node)

    def _add(self, parent, node):
        pl = parent.interval.left
        nl = node.interval.left
        if pl > nl:
            if parent.left_node == None:
                parent.left_node = node
            else:
                self._add(parent.left_node, node)
        else: 
            if parent.right_node == None:
                parent.right_node = node
            else:
                self._add(parent.right_node, node)

    def remove(self, node):
        """ 
        BST Tree remove rule 
        Search according to left value of interval
        """
        self._remove(self.root, node)

    def _del(self, gp, p, c):
            if gp == None:
                self.root = c
            elif p == gp.left_node:
                del gp.left_node # if node is left child
                gp.left_node = c
            else:
                del gp.right_node # if node is left child
                gp.right_node = c
            
    def _findMin(self, node):
        """ Find leftmost min """
        n = node
        while n.left_node != None:
            n = n.left_node
        return n

    def _remove(self, parent, node):
        pl = parent.interval.left
        nl = node.interval.left

        if parent == node:
            # We have found target node
            if node.left_node == None and node.right_node==None:
                self._del(node.parent, node, None)
            elif node.left_node != None and node.right_node==None:
                temp = node.left_node
                self._del(node.parent, node, temp)
            elif node.left_node == None and node.right_node!=None:
                temp = node.right
                self._del(node.parent, node, temp)
            else:
                self._del(node.parent, node,self._findMin(node.right_node))
            
        if pl > nl:
            if parent.left_node == None:
                return None
            else:
                self._remove(parent.left_node, node)
        else: 
            if parent.right_node == None:
                return None
            else:
                self._remove(parent.right_node, node)

    def check_overlap(self, interval):
        """ 
        Check if node overlaps 
        Steps:
            Recursively ->
            If node overlaps. Return node.
            Else check condition below
            condition: node->left is not null and node-left->maxval >= interval->left
            If condition
                Check left
            Else:
                Check right
        """
        if self.root == None:
            return None
        else:
            return self._check_overlap(self.root, interval)

    def _check_overlap(self, node, interval):
        if node.interval.check_overlap(interval):
            return node.interval
        else:
            if node.left_node != None and node.left_node.maxval >= interval.left:
                return self._check_overlap(node.left_node, interval)
            elif node.right_node !=None:
                return self._check_overlap(node.right_node, interval)
            else:
                return None
                
class IntervalAVLTree(IntervalTree):
    """ 
    Interval tree structure that uses simple 
    AVL Tree as underlying tree.

    Supports adding, removing and checking overlaps.
    """
    def add(self, node):
        """ BST Tree add rule """
        pass
    
    def remove(self, node):
        """ BST Tree remove rule """
        pass

    def check_overlap(self, node):
        """ Check if node overlaps """
        pass

class IntervalRBTree(IntervalTree):
    """ 
    Interval tree structure that uses simple 
    Red Black Tree as underlying tree.

    Supports adding, removing and checking overlaps.
    """
    def add(self, node):
        """ BST Tree add rule """
        pass
    
    def remove(self, node):
        """ BST Tree remove rule """
        pass

    def check_overlap(self, node):
        """ Check if node overlaps """
        pass

bintrees_enabled = False
# if Python 3
if ver == 3:
    import importlib
    from importlib import util
    bintrees_enabled = util.find_spec("bintrees") != None # some serious shit going on here
# if Python 2
if ver == 2:
    import imp
    try:
        imp.find_module("bintrees")
        bintrees_enabled = True
    except ImportError:
        bintrees_enabled = False


if bintrees_enabled:
    import bintrees
    print("Bintrees is enabled")
    class IntervalBSTreeBintreesAdapter(IntervalTree):
        """ 
        I do not know how this adapter pattern should work.
        Or if it is even possible to augment bintrees classes.
        Will try to interact underlying bintrees.BinaryTree with
        IntervalTree interface
        """
        def __init__(self, root):
            # super init TODO
            self._tree = bintrees.BinaryTree([(root.interval, root)])
            
        @property
        def tree():
            return self._tree

        def add(self, node):
            self._tree.insert(node.interval, node)

        def remove(self, node):
            self._tree.remove(node.interval)
        
        def check_overlap(self, interval):
            for k,v in self._tree.items():
                if k.check_overlap(interval):
                    return v
            return None
            

    class IntervalRBTreeBintreesAdapter(IntervalTree):
        """ 
        I do not know how this adapter pattern should work.
        Or if it is even possible to augment bintrees classes.
        Will try to interact underlying bintrees.BinaryTree with
        IntervalTree interface
        """
        def __init__(self, root):
            # super init TODO
            self._tree = bintrees.RBTree([(root.interval, root)])
            
        @property
        def tree():
            return self._tree

        def add(self, node):
            self._tree.insert(node.interval, node)

        def remove(self, node):
            self._tree.remove(node.interval)
        
        def check_overlap(self, interval):
            for k,v in self._tree.items():
                if k.check_overlap(interval):
                    return v
            return None

    class IntervalAVLTreeBintreesAdapter(IntervalTree):
        """ 
        I do not know how this adapter pattern should work.
        Or if it is even possible to augment bintrees classes.
        Will try to interact underlying bintrees.BinaryTree with
        IntervalTree interface
        """
        def __init__(self, root):
            # super init TODO
            self._tree = bintrees.AVLTree([(root.interval, root)])
            
        @property
        def tree():
            return self._tree

        def add(self, node):
            self._tree.insert(node.interval, node)

        def remove(self, node):
            self._tree.remove(node.interval)
        
        def check_overlap(self, interval):
            for k,v in self._tree.items():
                if k.check_overlap(interval):
                    return v
            return None

# create Strategy Pattern for each tree type TODO

# create a Strategy Factory TODO