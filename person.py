"""
File:    person.py
Author:  Ara Carmel Quinones
Date:    5/11/20
Section: 35
Description:

In Project 3, you will build a family tree program.
This program will allow you to enter people, and then query relations between various people in the family tree.
Another goal is to learn a bit about json and how we can use it to load and save dictionary structures in files.

"""

PARENTS = "parents"
CHILDREN = "children"

class Person:

    def __init__(self, name):
        """
        holds information of the parents and children of a person
        :param name: the name of the person whose information belongs to
        """
        self.person = name
        self.parents = []
        self.children = []

    def jsonify(self):
        """
        puts the information in a certain dictionary format to be use for saving the gaming
        :return: a dictionary of the person's parents and children information
        """
        # returns the information of each person in dictionary format to be used later to save the tree
        return {self.person: {PARENTS: self.parents, CHILDREN: self.children}}
