### Question:
In isosceles trapezoid $ABCD$, parallel bases $\overline{AB}$ and $\overline{CD}$ have lengths $500$ and $650$, respectively, and $AD=BC=333$. The angle bisectors of $\angle{A}$ and $\angle{D}$ meet at $P$, and the angle bisectors of $\angle{B}$ and $\angle{C}$ meet at $Q$. Find $PQ$.

### Answer:
Alright, let's tackle this problem step by step. I'll walk you through my thought process as I explore different strategies, check for correctness, and adjust my approach as needed.

### **Understanding the Problem**

We have an **isosceles trapezoid** \(ABCD\) with:
- **Parallel bases** \( \overline{AB} \) and \( \overline{CD} \) of lengths 500 and 650, respectively.
- **Non-parallel sides** \( AD = BC = 333 \).
- **Points \(P\) and \(Q\)** are defined as the intersections of the angle bisectors:
  - \( P \) is where the bisectors of \( \angle A \) and \( \angle D \) meet.
  - \( Q \) is where the bisectors of \( \angle B \) and \( \angle C \) meet.

Our goal is to find the distance \( PQ \).

### **First Thoughts**

- **Isosceles Trapezoid Properties:** Since the trapezoid is isosceles, the non-parallel sides are equal (\( AD = BC \)), and the base angles are equal (\( \angle A = \angle B \) and \( \angle C = \angle D \)).
  
- **Symmetry:** The trapezoid is symmetric about the perpendicular bisector of the bases. This suggests that placing the trapezoid on a coordinate system symmetrically might simplify calculations.

- **Angle Bisectors:** The intersections of angle bisectors in such a symmetric figure might lie on the symmetry axis. This could be a key insight for finding \( P \) and \( Q \).

### **Planning the Approach**

Given these properties, here's how I plan to proceed:

1. **Coordinate System Setup:** Place the trapezoid symmetrically on a coordinate plane to exploit its symmetry.

2. **Determine Coordinates of Vertices:** Using the given side lengths, calculate the coordinates of all four vertices.

3. **Find Equations of Angle Bisectors:** Determine the equations of the angle bisectors for the specified angles.

4. **Find Points \( P \) and \( Q \):** Solve the system of equations to find the coordinates of \( P \) and \( Q \).

5. **Calculate \( PQ \):** Use the distance formula to find the length between \( P \) and \( Q \).

### **Step 1: Setting Up the Coordinate System**

Let's place the trapezoid on the coordinate plane to exploit its symmetry:

- **Base \( AB \):** Place \( A \) at the origin \((0, 0)\) and \( B \) at \((500, 0)\), since \( AB = 500 \).

- **Base \( CD \):** Since \( CD = 650 \) and the trapezoid is symmetric, the midpoint of \( CD \) should align with the midpoint of \( AB \), which is at \( x = 250 \).

  Therefore:
  - The left endpoint \( D \) of \( CD \) is at \( x = 250 - \frac{650}{2} = 250 - 325 = -75 \).
  - The right endpoint \( C \) is at \( x = 250 + \frac{650}{2} = 250 + 325 = 575 \).

- **Coordinates of \( D \) and \( C \):**
  - Let’s denote \( D = (-75, h) \) and \( C = (575, h) \), where \( h \) is the height of the trapezoid.

**Check:** Does this make sense? Yes, because the bases are centered at \( x = 250 \), ensuring symmetry.

### **Step 2: Determining the Height \( h \)**

We know the lengths of the non-parallel sides \( AD \) and \( BC \) are 333. Let's use the distance formula to find \( h \).

Consider side \( AD \):
\[
AD = \sqrt{(x_D - x_A)^2 + (y_D - y_A)^2} = \sqrt{(-75 - 0)^2 + (h - 0)^2} = \sqrt{75^2 + h^2} = 333
\]
\[
\Rightarrow 75^2 + h^2 = 333^2
\]
\[
\Rightarrow 5625 + h^2 = 110889
\]
\[
\Rightarrow h^2 = 110889 - 5625 = 105264
\]
\[
\Rightarrow h = \sqrt{105264} = 324 \quad (\text{since height is positive})
\]

**Reflection:** Wait, does \( \sqrt{105264} = 324 \)? Let me double-check:
\[
324^2 = 104976
\]
\[
105264 - 104976 = 288
\]
So, \( h = \sqrt{105264} \approx 324.12 \). For simplicity, we'll use \( h \approx 324.12 \).

**Decision:** We'll keep \( h \) as \( \sqrt{105264} \) for exactness in further calculations.

### **Step 3: Finding Equations of Angle Bisectors**

Now, let's find the equations of the angle bisectors at \( A \), \( D \), \( B \), and \( C \).

**Angle Bisectors at \( A \) and \( D \):**

