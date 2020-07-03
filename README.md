# Genetic_Algorithm_Eight_Queens_Problem
Application of Genetic Algorithm in solving eight queens problem

Problem Description :
  The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens   share the same row, column, or diagonal.

Solution Description : 
  This program makes use of genetic algorithm approach to solve this puzzle. By applying crossover and mutations between the offsprings, we finally reach to a fittest generation     wherein we get the desired genes.

Fitness Function : 
  The fitness function calculates the fitness based on the number of Queens in a gene which are safe from attack. As this fitness maximises we receive a solution where all the       Queens are safe from the attack.

Gene : 
  A single gene represents a chess-board representation of Queen positions in the form of a list. Indices represent columns and respective values represents row.
  
Generation :
  A generation represents a population with different genes that will eventually cross and mutate to reach to a fittest gene. It is implemented in the form of list of list.
