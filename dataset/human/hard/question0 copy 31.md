### Question:

Find the number of permutations $x_1, x_2, x_3, x_4, x_5$ of numbers $1, 2, 3, 4, 5$ such that the sum of five products\[x_1x_2x_3 + x_2x_3x_4 + x_3x_4x_5 + x_4x_5x_1 + x_5x_1x_2\]is divisible by $3$.

### Answer:
So i've got this problem here. it says that there are real numbers a, b, c, and d such that -20 is a root of the cubic polynomial x³ + a x + b, and -21 is a root of another cubic polynomial x³ + c x² + d. these two polynomials share a complex root of the form m + sqrt(n) * i, where m and n are positive integers, and i is the imaginary unit.

my goal is to find the sum m + n.

alright, let's break this down. first, both polynomials are cubic, and they share a complex root. since the coefficients of the polynomials are real numbers, the complex roots must come in conjugate pairs. that means if m + sqrt(n) * i is a root, then its conjugate, m - sqrt(n) * i, must also be a root of the polynomial.

let's consider the first polynomial: x³ + a x + b. we know that -20 is one of its roots. so, if m + sqrt(n) * i is another root, then its conjugate m - sqrt(n) * i must also be a root. therefore, the three roots of this polynomial are:

1. -20

2. m + sqrt(n) * i

3. m - sqrt(n) * i

similarly, for the second polynomial: x³ + c x² + d, we know that -21 is one of its roots, and it shares the complex root m + sqrt(n) * i with the first polynomial. so, its roots must be:

1. -21

2. m + sqrt(n) * i

3. another root, which should be the conjugate of m + sqrt(n) * i, assuming the coefficients are real. wait, but the second polynomial is x³ + c x² + d, which is a cubic with a x² term and no x term, whereas the first polynomial is x³ + a x + b, which lacks the x² term. hmm, that's interesting.

given that the second polynomial has a different structure, maybe the third root isn't necessarily the conjugate. or perhaps there's something else going on here.

wait a minute. since the coefficients are real, the non-real roots must come in conjugate pairs. so, for the second polynomial, if m + sqrt(n) * i is a root, then m - sqrt(n) * i must also be a root. that means the roots of the second polynomial are:

1. -21

2. m + sqrt(n) * i

3. m - sqrt(n) * i

so both polynomials have the same pair of complex conjugate roots. that makes sense.

now, since both polynomials have these two complex roots, and one real root each (-20 and -21), perhaps there is some relationship between these polynomials.

let me recall that for a cubic polynomial, the sum of the roots is equal to - coefficient of x² divided by the leading coefficient. but in the first polynomial, there is no x² term, so the sum of the roots should be zero.

wait, the first polynomial is x³ + a x + b, which is x³ + 0 x² + a x + b. so, the sum of the roots is -0 = 0.

similarly, the second polynomial is x³ + c x² + d, so the sum of the roots is -c.

given that, for the first polynomial, the sum of the roots is:

-20 + (m + sqrt(n) * i) + (m - sqrt(n) * i) = -20 + 2m = 0.

so, -20 + 2m = 0 ⇒ 2m = 20 ⇒ m = 10.

alright, so m is 10.

now, for the second polynomial, the sum of the roots is:

-21 + (m + sqrt(n) * i) + (m - sqrt(n) * i) = -21 + 2m = -21 + 20 = -1.

but the sum of the roots should be equal to -c. so, -c = -1 ⇒ c = 1.

alright, that gives us c.

now, let's look at the product of the roots.

for the first polynomial, the product of the roots is -b (since the constant term is b, and for a cubic polynomial x³ + p x² + q x + r, the product of the roots is -r).

so, the product of the roots is:

(-20) * (m + sqrt(n) * i) * (m - sqrt(n) * i) = (-20) * (m² + n).

we already know m = 10, so:

(-20) * (100 + n) = -20*(100 + n) = -2000 - 20n = -b ⇒ b = 2000 + 20n.

similarly, for the second polynomial, the product of the roots is -d.

so, (-21) * (m + sqrt(n) * i) * (m - sqrt(n) * i) = (-21)*(m² + n) = (-21)*(100 + n) = -2100 - 21n = -d ⇒ d = 2100 + 21n.

now, let's look at the sum of the products of the roots taken two at a time.

