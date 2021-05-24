def isPresent(root, val):
    if root == None:
        return 0
    elif root.value == val:
        return 1
    elif root.value > val:
        return isPresent(root.left,val)
    else:
        return isPresent(root.right,val)
        