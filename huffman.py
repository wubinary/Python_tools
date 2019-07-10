import numpy as np
from ete3 import Tree

class HuffmanTreeLeaf():
    def __init__(self,value,possibility):
        self.value = value #in integer 用十進位表示
        self.possibility = possibility
        self.left = None
        self.right = None
        self.code = []
        self.code_string = ''
    def __str__(self):
        return 'HuffmanTreeLeaf Object, value: {v}, possibility: {p}, code: {c}'.format(v=self.value,p=self.possibility,c=self.code_string)

class HuffmanTreeNode():
    def __init__(self,possibility):
        self.possibility = possibility
        self.left = None
        self.right = None
        self.code = []
        self.code_string = ''
        self.code_len_size = 0
        self.leaf_list = []
    def __str__(self):
        return 'HuffmanTreeNode Object, possibility: {p}, code: {c}'.format(p=self.possibility,c=self.code_string)

class HuffmanTree():
    def __init__(self,counts_prob):
        self.root_node = None
        counts_prob = sorted(counts_prob, key=lambda x:x[1] ) #Ascend sorting    EX: [('quick',0.1),('fox',0.2),('cats',0.3),('dogs',0.4)]  從機率小到機率大
        leaf_list = []
        self.leaf_list = []
        for item in counts_prob:
            leaf = HuffmanTreeLeaf(item[0],item[1])
            leaf_list.append(leaf)
            self.leaf_list.append(leaf)
        #leaf_list = [HuffmanTreeLeaf(item[0],item[1]) for item in counts_prob]
        self.build_tree(leaf_list)
        
    def build_tree(self,node_leaf_list):
        i0 = 0 #possibility smallest leaf or node   當前node_leaf_list中機率最小的
        i1 = 1 #possibility second small leaf or node   當前node_leaf_list中機率第二小的
        while len(node_leaf_list)>1:
            top_node = self.merge(node_leaf_list[i0],node_leaf_list[i1])
            node_leaf_list.pop(i1)
            node_leaf_list.pop(i0)
            j = 0
            while(len(node_leaf_list)>0 and j!=len(node_leaf_list)-1 and node_leaf_list[j].possibility<top_node.possibility):
                j=j+1
            node_leaf_list.insert(j,top_node)
        self.root_node = node_leaf_list[0]
        self.generate_huffman_code(self.root_node)
        self.string = self.huffman_tree_string(self.root_node)
        
    def generate_huffman_code(self,node):
        if(node.left!=None):
            node.left.code = node.code+[0]
            node.left.code_string = node.code_string+'0'
            self.generate_huffman_code(node.left)
        if(node.right!=None):
            node.right.code = node.code+[1]
            node.right.code_string = node.code_string+'1'
            self.generate_huffman_code(node.right)
            
    def huffman_tree_string(self,node):
        if(node.left!=None):
            s0 = self.huffman_tree_string(node.left)
        else:
            s0 = ''
        if(node.right!=None):
            s1 = self.huffman_tree_string(node.right)
        else:
            s1 = ''
        if(node.left==node.right==None):
            return '{:->12} {:->20}  {:.5f}'.format(node.value,node.code_string,node.possibility)
        return '({},{});'.format(s0,s1)

    def draw_tree(self):
        t = Tree( self.string )
        t.show()
        
    def merge(self,node1,node2):
        possibility = node1.possibility+node2.possibility
        top_node = HuffmanTreeNode(possibility)
        #right bigger ,left smaller  左邊放大的,右邊放小的
        if node1.possibility >= node2.possibility :
            top_node.left = node2
            top_node.right = node1
        else:
            top_node.left = node1
            top_node.right = node2
        return top_node
    
    def __str__(self):
        return 'HuffmanTree Object'

     
'''huffmanTree = HuffmanTree([['cats', 0.16129032258064516], ['dogs', 0.0967741935483871], ['and', 0.08064516129032258], ['are', 0.06451612903225806],
                           ['love', 0.04838709677419355], ['the', 0.03225806451612903], ['great', 0.03225806451612903], ['sung', 0.03225806451612903],
                           ['be', 0.03225806451612903], ['quick', 0.016129032258064516], ['brown', 0.016129032258064516], ['fox', 0.016129032258064516],
                           ['jumped', 0.016129032258064516], ['over', 0.016129032258064516], ['lazy', 0.016129032258064516], ['dog', 0.016129032258064516],
                           ['I', 0.016129032258064516], ['we', 0.016129032258064516], ['all', 0.016129032258064516], ['likes', 0.016129032258064516],
                           ['she', 0.016129032258064516], ['loves', 0.016129032258064516], ['can', 0.016129032258064516], ['very', 0.016129032258064516], 
                           ['independent', 0.016129032258064516], ['companions', 0.016129032258064516], ['when', 0.016129032258064516], ['they', 0.016129032258064516], 
                           ['want', 0.016129032258064516], ['to', 0.016129032258064516], ['playful', 0.016129032258064516], ['natural', 0.016129032258064516],
                           ['hunters', 0.016129032258064516], ["It's", 0.016129032258064516], ['raining', 0.016129032258064516]])
'''
#print(huffmanTree.huffman_tree_string(huffmanTree.root_node))
