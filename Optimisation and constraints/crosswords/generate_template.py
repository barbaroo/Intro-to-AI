import sys
from collections import deque

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()


    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP - enforce arc consistency and search for the solution.
        """
        self.___()
        self.___()
        return self.___(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable, words in self.domains.items():  # Iterate over all variables and their potential words
            words_to_remove = set()  # Set to store words that will be removed from the variable's potential words
            for word in ___:
                if len(word) != variable.___:  # If word is not of the same length as the variable can hold, delete
                    ___.add(___)
            # Subtract the words that are unsuitable from variable's domain
            self.domains[variable] = words.difference(words_to_remove)

    def revise(self, x, y):
        """

        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = ___  # set revised to false to see if any consistency will be set
        overlap = self.crossword.___[x, y]  # find the overlap between two nodes (place in grid that they share)

        if overlap:
            v1, v2 = overlap
            xs_to_remove = set()  # store all x domains to remove
            for x_i in self.___[x]:
                overlaps = ___  # find if there is x variable that overlaps with y variable
                for y_j in self.___[y]:
                    if x_i != y_j and x_i[v1] == y_j[v2]:
                        overlaps = ___
                        break
                if not ___:  # if there is no overlap in variables, remove x variable
                    xs_to_remove.add(x_i)
            if xs_to_remove:  # if there are x variables to remove from the x domain, remove
                self.domains[x] = self.domains[x].difference(___)
                revised = ___  # set revised to true to shows that a revision was made

        return revised

    def ac3(self, arcs=None):
        """

        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:  # if given arcs is none, initialize a queue with all edges (arcs)
            arcs = deque()
            for v1 in self.crossword.___:
                for v2 in self.crossword.___(v1):
                    ___.appendleft((v1, v2))
        else:  # if given arcs is not None, convert the list to deque
            ___ = deque(___)

        while arcs:
            x, y = ___.pop()
            if self.___(x, y):  # revise each combination of nodes in an edge (arc)
                # if there are no variables for x, return False, meaning that arc
                # consistency is impossible
                if len(self.domains[x]) == 0:
                    return False

                # take all x's neighbors except Y and add the edges between them and x to the queue
                for z in self.crossword.___(x) - {y}:
                    arcs.appendleft((___, ___))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # traverse over all variables in the crossword
        for variable in self.crossword.variables:
            # if variable is not in the assignment, meaning it doesn't have a
            # word assigned to it, return False
            if variable not in ___.keys():
                return False
            # if variable is in the assignment and the word assigned to it
            # is not among words that are still available, return False
            if assignment[___] not in self.crossword.___:
                return False
        # Otherwise everything is nice, return True
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for variable_x, word_x in assignment.items():
            if variable_x.length != len(word_x):  # check if assigned word is of the proper length for the variable
                return ___

            for variable_y, word_y in assignment.items():
                if variable_x != variable_y:
                    # check if the word assigned to variable x is unique (not used in other variables)
                    if word_x == ___:
                        return ___

                    # check if the variables have an overlap in their characters
                    overlap = self.crossword.___[___, ___]  # it returns indices where they overlap
                    if ___:  # if there is an overlap, make sure that the certain character is the same
                        a, b = overlap
                        if word_x[a] != word_y[b]:  # if the characters are different, then it is inconsistent
                            return ___

        return ___

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # find all neighbors of the given variable
        neighbors = self.crossword.neighbors(var)
        # traverse over the assignment and see if some neighboring variables are already assigned a word
        for variable in assignment:
            # if variable is in neighbors and in assignment, it already has a value and is not considered a neighbor
            if variable in neighbors:
                neighbors.remove(variable)

        # initialize a result list that will be sorted according to heuristics (least-constraining values)
        result = []
        for variable in self.domains[var]:
            ruled_out = 0  # keep count of how many domain options will be ruled out from neighboring variables
            for neighbor in neighbors:
                for variable_2 in self.domains[neighbor]:
                    overlap = self.crossword.overlaps[var, neighbor]

                    # if there is overlap between variables,
                    # then the one of them can't have that domain anymore
                    if overlap:
                        a, b = overlap
                        if variable[a] != variable_2[b]:
                            ruled_out += 1
            # store the variable with the number of options it will rule out from its neighbors
            result.append([variable, ruled_out])

        # sort all variables by the number of ruled out domain options they will eliminate
        result.sort(key=lambda x: x[1])
        return [i[0] for i in result]  # return only the list of variables, without the ruled_out parameter

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # initialize a list of potential variables to consider with heuristics (minimum remaining value and degree)
        potential_variables = []
        for ___ in self.crossword.___:  # iterate over all variables in the crossword
            if variable not in ___:  # if the variable is unassigned (meaning it is not in assignment)
                # then add it to potentials with the number of domain options (minimum remaining value heuristic)
                # and number of neighbors (degree heuristic)
                potential_variables.append([___, len(self.___[variable]), len(self.crossword.___(variable))])

        # sort potential variables by the number of domain options (ascending) and number of neighbors (descending)
        if potential_variables:
            potential_variables.sort(key=lambda x: (x[1], -x[2]))
            return potential_variables[0][0]

        # If there are no potential variables, simply return None
        return None

    def backtrack(self, assignment):
        """
        USE PSEUDOCODE FROM THE LECTURE NOTES

        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # assignment is already complete (all variables have words), simply return assignment
        if self.assignment_complete(assignment): return assignment

        # select an unassigned variable to choose its domain (word)
        variable = self.___(___)

        # traverse over all values in the domain that it sorted with heuristics (least constraining values)
        for value in self.order_domain_values(___, ___):
            # assign the variable selected to assignment to see if it fits
            assignment[variable] = ___
            # if the assignment remains consistent (all words unique and all overlaps are of the same characters)
            if self.___(assignment):
                # recursive call on this method to see if further values that arise from this choice are consistent
                result = self.___(___)
                if result:  # if the result received assignment (base case is on line 289), then the variable works
                    return result

                # if the result did not receive assignment (received None), then remove the variable from assignment,
                # as it doesn't produce a solution
                assignment.pop(___, None)

        # return None if the chosen variable does not fit in the assignment (used for recursion, to check line 302)
        return None


def main():
    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)



if __name__ == "__main__":
    main()
