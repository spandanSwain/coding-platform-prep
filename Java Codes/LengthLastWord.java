class Solution {
    public int lengthOfLastWord(String s) {
        if(s.length() == 1 && !s.equals(" ")) return 1;

        int e = s.length()-1;
        while(e >= 0 && s.charAt(e) == ' ') e--;

        int st = e;
        while(st>=0 && s.charAt(st) != ' ') st--;

        return e-st;
    }
}