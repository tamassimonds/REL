### Question:

Find the point in the plane $3x - 4y + 5z = 30$ that is closest to the point $(1,2,3).$

### Answer:

**Find the point in the plane 3x−4y+5z=303x - 4y + 5z = 303x−4y+5z=30 that is closest to the point (1,2,3)(1, 2, 3)(1,2,3).**

At first glance, it seems a bit tricky, but I remember there are a few methods I can use to approach this. Let me think through them:

1. **Orthogonal Projection Method:** This involves projecting the given point onto the plane along the direction perpendicular to the plane.
2. **Minimizing the Distance Function:** Here, I'd set up the distance formula between the given point and a general point on the plane and then minimize this distance.
3. **Using Lagrange Multipliers:** This is a calculus-based method where I'd optimize the distance function subject to the plane's equation.

I think the **Orthogonal Projection Method** might be the most straightforward, so I'll start with that.

---

### **Method 1: Orthogonal Projection**

**Step 1: Identify the Plane and the Given Point**

- **Plane Equation:** 3x−4y+5z=30
    
    3x−4y+5z=303x - 4y + 5z = 30
    
- **Given Point:** P0=(1,2,3)
    
    P0=(1,2,3)P_0 = (1, 2, 3)
    

*Reflection:* Okay, I need to find a point P=(x,y,z)P = (x, y, z)P=(x,y,z) on the plane that's closest to P0P_0P0. The closest point should lie along the line that's perpendicular to the plane.

**Step 2: Determine the Normal Vector of the Plane**

The coefficients of xxx, yyy, and zzz in the plane equation give the **normal vector** n\mathbf{n}n to the plane.

n=(3,−4,5)\mathbf{n} = (3, -4, 5)

n=(3,−4,5)

*Reflection:* This normal vector is crucial because the direction from P0P_0P0 to the closest point PPP will be along this vector.

**Step 3: Express the Closest Point Using a Parameter**

I can express the closest point PPP as moving from P0P_0P0 in the direction of the normal vector by some scalar ttt:

P=P0+tn=(1,2,3)+t(3,−4,5)P = P_0 + t\mathbf{n} = (1, 2, 3) + t(3, -4, 5)

P=P0+tn=(1,2,3)+t(3,−4,5)

Breaking this down into components:

