# PositionAwareMerkleTree

In contrast to the typical Merkle Tree, PositionAware Merkle tree consists of nodes with following data
1. Relative position to its parent (i.e right or left child)
2. Hash of the node contents of the children nodes
3. Number of leaf nodes in its subtree

So each node is a tuple (integer(0 or 1), hash, integer(>=1))

Operations proposed
1. Verify 
2. Insert
3. Delete


How does this provide Public verifiability?
Further Algorithms needs be explained

