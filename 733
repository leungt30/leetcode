import java.util.*;
class Solution {
    ArrayList<int[]> nextCoords;
    public Solution(){
        nextCoords = new ArrayList<int[]>();
    }
    
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int oldColor = image[sr][sc];
        Queue<int[]> q = new LinkedList();
        int[] first = {sr,sc};
        q.add(first);
        ArrayList<int[]> visited = new ArrayList<int[]>();
        while (!q.isEmpty()){
            int[] coords = q.remove();
            visited.add(coords);
            image = oneCycle(image,coords[0],coords[1],color,oldColor);
            for (int[] coor : nextCoords){
                // CHECK FOR VISITED BEFORE ADDING
                if (!contains(visited, coor)){
                    q.add(coor);
                }
            }

            nextCoords.clear();
            visited.add(coords);
        }

        return image;
    }
    public boolean contains(ArrayList<int[]> visited, int[] checking){
        for (int[] element : visited){
            if ((element[0] == checking[0] && element[1] == checking[1])){
                return true;
            }
        }
        return false;
    }
    public int[][] oneCycle(int[][] image, int sr, int sc, int newColor, int origColor){
        image[sr][sc] = newColor;
        try{
            if (image[sr+1][sc] == origColor){
                image[sr+1][sc] = newColor;
                int[] temp = {sr+1,sc};
                nextCoords.add(temp);
            }
        }
        catch(Exception e){
        }
        try{
            if (image[sr-1][sc] == origColor){
                image[sr-1][sc] = newColor;
                int[] temp = {sr-1,sc};
                nextCoords.add(temp);
            }
        }
        catch(Exception e){
        }
        try{
            if (image[sr][sc+1] == origColor){
                image[sr][sc+1] = newColor;
                int[] temp = {sr,sc+1};
                nextCoords.add(temp);
            }
        }
        catch(Exception e){
        }
        try{
            if (image[sr][sc-1] == origColor){
                image[sr][sc-1] = newColor;
                int[] temp = {sr,sc-1};
                nextCoords.add(temp);
            }
        }
        catch(Exception e){
        }
        return image;
    }

}