- **At Vertex \( A \):**
  - \( \angle A \) is between sides \( AB \) and \( AD \).
  - The bisector of \( \angle A \) divides it into two equal angles.
  - To find the direction of the bisector, we can use vectors.

- **Direction Vectors:**
  - Vector \( \overrightarrow{AB} = (500 - 0, 0 - 0) = (500, 0) \).
  - Vector \( \overrightarrow{AD} = (-75 - 0, h - 0) = (-75, h) \).

- **Unit Vectors:**
  - Normalize \( \overrightarrow{AB} \) and \( \overrightarrow{AD} \):
    \[
    \text{Unit vector } \overrightarrow{AB} = \left( \frac{500}{500}, \frac{0}{500} \right) = (1, 0)
    \]
    \[
    \text{Unit vector } \overrightarrow{AD} = \left( \frac{-75}{333}, \frac{h}{333} \right)
    \]
    (Since \( AD = 333 \)).

- **Bisector Direction:**
  - The angle bisector direction vector is the sum of the unit vectors:
    \[
    \overrightarrow{b_A} = (1, 0) + \left( \frac{-75}{333}, \frac{h}{333} \right) = \left(1 - \frac{75}{333}, \frac{h}{333}\right)
    \]
    \[
    = \left(\frac{333 - 75}{333}, \frac{h}{333}\right) = \left(\frac{258}{333}, \frac{h}{333}\right)
    \]
    Simplify:
    \[
    \overrightarrow{b_A} = \left(\frac{86}{111}, \frac{h}{333}\right)
    \]

- **At Vertex \( D \):**
  - \( \angle D \) is between sides \( DC \) and \( DA \).
  - Vector \( \overrightarrow{DC} = (575 - (-75), h - h) = (650, 0) \).
  - Vector \( \overrightarrow{DA} = (0 - (-75), 0 - h) = (75, -h) \).

- **Unit Vectors:**
  - \( \overrightarrow{DC} \) normalized:
    \[
    \left( \frac{650}{650}, \frac{0}{650} \right) = (1, 0)
    \]
  - \( \overrightarrow{DA} \) normalized:
    \[
    \left( \frac{75}{333}, \frac{-h}{333} \right)
    \]

- **Bisector Direction:**
  - Sum of unit vectors:
    \[
    \overrightarrow{b_D} = (1, 0) + \left( \frac{75}{333}, \frac{-h}{333} \right) = \left(1 + \frac{75}{333}, \frac{-h}{333}\right)
    \]
    \[
    = \left(\frac{333 + 75}{333}, \frac{-h}{333}\right) = \left(\frac{408}{333}, \frac{-h}{333}\right)
    \]
    Simplify:
    \[
    \overrightarrow{b_D} = \left(\frac{136}{111}, \frac{-h}{333}\right)
    \]

**Equation of Bisectors:**

- **Bisector at \( A \):**
  - Passes through \( A(0, 0) \).
  - Direction vector \( \left(\frac{86}{111}, \frac{h}{333}\right) \).
  - Slope \( m_A = \frac{\frac{h}{333}}{\frac{86}{111}} = \frac{h \cdot 111}{333 \cdot 86} = \frac{h}{258} \).

- **Bisector at \( D \):**
  - Passes through \( D(-75, h) \).
  - Direction vector \( \left(\frac{136}{111}, \frac{-h}{333}\right) \).
  - Slope \( m_D = \frac{\frac{-h}{333}}{\frac{136}{111}} = \frac{-h \cdot 111}{333 \cdot 136} = \frac{-h}{408} \).

**Checking Slopes:**
- Given \( h = \sqrt{105264} \), both slopes are negative reciprocals scaled appropriately, which makes sense for angle bisectors in an isosceles trapezoid.

### **Step 4: Finding Point \( P \)**

Point \( P \) is the intersection of the bisectors at \( A \) and \( D \).

**Equations of Bisectors:**

1. **Bisector at \( A \):**
   \[
   y = m_A x = \frac{h}{258} x
   \]

2. **Bisector at \( D \):**
   \[
   y - h = m_D (x + 75)
   \]
   \[
   y = \frac{-h}{408} (x + 75) + h
   \]

**Solving for Intersection:**

