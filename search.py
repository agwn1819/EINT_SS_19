# coding=utf-8
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def graphSearch(problem, structure):
    """

    :param problem: Das Suchproblem
    :param structure: Stack/Queue
    :return: Allgemeinen Algorithmus der von den verschiedenen Suchalgorithmen verwendet wird
    """

    # Start initialisieren
    # structure ist ein Stack/Queue da bei den Suchalgorithmen verschiedene Structures zum Einsatz kommen
    # structure hat folgendes Format: [Position, Richtung, Kosten]
    structure.push([(problem.getStartState(), "Stop", 0)])

    # variable für die Besuchten Positionen
    visited = []

    while not structure.isEmpty():
        # Für die Rekursion des Weges
        path = structure.pop()

        # Weist Position aus path dem currentPosition zu
        # Mit [-1] kriegt es das ganze letzte Element aus path, mit [0] die Position aus dem structure Format

        currentPosition = path[-1][0]
        succesorsOfCurrentPosition = problem.getSuccessors(currentPosition)

        # Wenn currentPosition das Ziel ist, dann return die Richtung in die Pacman sich bewegen muss
        # [1:] schließt den ersten Eintrag aus ("Stop")
        if problem.isGoalState(currentPosition):
            return [x[1] for x in path][1:]

        # Wenn currentPosition nicht in visited, dann currentPosition in visited hinzufügen
        if currentPosition not in visited:
            visited.append(currentPosition)

            for successor in succesorsOfCurrentPosition:
                # successor[0] = (position, richtung, kosten)[0] = position
                if successor[0] not in visited:
                    # Elternweg
                    successorPath = path[:]
                    successorPath.append(successor)
                    structure.push(successorPath)
    return False


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """

    stack = util.Stack()
    return graphSearch(problem, stack)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    return graphSearch(problem, queue)


def uniformCostSearch(problem):
    # PriorityQueue kann mit hilfe von Funktionen aus util.py ersetllt werden
    # priority queue mit den Kosten erstellen
    cost = lambda path: problem.getCostOfActions([x[1] for x in path][1:])
    pq = util.PriorityQueueWithFunction(cost)
    return graphSearch(problem, pq)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # a* ist das gleiche wie ucf nur das f(x) = g(x) + h(x) -> g(x) ist die Lambdafunktion aus ucf
    # h(x) muss mit in den Kosten übergeben werden und dann daraus eine PriorityQueue erstellen
    cost = lambda path: problem.getCostOfActions([x[1] for x in path][1:]) + heuristic(path[-1][0], problem)

    pq = util.PriorityQueueWithFunction(cost)
    return graphSearch(problem, pq)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
