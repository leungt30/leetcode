class Solution {
    public boolean isSubsequence(String s, String t) {
        int sIndex = 0;
        if (sIndex >= s.length()){
                return true;
        }
        for (int i = 0 ; i < t.length(); i++){

            if (t.charAt(i) == s.charAt(sIndex)){
                sIndex ++;
            }
            if (sIndex >= s.length()){
                return true;
            }
        }
        return false;
    }
}