/** Java program for implementing following requirements using backtracking and recursion:
Given a matrix mat[][] of dimension N*M, a positive integer K and the source cell (X, Y), the task is to print all possible paths to move out of the matrix from the source cell (X, Y) by moving in all four directions in each move in at most K moves.
**/  

import java.io.*;
import java.util.*;
  
public class GFG {
  
    // Class for the pairs
    static class Pair {
        int a;
        int b;
        Pair(int a, int b)
        {
            this.a = a;
            this.b = b;
        }
    }
  
    // Function to print all the paths
    // that are outside of the matrix
    static void printAllmoves(
        int n, int m, int x, int y,
        int moves, ArrayList<Pair> ArrayOfMoves)
    {
        // Base Case
        if (x <= 0 || y <= 0 || x >= n + 1
            || y >= m + 1 && moves >= 0) {
  
            // Add the last position
            ArrayOfMoves.add(new Pair(x, y));
  
            // Traverse the pairs
            for (Pair ob : ArrayOfMoves) {
  
                // Print all the paths
                System.out.print("(" + ob.a
                                 + " " + ob.b
                                 + ")");
            }
  
            System.out.println();
  
            // Backtracking Steps
            if (ArrayOfMoves.size() > 1)
                ArrayOfMoves.remove(
                    ArrayOfMoves.size() - 1);
  
            return;
        }
  
        // If no moves remain
        if (moves <= 0) {
            return;
        }
  
        // Add the current position
        // in the list
        ArrayOfMoves.add(new Pair(x, y));
  
        // Recursive function Call
        // in all the four directions
        printAllmoves(n, m, x, y - 1, moves - 1,
                      ArrayOfMoves);
        printAllmoves(n, m, x, y + 1, moves - 1,
                      ArrayOfMoves);
        printAllmoves(n, m, x - 1, y, moves - 1,
                      ArrayOfMoves);
        printAllmoves(n, m, x + 1, y, moves - 1,
                      ArrayOfMoves);
  
        // Backtracking Steps
        if (ArrayOfMoves.size() > 1) {
            ArrayOfMoves.remove(
                ArrayOfMoves.size() - 1);
        }
    }
  
    // Driver Code
    public static void main(String[] args)
    {
        int N = 2, M = 2;
        int X = 1;
        int Y = 1;
        int K = 2;
        ArrayList<Pair> ArrayOfMoves
            = new ArrayList<>();
  
        // Function Call
        printAllmoves(N, M, X, Y, K,
                      ArrayOfMoves);
    }
}
Output:

(1 1)(1 0)
(1 1)(1 2)(1 3)
(1 1)(1 2)(0 2)
(1 1)(0 1)
(1 1)(2 1)(2 0)
(1 1)(2 1)(3 1)

Time Complexity: O(4^N)
Auxiliary Space: O(4^N)