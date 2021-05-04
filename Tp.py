import Node as nd
import os
#just a trick to clear the screen everytime our program runs 
os.system('cls' if os.name == 'nt' else 'clear')
#main program 
A= input("Enter the word to code:\n")
print("##################################################")
print(f'Word to Code: {A}')
# print("##################################################")
list=nd.sortedL(A)
# print(list)
root=nd.Node([])
nd.FillCodeTree(root,list)
coded_char=nd.printLeafNodes(root)
# print(coded_char)
print("##################################################")
print("Coded word is:",nd.channon_fano(A,coded_char))
