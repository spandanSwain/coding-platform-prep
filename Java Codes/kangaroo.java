class Kangaroo{
    public static String kangaroo(int x1, int v1, int x2, int v2) {
        if(v1==v2){
            return (x1==x2) ? "YES" : "NO";
        }
        
        int diffX = x1 - x2;
        int diffV = v2 - v1;
        
        if(diffX * diffV < 0) return "NO";
        else if (diffX%diffV == 0) return "YES";
        else return "NO";
    }
}

/*
https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

if kangaroos meet then yes else no
let s1 and s2 be distance, x2 x1 be start point and v1 v2 be the speed
s1 = x1 + n*v1 (n=no.of jumps) (same for 2)
so for the kangaroos to meet s1=s2

x1 + n*v1 = x2 + n*v2

x1 - x2 = n(v2-v1)
n = x1-x2 / v2-v1 , so if n is integer (no remainder) then they meet

1-2  2-1
see this explains why prod of both shouldn't be < 0, becuase they can't meet together like this
*/