Set the two equations for \( y \) equal:
\[
\frac{h}{258} x = \frac{-h}{408} (x + 75) + h
\]
Simplify:
\[
\frac{h}{258} x = \frac{-h}{408} x - \frac{75h}{408} + h
\]
Multiply both sides by \( 408 \) to eliminate denominators:
\[
\frac{408h}{258} x = -h x - 75h + 408h
\]
Simplify \( \frac{408}{258} \):
\[
\frac{408}{258} = \frac{24 \times 17}{17 \times 15.176} \approx 1.58 \quad (\text{Actually, exact fraction is } \frac{68}{43})
\]
But for exactness, let's reduce:
\[
\frac{408}{258} = \frac{408 \div 6}{258 \div 6} = \frac{68}{43}
\]
So:
\[
\frac{68}{43} h x = -h x - 75h + 408h
\]
Divide both sides by \( h \) (since \( h \neq 0 \)):
\[
\frac{68}{43} x = -x - 75 + 408
\]
Simplify the right side:
\[
\frac{68}{43} x = -x + 333
\]
Bring like terms together:
\[
\frac{68}{43} x + x = 333
\]
\[
\left(\frac{68}{43} + 1\right) x = 333
\]
\[
\frac{68 + 43}{43} x = 333
\]
\[
\frac{111}{43} x = 333
\]
Solve for \( x \):
\[
x = 333 \times \frac{43}{111} = 3 \times 43 = 129
\]
Now, find \( y \) using the bisector at \( A \):
\[
y = \frac{h}{258} \times 129 = \frac{h}{2}
\]
So, \( P = (129, \frac{h}{2}) \).

**Reflection:** Does this make sense? Yes, given the symmetry, \( P \) lies halfway up the height at \( x = 129 \).

### **Step 5: Finding Point \( Q \)**

Similarly, \( Q \) is the intersection of the bisectors at \( B \) and \( C \).

**Bisectors at \( B \) and \( C \):**

- **At Vertex \( B \):**
  - \( \angle B \) is between \( BA \) and \( BC \).
  - Vector \( \overrightarrow{BA} = (-500, 0) \).
  - Vector \( \overrightarrow{BC} = (575 - 500, h - 0) = (75, h) \).
  
- **Unit Vectors:**
  - \( \overrightarrow{BA} \) normalized:
    \[
    \left( \frac{-500}{500}, \frac{0}{500} \right) = (-1, 0)
    \]
  - \( \overrightarrow{BC} \) normalized:
    \[
    \left( \frac{75}{333}, \frac{h}{333} \right)
    \]
  
- **Bisector Direction:**
  \[
  \overrightarrow{b_B} = (-1, 0) + \left( \frac{75}{333}, \frac{h}{333} \right) = \left(-1 + \frac{75}{333}, \frac{h}{333}\right)
  \]
  \[
  = \left(-\frac{333}{333} + \frac{75}{333}, \frac{h}{333}\right) = \left(-\frac{258}{333}, \frac{h}{333}\right)
  \]
  Simplify:
  \[
  \overrightarrow{b_B} = \left(-\frac{86}{111}, \frac{h}{333}\right)
  \]
  
- **At Vertex \( C \):**
  - \( \angle C \) is between \( CB \) and \( CD \).
  - Vector \( \overrightarrow{CB} = (-75, 0) \).
  - Vector \( \overrightarrow{CD} = (-650, 0) \).
  
- **Unit Vectors:**
  - \( \overrightarrow{CB} \) normalized:
    \[
    \left( \frac{-75}{333}, \frac{0}{333} \right) = \left(-\frac{75}{333}, 0\right)
    \]
  - \( \overrightarrow{CD} \) normalized:
    \[
    \left( \frac{-650}{650}, \frac{0}{650} \right) = (-1, 0)
    \]
  
- **Bisector Direction:**
  \[
  \overrightarrow{b_C} = \left(-\frac{75}{333}, 0\right) + (-1, 0) = \left(-\frac{75}{333} - 1, 0\right)
  \]
  \[
  = \left(-\frac{75 + 333}{333}, 0\right) = \left(-\frac{408}{333}, 0\right)
  \]
  Simplify:
  \[
  \overrightarrow{b_C} = \left(-\frac{136}{111}, 0\right)
  \]
  
**Equation of Bisectors:**

1. **Bisector at \( B \):**
   - Passes through \( B(500, 0) \).
   - Direction vector \( \left(-\frac{86}{111}, \frac{h}{333}\right) \).
   - Slope \( m_B = \frac{\frac{h}{333}}{-\frac{86}{111}} = -\frac{h \cdot 111}{333 \cdot 86} = -\frac{h}{258} \).

2. **Bisector at \( C \):**
   - Passes through \( C(575, h) \).
   - Direction vector \( \left(-\frac{136}{111}, 0\right) \).
   - Slope \( m_C = 0 \) (horizontal line).

**Solving for Intersection \( Q \):**

Since the bisector at \( C \) is horizontal, its equation is:
\[
y = h
\]

The bisector at \( B \) has the equation:
\[
y = m_B (x - 500) = -\frac{h}{258} (x - 500)
\]

Set \( y = h \):
\[
h = -\frac{h}{258} (x - 500)
\]
Divide both sides by \( h \) (since \( h \neq 0 \)):
\[
1 = -\frac{1}{258} (x - 500)
\]
Multiply both sides by 258:
\[
258 = -(x - 500)
\]
\[
x - 500 = -258
\]
\[
x = 500 - 258 = 242
\]
Now, \( y = h \).

