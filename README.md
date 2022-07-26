# WordLadder
The purpose of this repository is to gain experience with graph data structures and algorithms. 

In essence, the script creates a graph from inputted words where the words are neighbors if they have a single letter character difference in exactly the same position. The graph is then used to produce statistics, such as find the number of connected components, and perform tasks, such as find the shortest path between two words.

## Input 
The script reads in a file of 6 letter words (not guaranteed to be sorted, but guaranteed unique, and also all lowercase) and builds a graph from it where words are neighbors if they have a single letter character difference in exactly the same position. The input file provided in this repo is named words.txt. The user can specify which input file they would like to run the script on. 

## Output
The output includes the word count, edge count, degree list, construction time, second degree word, connected component size count, largest component size, k2 count, k3 count, k4 count, neighbors of an inputted word, the word farthests from an inputted word, and the shortest path between two inputted words. 
