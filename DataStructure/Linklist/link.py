class Node():

	def __init__(self,data):
		
		self.data=data
		self.next=None

class Linklist():

	def __init__(self):

		self.head=None


	def InsertAtFirst(self,new_data):

		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node

	def InsertAtBetween(self,prev_node,new_data):


		if prev_node is None:
			print('previous node not in the given linklist')

		new_node=Node(new_data)
		new_node.next=prev_node.next
		prev_node.next=new_node

	def InsertAtLast(self,new_data):

		new_node=Node(new_data)

		if self.head is None:
			self.head=new_node
			return

		last=self.head
		while(last.next):
			last=last.next
		last.next=new_node



	def DeleteByKey(self,skey):

		temp=self.head

		if temp is not None:

			if temp.data==skey:
				self.head=temp.next
				temp=None
				return

		if temp is not None:

			if temp.data==skey:
				break
			prev=temp
			temp=temp.next

		if temp is None:
			return

		prev.next=temp.next
		temp=None

	def DeleteByPosition(self,pos):

		if self.head is None:
			return

		temp=self.head
		
		if pos==0:
			self.head=temp.next
			temp=None
			return

		for i in range(pos-1):
			temp=temp.next
			if temp is None:
				break
		if temp is None:
			return
		if temp.data is None:
			return

		next=temp.next.next
				
		temp.next=None
		temp.next=next

	def DeleteWholeNode(self):

		prev=None
		current=self.head
		while(current!=None):
			prev=current.next
			del current
			current=prev

	def NodeCount(self):

		current=self.head
		count=0
		while(current!=None):

			count+=1
			current=current.next
		return count
		
	def SearchNode(self,snode):
		
		temp=self.head
		while(temp!=None):

			if temp.data==snode:
				return True

			temp=temp.next

		return false				

	def NodeDataAtGivenPosition(self,index):

		temp=self.head
		count=0
		while(temp is not None):
			if count==index:
				print(temp.data)
			count+=1
			temp=temp.next

	def MiddleElementOfLinklist(self):
	
		mid=self.head
		count=0
		while(self.head is not None):

			if (count & 1):

				mid=mid.next
			count+=1
			self.head=self.head.next

		print("Middle node of the given linklist:",mid.data)
		
	def MiddleElementOfLinklist2(self):
		fast_p=self.head
		slow_p=self.head

		if self.head is not None:

			while(fast_p!=None and fast_p.next!=None):

				fast_p=fast_p.next.next	
				slow_p=slow_p.next

			print("Middle Node Of The  Given LinkList:",slow_p.data)
			

	def DetectLoop(self):
		
		slow_p=self.head
		fast_p=self.head

		while(slow_p and fast_p and fast_p.next):

			slow_p=slow_p.next
			fast_p=fast_p.next.next

			if slow_p==fast_p:
				print("Loop is Detect")
				return
			else:
				print("Loop not Detect")

	def DetectLoop(self):
		s=set()
		temp=self.head
		while(temp):

			if (temp in s):

				return True
			s.add(temp)
			temp=temp.next

	def RemoveDuplicateNode(self):
		
		first_n=self.node

		while(first_n!=None and first_n.next!=None):

			second_n=first_n

			while(second_n!=None):

				if first_n.data==second_n.next.data:

					duplicate=second_n.next
					second_n.next=second_n.next.next
					duplicate=None	
				
				second_n=second_n.next

			first_n=first_n.next	

	def ReverseLinklist(self):
	
		prev=None
		next=None
		current=self.head
		while(current!=None):

			next=current.next
			current.next=prev
			prev=current
			current=next
		self.head=prev			

	def SwappingDataWithoutSwappingNode(self,node1,node2):

		prev_node1=None
		current_node1=self.head
		
		while(current_node1 != None and current_node1.next != None ):

			prev_node1=current_node1
			current_node1=current_node1.next

		prev_node2=None
		current_node2=self.head

		while(current_node2!=None and current_node2.next != None):

			prev_node2=current_node2
			current_node2=current_node2.next

		if prev_node1 is not None:
			prev_node1.next=current_node2
		else:
			self.head=current_node2

		if prev_node2 is not None:
			prev_node2.next=current_node1
		else:
			self.head=current_node1

		temp=current_node1.next
		current_node1.next=current_node2.next
		current_node2.next=temp				
				

			


				
	def PrintLinklist(self):

		temp=self.head
		while(temp):
			print(temp.data)
			temp=temp.next


l=Linklist()
l.InsertAtFirst(6)
l.InsertAtFirst(4)
l.InsertAtFirst(3)
l.InsertAtFirst(2)
l.InsertAtFirst(1)
l.InsertAtBetween(l.head.next.next.next,5)
l.InsertAtLast(10)
l.PrintLinklist()


			

			
		
		


