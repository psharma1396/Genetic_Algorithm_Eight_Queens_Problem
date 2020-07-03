import random

class Gene:

	def __init__(self,size,minval,maxval):
		self.size=size
		self.minval=minval
		self.maxval=maxval
		
	def generate(self):
		genes_array=[random.randint(self.minval,self.maxval) for i in range(self.size)]
		return genes_array

		
class Genetic_Algorithm:
	
	def __init__(self,size,min,max):
		self.size=size
		self.min=min
		self.max=max
		
	def fitness_function(self,nums):
		fitness=0
		skip=[] #for tracking the preceding genes
		
		for i in range(len(nums)-1):
			a=i
			b=nums[i]
				
			flag=0	
			for j in range(i+1,len(nums)):
				x=j
				y=nums[j]
				
				if x!=a and y!=b and abs((y-b))!=abs((x-a)):
					continue
					
				else:
					flag+=1
					skip.append(j)
					
			if flag==0 and i not in skip:
				fitness+=1
		
		
		if fitness==self.size-1 and len(set(nums))==self.size:
			fitness+=1
			
		return fitness
		
	def crossover(self,nums1,nums2):
		midval=self.size//2
		crossed=nums1[0:midval]
		for i in range(midval,len(nums1)):
			crossed.append(nums2[i])
		return crossed
		
	def mutation(self,nums):
		a=random.randint(self.min,self.max)
		i=random.randint(0,self.size-1)
		mutated=nums
		if a!=nums[i]:
			mutated[i]=a
		else:
			mutated[i]=(a+1)%self.size
		return mutated	

		
class Generation(Genetic_Algorithm):

	def __init__(self,generation_size,genesize,min,max):
		Genetic_Algorithm.__init__(self,genesize,min,max)
		self.generation=[]
		self.generation_size=generation_size
		self.genesize=genesize
		
	def inital_generation(self):
		for i in range(self.generation_size):
			self.generation.append(Gene(self.genesize,self.min,self.max).generate())
		return self.generation
	
	def sort_population(self,population):
		fitness=[self.fitness_function(nums) for nums in population]
			
		population = [i for i in zip(population,fitness)]
		population.sort(key=lambda x:x[1],reverse=True)
		return population
	
	def child_generation(self,randlist):
		child_gen=[]
		
		population=self.sort_population(randlist)
		
		
		passing=40*len(randlist)//100
		mutating=20*len(randlist)//100
		crossing=len(randlist)-(passing+mutating)
		
		
		### Distributing the cross over, mutation and passing over generation ####
		
		
		# Passing over 
		
		for a,b in population[:passing]:
			child_gen.append(a)
		
		# Crossing over
		
		for i in range(crossing):
			parent1=random.choice(population[:])[0]
			parent2=random.choice(population[:])[0]
			cross_seq=self.crossover(parent1,parent2)
			child_gen.append(cross_seq)
			
		# Mutating
		
		for i in range(mutating):
			parent=random.choice(population[0:passing])[0]
			mut_seq=self.mutation(parent)
			child_gen.append(mut_seq)
			
		
		return child_gen
		
def main():

	generation=Generation(8,8,0,7)
	parents=generation.inital_generation()
	print(parents)
	found=False
	generation_age=0
	while not found:
		population=generation.sort_population(parents)
		print("fitness: ")
		print(population[0][1])
		
		if population[0][1]==8:
			found=True
	
		generation_age+=1
		
		print("Generation {}  : {} ".format(generation_age,population[0][0]))
		
		childs=generation.child_generation(parents)
		parents=childs
		
if __name__=='__main__':
	main()