So, \( Q = (242, h) \).

**Wait a Second:** Does this make sense? Earlier, we found \( P = (129, \frac{h}{2}) \). Given the symmetry, I would expect \( Q \) to also be at \( y = \frac{h}{2} \), not at \( y = h \). There seems to be a mistake here.

**Re-evaluating:** Let's double-check the bisectors at \( B \) and \( C \).

**Correction:**

I realize now that the bisector at \( C \) was incorrectly determined. Let's revisit the bisector at \( C \).

**At Vertex \( C \):**
- \( \angle C \) is between \( CB \) and \( CD \).
- Vector \( \overrightarrow{CB} = (500 - 575, 0 - h) = (-75, -h) \).
- Vector \( \overrightarrow{CD} = (-650, 0) \).

**Unit Vectors:**
- \( \overrightarrow{CB} \) normalized:
  \[
  \left( \frac{-75}{333}, \frac{-h}{333} \right)
  \]
  (Since \( BC = 333 \)).

- \( \overrightarrow{CD} \) normalized:
  \[
  \left( \frac{-650}{650}, \frac{0}{650} \right) = (-1, 0)
  \]

**Bisector Direction:**
\[
\overrightarrow{b_C} = \left( \frac{-75}{333}, \frac{-h}{333} \right) + (-1, 0) = \left( \frac{-75}{333} - 1, \frac{-h}{333} \right)
\]
\[
= \left( \frac{-75 - 333}{333}, \frac{-h}{333} \right) = \left( \frac{-408}{333}, \frac{-h}{333} \right)
\]
Simplify:
\[
\overrightarrow{b_C} = \left( -\frac{136}{111}, -\frac{h}{333} \right)
\]

**Equation of Bisector at \( C \):**

- Passes through \( C(575, h) \).
- Direction vector \( \left( -\frac{136}{111}, -\frac{h}{333} \right) \).
- Slope \( m_C = \frac{-\frac{h}{333}}{-\frac{136}{111}} = \frac{h \cdot 111}{333 \cdot 136} = \frac{h}{408} \).

**Now, Equations of Bisectors at \( B \) and \( C \):**

1. **Bisector at \( B \):**
   \[
   y = -\frac{h}{258} (x - 500)
   \]

2. **Bisector at \( C \):**
   \[
   y - h = \frac{h}{408} (x - 575)
   \]
   \[
   y = \frac{h}{408} (x - 575) + h
   \]

**Solving for Intersection \( Q \):**

Set the two equations equal:
\[
-\frac{h}{258} (x - 500) = \frac{h}{408} (x - 575) + h
\]
Divide both sides by \( h \) (since \( h \neq 0 \)):
\[
-\frac{1}{258} (x - 500) = \frac{1}{408} (x - 575) + 1
\]
Multiply all terms by \( 258 \times 408 \) to eliminate denominators:
\[
-408 (x - 500) = 258 (x - 575) + 258 \times 408
\]
Expand:
\[
-408x + 204,000 = 258x - 148,350 + 105,264
\]
Simplify the right side:
\[
258x - 148,350 + 105,264 = 258x - 43,086
\]
Bring all terms to one side:
\[
-408x + 204,000 - 258x + 43,086 = 0
\]
Combine like terms:
\[
-666x + 247,086 = 0
\]
Solve for \( x \):
\[
-666x = -247,086
\]
\[
x = \frac{247,086}{666} = 371
\]
Now, find \( y \) using the bisector at \( B \):
\[
y = -\frac{h}{258} (371 - 500) = -\frac{h}{258} (-129) = \frac{h}{258} \times 129 = \frac{h}{2}
\]
So, \( Q = (371, \frac{h}{2}) \).

**Reflection:** This makes sense! Both \( P \) and \( Q \) lie at \( y = \frac{h}{2} \), which aligns with the symmetry of the trapezoid.

### **Step 6: Calculating \( PQ \)**

Now that we have the coordinates of \( P \) and \( Q \):
- \( P = (129, \frac{h}{2}) \)
- \( Q = (371, \frac{h}{2}) \)

The distance \( PQ \) is the horizontal distance between these points since their \( y \)-coordinates are the same.

\[
PQ = |371 - 129| = 242
\]

### **Final Check**

- **Symmetry:** Given the trapezoid's symmetry, \( P \) and \( Q \) should be equidistant from the center line \( x = 250 \). 

  - Distance of \( P \) from 250: \( 250 - 129 = 121 \)
  - Distance of \( Q \) from 250: \( 371 - 250 = 121 \)

  This confirms our calculation \( PQ = 242 \) because \( PQ = 2 \times 121 = 242 \).

- **Reasonableness:** All steps align with the properties of an isosceles trapezoid, and the distances make sense given the side lengths.

### **Answer**

\(\boxed{242}\)