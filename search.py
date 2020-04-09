"""
In search.py, you will implement generic search algorithms
"""

import util

class Node:
    def __init__(self, father, triplet):
        self.father = father
        self.state = triplet[0]
        self.action = triplet[1] #the action that lead to this state
        self.cost = triplet[2]

    def get_state(self):
        return self.state

    def get_action(self):
        return self.action

    def get_cost(self):
        return self.cost

    def get_father(self):
        return self.father

    def get_action_list(self):
        cur = self
        lst = []
        while cur.get_father() is not None:
            lst.append(cur.get_action)
            cur = cur.get_father()
        return lst[::-1]

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()




def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

	print("Start:", problem.get_start_state().state)
    print("Is the start a goal?", problem.is_goal_state(problem.get_start_state()))
    print("Start's successors:", problem.get_successors(problem.get_start_state()))
    """
    "* YOUR CODE HERE *"
    root = Node(None, (None, None, problem.get_start_state()))
    fringe = util.Stack()
    fringe.push(root)
    while not fringe.isEmpty():
        current = fringe.pop()
        if problem.is_goal_state(current):
            return current.get_action_list
        else:
            children = problem.get_successors(current)
            for child in children:
                fringe.push(Node(current, child))
    util.raiseNotDefined()

def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    root = Node(None, (None, None, problem.get_start_state()))
    fringe = util.Queue()
    fringe.push(root)
    while not fringe.isEmpty():
        current = fringe.pop()
        if problem.is_goal_state(current):
            return current.get_action_list
        else:
            children = problem.get_successors(current)
            for child in children:
                fringe.push(Node(current, child))
    util.raiseNotDefined()


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()



# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
