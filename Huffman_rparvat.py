from queue import PriorityQueue

class huffman_code:
    def __init__(self, char,freq, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
# Reading the text file and passing the data into frequency function to form a dictionary lookup table.
def load_text(filename):
    word_count = {}
    with open(filename, 'r', encoding='ascii',errors='ignore') as infile:
        lines = infile.readlines()
        for i in lines:
           freq = frequency(i.strip('\n'), word_count)
        infile.close()
    return freq
#Calculate the Lookup dictionary table.
def frequency(text,word_count ):
    for sentence in text:
        for char in sentence:
            if char not in word_count:
                word_count[char] = 1
            else:
                word_count[char] += 1
    return word_count

#Build the Huffman Tree .
def build_h_tree(prior_q,node_dictionary):
    while prior_q.qsize() > 1 :
        left = node_dictionary[prior_q.get()[1]]
        right = node_dictionary[prior_q.get()[1]]
        freq = left.freq + right.freq
        tree_final = huffman_code("node", freq,left,right)
        node_dictionary[tree_final.__hash__()] = tree_final
        prior_q.put((tree_final.freq, tree_final.__hash__()))
    _,tree=prior_q.get()
    return node_dictionary[tree]

# refered the walk down from :: https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding
def assign_codes(node,str,code_d):
    if node.left:
        assign_codes(node.left,str+"0",code_d)
    if node.right:
        assign_codes(node.right,str+"1",code_d)
    if node.left == None and node.right == None:
        code_d[node.char] = (node.freq,str)

if __name__ == "__main__":
    path = "C:\\Users\\rutvi\\PycharmProjects\\Algo\\Book\\thelogoftheark.txt"
    text_data_freq = load_text(path)
    sorted_freq = sorted(text_data_freq.items(), key=lambda x: x[1])
    print(sorted_freq)
    prior_q = PriorityQueue()
    char_dict = {}
    n_dictionary = {}
    code_dictionary = {}

    #enter values into priority queue
    for node in sorted_freq:
        h = huffman_code(node[0],node[1])
        n_dictionary[h.__hash__()] = h
        prior_q.put((h.freq, h.__hash__()))

    #build Huffman Tree
    huffman_tree = build_h_tree(prior_q,n_dictionary)
    #Walking down to assign Huffman Codes.
    assign_codes(huffman_tree,'',code_dictionary)
    #Sort the list to display the solution.
    Solution_list = sorted(code_dictionary.items(), key=lambda x: x[1][0], reverse=True)
    for i in Solution_list:
        print("   " + i[0] + "        " + str(i[1][0]) + "           " + i[1][1])
    #Calculate number of bits for ascii encoding
    total_freq = 0
    for i,j in text_data_freq.items():
        total_freq += j
    print("The bits required for calculating the ascii code ::",total_freq * 7)
    acii_val = total_freq*7
    #Calculate number of bits for huffman encoding
    total_y = 0
    for p in Solution_list:
        total_y += p[1][0]* (len(p[1][1]))
    print("The bits required if huffman encoding is used is :",total_y)
    #Calculate number of bits for huffman look-up table
    # total_z = 0
    # for k in Solution_list:
    #     total_z += 7 + (len(k[1][1]))
    # print("the huffman table is : ",total_z)
    # #Calculate number of bits for the final saving (including the size of the huffman table)
    # print("The final saving (including huffman table bits) :",acii_val-(total_y))
    # #calculate number of bits for the final saving (not including the size of the huffman table)
    print("---------------------------------------------------")
    print("The final bits saving  :",acii_val-total_y)










