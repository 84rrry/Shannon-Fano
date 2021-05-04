#Return sorted list of letters based on occurence
def sortedL(s):
    letters={}
    for i in s:
        if i not in letters.keys():
            letters[i]=s.count(i)
        else: continue
    sortedL = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    return sortedL
#Calculate the sum of values
def calc_sum(l):
    s=[m[1] for m in l]
    return sum(s)
# split the lists
def new_list(l):
        Lc=[]
        Rc=[]
        count=0
        i=0
        if len(l)==2:
            Lc.append(l[0])
            Rc.append(l[1])
        else:
            while l[i][1]+count<=calc_sum(l)//2:
                # print('index: ',i)
                count+=l[i][1]
                i+=1
            Lc=l[:i]
            Rc=l[i:]   
        return Lc,Rc
# Function to print leaf
# nodes from left to right
Leaf_nodes={}
def printLeafNodes(root)-> None :
        global Leaf_nodes
        # If node is null, return
        if (not root):
            return 
        # If node is leaf node, 
        # print its data
        if (not root.left and
            not root.right):
            # print(f'character: {root.data[0][0]}',f'Occurence: {root.data[0][1]} times', f'code:{root.code}' )
            Leaf_nodes[root.data[0][0]]=root.code
            return
        # If left child exists 
        # check for leaf recursively
        if root.left:
            
            printLeafNodes(root.left)
        # If right child exists, 
        # check for leaf recursively
        if root.right:
            printLeafNodes(root.right)
        return Leaf_nodes
        
#insert into the coding tree 
def FillCodeTree(root,list):
        if len(list) == 1:
            root.data=list
        else:
            LL=new_list(list)[0]
            # print(LL)
            RL=new_list(list)[1]
            # print(RL)
            root.data=list
            root.left=Node(LL)
            root.left.code=root.code+'0'
            root.right=Node(RL)
            root.right.code=root.code+'1'
            FillCodeTree(root.left,root.left.data)
            FillCodeTree(root.right,root.right.data)
#Code the word
def channon_fano(word,dic):
    s=''
    for i in word:
        s+=dic[i]+' '
    return s

# node class
class Node:
    def __init__(self, data):
        # left child
        self.left = None
        # right child
        self.right = None
        # node's value
        self.data = data
        #charecter Code
        self.code=""
    
