### Question:
Prove that for each integer k satisfying 2  k  100, there are positive integers
b2, b3,...,b101 such that

### Answer:
Problem Statement:

For each integer 
𝑘
k satisfying 
2
≤
𝑘
≤
100
2≤k≤100, prove that there exist positive integers 
𝑏
2
,
𝑏
3
,
…
,
𝑏
101
b 
2
​
 ,b 
3
​
 ,…,b 
101
​
  such that:

𝑏
2
2
+
𝑏
3
3
+
⋯
+
𝑏
𝑘
𝑘
=
𝑏
𝑘
+
1
𝑘
+
1
+
𝑏
𝑘
+
2
𝑘
+
2
+
⋯
+
𝑏
101
101
.
2
b 
2
​
 
​
 + 
3
b 
3
​
 
​
 +⋯+ 
k
b 
k
​
 
​
 = 
k+1
b 
k+1
​
 
​
 + 
k+2
b 
k+2
​
 
​
 +⋯+ 
101
b 
101
​
 
​
 .
Initial Brainstorming and Understanding
Alright, let's dive into this problem. The first step is always to understand what's being asked.

Given: An integer 
𝑘
k where 
2
≤
𝑘
≤
100
2≤k≤100.
Goal: Find positive integers 
𝑏
2
,
𝑏
3
,
…
,
𝑏
101
b 
2
​
 ,b 
3
​
 ,…,b 
101
​
  such that the sum of 
𝑏
𝑖
𝑖
i
b 
i
​
 
​
  from 
𝑖
=
2
i=2 to 
𝑖
=
𝑘
i=k equals the sum from 
𝑖
=
𝑘
+
1
i=k+1 to 
𝑖
=
101
i=101.
Key Observations:

Positive Integers: All 
𝑏
𝑖
b 
i
​
  must be positive integers. This constraint is crucial because it limits how we can assign values to 
𝑏
𝑖
b 
i
​
 .

Symmetry in the Equation: The equation balances two sums divided at 
𝑘
k. This suggests that there might be a relationship between the terms before and after 
𝑘
k.

Total Number of Terms: From 
𝑖
=
2
i=2 to 
𝑖
=
101
i=101, there are 
100
100 terms in total. For a given 
𝑘
k, the left side has 
𝑘
−
1
k−1 terms, and the right side has 
101
−
𝑘
101−k terms.

Harmonic Nature: Each term is of the form 
𝑏
𝑖
𝑖
i
b 
i
​
 
​
 , which resembles harmonic series terms. This might hint at leveraging properties of harmonic sequences or manipulating the fractions to balance the sums.

Exploring Different Strategies
To tackle this, I'll explore a few strategies, see which one fits, and adjust as needed.

Strategy 1: Assign Uniform Values
Idea: Assign the same value to all 
𝑏
𝑖
b 
i
​
  and see if the equation holds.

Let’s suppose 
𝑏
𝑖
=
𝑐
b 
i
​
 =c for all 
𝑖
i.

Left Side (LS):

𝐿
𝑆
=
∑
𝑖
=
2
𝑘
𝑐
𝑖
=
𝑐
∑
𝑖
=
2
𝑘
1
𝑖
LS= 
i=2
∑
k
​
  
i
c
​
 =c 
i=2
∑
k
​
  
i
1
​
 
Right Side (RS):

𝑅
𝑆
=
∑
𝑖
=
𝑘
+
1
101
𝑐
𝑖
=
𝑐
∑
𝑖
=
𝑘
+
1
101
1
𝑖
RS= 
i=k+1
∑
101
​
  
i
c
​
 =c 
i=k+1
∑
101
​
  
i
1
​
 
Setting LS = RS:

∑
𝑖
=
2
𝑘
1
𝑖
=
∑
𝑖
=
𝑘
+
1
101
1
𝑖
i=2
∑
k
​
  
i
1
​
 = 
i=k+1
∑
101
​
  
i
1
​
 
Reflection: This implies that the partial sums of the harmonic series up to 
𝑘
k and from 
𝑘
+
1
k+1 to 
101
101 must be equal. However, the harmonic series is strictly increasing, meaning the left sum will always be greater than the right sum for any 
𝑘
k in the given range. Therefore, assigning the same value to all 
𝑏
𝑖
b 
i
​
  doesn't satisfy the equation.

