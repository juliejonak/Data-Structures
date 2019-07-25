class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # TODO: If = to, then what?

    if value < self.value:
      # go to the left
      # if nothing to the left, add it
      if not self.left:
        return self.left = BinarySearchTree(value)
      else:
        # keep searching
        return self.left.insert(value)

    else:
      # go to the right
      # if nothing to the right, add it:
      if not self.right:
        return self.right = BinarySearchTree(value)
      else:
        # keep searching
        return self.right.insert(value)
    

  def contains(self, target):
    # if the current is the target, return True
    if self.value == target:
      return True

    if target < self.value:
      # then we need to search down the left
      if not self.left:
        # if we can't go any further left, it isn't here
        return False
      else:
        return self.left.contains(target)
      
    else:
      # we need to search down the right
      if not self.right:
        # it isn't here
        return False
      else: return self.right.contains(target)

  def get_max(self):
    # if nothing in the tree, return None
    if not self:
      return None
    # search down the right
    # if there is no right to search, return current
    if not self.right:
      return self.value
    else:
      # keep searching for the end
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)

    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

