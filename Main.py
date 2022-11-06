class Solution:     def 
__init__(self, size):         self.size 
= size         self.lst =  
[None]*size         self.queue = [None]*size         self.top = -1         self.rear = -1         self.front = 
-1     def 
is_stack_empty(self):         if self.top == -1:             return 1         else:             return 0   
   
def is_queue_empty(self):         if self.front==-1 
or self.front>self.rear:   
            return 1         else:              
return 0     def  is_stack_full(self):         if self.top == (self.size - 1):   
            return 1         else :              
return  0  	  	  	  	 
 def is_queue_full(self):         if self.rear==(self.size-1):   
            return 1          else:             return 0     def  push_character(self, character):         if not self.is_stack_full():             self.top+=1             self.lst[self.top]=character     def enqueue_character(self, character):         if not self.is_queue_full():             if self.front==-1:                 self.front=0             self.rear+=1              self.queue[self.rear]=character   
               
    def pop_character(self):         if  not  	self.is_stack_empty():             t=self.lst[self.top]             del self.lst[self.top]             self.top=1             return t   
    def dequeue_character(self):         if 
not 	self.is_queue_empty():              r=self.queue[0]             del 
self.queue[0]             self.front+=1             return r   
           
text = input() length_of_text = len(text) solution = Solution(length_of_text) for index in range(length_of_text):     solution.push_character(text[index])     
solution.enqueue_character(text[index]) is_palindrome = True a="" b="" for i in range(solution.front,solution.rear+1):      
a+=solution.pop_character()     b+=solution.dequeue_character() if a!=b:      is_palindrome = False else:      is_palindrome = True if is_palindrome:   print("The word, " + text + ", is a palindrome.") 
else:     print("The word, " + text + ", is not a palindrome.")   
