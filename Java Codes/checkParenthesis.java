class Solution {
    public boolean isValid(String s) {
        if(s == null || s == "" || s.length()%2 != 0) return false;

        Map<Character, Character> m = new HashMap<>(){{
            put(')', '('); put(']', '['); put('}', '{');
        }};
        List<Character> l = new ArrayList<>();
        int top = -1;
        
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{'){
                l.add(s.charAt(i)); top++;
            }
            else{
                if(l.size() == 0 || l.get(top) != m.get(s.charAt(i))) return false;
                l.remove(top); top--;
            }
        }

        return (l.size() == 0) ? true : false;
    }
}
// https://leetcode.com/problems/valid-parentheses/