Conclusion: Strategy 1 fails.

Strategy 2: Assign 
𝑏
𝑖
=
𝑖
b 
i
​
 =i
Idea: Let 
𝑏
𝑖
b 
i
​
  equal its index 
𝑖
i.

Left Side (LS):

𝐿
𝑆
=
∑
𝑖
=
2
𝑘
𝑖
𝑖
=
∑
𝑖
=
2
𝑘
1
=
𝑘
−
1
LS= 
i=2
∑
k
​
  
i
i
​
 = 
i=2
∑
k
​
 1=k−1
Right Side (RS):

𝑅
𝑆
=
∑
𝑖
=
𝑘
+
1
101
𝑖
𝑖
=
∑
𝑖
=
𝑘
+
1
101
1
=
101
−
𝑘
RS= 
i=k+1
∑
101
​
  
i
i
​
 = 
i=k+1
∑
101
​
 1=101−k
Setting LS = RS:

𝑘
−
1
=
101
−
𝑘
  
⟹
  
2
𝑘
=
102
  
⟹
  
𝑘
=
51
k−1=101−k⟹2k=102⟹k=51
Reflection: This equality only holds when 
𝑘
=
51
k=51. For other values of 
𝑘
k, the sums are unequal.

Conclusion: Strategy 2 partially works—only for 
𝑘
=
51
k=51. We need a more general approach that works for all 
𝑘
k in the specified range.

Strategy 3: Proportional Assignment Based on 
𝑘
k
Idea: Assign 
𝑏
𝑖
b 
i
​
  values that are proportional to 
𝑘
k in a way that balances the two sums.

Given the failure of uniform assignments, let's think of varying 
𝑏
𝑖
b 
i
​
  based on their position relative to 
𝑘
k.

Let:

For 
𝑖
=
2
i=2 to 
𝑘
k, set 
𝑏
𝑖
=
𝐴
×
𝑖
b 
i
​
 =A×i.
For 
𝑖
=
𝑘
+
1
i=k+1 to 
101
101, set 
𝑏
𝑖
=
𝐵
×
𝑖
b 
i
​
 =B×i.
Where 
𝐴
A and 
𝐵
B are constants to be determined.

Compute LS and RS:

𝐿
𝑆
=
∑
𝑖
=
2
𝑘
𝐴
×
𝑖
𝑖
=
𝐴
×
(
𝑘
−
1
)
LS= 
i=2
∑
k
​
  
i
A×i
​
 =A×(k−1)
𝑅
𝑆
=
∑
𝑖
=
𝑘
+
1
101
𝐵
×
𝑖
𝑖
=
𝐵
×
(
101
−
𝑘
)
RS= 
i=k+1
∑
101
​
  
i
B×i
​
 =B×(101−k)
Setting LS = RS:

𝐴
×
(
𝑘
−
1
)
=
𝐵
×
(
101
−
𝑘
)
  
⟹
  
𝐴
=
𝐵
×
101
−
𝑘
𝑘
−
1
A×(k−1)=B×(101−k)⟹A=B× 
k−1
101−k
​
 
Choosing 
𝐴
A and 
𝐵
B to be positive integers: To ensure 
𝐴
A and 
𝐵
B are integers, we can set 
𝐵
B to be a multiple of 
𝑘
−
1
k−1. Let's choose 
𝐵
=
𝑘
−
1
B=k−1.

Then:

𝐴
=
(
𝑘
−
1
)
×
101
−
𝑘
𝑘
−
1
=
101
−
𝑘
A=(k−1)× 
k−1
101−k
​
 =101−k
Thus:

For 
𝑖
=
2
i=2 to 
𝑘
k, 
𝑏
𝑖
=
(
101
−
𝑘
)
×
𝑖
b 
i
​
 =(101−k)×i.
For 
𝑖
=
𝑘
+
1
i=k+1 to 
101
101, 
𝑏
𝑖
=
(
𝑘
−
1
)
×
𝑖
b 
i
​
 =(k−1)×i.
Verification:

