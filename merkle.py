# 0. Import the needed library
import hashlib,json
from collections import OrderedDict
# 1. Declare the class trees



class Jae_MerkTree:
	
	# 2. Initiate the class object
	def __init__(self,curr,listoffileblock=None):
		self.listoffileblock = listoffileblock
		self.past_fileblock = OrderedDict()
		self.curr = curr

	# 3. Create the Merkle Tree  
	def create_tree(self,curr):

		# 3.0 Continue on the declaration
		listoffileblock = self.listoffileblock
		past_fileblock = self.past_fileblock
		temp_fileblock = []
		#i=curr

		# 3.1 Loop until the list finishes
		for index in range(0,len(listoffileblock),2):

			# 3.2 Get the most left element 
			current = listoffileblock[index]
			#print listoffileblock[index]
			# 3.3 If there is still index left get the right of the left most element
			if index+1 != len(listoffileblock):
				current_right = listoffileblock[index+1]
			#	print listoffileblock[index+1]
			# 3.4 If we reached the limit of the list then make a empty string
			else:
				current_right = ''

			# 3.5 Apply the Hash 256 function to the current values
			print "0"+current[0]+str(current[1])
			#current_hash = hashlib.sha256("0"+current[0]+str(current[1]))
			current_hash = ("0"+current[0]+str(current[1]))

			# 3.6 If the current right hash is not a '' <- empty string
			if current_right != '':
				print "1"+current_right[0]+str(current_right[1])
				#current_right_hash = hashlib.sha256("1"+current_right[0]+str(current_right[1]))
				current_right_hash = ("1"+current_right[0]+str(current_right[1]))

			# 3.7 Add the fileblock to the dictionary 
			#past_fileblock[curr] = [0,current_hash.hexdigest(),str(current[1])]
			past_fileblock[curr] = [0,current_hash,str(current[1])]
			curr=curr+1

			# 3.8 If the next right is not empty
			if current_right != '':
				#past_fileblock[curr] = [1,current_right_hash.hexdigest(),str(current_right[1])]
				past_fileblock[curr] = [0,current_right_hash,str(current[1])]
				curr=curr+1

			# 3.9 Create the new list of fileblock
			if current_right != '':
				#temp_fileblock.append([current_hash.hexdigest() + current_right_hash.hexdigest(),current_right[1]+current[1]] )
				temp_fileblock.append([current_hash + current_right_hash,current_right[1]+current[1]] )			
			# 3.01 If the left most is an empty string then only add the current value
			else:
				#temp_fileblock.append([current_hash.hexdigest(),current[1]])
				temp_fileblock.append([current_hash,current[1]])
		
		# 3.02 Update the variables and rerun the function again 
		if len(listoffileblock) != 1:
			self.listoffileblock = temp_fileblock
			self.past_fileblock = past_fileblock

			# 3.03 Call the function repeatly again and again until we get the root 
			self.create_tree(curr)

	# 4. Return the past fileblock 
	def Get_past_transacion(self):
		return self.past_fileblock

	# 5. Get the root of the fileblock
	def Get_Root_leaf(self):
		last_key = self.past_fileblock.keys()[-1]
		return self.past_fileblock[last_key]


# Declare the main part of the function to run
if __name__ == "__main__":
	# a) Create the new class of Jae_MerkTree
	#i=0
	Jae_Tree = Jae_MerkTree(1)
	
	# b) Give list of fileblock
	fileblock = [['a',1],['b',1],['c',1],['d',1],['e',1]]
	# c) pass on the fileblock list 
	Jae_Tree.listoffileblock = fileblock

	# d) Create the Merkle Tree fileblock
	Jae_Tree.create_tree(1)

	# e) Retrieve the fileblock 
	past_fileblock = Jae_Tree.Get_past_transacion()

	# f) Get the last fileblock and print all 
	print 'Final root of the tree : ',Jae_Tree.Get_Root_leaf()
	print(json.dumps(past_fileblock))
	print "-" * 50 

	# h) Second example



# ---- END OF THE CODE ------
