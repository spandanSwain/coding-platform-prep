// https://youtu.be/SgMO9cHTZ0U?si=gXSOlOmlkkpb5m7H
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i=a.length()-1, j=b.length()-1, carry=0;

        while(i>=0 || j>=0 || carry == 1){
            int sum = carry;
            if(i>=0){
                sum+=(a.charAt(i) - '0'); i--;
            }
            if(j>=0){
                sum+=(b.charAt(j) - '0'); j--;
            }
            sb.append(sum%2); carry = sum/2;
        }
        return sb.reverse().toString();
    }
}
// https://leetcode.com/problems/add-binary/
/*
    1+1 c=1 v=0 -> in maths 1+1=2, so v is 0 means it is 2%2=0 and c is 1 means 2/2
    1+0 c=0 v=1
    0+0 c=0 v=0
*/