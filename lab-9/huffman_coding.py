import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(chars, freqs):
    heap = []

    # Create leaf nodes
    for c, f in zip(chars, freqs):
        heapq.heappush(heap, Node(f, c))

    # Build the tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, merged)

    return heap[0]


def get_code_lengths(node, depth=0, code_lengths={}):
    if node is None:
        return

    # Leaf node
    if node.char is not None:
        code_lengths[node.char] = depth
        return

    get_code_lengths(node.left, depth + 1, code_lengths)
    get_code_lengths(node.right, depth + 1, code_lengths)

    return code_lengths


def total_encoded_length(chars, freqs):
    root = build_huffman_tree(chars, freqs)
    code_lengths = get_code_lengths(root)

    total = 0
    for c, f in zip(chars, freqs):
        total += f * code_lengths[c]

    return total, code_lengths


# Input
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freqs = [5, 9, 12, 13, 16, 45]

# Compute
total_bits, code_lengths = total_encoded_length(chars, freqs)

print("Code Lengths:", code_lengths)
print("Total Encoded Length:", total_bits)