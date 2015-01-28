#!/usr/bin/env python


##
# binsort.py - Implementation of binary sort
# v2.0
#
# Author: Nick Corso-Passaro
# Date: 12/1/14
# Usage: python binsort.py
##

import csv

#student class to hold student information in student objects
class student(object):
	
	def __init__(self, num, name, age, gpa):
		self.num=int(num)
		self.name=str(name)
		self.age=int(age)
		self.gpa=float(gpa)
	
	def __repr__(self):
		return "{},{},{},{}".format(self.num, self.name, self.age, self.gpa)

def binsort(seq): #binary insertion sort algorithm
	print seq
	for i in range(1, len(seq)):
        	key = seq[i]
		left, right = 0, i
        	while right > left:
            		middle = (left + right) // 2
            		if seq[middle].num < key.num:
                		left = middle + 1              
            		else:
                		right = middle
        	#insert key at position ``low``
        	seq[:] = seq[:left] + [key] + seq[left:i] + seq[i + 1:] #slicing is cool
	print seq
	return seq

if __name__ == "__main__":
	students=[] #array to hold student objects
	reader = csv.reader(open("input.txt"), delimiter=",") #read student information from csv
	for numid, name, age, gpa in reader:
		person = student(numid,name,age,gpa) #create student object for each row in csv
		students.append(person)	#add object to students array
	
	students=binsort(students) #sort students array

	writer = csv.writer(open("output.txt", "w"), delimiter=",") #write student information
	for i in range(0, len(students)):
		writer.writerow([students[i]]) #write each index of array to a row		
