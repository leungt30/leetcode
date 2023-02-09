import java.util.*;
class Solution {
    private int[] f;
    public int fib(int n) {
        if (n>1){
            f = new int[n+1];
        }
        else{
             f = new int[2];
        }
        f[0] = 0;
        f[1] = 1;
        for (int i = 2; i < n+1; i++){
            f[i] = -1;
        }
        return realFib(n);
    }

    private int realFib(int n){
        if (f[n] >= 0){
            return f[n];
        }
        return realFib(n-1) + realFib(n-2);
    }
}