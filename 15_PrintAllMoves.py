#Given a matrix mat[][] of dimension N*M, a positive #integer K and the source cell (X, Y), the task is to #print all possible paths to move out of the matrix from #the source cell (X, Y) by moving in all four directions #in each move in at most K moves.

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def printAllMoves(totalRows,totalCols,X,Y,moves,arrayOfMoves):

    # base case
    if X <= 0 or Y <= 0 or X >= totalRows + 1 or Y >= totalCols and moves >= 0:
        # add the last position
        arrayOfMoves.append(Pair(X, Y))

        # traverse the pairs
        for ob in arrayOfMoves:
            #Print all the paths
            print("( {} {} )".format(ob.a, ob.b))

        print("")

        # backtracking steps
        if len(arrayOfMoves) > 1:
            arrayOfMoves.pop()

        return

    # If no moves remain
    if moves <= 0:
        return

    # Add the current position in the list
    arrayOfMoves.append(Pair(X, Y))

    # Recursive function call in all the four directions
    printAllMoves(totalRows, totalCols, X, Y-1, moves-1, arrayOfMoves)
    printAllMoves(totalRows, totalCols, X, Y+1, moves-1, arrayOfMoves)
    printAllMoves(totalRows, totalCols, X-1, Y, moves-1, arrayOfMoves)
    printAllMoves(totalRows, totalCols, X+1, Y, moves-1, arrayOfMoves)

    # backtracking steps
    if len(arrayOfMoves) > 1:
        arrayOfMoves.pop()


def main():
    N = 2
    M = 2
    X = 1
    Y = 1
    K = 2

    arrayOfMoves = []

    # Function Call
    printAllMoves(N, M, X, Y, K, arrayOfMoves)

main()