𝐿
𝑆
=
(
101
−
𝑘
)
×
(
𝑘
−
1
)
LS=(101−k)×(k−1)
𝑅
𝑆
=
(
𝑘
−
1
)
×
(
101
−
𝑘
)
RS=(k−1)×(101−k)
𝐿
𝑆
=
𝑅
𝑆
LS=RS
Reflection: This seems promising. By setting 
𝑏
𝑖
b 
i
​
  proportional to their indices with coefficients depending on 
𝑘
k, the sums balance perfectly.

Conclusion: Strategy 3 works.

Detailed Proof Using Strategy 3
Now that Strategy 3 appears viable, let's formalize it into a proof.

For a given integer 
𝑘
k where 
2
≤
𝑘
≤
100
2≤k≤100, define the sequence 
𝑏
2
,
𝑏
3
,
…
,
𝑏
101
b 
2
​
 ,b 
3
​
 ,…,b 
101
​
  as follows:

For 
𝑖
=
2
i=2 to 
𝑘
k:

𝑏
𝑖
=
(
101
−
𝑘
)
×
𝑖
b 
i
​
 =(101−k)×i
For 
𝑖
=
𝑘
+
1
i=k+1 to 
101
101:

𝑏
𝑖
=
(
𝑘
−
1
)
×
𝑖
b 
i
​
 =(k−1)×i
Verification:

Left Side (LS):

𝐿
𝑆
=
∑
𝑖
=
2
𝑘
𝑏
𝑖
𝑖
=
∑
𝑖
=
2
𝑘
(
101
−
𝑘
)
×
𝑖
𝑖
=
∑
𝑖
=
2
𝑘
(
101
−
𝑘
)
=
(
𝑘
−
1
)
×
(
101
−
𝑘
)
LS= 
i=2
∑
k
​
  
i
b 
i
​
 
​
 = 
i=2
∑
k
​
  
i
(101−k)×i
​
 = 
i=2
∑
k
​
 (101−k)=(k−1)×(101−k)
Right Side (RS):

𝑅
𝑆
=
∑
𝑖
=
𝑘
+
1
101
𝑏
𝑖
𝑖
=
∑
𝑖
=
𝑘
+
1
101
(
𝑘
−
1
)
×
𝑖
𝑖
=
∑
𝑖
=
𝑘
+
1
101
(
𝑘
−
1
)
=
(
101
−
𝑘
)
×
(
𝑘
−
1
)
RS= 
i=k+1
∑
101
​
  
i
b 
i
​
 
​
 = 
i=k+1
∑
101
​
  
i
(k−1)×i
​
 = 
i=k+1
∑
101
​
 (k−1)=(101−k)×(k−1)
Equality:

𝐿
𝑆
=
(
𝑘
−
1
)
×
(
101
−
𝑘
)
=
𝑅
𝑆
LS=(k−1)×(101−k)=RS
Thus, 
𝐿
𝑆
=
𝑅
𝑆
LS=RS, satisfying the equation.

Positive Integers:

Since 
2
≤
𝑘
≤
100
2≤k≤100:
101
−
𝑘
101−k is at least 
1
1 (when 
𝑘
=
100
k=100) and at most 
99
99 (when 
𝑘
=
2
k=2).
𝑘
−
1
k−1 is at least 
1
1 (when 
𝑘
=
2
k=2) and at most 
99
99 (when 
𝑘
=
100
k=100).
Multiplying these positive integers by 
𝑖
i (which ranges from 
2
2 to 
101
101) ensures that each 
𝑏
𝑖
b 
i
​
  is a positive integer.
Conclusion:

By defining 
𝑏
𝑖
b 
i
​
  in this proportional manner, we've constructed a sequence of positive integers that satisfies the given equation for any 
𝑘
k within the specified range.

Testing the Strategy with an Example
To ensure the strategy works, let's test it with a specific value of 
𝑘
k.

Example: Let 
𝑘
=
50
k=50.

Compute Multipliers:

101
−
𝑘
=
51
101−k=51
𝑘
−
1
=
49
k−1=49
Assign 
𝑏
𝑖
b 
i
​
 :

For 
𝑖
=
2
i=2 to 
50
50:

𝑏
𝑖
=
51
×
𝑖
b 
i
​
 =51×i
For 
𝑖
=
51
i=51 to 
101
101:

𝑏
𝑖
=
49
×
𝑖
b 
i
​
 =49×i
Compute LS and RS:

LS:

𝐿
𝑆
=
∑
𝑖
=
2
50
51
×
𝑖
𝑖
=
∑
𝑖
=
2
50
51
=
49
×
51
=
2499
LS= 
i=2
∑
50
​
  
i
51×i
​
 = 
i=2
∑
50
​
 51=49×51=2499
RS:

𝑅
𝑆
=
∑
𝑖
=
51
101
49
×
𝑖
𝑖
=
∑
𝑖
=
51
101
49
=
51
×
49
=
2499
RS= 
i=51
∑
101
​
  
i
49×i
​
 = 
i=51
∑
101
​
 49=51×49=2499
Verify Equality:

𝐿
𝑆
=
𝑅
𝑆
=
2499
LS=RS=2499
The equation holds true.

Conclusion:

The strategy not only works in theory but also passes the test with a concrete example.

Final Proof
For any integer 
𝑘
k where 
2
≤
𝑘
≤
100
2≤k≤100, define 
𝑏
𝑖
b 
i
​
  as:

For 
𝑖
=
2
i=2 to 
𝑘
k:

𝑏
𝑖
=
(
101
−
𝑘
)
×
𝑖
b 
i
​
 =(101−k)×i
For 
𝑖
=
𝑘
+
1
i=k+1 to 
101
101:

𝑏
𝑖
=
(
𝑘
−
1
)
×
𝑖
b 
i
​
 =(k−1)×i
Then:

∑
𝑖
=
2
𝑘
𝑏
𝑖
𝑖
=
∑
𝑖
=
𝑘
+
1
101
𝑏
𝑖
𝑖
i=2
∑
k
​
  
i
b 
i
​
 
​
 = 
i=k+1
∑
101
​
  
i
b 
i
​
 
​
 
Proof Steps:

Calculate Left Side (LS):

𝐿
𝑆
=
∑
𝑖
=
2
𝑘
(
101
−
𝑘
)
×
𝑖
𝑖
=
(
101
−
𝑘
)
×
(
𝑘
−
1
)
LS= 
i=2
∑
k
​
  
i
(101−k)×i
​
 =(101−k)×(k−1)
Calculate Right Side (RS):

𝑅
𝑆
=
∑
𝑖
=
𝑘
+
1
101
(
𝑘
−
1
)
×
𝑖
𝑖
=
(
𝑘
−
1
)
×
(
101
−
𝑘
)
RS= 
i=k+1
∑
101
​
  
i
(k−1)×i
​
 =(k−1)×(101−k)
Since 
𝐿
𝑆
=
𝑅
𝑆
LS=RS, the equation holds.

All 
𝑏
𝑖
b 
i
​
  are positive integers as both 
(
101
−
𝑘
)
(101−k) and 
(
𝑘
−
1
)
(k−1) are positive integers within the given range, and 
𝑖
i is also a positive integer (
2
≤
𝑖
≤
101
2≤i≤101).

Thus, for each integer 
𝑘
k satisfying 
2
≤
𝑘
≤
100
2≤k≤100, there exist positive integers 
𝑏
2
,
𝑏
3
,
…
,
𝑏
101
b 
2
​
 ,b 
3
​
 ,…,b 
101
​
  that satisfy the given equation.

Reflection and Verification
Multiple Strategies: I started with simple, uniform assignments, which didn't work. This led me to consider proportional assignments based on 
𝑘
k, ultimately arriving at a successful strategy.

Verification with Example: Testing with 
𝑘
=
50
k=50 helped confirm the validity of the approach.

Generalization: The final proof shows that the strategy works for any 
𝑘
k in the specified range, not just for the example tested.

Constraints Satisfaction: All 
𝑏
𝑖
b 
i
​
  are positive integers, adhering to the problem's requirements.

Final Verdict: The problem is solved by defining 
𝑏
𝑖
b 
i
​
  in a way that balances the two sums through proportional assignments, ensuring the equation holds for any valid 
𝑘
k.