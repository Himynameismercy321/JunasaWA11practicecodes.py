import java.util.*;

public class W2Exer1Junasa {
    public static void main(String[] args) {
        int[][] junasa_matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
            
        };
        
        System.out.println("Original matrix");
        for (int junasa_row = 0; junasa_row < 3; junasa_row++ ) {
            for (int junasa_col = 0; junasa_col < 3; junasa_col++) {
                System.out.print(junasa_matrix[junasa_row][junasa_col] + "  ");
                
            }
            System.out.println();
            }
            
            int[] Rowsums = new int[3];
            for (int junasa_row = 0; junasa_row < 3; junasa_row++) {
                for (int junasa_col = 0; junasa_col < 3; junasa_col++) {
                    Rowsums[junasa_row] += junasa_matrix[junasa_row][junasa_col];
            }
            }
            
            System.out.print("Row sums: ");
            System.out.print(Rowsums[0] + "," + Rowsums[1] + "," + Rowsums[2]);
            
            int[] Colsums = new int[3];
            for (int junasa_col = 0; junasa_col < 3; junasa_col++) {
                for (int junasa_row = 0; junasa_row < 3; junasa_row++) {
                    Colsums[junasa_col] += junasa_matrix[junasa_row][junasa_col];
                }
            }
            System.out.print("\nColumn sums: " + Colsums[0] + "," + Colsums[1] + "," + Colsums[2]);
            
            int diagonalSum = 0;

            for (int junasa_row = 0; junasa_row < 3; junasa_row++) {
                int junasa_col = junasa_row;

            diagonalSum += junasa_matrix[junasa_row][junasa_col];
                }

        System.out.println("\nMain diagonal sum: " + diagonalSum);

        
        System.out.println("\nTranspose:");

        for (int junasa_row = 0; junasa_row < 3; junasa_row++) {
            for (int junasa_col = 0; junasa_col < 3; junasa_col++) {
                System.out.print(junasa_matrix[junasa_col][junasa_row] + " ");
            }
            System.out.println();
        }
            
            
      
    }
}