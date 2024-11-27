### Question:
Adults made up $\frac5{12}$ of the crowd of people at a concert. After a bus carrying $50$ more people arrived, adults made up $\frac{11}{25}$ of the people at the concert. Find the minimum number of adults who could have been at the concert after the bus arrived.


### Answer:
Let's dive into this problem step by step. so, we've got a concert with a certain number of people, and adults make up 5/12 of that crowd. then, a bus arrives with 50 more people, and after that, adults make up 11/25 of the entire crowd. we need to find the minimum number of adults after the bus arrived.

first, let's define some variables to make this clearer. let's say the initial number of people at the concert is 
c
c. according to the problem, adults are 
5
12
12
5
​
  of that crowd. so, the number of adults initially is 
5
12
c
12
5
​
 c.

then, a bus arrives with 50 more people. so, the new total number of people at the concert is 
c
+
50
c+50. after this, adults make up 
11
25
25
11
​
  of the crowd. but here's the thing: we don't know how many of those 50 new people are adults. that's a bit tricky.

wait, actually, the problem doesn't specify anything about the composition of the 50 people who arrived on the bus. it just says that after they arrived, the proportion of adults changed to 
11
25
25
11
​
 . so, we have to assume that the 50 people could be any combination of adults and non-adults, but we're looking for the minimum number of adults after the bus arrived.

hmm, actually, no. let's read it again: "after a bus carrying 50 more people arrived, adults made up 
11
25
25
11
​
  of the people at the concert." it doesn't specify how many of the 50 are adults, so we need to consider that the 50 could include any number of adults, but we're to find the minimum number of adults after the bus arrived. so, to minimize the number of adults after the bus arrived, we'd want to assume that as few adults as possible came on the bus.

wait, but we're to find the minimum number of adults after the bus arrived, given that the proportion is 
11
25
25
11
​
 . actually, i think i need to set up an equation based on the proportions.

let's denote:

- initial number of people: 
c
c

- initial number of adults: 
5
12
c
12
5
​
 c

- number of people after the bus arrives: 
c
+
50
c+50

- number of adults after the bus arrives: 
a
a

given that after the bus arrives, adults make up 
11
25
25
11
​
  of the crowd, so:

a
=
11
25
(
c
+
50
)
a= 
25
11
​
 (c+50)
but we also know that the number of adults after the bus arrives is the initial number of adults plus the number of adults who arrived on the bus. let's denote the number of adults who arrived on the bus as 
x
x. so:

a
=
5
12
c
+
x
a= 
12
5
​
 c+x
but we don't know 
x
x, and we're trying to minimize 
a
a, which would mean minimizing 
x
x. however, since we don't have any restrictions on 
x
x, it seems like we need another approach.

maybe i should consider that the number of adults after the bus arrives must be an integer, as you can't have a fraction of a person. so, 
a
=
11
25
(
c
+
50
)
a= 
25
11
​
 (c+50) must be an integer.

similarly, the initial number of adults 
5
12
c
12
5
​
 c must also be an integer.

so, both 
c
c and 
c
+
50
c+50 must be such that when multiplied by their respective fractions, they result in integers.

let's first find conditions on 
c
c.

for 
5
12
c
12
5
​
 c to be an integer, 
c
c must be a multiple of 12. let's set 
c
=
12
k
c=12k, where 
k
k is a positive integer.

then, the initial number of adults is 
5
12
×
12
k
=
5
k
12
5
​
 ×12k=5k.

after the bus arrives, the total number of people is 
12
k
+
50
12k+50, and the number of adults is 
11
25
(
12
k
+
50
)
25
11
​
 (12k+50).

this must also be an integer, so 
12
k
+
50
12k+50 must be a multiple of 25.

let’s denote 
12
k
+
50
=
25
m
12k+50=25m, where 
m
m is a positive integer.

so, 
12
k
=
25
m
−
50
12k=25m−50

simplify:

12
k
=
25
(
m
−
2
)
12k=25(m−2)

this tells us that 
12
k
12k is a multiple of 25, but 12 and 25 are coprime (their greatest common divisor is 1), so 
k
k must be a multiple of 25.

let’s set 
k
=
25
n
k=25n, where 
n
n is a positive integer.

then, 
c
=
12
k
=
12
×
25
n
=
300
n
c=12k=12×25n=300n

and the number of adults after the bus arrives is:

a
=
11
25
(
c
+
50
)
=
11
25
(
300
n
+
50
)
=
11
25
×
50
(
6
n
+
1
)
=
11
×
2
(
6
n
+
1
)
=
22
(
6
n
+
1
)
a= 
25
11
​
 (c+50)= 
25
11
​
 (300n+50)= 
25
11
​
 ×50(6n+1)=11×2(6n+1)=22(6n+1)

so, 
a
=
22
(
6
n
+
1
)
a=22(6n+1)

we need to find the minimum 
a
a, which occurs when 
n
n is as small as possible.

since 
n
n is a positive integer, the smallest value 
n
n can take is 1.

therefore, the minimum number of adults after the bus arrived is:

a
=
22
(
6
×
1
+
1
)
=
22
×
7
=
154
a=22(6×1+1)=22×7=154

but wait a second, let's check if this makes sense.

if 
n
=
1
n=1, then 
c
=
300
×
1
=
300
c=300×1=300

initial number of adults: 
5
12
×
300
=
125
12
5
​
 ×300=125

after the bus arrives, total people: 
300
+
50
=
350
300+50=350

number of adults after: 
11
25
×
350
=
154
25
11
​
 ×350=154

so, yes, that checks out.

but the problem asks for the minimum number of adults after the bus arrived, and from this calculation, it's 154. however, we need to make sure that there isn't a smaller possible value for 
a
a.

let’s see if there are smaller values of 
n
n that could work. since 
n
n is a positive integer starting from 1, and 
a
=
22
(
6
n
+
1
)
a=22(6n+1), for 
n
=
1
n=1, 
a
=
154
a=154, for 
n
=
2
n=2, 
a
=
22
(
13
)
=
286
a=22(13)=286, and so on. so, indeed, the smallest possible 
a
a is 154.

but let's double-check our earlier assumption that 
k
=
25
n
k=25n. we set 
k
=
25
n
k=25n because 
12
k
=
25
(
m
−
2
)
12k=25(m−2), and since 12 and 25 are coprime, 
k
k must be a multiple of 25. that seems correct.

alternatively, maybe there are other constraints we need to consider. for instance, 
c
c must be a positive integer, and so must be 
m
m, and the number of adults after the bus must also be an integer.

wait, but from our earlier steps, we've already ensured that 
a
a is an integer by choosing 
k
k as a multiple of 25.

is there any other condition we might be missing?

let’s consider if there are any restrictions on the number of adults that arrive on the bus. we assumed that the bus could bring any number of adults, but the problem doesn't specify, so our approach seems valid.

therefore, the minimum number of adults after the bus arrived is indeed 154.

**final answer**

154
154
​