{x=1+3ty=2−4tz=3+5t\begin{cases}
x = 1 + 3t \\
y = 2 - 4t \\
z = 3 + 5t \\
\end{cases}

⎩

⎨

⎧x=1+3ty=2−4tz=3+5t

*Reflection:* Here, ttt determines how far I move along the normal vector from P0P_0P0 to reach the plane.

**Step 4: Substitute into the Plane Equation to Solve for ttt**

Since PPP lies on the plane, its coordinates must satisfy 3x−4y+5z=303x - 4y + 5z = 303x−4y+5z=30. Plugging in the expressions for xxx, yyy, and zzz:

3(1+3t)−4(2−4t)+5(3+5t)=303(1 + 3t) - 4(2 - 4t) + 5(3 + 5t) = 30

3(1+3t)−4(2−4t)+5(3+5t)=30

Let's expand each term:

3+9t−8+16t+15+25t=303 + 9t - 8 + 16t + 15 + 25t = 30

3+9t−8+16t+15+25t=30

*Reflection:* Wait, let me double-check that expansion:

- 3(1+3t)=3+9t3(1 + 3t) = 3 + 9t3(1+3t)=3+9t ✅
- −4(2−4t)=−8+16t4(2 - 4t) = -8 + 16t−4(2−4t)=−8+16t ✅
- 5(3+5t)=15+25t5(3 + 5t) = 15 + 25t5(3+5t)=15+25t ✅

Now, combining like terms:

(3−8+15)+(9t+16t+25t)=3010+50t=30(3 - 8 + 15) + (9t + 16t + 25t) = 30 \\
10 + 50t = 30

(3−8+15)+(9t+16t+25t)=3010+50t=30

*Reflection:* Looks good so far. No mistakes here.

**Step 5: Solve for ttt**

10+50t=3050t=20t=2050=2510 + 50t = 30 \\
50t = 20 \\
t = \frac{20}{50} = \frac{2}{5}

10+50t=3050t=20t=5020=52

*Reflection:* Great, I've found ttt. Now, let's use it to find the coordinates of the closest point PPP.

**Step 6: Find the Coordinates of PPP**

Substituting t=25t = \frac{2}{5}t=52 back into the expressions for xxx, yyy, and zzz:

x=1+3(25)=1+65=115=2.2y=2−4(25)=2−85=25=0.4z=3+5(25)=3+2=5x = 1 + 3\left(\frac{2}{5}\right) = 1 + \frac{6}{5} = \frac{11}{5} = 2.2 \\
y = 2 - 4\left(\frac{2}{5}\right) = 2 - \frac{8}{5} = \frac{2}{5} = 0.4 \\
z = 3 + 5\left(\frac{2}{5}\right) = 3 + 2 = 5 \\

x=1+3(52)=1+56=511=2.2y=2−4(52)=2−58=52=0.4z=3+5(52)=3+2=5

*Reflection:* So, the closest point PPP is (115,25,5)\left( \frac{11}{5}, \frac{2}{5}, 5 \right)(511,52,5) or (2.2,0.4,5)(2.2, 0.4, 5)(2.2,0.4,5). This makes sense since I've moved along the direction of the normal vector from P0P_0P0 to reach the plane.

---

### **Method 2: Minimizing the Distance Function**

**Step 1: Set Up the Distance Formula**

Another approach is to minimize the distance between P0=(1,2,3)P_0 = (1, 2, 3)P0=(1,2,3) and a general point P=(x,y,z)P = (x, y, z)P=(x,y,z) on the plane.

D=(x−1)2+(y−2)2+(z−3)2D = \sqrt{(x - 1)^2 + (y - 2)^2 + (z - 3)^2}

D=(x−1)2+(y−2)2+(z−3)2

*Reflection:* To simplify, I'll minimize D2D^2D2 instead of DDD to avoid dealing with the square root.

D2=(x−1)2+(y−2)2+(z−3)2D^2 = (x - 1)^2 + (y - 2)^2 + (z - 3)^2

D2=(x−1)2+(y−2)2+(z−3)2

**Step 2: Use the Plane Constraint**

Since PPP lies on the plane 3x−4y+5z=303x - 4y + 5z = 303x−4y+5z=30, I can express one variable in terms of the others. Let's solve for zzz:

3x−4y+5z=305z=30−3x+4yz=30−3x+4y53x - 4y + 5z = 30 \\
5z = 30 - 3x + 4y \\
z = \frac{30 - 3x + 4y}{5}

3x−4y+5z=305z=30−3x+4yz=530−3x+4y

*Reflection:* Now, I can substitute this expression for zzz back into the distance squared formula, making it a function of xxx and yyy only.

**Step 3: Substitute zzz into the Distance Formula**

D2=(x−1)2+(y−2)2+(30−3x+4y5−3)2D^2 = (x - 1)^2 + (y - 2)^2 + \left( \frac{30 - 3x + 4y}{5} - 3 \right)^2

D2=(x−1)2+(y−2)2+(530−3x+4y−3)2

Simplifying the expression inside the last square:

30−3x+4y5−3=30−3x+4y−155=15−3x+4y5\frac{30 - 3x + 4y}{5} - 3 = \frac{30 - 3x + 4y - 15}{5} = \frac{15 - 3x + 4y}{5}

530−3x+4y−3=530−3x+4y−15=515−3x+4y

So,

D2=(x−1)2+(y−2)2+(15−3x+4y5)2D^2 = (x - 1)^2 + (y - 2)^2 + \left( \frac{15 - 3x + 4y}{5} \right)^2

D2=(x−1)2+(y−2)2+(515−3x+4y)2

*Reflection:* This expression is a bit messy, but I can work with it. Next, I'll take partial derivatives with respect to xxx and yyy to find the minimum.

**Step 4: Take Partial Derivatives and Set Them to Zero**

To minimize D2D^2D2, I'll take the partial derivatives with respect to xxx and yyy, set them to zero, and solve for xxx and yyy.

1. **Partial derivative with respect to xxx:**

∂D2∂x=2(x−1)+2(15−3x+4y5)(−35)\frac{\partial D^2}{\partial x} = 2(x - 1) + 2\left( \frac{15 - 3x + 4y}{5} \right) \left( \frac{-3}{5} \right)

∂x∂D2=2(x−1)+2(515−3x+4y)(5−3)

Simplifying:

∂D2∂x=2(x−1)−6(15−3x+4y)25\frac{\partial D^2}{\partial x} = 2(x - 1) - \frac{6(15 - 3x + 4y)}{25}

∂x∂D2=2(x−1)−256(15−3x+4y)

1. **Partial derivative with respect to yyy:**

∂D2∂y=2(y−2)+2(15−3x+4y5)(45)\frac{\partial D^2}{\partial y} = 2(y - 2) + 2\left( \frac{15 - 3x + 4y}{5} \right) \left( \frac{4}{5} \right)

∂y∂D2=2(y−2)+2(515−3x+4y)(54)

Simplifying:

∂D2∂y=2(y−2)+8(15−3x+4y)25\frac{\partial D^2}{\partial y} = 2(y - 2) + \frac{8(15 - 3x + 4y)}{25}

∂y∂D2=2(y−2)+258(15−3x+4y)

*Reflection:* These derivatives look quite complicated. Solving them simultaneously might be time-consuming and prone to errors. Maybe there's a better approach, or perhaps the Orthogonal Projection Method is indeed more efficient.

**Step 5: Re-evaluating the Approach**

Given the complexity of the partial derivatives, I'm starting to think that **Method 1: Orthogonal Projection** was the better choice. However, for thoroughness, I'll attempt to proceed with this method using Lagrange multipliers.

**Alternative Approach: Using Lagrange Multipliers**

To minimize D2D^2D2 subject to the constraint 3x−4y+5z=303x - 4y + 5z = 303x−4y+5z=30, I'll set up the Lagrangian:

L(x,y,z,λ)=(x−1)2+(y−2)2+(z−3)2+λ(3x−4y+5z−30)\mathcal{L}(x, y, z, \lambda) = (x - 1)^2 + (y - 2)^2 + (z - 3)^2 + \lambda(3x - 4y + 5z - 30)

L(x,y,z,λ)=(x−1)2+(y−2)2+(z−3)2+λ(3x−4y+5z−30)

**Taking Partial Derivatives:**

1. **With respect to xxx:**

∂L∂x=2(x−1)+3λ=0\frac{\partial \mathcal{L}}{\partial x} = 2(x - 1) + 3\lambda = 0

∂x∂L=2(x−1)+3λ=0

1. **With respect to yyy:**

∂L∂y=2(y−2)−4λ=0\frac{\partial \mathcal{L}}{\partial y} = 2(y - 2) - 4\lambda = 0

∂y∂L=2(y−2)−4λ=0

1. **With respect to zzz:**

∂L∂z=2(z−3)+5λ=0\frac{\partial \mathcal{L}}{\partial z} = 2(z - 3) + 5\lambda = 0

∂z∂L=2(z−3)+5λ=0

1. **With respect to λ\lambdaλ:**

∂L∂λ=3x−4y+5z−30=0\frac{\partial \mathcal{L}}{\partial \lambda} = 3x - 4y + 5z - 30 = 0

∂λ∂L=3x−4y+5z−30=0

*Reflection:* Now, I have a system of four equations. Let's solve them step by step.

**Solving the Equations:**

From the first equation:

2(x−1)+3λ=0⇒2x−2+3λ=0⇒2x+3λ=2(1)2(x - 1) + 3\lambda = 0 \\
\Rightarrow 2x - 2 + 3\lambda = 0 \\
\Rightarrow 2x + 3\lambda = 2 \quad \text{(1)}

2(x−1)+3λ=0⇒2x−2+3λ=0⇒2x+3λ=2(1)

From the second equation:

2(y−2)−4λ=0⇒2y−4−4λ=0⇒2y−4λ=4(2)2(y - 2) - 4\lambda = 0 \\
\Rightarrow 2y - 4 - 4\lambda = 0 \\
\Rightarrow 2y - 4\lambda = 4 \quad \text{(2)}

2(y−2)−4λ=0⇒2y−4−4λ=0⇒2y−4λ=4(2)

From the third equation:

2(z−3)+5λ=0⇒2z−6+5λ=0⇒2z+5λ=6(3)2(z - 3) + 5\lambda = 0 \\
\Rightarrow 2z - 6 + 5\lambda = 0 \\
\Rightarrow 2z + 5\lambda = 6 \quad \text{(3)}

2(z−3)+5λ=0⇒2z−6+5λ=0⇒2z+5λ=6(3)

And the fourth equation is the plane equation:

3x−4y+5z=30(4)3x - 4y + 5z = 30 \quad \text{(4)}

3x−4y+5z=30(4)

*Reflection:* Now, I'll solve for λ\lambdaλ from Equation (1):

2x+3λ=2⇒3λ=2−2x⇒λ=2−2x32x + 3\lambda = 2 \\
\Rightarrow 3\lambda = 2 - 2x \\
\Rightarrow \lambda = \frac{2 - 2x}{3}

2x+3λ=2⇒3λ=2−2x⇒λ=32−2x

*Reflection:* Next, I'll substitute λ\lambdaλ into Equations (2) and (3) to express yyy and zzz in terms of xxx.

**Substituting λ\lambdaλ into Equation (2):**

2y−4(2−2x3)=4⇒2y−8−8x3=4⇒2y=4+8−8x3⇒2y=12+8−8x3⇒2y=20−8x3⇒y=20−8x6=10−4x3(5)2y - 4\left( \frac{2 - 2x}{3} \right) = 4 \\
\Rightarrow 2y - \frac{8 - 8x}{3} = 4 \\
\Rightarrow 2y = 4 + \frac{8 - 8x}{3} \\
\Rightarrow 2y = \frac{12 + 8 - 8x}{3} \\
\Rightarrow 2y = \frac{20 - 8x}{3} \\
\Rightarrow y = \frac{20 - 8x}{6} = \frac{10 - 4x}{3} \quad \text{(5)}

2y−4(32−2x)=4⇒2y−38−8x=4⇒2y=4+38−8x⇒2y=312+8−8x⇒2y=320−8x⇒y=620−8x=310−4x(5)

**Substituting λ\lambdaλ into Equation (3):**

2z+5(2−2x3)=6⇒2z+10−10x3=6⇒2z=6−10−10x3⇒2z=18−10+10x3⇒2z=8+10x3⇒z=8+10x6=4+5x3(6)2z + 5\left( \frac{2 - 2x}{3} \right) = 6 \\
\Rightarrow 2z + \frac{10 - 10x}{3} = 6 \\
\Rightarrow 2z = 6 - \frac{10 - 10x}{3} \\
\Rightarrow 2z = \frac{18 - 10 + 10x}{3} \\
\Rightarrow 2z = \frac{8 + 10x}{3} \\
\Rightarrow z = \frac{8 + 10x}{6} = \frac{4 + 5x}{3} \quad \text{(6)}

2z+5(32−2x)=6⇒2z+310−10x=6⇒2z=6−310−10x⇒2z=318−10+10x⇒2z=38+10x⇒z=68+10x=34+5x(6)

*Reflection:* Now, I'll substitute yyy and zzz from Equations (5) and (6) into the plane equation (Equation 4) to solve for xxx:

3x−4(10−4x3)+5(4+5x3)=303x - 4\left( \frac{10 - 4x}{3} \right) + 5\left( \frac{4 + 5x}{3} \right) = 30

3x−4(310−4x)+5(34+5x)=30

Simplifying:

3x−40−16x3+20+25x3=303x - \frac{40 - 16x}{3} + \frac{20 + 25x}{3} = 30

3x−340−16x+320+25x=30

To eliminate the fractions, multiply each term by 3:

9x−(40−16x)+(20+25x)=909x - (40 - 16x) + (20 + 25x) = 90

9x−(40−16x)+(20+25x)=90

Expanding:

9x−40+16x+20+25x=90(9x+16x+25x)+(−40+20)=9050x−20=9050x=110x=11050=115=2.29x - 40 + 16x + 20 + 25x = 90 \\
(9x + 16x + 25x) + (-40 + 20) = 90 \\
50x - 20 = 90 \\
50x = 110 \\
x = \frac{110}{50} = \frac{11}{5} = 2.2

9x−40+16x+20+25x=90(9x+16x+25x)+(−40+20)=9050x−20=9050x=110x=50110=511=2.2

*Reflection:* I've found x=115x = \frac{11}{5}x=511. Now, let's find yyy and zzz using Equations (5) and (6):

**Finding yyy:**

y=10−4x3=10−4×1153=10−4453=50−4453=653=615=25=0.4y = \frac{10 - 4x}{3} = \frac{10 - 4 \times \frac{11}{5}}{3} = \frac{10 - \frac{44}{5}}{3} = \frac{\frac{50 - 44}{5}}{3} = \frac{\frac{6}{5}}{3} = \frac{6}{15} = \frac{2}{5} = 0.4

y=310−4x=310−4×511=310−544=3550−44=356=156=52=0.4

**Finding zzz:**

z=4+5x3=4+5×1153=4+113=153=5z = \frac{4 + 5x}{3} = \frac{4 + 5 \times \frac{11}{5}}{3} = \frac{4 + 11}{3} = \frac{15}{3} = 5

z=34+5x=34+5×511=34+11=315=5

*Reflection:* So, the closest point PPP is (115,25,5)\left( \frac{11}{5}, \frac{2}{5}, 5 \right)(511,52,5) or (2.2,0.4,5)(2.2, 0.4, 5)(2.2,0.4,5). This matches the result from the Orthogonal Projection Method, which is reassuring.

---

### **Conclusion**

After exploring both methods, it's clear that **Method 1: Orthogonal Projection** is more straightforward and efficient for this problem. It allowed me to directly find the closest point by leveraging the plane's normal vector without getting bogged down in complex algebra.

**Final Answer**

The point on the plane 3x−4y+5z=303x - 4y + 5z = 303x−4y+5z=30 that is closest to (1,2,3)(1, 2, 3)(1,2,3) is:

(115, 25, 5)or(2.2, 0.4, 5)\boxed{\left( \frac{11}{5},\ \frac{2}{5},\ 5 \right)} \quad \text{or} \quad \boxed{(2.2,\ 0.4,\ 5)}

(511, 52, 5)or(2.2, 0.4, 5)

*Final Reflection:* While both methods led me to the correct answer, the Orthogonal Projection Method was undeniably more efficient. It highlights the importance of choosing the right strategy to simplify problem-solving, especially under exam conditions where time is of the essence.

---

### **Extra Step: Verifying the Solution**

To ensure that the point (115, 25, 5)\left( \frac{11}{5},\ \frac{2}{5},\ 5 \right)(511, 52, 5) indeed lies on the plane 3x−4y+5z=303x - 4y + 5z = 303x−4y+5z=30, I'll substitute the coordinates back into the plane equation.

**Substituting x=115x = \frac{11}{5}x=511, y=25y = \frac{2}{5}y=52, and z=5z = 5z=5 into the plane equation:**

3(115)−4(25)+5(5)=303\left( \frac{11}{5} \right) - 4\left( \frac{2}{5} \right) + 5(5) = 30

3(511)−4(52)+5(5)=30

Calculating each term:

335−85+25=30\frac{33}{5} - \frac{8}{5} + 25 = 30

533−58+25=30

Combining the fractions:

33−85+25=255+25=5+25=30\frac{33 - 8}{5} + 25 = \frac{25}{5} + 25 = 5 + 25 = 30

533−8+25=525+25=5+25=30

*Reflection:* The left side equals the right side (30=3030 = 3030=30), confirming that the point (115, 25, 5)\left( \frac{11}{5},\ \frac{2}{5},\ 5 \right)(511, 52, 5) lies on the plane. This verification step assures me that the solution is correct.

---

*Final Reflection:* Adding a verification step not only reinforces the correctness of the solution but also builds confidence in the methods used. It's a good practice to always check your final answer, especially in exam settings, to avoid any unnoticed errors.

### Actual Solution:

Let $A = (1,2,3),$ and let $P$ be the point in the plane which is closest to $A.$ [asy] import three; size(180); currentprojection = perspective(6,3,2); triple I = (1,0,0), J = (0,1,0), K = (0,0,1), O = (0,0,0); triple A = (0,1.8,1), P = (0,1.8,0); draw(surface((2*I + 3*J)--(2*I - 1*J)--(-2*I - 1*J)--(-2*I + 3*J)--cycle),paleyellow,nolight); draw((2*I + 3*J)--(2*I - 1*J)--(-2*I - 1*J)--(-2*I + 3*J)--cycle); draw(A--P); dot("$A$", A, N); dot("$P$", P, E); [/asy] Then $\overrightarrow{AP}$ is a multiple of the normal vector of the plane, which is $\begin{pmatrix} 3 \\ -4 \\ 5 \end{pmatrix}.$ Thus, \[\overrightarrow{AP} = t \begin{pmatrix} 3 \\ -4 \\ 5 \end{pmatrix}\]for some scalar $t.$ This means point $P$ is of the form $(1 + 3t, 2 - 4t, 3 + 5t).$ But we also know $P$ lies in the plane $3x - 4y + 5z = 30,$ so \[3(1 + 3t) - 4(2 - 4t) + 5(3 + 5t) = 30.\]Solving for $t,$ we find $t = \frac{2}{5}.$ Therefore, $P = \boxed{\left( \frac{11}{5}, \frac{2}{5}, 5 \right)}.$

---

---