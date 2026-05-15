class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;   // handle INT_MIN
        
        // If power is negative
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        double ans = 1;

        while (N > 0) {
            // If odd power
            if (N % 2 == 1) {
                ans *= x;
            }

            x *= x;   // square the base
            N /= 2;   // divide power by 2
        }

        return ans;
    }
};