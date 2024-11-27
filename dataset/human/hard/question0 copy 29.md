### Question:

A right square pyramid with volume $54$ has a base with side length $6.$ The five vertices of the pyramid all lie on a sphere with radius $\frac mn$, where $m$ and $n$ are relatively prime positive integers. Find $m+n$.

### Answer:
So i've got this problem here about a right square pyramid with a given volume and base side length, and i need to find the radius of a sphere that passes through all its vertices. the answer should be in the form of a fraction m/n, where m and n are coprime, and then find m + n. okay, let's break this down step by step.

first, i need to recall what a right square pyramid is. it's a pyramid with a square base and the apex (the top point) directly above the center of the base. that makes sense. the base has side length 6, and the volume is 54. i know the formula for the volume of a pyramid is (1/3) * base area * height. so, i can use that to find the height of the pyramid.

let's calculate the base area. since it's a square with side length 6, the area is 6 * 6 = 36. so, volume = (1/3) * 36 * height = 54. that means 12 * height = 54, so height = 54 / 12 = 4.5. okay, so the height of the pyramid is 4.5 units.

now, the problem says that all five vertices of the pyramid lie on a sphere. i need to find the radius of this sphere. hmm, that sounds like the sphere is the circumscribed sphere of the pyramid.

to find the radius of the sphere that passes through all the vertices of the pyramid, i need to find the distance from the center of the sphere to any of the vertices, since all these distances are equal to the radius.

but where is the center of this sphere? in general, for a regular pyramid, the center of the circumscribed sphere isn't necessarily at the same point as the apex or the centroid of the pyramid. i might need to find the coordinates of all the vertices and then find the circumradius from there.

maybe it's easier to set up a coordinate system to model this situation. let's place the base of the pyramid on the xy-plane, centered at the origin. since it's a square base with side length 6, the coordinates of the base vertices can be:

a: (3, 3, 0)

b: (3, -3, 0)

c: (-3, -3, 0)

d: (-3, 3, 0)

and the apex, e, is directly above the center of the base, which is at (0, 0, h), where h is the height of the pyramid, which we found to be 4.5.

so, e: (0, 0, 4.5)

now, all five points a, b, c, d, and e lie on a sphere. i need to find the radius of this sphere.

one way to find the center of the sphere is to solve the system of equations that equate the distances from the center to each of the points.

let’s denote the center of the sphere as (x, y, z). then, the distance from (x, y, z) to each vertex is equal to the radius r.

so, for point a: (x - 3)^2 + (y - 3)^2 + (z - 0)^2 = r^2

for point b: (x - 3)^2 + (y + 3)^2 + z^2 = r^2

for point c: (x + 3)^2 + (y + 3)^2 + z^2 = r^2

for point d: (x + 3)^2 + (y - 3)^2 + z^2 = r^2

for point e: x^2 + y^2 + (z - 4.5)^2 = r^2

since all these equal r^2, i can set them equal to each other pairwise to eliminate r.

first, set the equations for a and b equal:

(x - 3)^2 + (y - 3)^2 + z^2 = (x - 3)^2 + (y + 3)^2 + z^2

simplify:

(y - 3)^2 = (y + 3)^2

expand both sides:

y^2 - 6y + 9 = y^2 + 6y + 9

subtract y^2 and 9 from both sides:

-6y = 6y

so, -12y = 0 → y = 0

okay, so the y-coordinate of the center is 0.

next, set the equations for a and c equal:

(x - 3)^2 + (y - 3)^2 + z^2 = (x + 3)^2 + (y + 3)^2 + z^2

we already know y = 0, so plug that in:

(x - 3)^2 + (0 - 3)^2 + z^2 = (x + 3)^2 + (0 + 3)^2 + z^2

simplify:

(x - 3)^2 + 9 + z^2 = (x + 3)^2 + 9 + z^2

cancel out the 9 and z^2:

(x - 3)^2 = (x + 3)^2

expand both sides:

x^2 - 6x + 9 = x^2 + 6x + 9

subtract x^2 and 9 from both sides:

-6x = 6x → -12x = 0 → x = 0

so, the x-coordinate of the center is also 0.

now, we know the center is at (0, 0, z). let's use points a and e to find z.

from point a: (0 - 3)^2 + (0 - 0)^2 + (z - 0)^2 = r^2 → 9 + z^2 = r^2

