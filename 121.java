class Solution {
    public int maxProfit(int[] prices) {
        int bestProfit = 0;
        
        int min = prices[0];
        int max = prices[0];
        for (int i = 0; i < prices.length; i++){
            if (prices[i] < min){
                min = prices[i];
                max = prices[i];
            }
            else if (prices[i] > max){
                max = prices[i];
            }
            if (max - min > bestProfit){
                    bestProfit = max - min;
                }
        }
        return bestProfit;
    }

}