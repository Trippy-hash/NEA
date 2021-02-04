6.1) State the name of an identifier for a built-in function used in the Skeleton Program that has a string parameter and returns an integer value.
                              
DisplayTileValues 

6.2) State the name of an identifier for a local variable in a method in the
QueueOfTiles class.

MaxSize 
 
[1 mark]
[1 mark]
 


6.3) The QueueOfTiles class implements a linear queue. A circular queue could have been used instead.

Explain why a circular queue is often a better choice of data structure than a linear queue.

A circular queue is better because it takes up less memory and items can be inserted from where previous ones were deleted  
[2 marks]


0	6	.	4)	It could be argued that the algorithms for a linear queue lead to simpler program code.

State one other reason why a linear queue is an appropriate choice in the Skeleton Program even though circular queues are normally a better choice.
			Uses arrays, those are static, cannot reuse a space in data stuctures. 
	[1 mark]

  

0 6	.	5)	State one additional attribute that must be added to the QueueOfTiles class if
		it were to be implemented as a circular queue instead of as a linear queue.

[1 mark]


0	6	.	6)	
Describe the changes that would need to be made to the Skeleton Program so
that the probability of a player getting a one point tile is the same as the
probability of them getting a tile worth more than one point. The changes you
describe should not result in any changes being made to the points value of any
tile.

The generation of the tiles happens in a function called CreateTileDictionary. 
It chooses the predefined letters from the alphabet. You have a 8 / 26 letters 
to get a letter worth one point, 8/26 letters to get a tile worth 2 points,
6 / 26 letters  giving a tile worth three point and 5 / 26 letters will give you 5 points. 
If we try to make all probability equal you cannot split 26 four ways so instead you
must use a list of the alphabet and randomize its designation of points. 
As long as there are 13, 1 point letters then there is a equal chance of one and the other. 


[4 marks]
 

6.7) The GetChoice subroutine uses a built-in function to convert a string to uppercase.

Describe how a string consisting of lowercase characters could be converted to uppercase using only one iterative structure if the programming language being used does not have a built-in function that can do this conversion.
You may assume that only lowercase characters are entered by the user. You should not change the Skeleton Program when answering this question.

I would recommend taking advantage of dictionary’s in this situation, 
it allows to easily set a value and a key which can be ‘Lowercase’: ‘Uppercase’. 
Once the dictionary has been built then take the users input using the input 
function and it .get() of the dictionary and use the input (which will be a letter) 
and have it looked up In the dictionary and then print the output. 

