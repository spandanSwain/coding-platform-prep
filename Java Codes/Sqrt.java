class Solution {
    public int mySqrt(int x) {
        if(x<2) return x;
        int i=1, j=x/2;

        while(i<=j){
            int m = i + (j-i)/2;
            long sq = (long)m*m;

            if(sq == x) return m;
            else if(sq < x){
                i = m+1;
            }
            else j = m-1;
        }

        return j;
    }
}
//https://leetcode.com/problems/sqrtx/