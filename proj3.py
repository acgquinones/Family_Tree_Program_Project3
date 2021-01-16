"""
File:    proj3.py
Author:  Ara Carmel Quinones
Date:    5/11 /20
Section: 35
E-mail:  aquinon1@umbc.edu
Description:

In Project 3, you will build a family tree program.
This program will allow you to enter people, and then query relations between various people in the family tree.
Another goal is to learn a bit about json and how we can use it to load and save dictionary structures in files.

"""
import json
from person import Person

ADD = "add"
RELATE = "relate"
GET_CHILDREN = "get children"
GET_SIBLINGS = "get siblings"
GET_DESCENDANTS = "get descendants"
GET_COUSINS = 'get cousins'
GET_PARENTS = "get parents"
GET_GRANDPARENTS = "get grandparents"
GET_ANCESTORS = "get ancestors"
SAVE_TREE = "save tree"
LOAD_TREE = "load tree"
QUIT = 'quit'
TWO_PARENTS = 2
ONE_PARENT = 1
ZERO_PARENT = 0
UNKNOWN_PARENTS = 'unknown'
PARENTS = "parents"
CHILDREN = "children"

class DynasticDescent:

    def __init__(self):

        self.family_tree = {}

    def play(self):
        """
        this is the main function of this program that adds and relate people in the family tree, saves and load the game, and get information from the family tree.
        :return: does not return anything
        """
        what_to_do = input("What would you like to do next? ").lower().strip()

        while what_to_do != QUIT:

            if what_to_do == ADD:
                name = input("\twhat is the name of the human? ")
                new_person = Person(name)
                family_names = list(self.family_tree.keys())
                # make sure the person is not already added
                if name not in family_names:
                    self.family_tree[name] = new_person
                    print("\t" + name, "has been added to the family tree.")
                else:
                    print("\tThe name already exist.")

            elif what_to_do == RELATE:
                parent_human = input("\twhat is the name of the parent human? ")
                child_human = input("\twhat is the name of the child human? ")
                # all the names already added as a list
                added_names = list(self.family_tree.keys())
                # if the parent and child has been added, continue with the program
                if parent_human in added_names and child_human in added_names:
                    # same name cannot be both the parent and the child
                    if parent_human != child_human:
                        # checks how many parents the child has at the moment
                        total_parents = len(self.family_tree[child_human].parents)
                        # list of the child's parents
                        parents_list = list(self.family_tree[child_human].parents)
                        # list of children
                        children_list = self.family_tree[parent_human].children
                        # print("length of parents", len(self.family_tree[child_human].parents))

                        if parent_human.lower() != UNKNOWN_PARENTS:
                            if total_parents == ZERO_PARENT or total_parents == ONE_PARENT:

                                # if parent_human and child_human doesn't exist, add the parent and child to their list
                                if parent_human not in parents_list and child_human not in children_list:
                                    # this add the parent to the child's parents list
                                    self.family_tree[child_human].parents.append(parent_human)
                                    # add the child to each parent's children list
                                    self.family_tree[parent_human].children.append(child_human)

                                    print("\t" + parent_human, "and", child_human, "are now related.")

                                # if parent_human exist, but the child doesn't, only add the child
                                elif parent_human in parents_list and child_human not in children_list:
                                    for parent in parents_list:
                                        parent_children = self.family_tree[parent].children
                                        # check if child in already in the list before adding the child
                                        if child_human not in parent_children:
                                            self.family_tree[parent].children.append(child_human)

                                    print("\t" + parent_human, "already exist.")
                                    print("\t" + parent_human, "and", child_human, "are now related.")

                                # if parent_human doesn't exist, but the child exist, only add the parent
                                elif parent_human not in parents_list and child_human in children_list:
                                    # add the parent
                                    self.family_tree[child_human].parents.append(parent_human)
                                    print("\t" + child_human, "already exist.")
                                    print("\t" + parent_human, "and", child_human, "are now related.")

                                # if both parent and child exist, do not do anything
                                else:
                                    print("\t" + parent_human, "and", child_human, "already exist.")

                            elif total_parents == TWO_PARENTS:

                                # if parent_human exist, but the child_human doesn't, only add the child
                                if parent_human in parents_list and child_human not in children_list:
                                    for parent in self.family_tree[child_human].parents:
                                        parent_children = self.family_tree[parent].children
                                        # check if child in already in the list before adding the child
                                        if child_human not in self.family_tree[parent].children:
                                            self.family_tree[parent].children.append(child_human)
                                    print("\t" + parent_human, "already exist.")
                                    print("\t" + parent_human, "and", child_human, "are now related.")

                                # if parent_human doesn't exist, but child exist, do not add parent and do not add child
                                elif parent_human not in parents_list and child_human in children_list:
                                    print("\t" + child_human, "can only have a maximum of 2 parents.")

                                # if both the parent and child exist, do not do anything
                                else:
                                    print("\t" + parent_human, "and", child_human, "were already related.")

                        # parent is unknown
                        elif parent_human.lower() == UNKNOWN_PARENTS:

                            if parent_human in added_names and child_human in added_names:
                                # if parent is unknown, append "unknown" to parent list and the child to children list
                                if parent_human not in parents_list and child_human not in children_list:
                                    self.family_tree[child_human].parents.append(parent_human)
                                    self.family_tree[parent_human].children.append(child_human)
                                    print("\t" + parent_human, "and", child_human, "are now related.")

                                # if unknown parent exist, but the child doesn't, only add the child
                                elif parent_human in parents_list and child_human not in children_list:
                                    self.family_tree[parent_human].children.append(child_human)
                                    print("\t" + parent_human, "already exist.")
                                    print("\t" + parent_human, "and", child_human, "are now related.")

                                # if unknown doesn't exist, but the child exist, only add unknown parent
                                elif parent_human not in parents_list and child_human in children_list:
                                    self.family_tree[child_human].parents.append(parent_human)
                                    print("\t" + child_human, "already exist.")
                                    print("\t" + parent_human, "and", child_human, "are now related.")

                                # if both unknown parent and child exist, do not do anything
                                else:
                                    print("\t" + parent_human, "and", child_human, "already exist.")

                # if a name was not added first before "relate", do not relate anyone
                else:
                    if parent_human not in added_names:
                        print("\t" + "You must add", parent_human, "to the family before you can relate to anyone.")
                    if child_human not in added_names:
                        print("\t" + "You must add", child_human, "to the family before you can relate to anyone.")

            elif what_to_do == GET_CHILDREN:

                # function call
                self.get_children()

            elif what_to_do == GET_SIBLINGS:
                # function call
                self.get_siblings()

            elif what_to_do == GET_DESCENDANTS:
                starting_human = input("\twhat is the name of starting human? ")
                added_names = list(self.family_tree.keys())
                # makes sure the name is added first
                if starting_human not in added_names:
                    print(starting_human, "is not in the family tree. ")

                degree_descents = int(input("\twhat is the degree of descent? "))
                list_of_children = self.family_tree[starting_human].children
                # function call to get descendants
                descendants = self.get_descendants(list_of_children, degree_descents)

                print("\tThe level", degree_descents, "descendants of", starting_human, "are:", descendants)

            elif what_to_do == GET_PARENTS:
                # function call
                self.get_parents()

            elif what_to_do == GET_GRANDPARENTS:
                # function call
                self.get_grandparents()

            elif what_to_do == GET_ANCESTORS:
                starting_human = input("\twhat is the name of starting human? ")
                added_names = list(self.family_tree.keys())
                # checks if the name is added first
                if starting_human not in added_names:
                    print(starting_human, "is not in the family tree.")

                degree_ancestors = int(input("\twhat is the degree of descent?"))
                list_of_parents = self.family_tree[starting_human].parents
                # function call to get ancestors
                ancestors = self.get_ancestors(list_of_parents, degree_ancestors)
                print("\tThe level", degree_ancestors, "ancestors of", starting_human, "are:", ancestors)

            elif what_to_do == SAVE_TREE:
                file_name = input('What file name do you want to save as? ')
                # function call
                self.save(file_name)

            elif what_to_do == LOAD_TREE:
                file_name = input('What file name do you want to load? ')
                # function call
                self.load(file_name)

            what_to_do = input("What would you like to do next? ").lower().strip()


    def get_children(self):
        """
        finds the children of a person
        :return: print function
        """
        person = input("\twhat is the name of the human? ")
        children = self.family_tree[person].children

        print("\tThe children are: ", ",".join(children))

    def get_siblings(self):
        """
        this finds the siblings of a person
        :return: print function
        """
        # keeps track of the children
        children_list = []

        name = input("\twhat is the name of the human? ")
        parents = self.family_tree[name].parents
        # finds each children of the parent and gets added the children list
        for i in range(len(parents)):
            children = self.family_tree[parents[i]].children
            children_list.extend(children)
        # removes the name of the human given to be left with just the sibings
        children_list.remove(name)

        print("\tThe siblings of", name, "are: ", ",".join(children_list))

    def get_descendants(self, the_children, degree):
        """
        finds the descendants of a person from 1st degree to however many

        :param the_children: the children of the starting human
        :param degree: the degree of the descendant from children to great great children etc
        :return: list of children
        """

        list_of_children = list(the_children)
        length_children = len(list_of_children)
        # program ends when degree hits 1 and returns a list of parents na,e
        if degree == 1:
            return ",".join(list_of_children)
        # return nothing if there are not parents or parent is unknown
        elif length_children == 0:
            return
        # recursion call
        else:
            # keep calling the function to get the parents of the parent
            child = self.get_descendants(self.family_tree[list_of_children[0]].children, degree - 1)
            # remove that parent so we can find the next parent's parents
            list_of_children.remove(list_of_children[0])
            # call the function again which will then lead us to next list of parents' parents to look for
            return child

    def get_parents(self):
        """
        finds the parents of the starting human
        :return: print function
        """

        person = input("\twhat is the name of the human? ")
        # the person parents
        parents = self.family_tree[person].parents

        print("\tThe parents are: ", ",".join(parents))

    def get_grandparents(self):
        """
        finds the grandparents of a person
        :return: print fucntion
        """

        grandparents = []

        person = input("\twhat is the name of the human? ")
        # the person's parents
        parents = self.family_tree[person].parents
        # this is the parent's parents
        for name in parents:
            grandparents.extend(self.family_tree[name].parents)

        print("\tThe grandparents are: ", ",".join(grandparents))

    def get_ancestors(self, the_parents, degree):
        """
        find the ancestors of a person. From parents to great-great grandparents and etc
        :param the_parents: a list of the starting person's parents
        :param degree: the degree of how far the ancestor the program should look back to
        :return: list of the person's ancestors
        """

        list_of_parents = list(the_parents)
        length_parents = len(list_of_parents)
        # program ends when degree hits 1 and returns a list of parents na,e
        if degree == 1:
            return ",".join(list_of_parents)
        # return nothing if there are not parents or parent is unknown
        elif length_parents == 0 or list_of_parents[0] == UNKNOWN_PARENTS:
            return
        # recursion call
        else:
            # keep calling the function to get the parents of the parent
            ancestor = self.get_ancestors(self.family_tree[list_of_parents[0]].parents, degree - 1)
            # remove that parent so we can find the next parent's parents
            list_of_parents.remove(list_of_parents[0])
            # call the function again which will then lead us to next list of parents' parents to look for
            return ancestor

    def save(self, filename):
        """
        saves the family tree using json.dumps

        :param filename: the name the user wants to name the file
        :return: print function
        """
        # keeps track of each person's dictionary information
        person_class_dictionary = {}
        # loops through each name in the family and gets added to person_class_dictionary
        for person in self.family_tree:
            person_class_dictionary.update(self.family_tree[person].jsonify())
        # writes the person_class_dictionary to the name of the file the user wanted
        # uses json.dumps to be able to write the dictionary format to a file by converting them to string
        with open(filename, "w") as game_file:
            game_file.write(json.dumps(person_class_dictionary))

        print("\tTree saved.")

    def load(self, filename):
        """
        loads information from a file and uses json.loads to convert the data from string back to dictionary/lists

        :param filename: the filename the user wants to load
        :return: print function
        """
        # opens and closes the file given in read mode
        with open(filename, 'r') as read_json:
            the_entire_file = read_json.read()
            # converts data from string to dictionary
            the_entire_dictionary = json.loads(the_entire_file)
            # reset family tree
            self.family_tree = {}
            # start loading names and their content from the file
            for person in the_entire_dictionary:
                # person becomes dict key and person becomes class Person object as dict value
                self.family_tree[person] = Person(person)
                # assigns the parents and children to its respective names that it belongs to
                person_parents = the_entire_dictionary[person][PARENTS]
                person_children = the_entire_dictionary[person][CHILDREN]
                # assigns the parents and children to its respective names that it belongs to
                self.family_tree[person].parents = person_parents
                self.family_tree[person].children = person_children

        print("\tTree loaded.")


if __name__ == '__main__':
    game = DynasticDescent()
    game.play()