for the first polynomial, which is x³ + 0 x² + a x + b, the sum of the products of roots two at a time is equal to the coefficient of x, which is a.

so:

(-20)*(m + sqrt(n) * i) + (-20)*(m - sqrt(n) * i) + (m + sqrt(n) * i)*(m - sqrt(n) * i) = a.

plugging in m = 10:

(-20)*(10 + sqrt(n) * i) + (-20)*(10 - sqrt(n) * i) + (10 + sqrt(n) * i)*(10 - sqrt(n) * i) = a.

simplify:

-200 - 20 sqrt(n) * i - 200 + 20 sqrt(n) * i + (100 + n) = a.

the imaginary parts cancel out:

-400 + 100 + n = a ⇒ a = -300 + n.

similarly, for the second polynomial, x³ + c x² + d, the sum of the products of roots two at a time is equal to the coefficient of x, which is 0 (since it's x³ + c x² + d), but wait, no. for a cubic polynomial x³ + p x² + q x + r, the sum of the products of roots two at a time is q.

wait, actually, in general, for x³ + p x² + q x + r, the sum of the roots is -p, the sum of the products two at a time is q, and the product of the roots is -r.

wait no, let me recall vieta's formulas correctly.

for a cubic equation x³ + a x² + b x + c = 0, with roots r, s, t:

- sum of roots: r + s + t = -a

- sum of products two at a time: rs + rt + st = b

- product of roots: r s t = -c

so, in the first polynomial, x³ + 0 x² + a x + b, so a is the sum of the products two at a time, and b is related to the product of the roots.

similarly, in the second polynomial, x³ + c x² + 0 x + d, assuming that there is no x term, but actually, the problem says x³ + c x² + d, so it's x³ + c x² + 0 x + d.

therefore, for the second polynomial, the sum of the products two at a time is 0.

wait, but that doesn't make sense because in the second polynomial, x³ + c x² + d, the coefficient of x is 0, so the sum of the products two at a time is 0.

so, for the second polynomial, sum of products two at a time is 0.

therefore:

(-21)*(m + sqrt(n) * i) + (-21)*(m - sqrt(n) * i) + (m + sqrt(n) * i)*(m - sqrt(n) * i) = 0.

plugging m = 10:

-21*(10 + sqrt(n) * i) + -21*(10 - sqrt(n) * i) + (10 + sqrt(n) * i)*(10 - sqrt(n) * i) = 0.

simplify:

-210 - 21 sqrt(n) * i - 210 + 21 sqrt(n) * i + (100 + n) = 0.

again, imaginary parts cancel out:

-420 + 100 + n = 0 ⇒ -320 + n = 0 ⇒ n = 320.

alright, so n is 320.

now, recall that for the first polynomial, a = -300 + n = -300 + 320 = 20.

and for the second polynomial, d = 2100 + 21n = 2100 + 21*320 = 2100 + 6720 = 8820.

also, c = 1, as found earlier.

so, now we've determined m = 10 and n = 320.

therefore, m + n = 10 + 320 = 330.

wait a second, but the problem states that m and n are positive integers, and i've found m = 10 and n = 320, which are both positive integers. so, that seems to fit.

but let me double-check to make sure there are no mistakes.

first, confirming m:

from the first polynomial, sum of roots is 0:

-20 + (10 + sqrt(320)i) + (10 - sqrt(320)i) = -20 + 20 = 0. correct.

second, for the second polynomial, sum of roots is -c:

-21 + (10 + sqrt(320)i) + (10 - sqrt(320)i) = -21 + 20 = -1. so, c = 1. correct.

sum of products two at a time for the second polynomial is 0:

(-21)*(10 + sqrt(320)i) + (-21)*(10 - sqrt(320)i) + (10 + sqrt(320)i)*(10 - sqrt(320)i) = -210 - 210 + 100 + 320 = (-420) + 420 = 0. correct.

and for the first polynomial, sum of products two at a time is a = -300 + 320 = 20.

product of roots for the first polynomial is -b:

-20*(10 + sqrt(320)i)*(10 - sqrt(320)i) = -20*(100 + 320) = -20*420 = -8400 = -b ⇒ b = 8400.

similarly, for the second polynomial, product of roots is -d:

-21*(10 + sqrt(320)i)*(10 - sqrt(320)i) = -21*(100 + 320) = -21*420 = -8820 = -d ⇒ d = 8820.

everything checks out.

therefore, the answer is m + n = 10 + 320 = 330.

**final answer**

330
330
​
 
Given the problem, we need to find the sum 
m
+
n
m+n for the complex root 
m
+
n
i
m+ 
n
​
 i shared by two polynomials with real coefficients.

for the polynomial 
x
3
+
a
x
+
b
x 
3
 +ax+b with root 
−
20
−20, the roots are:

−
20
,
m
+
n
i
,
m
−
n
i
−20,m+ 
n
​
 i,m− 
n
​
 i
the sum of the roots is:

−
20
+
(
m
+
n
i
)
+
(
m
−
n
i
)
=
0
  
⟹
  
−
20
+
2
m
=
0
  
⟹
  
m
=
10
−20+(m+ 
n
​
 i)+(m− 
n
​
 i)=0⟹−20+2m=0⟹m=10
for the polynomial 
x
3
+
c
x
2
+
d
x 
3
 +cx 
2
 +d with root 
−
21
−21, the roots are:

−
21
,
m
+
n
i
,
m
−
n
i
−21,m+ 
n
​
 i,m− 
n
​
 i
the sum of the roots is:

−
21
+
(
m
+
n
i
)
+
(
m
−
n
i
)
=
−
c
  
⟹
  
−
21
+
2
m
=
−
1
  
⟹
  
c
=
1
−21+(m+ 
n
​
 i)+(m− 
n
​
 i)=−c⟹−21+2m=−1⟹c=1
the product of the roots for the first polynomial:

(
−
20
)
(
m
+
n
i
)
(
m
−
n
i
)
=
−
b
  
⟹
  
−
20
(
m
2
+
n
)
=
−
b
  
⟹
  
b
=
20
(
m
2
+
n
)
(−20)(m+ 
n
​
 i)(m− 
n
​
 i)=−b⟹−20(m 
2
 +n)=−b⟹b=20(m 
2
 +n)
substituting 
m
=
10
m=10:

b
=
20
(
100
+
n
)
b=20(100+n)
the product of the roots for the second polynomial:

(
−
21
)
(
m
+
n
i
)
(
m
−
n
i
)
=
−
d
  
⟹
  
−
21
(
m
2
+
n
)
=
−
d
  
⟹
  
d
=
21
(
m
2
+
n
)
(−21)(m+ 
n
​
 i)(m− 
n
​
 i)=−d⟹−21(m 
2
 +n)=−d⟹d=21(m 
2
 +n)
substituting 
m
=
10
m=10:

d
=
21
(
100
+
n
)
d=21(100+n)
the sum of the products of the roots taken two at a time for the first polynomial:

(
−
20
)
(
m
+
n
i
)
+
(
−
20
)
(
m
−
n
i
)
+
(
m
+
n
i
)
(
m
−
n
i
)
=
a
(−20)(m+ 
n
​
 i)+(−20)(m− 
n
​
 i)+(m+ 
n
​
 i)(m− 
n
​
 i)=a
simplifying:

−
20
(
10
+
n
i
)
−
20
(
10
−
n
i
)
+
(
100
+
n
)
=
a
  
⟹
  
−
400
+
100
+
n
=
a
  
⟹
  
a
=
−
300
+
n
−20(10+ 
n
​
 i)−20(10− 
n
​
 i)+(100+n)=a⟹−400+100+n=a⟹a=−300+n
the sum of the products of the roots taken two at a time for the second polynomial:

(
−
21
)
(
m
+
n
i
)
+
(
−
21
)
(
m
−
n
i
)
+
(
m
+
n
i
)
(
m
−
n
i
)
=
0
(−21)(m+ 
n
​
 i)+(−21)(m− 
n
​
 i)+(m+ 
n
​
 i)(m− 
n
​
 i)=0
simplifying:

−
21
(
10
+
n
i
)
−
21
(
10
−
n
i
)
+
(
100
+
n
)
=
0
  
⟹
  
−
420
+
100
+
n
=
0
  
⟹
  
n
=
320
−21(10+ 
n
​
 i)−21(10− 
n
​
 i)+(100+n)=0⟹−420+100+n=0⟹n=320
therefore, 
m
=
10
m=10 and 
n
=
320
n=320, so:

m
+
n
=
10
+
320
=
330
m+n=10+320=330
330
330
​