from point e: 0^2 + 0^2 + (z - 4.5)^2 = r^2 → (z - 4.5)^2 = r^2

set them equal: 9 + z^2 = (z - 4.5)^2

expand the right side: z^2 - 9z + 20.25 = 9 + z^2

subtract z^2 from both sides: -9z + 20.25 = 9

then, -9z = 9 - 20.25 → -9z = -11.25 → z = (-11.25)/(-9) = 1.25

so, z = 1.25

now, the center of the sphere is at (0, 0, 1.25), and the radius r can be found using the distance from the center to any vertex.

let's use point a: r^2 = (3)^2 + (3)^2 + (1.25)^2 = 9 + 9 + 1.5625 = 19.5625

so, r = sqrt(19.5625)

hmm, 19.5625 is 313/16, so sqrt(313/16) = sqrt(313)/4

wait, 19.5625 is 313/16? let me check: 16 * 1.2225 = 19.5625? wait, no. wait, 19.5625 is 313/16. let's confirm:

313 divided by 16 is 19.5625, yes.

so, r = sqrt(313)/4

but 313 is a prime number, i think, so it can't be simplified further.

wait, is 313 prime? let's check:

313 divided by 2 is not an integer.

313 divided by 3: 3*104=312, remainder 1.

313 divided by 5: ends with 3, so no.

313 divided by 7: 7*44=308, remainder 5.

313 divided by 11: 11*28=308, remainder 5.

313 divided by 13: 13*24=312, remainder 1.

so, yes, 313 is prime.

therefore, the radius is sqrt(313)/4.

but the problem asks for the radius in the form m/n, where m and n are relatively prime positive integers. hmm, sqrt(313) is irrational, so perhaps i made a mistake somewhere.

wait a minute, maybe i should double-check my calculations.

let me go back to where i set up the equations.

i had the center at (0,0,z), and i used points a and e to find z.

from a: 9 + z^2 = r^2

from e: (z - 4.5)^2 = r^2

setting equal: 9 + z^2 = z^2 - 9z + 20.25 → 9 = -9z + 20.25 → -9z = 9 - 20.25 → -9z = -11.25 → z = 1.25

then, r^2 = 9 + (1.25)^2 = 9 + 1.5625 = 10.5625, not 19.5625.

wait, i think i miscalculated earlier. let me recalculate:

from point a: (0 - 3)^2 + (0 - 0)^2 + (z - 0)^2 = r^2 → 9 + z^2 = r^2

from point e: 0^2 + 0^2 + (z - 4.5)^2 = r^2 → (z - 4.5)^2 = r^2

set equal: 9 + z^2 = z^2 - 9z + 20.25 → 9 = -9z + 20.25 → -9z = -11.25 → z = 1.25

then, r^2 = 9 + (1.25)^2 = 9 + 1.5625 = 10.5625

so, r = sqrt(10.5625). wait, 10.5625 is 10 + 9/16 = 169/16, since 16*10=160 + 9 = 169.

so, sqrt(169/16) = 13/4.

ah, there we go. so, r = 13/4.

wait, but earlier i thought 19.5625 was 313/16, but actually, it's 10.5625, which is 169/16, and sqrt of that is 13/4.

so, the radius is 13/4.

therefore, m = 13, n = 4, and m + n = 17.

but let me confirm this with another point to ensure consistency.

let's use point b: (3, -3, 0)

distance from center (0,0,1.25) to b: sqrt((3)^2 + (-3)^2 + (1.25)^2) = sqrt(9 + 9 + 1.5625) = sqrt(19.5625) = sqrt(313/16) = sqrt(313)/4

wait, that's not equal to 13/4. there's inconsistency here.

wait, no. if r is 13/4, then r^2 should be (13/4)^2 = 169/16 = 10.5625.

but for point b: (3)^2 + (-3)^2 + (1.25)^2 = 9 + 9 + 1.5625 = 19.5625, which is 313/16, which is not equal to 169/16.

this inconsistency suggests i made a mistake in assuming that all points lie on the same sphere with center at (0,0,1.25). perhaps my approach is flawed.

let me try another method.

i recall that for a pyramid to have all its vertices on a sphere, it must be a regular tetrahedron or something similar, but this is a square pyramid, not a regular tetrahedron.

