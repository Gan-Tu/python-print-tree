class Node:

  def __init__(self, val, parent=None):
    self.val = val
    self.parent = parent
    self.children = []
    if self.parent:
      self.parent.children.append(self)

  def __str__(self):
    return f"[{self.val}]"

  def __repr__(self):
    return str(self)

def add_connectors(lst):
  if len(lst) == 1:
    return lst
  startingFanIndex = None
  endingFanIndex = None
  for i in range(0, len(lst)):
    # if we haven't seen an non empty element yet, only add space
    if lst[i].startswith(" ") and startingFanIndex is None:
      continue
    # mark that we just found the first line that doesn't start with indentation
    if startingFanIndex is None:
      startingFanIndex = i
    # update this index as the index of the latest label
    if not lst[i].startswith(" "):
      endingFanIndex = i
  # prepend connectors
  if startingFanIndex == endingFanIndex:
    return lst
  for i in range(len(lst)):
    if i == startingFanIndex:
      lst[i] = f"┌{lst[i]}"
    elif i == endingFanIndex:
      lst[i] = f"└{lst[i]}"
    elif i > startingFanIndex and i < endingFanIndex:
      if lst[i].startswith(" "):
        lst[i] = f"│{lst[i]}"
      else:
        lst[i] = f"├{lst[i]}"
    else:
      lst[i] = f" {lst[i]}"
  return lst


def labelFan(node, lst):
  name = str(node)
  if len(lst) == 0:
    lst = [name]
  for i in range(len(lst)):
    # add label to the middle of the fan
    if i == len(lst) // 2:
      lst[i] = f"{name}─{lst[i]}"
    else:
      # push the other labels out with indentation
      indent = " " * len(name)
      lst[i] = f"{indent} {lst[i]}"
  return lst

def connectFans(args):
  union = []
  for n in args:
    union += n
  add_connectors(union)
  return union


def printTree(node):
  def get_repr(node):
    if len(node.children) == 0:
      return [str(node)]
    fans = [get_repr(x) for x in node.children]
    labelled = labelFan(node, connectFans(fans))
    return labelled
  print("\n".join(get_repr(node)))


shame = Node("shame")

conscience = Node("conscience", shame)
selfdisgust = Node("selfdisgust", shame)
embarrassment = Node("embarrassment", shame)

selfconsciousness = Node("selfconsciousness", embarrassment)
shamefacedness = Node("shamefacedness", embarrassment)
chagrin = Node("chagrin", embarrassment)
discomfiture = Node("discomfiture", embarrassment)
abashment = Node("abashment", embarrassment)
confusion = Node("confusion", embarrassment)

selfconsciousness2 = Node("selfconsciousness2", selfconsciousness)
shamefacedness = Node("shamefacedness", selfconsciousness2)
chagrin = Node("chagrin", selfconsciousness2)
discomfiture = Node("discomfiture", selfconsciousness2)
abashment = Node("abashment", selfconsciousness2)
confusion = Node("confusion", selfconsciousness2)


#         ┌[conscience]
#         ├[selfdisgust]
#         │                                                          ┌[shamefacedness]
#         │                                                          ├[chagrin]
#         │                ┌[selfconsciousness]─[selfconsciousness2]─├[discomfiture]
#         │                │                                         ├[abashment]
# [shame]─│                │                                         └[confusion]
#         └[embarrassment]─├[shamefacedness]
#                          ├[chagrin]
#                          ├[discomfiture]
#                          ├[abashment]
#                          └[confusion]

printTree(shame)