alternatively, maybe i can use the formula for the circumradius of a tetrahedron, but this is a square pyramid, not a general tetrahedron.

wait, perhaps i should consider the coordinates again, but this time ensure that the distances from the center to all points are equal.

let me set the center at (0,0,z), as before.

from point a: (3)^2 + (3)^2 + z^2 = r^2 → 9 + 9 + z^2 = r^2 → 18 + z^2 = r^2

from point e: 0^2 + 0^2 + (z - 4.5)^2 = r^2 → z^2 - 9z + 20.25 = r^2

set equal: 18 + z^2 = z^2 - 9z + 20.25 → 18 = -9z + 20.25 → -9z = -2.25 → z = 0.25

wait, earlier i got z = 1.25, but now i get z = 0.25. there's inconsistency here.

wait, no, let's see.

from point a: 9 + 9 + z^2 = r^2 → 18 + z^2 = r^2

from point e: z^2 - 9z + 20.25 = r^2

set equal: 18 + z^2 = z^2 - 9z + 20.25 → 18 = -9z + 20.25 → -9z = 2.25 → z = -0.25

wait, now z = -0.25? that can't be right, because the apex is at z = 4.5, and the base is at z = 0, so the center shouldn't be below the base.

i must have messed up the sign somewhere.

let me re-express the distance from center to e.

the center is at (0,0,z), and e is at (0,0,4.5).

so, distance squared is (0 - 0)^2 + (0 - 0)^2 + (z - 4.5)^2 = (z - 4.5)^2 = r^2

from point a: (3 - 0)^2 + (3 - 0)^2 + (0 - z)^2 = 9 + 9 + z^2 = 18 + z^2 = r^2

set equal: 18 + z^2 = (z - 4.5)^2

expand the right side: z^2 - 9z + 20.25 = 18 + z^2

subtract z^2 from both sides: -9z + 20.25 = 18

then, -9z = 18 - 20.25 = -2.25 → z = (-2.25)/(-9) = 0.25

so, z = 0.25

now, r^2 = 18 + (0.25)^2 = 18 + 0.0625 = 18.0625

which is 18 + 1/16 = 289/16, so r = sqrt(289/16) = 17/4

wait, earlier i thought it was 13/4, but now it's 17/4.

this suggests that perhaps i made a mistake in earlier calculations.

let me verify with another point.

take point b: (3, -3, 0)

distance to center (0,0,0.25):

sqrt((3)^2 + (-3)^2 + (0 - 0.25)^2) = sqrt(9 + 9 + 0.0625) = sqrt(18.0625) = sqrt(289/16) = 17/4

similarly, point d: (-3, 3, 0), same as point a.

point e: (0,0,4.5)

distance to center: sqrt(0^2 + 0^2 + (4.5 - 0.25)^2) = sqrt(4.25^2) = 4.25, which is 17/4.

yes, that matches.

earlier, i mistakenly calculated r^2 as 10.5625, but that was incorrect.

so, the correct radius is 17/4.

therefore, m = 17, n = 4, and m + n = 21.

wait, but the problem mentions that m and n are relatively prime positive integers. 17 and 4 are coprime, so that should be fine.

let me just double-check everything again to be sure.

given a right square pyramid with base side 6 and volume 54.

volume = (1/3)*base area*height → 54 = (1/3)*36*height → 54 = 12*height → height = 4.5

set up coordinates:

base vertices: (3,3,0), (3,-3,0), (-3,-3,0), (-3,3,0)

apex: (0,0,4.5)

find sphere passing through all five points.

assume center at (0,0,z), since by symmetry x and y should be zero.

from a: 3^2 + 3^2 + z^2 = r^2 → 9 + 9 + z^2 = r^2 → 18 + z^2 = r^2

from e: 0^2 + 0^2 + (z - 4.5)^2 = r^2 → z^2 - 9z + 20.25 = r^2

set equal: 18 + z^2 = z^2 - 9z + 20.25 → 18 = -9z + 20.25 → -9z = 2.25 → z = -0.25

wait, earlier i got z = 0.25, but solving it correctly, it's z = -0.25.

wait, now i'm confused.

from 18 + z^2 = z^2 - 9z + 20.25

subtract z^2: 18 = -9z + 20.25

then, -9z = 18 - 20.25 = -2.25 → z = (-2.25)/(-9) = 0.25

wait, i'm getting z = 0.25 again.

but according to this, z = 0.25, which is above the base, which is at z=0, and below the apex at z=4.5, which makes sense.

then, r^2 = 18 + (0.25)^2 = 18 + 0.0625 = 18.0625 = 289/16

so, r = sqrt(289/16) = 17/4

now, check with point b: (3,-3,0)

distance to center (0,0,0.25): sqrt(9 + 9 + 0.0625) = sqrt(18.0625) = 17/4

similarly, point e: (0,0,4.5)

distance to center: sqrt(0 + 0 + (4.5 - 0.25)^2) = sqrt(4.25^2) = 4.25 = 17/4

all points give the same radius, so this seems consistent.

earlier, i thought i had z = 1.25 and r = 13/4, but that was a mistake.

therefore, the correct radius is 17/4, so m = 17, n = 4, and m + n = 21.

wait, but the problem says to give m + n where m and n are coprime, and 17 and 4 are coprime, so 21 should be the answer.

however, i recall that in the initial approach, i had a different answer, but upon rechecking, 17/4 seems correct.

alternatively, perhaps there's a formula for the circumradius of a right square pyramid.

alternatively, maybe i can use the fact that the sphere passes through the base square and the apex, and find the circumradius using properties of pyramids.

but given that the coordinate method seems consistent, i'll stick with r = 17/4, so m + n = 21.

**final answer**

21
21
​
 
Given a right square pyramid with a base side length of 6 and a volume of 54, we need to find the radius of the sphere that passes through all its vertices and express it as 
m
n
n
m
​
 , where 
m
m and 
n
n are relatively prime positive integers, and then find 
m
+
n
m+n.

first, we calculate the height of the pyramid using the volume formula:

volume
=
1
3
×
base area
×
height
volume= 
3
1
​
 ×base area×height
54
=
1
3
×
36
×
height
  
⟹
  
54
=
12
×
height
  
⟹
  
height
=
4.5
54= 
3
1
​
 ×36×height⟹54=12×height⟹height=4.5
next, we place the base of the pyramid on the 
x
y
xy-plane centered at the origin, with vertices at:

a
:
(
3
,
3
,
0
)
,
b
:
(
3
,
−
3
,
0
)
,
c
:
(
−
3
,
−
3
,
0
)
,
d
:
(
−
3
,
3
,
0
)
a:(3,3,0),b:(3,−3,0),c:(−3,−3,0),d:(−3,3,0)
and the apex at:

e
:
(
0
,
0
,
4.5
)
e:(0,0,4.5)
we assume the center of the sphere is at 
(
0
,
0
,
z
)
(0,0,z). using the distance formula, we set up equations for the radius 
r
r:

(
3
)
2
+
(
3
)
2
+
z
2
=
r
2
  
⟹
  
18
+
z
2
=
r
2
(3) 
2
 +(3) 
2
 +z 
2
 =r 
2
 ⟹18+z 
2
 =r 
2
 
(
0
)
2
+
(
0
)
2
+
(
z
−
4.5
)
2
=
r
2
  
⟹
  
z
2
−
9
z
+
20.25
=
r
2
(0) 
2
 +(0) 
2
 +(z−4.5) 
2
 =r 
2
 ⟹z 
2
 −9z+20.25=r 
2
 
equating the two expressions for 
r
2
r 
2
 :

18
+
z
2
=
z
2
−
9
z
+
20.25
  
⟹
  
18
=
−
9
z
+
20.25
  
⟹
  
−
9
z
=
2.25
  
⟹
  
z
=
0.25
18+z 
2
 =z 
2
 −9z+20.25⟹18=−9z+20.25⟹−9z=2.25⟹z=0.25
substituting 
z
=
0.25
z=0.25 back to find 
r
r:

r
2
=
18
+
(
0.25
)
2
=
18
+
0.0625
=
18.0625
=
289
16
r 
2
 =18+(0.25) 
2
 =18+0.0625=18.0625= 
16
289
​
 
r
=
289
16
=
17
4
r= 
16
289
​
 
​
 = 
4
17
​
 
thus, the radius of the sphere is 
17
4
4
17
​
 , and since 17 and 4 are coprime, we have:

m
=
17
,
n
=
4
  
⟹
  
m
+
n
=
21
m=17,n=4⟹m+n=21
21
21
​
 

