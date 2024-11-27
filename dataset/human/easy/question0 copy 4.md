### Question:
Let $P$ be a point on the circle circumscribing square $ABCD$ that satisfies $PA \cdot PC = 56$ and $PB \cdot PD = 90.$ Find the area of $ABCD.$


### Answer:

Alright, let's tackle this geometry problem together. I'll walk you through my entire thought process, exploring different strategies, encountering and correcting mistakes, and ultimately arriving at the solution. Let's dive in!

---

**Problem Statement:**

Let \( P \) be a point on the circle circumscribing square \( ABCD \) such that \( PA \cdot PC = 56 \) and \( PB \cdot PD = 90 \). Find the area of \( ABCD \).

---

**Step 1: Understanding the Problem**

First, let's visualize the setup:

- We have a square \( ABCD \) inscribed in a circle (the circumcircle).
- Point \( P \) lies somewhere on this circle.
- We're given two products of distances:
  - \( PA \cdot PC = 56 \)
  - \( PB \cdot PD = 90 \)
  
Our goal is to find the area of square \( ABCD \).

**Initial Thoughts:**

- Since \( ABCD \) is a square inscribed in a circle, all its vertices lie on the circle.
- The center of the circle coincides with the center of the square.
- The diagonals of the square are diameters of the circle.
- The products \( PA \cdot PC \) and \( PB \cdot PD \) involve opposite vertices of the square.

This setup reminds me of properties related to cyclic quadrilaterals and perhaps the Power of a Point theorem. However, since \( P \) lies on the circle, the traditional Power of a Point might not directly apply here. I'll need to think differently.

---

**Step 2: Setting Up a Coordinate System**

To make calculations manageable, let's place the square and circle on a coordinate plane:

1. **Centering the Square and Circle:**
   - Let’s place the center \( O \) of square \( ABCD \) at the origin \( (0, 0) \).
   
2. **Determining the Coordinates of the Square's Vertices:**
   - Let’s denote the side length of the square as \( s \).
   - Since \( ABCD \) is a square, its vertices can be placed at:
     - \( A \left( \frac{s}{2}, \frac{s}{2} \right) \)
     - \( B \left( -\frac{s}{2}, \frac{s}{2} \right) \)
     - \( C \left( -\frac{s}{2}, -\frac{s}{2} \right) \)
     - \( D \left( \frac{s}{2}, -\frac{s}{2} \right) \)
   
3. **Parametrizing Point \( P \) on the Circumcircle:**
   - Since \( P \) lies on the circumcircle, its coordinates can be represented in polar form:
     - \( P \left( R \cos \theta, R \sin \theta \right) \)
   - Here, \( R \) is the radius of the circumcircle, and \( \theta \) is the angle \( P \) makes with the positive \( x \)-axis.

**Reflection:**

Wait a minute—before proceeding, let's verify if the placement of the square's vertices is accurate. If \( O \) is at the origin, and the square is centered at \( O \), the vertices should be at equal distances from the center. However, in a square inscribed in a circle, the distance from the center to any vertex is equal to the radius \( R \) of the circle.

**Correction:**

I realize that I misrepresented the coordinates of the square's vertices. Since each vertex lies on the circle of radius \( R \), the correct coordinates should be:

- \( A \left( R \cos 45^\circ, R \sin 45^\circ \right) = \left( \frac{R}{\sqrt{2}}, \frac{R}{\sqrt{2}} \right) \)
- \( B \left( R \cos 135^\circ, R \sin 135^\circ \right) = \left( -\frac{R}{\sqrt{2}}, \frac{R}{\sqrt{2}} \right) \)
- \( C \left( R \cos 225^\circ, R \sin 225^\circ \right) = \left( -\frac{R}{\sqrt{2}}, -\frac{R}{\sqrt{2}} \right) \)
- \( D \left( R \cos 315^\circ, R \sin 315^\circ \right) = \left( \frac{R}{\sqrt{2}}, -\frac{R}{\sqrt{2}} \right) \)

This correction ensures that each vertex is at a distance \( R \) from the center \( O \).

---

**Step 3: Expressing Distances \( PA, PB, PC, PD \)**

Now, let's express the distances from \( P \) to each vertex using the distance formula:

1. **Distance \( PA \):**
   \[
   PA = \sqrt{ \left( R \cos \theta - \frac{R}{\sqrt{2}} \right)^2 + \left( R \sin \theta - \frac{R}{\sqrt{2}} \right)^2 }
   \]
   
2. **Distance \( PC \):**
   \[
   PC = \sqrt{ \left( R \cos \theta + \frac{R}{\sqrt{2}} \right)^2 + \left( R \sin \theta + \frac{R}{\sqrt{2}} \right)^2 }
   \]
   
3. **Distance \( PB \):**
   \[
   PB = \sqrt{ \left( R \cos \theta + \frac{R}{\sqrt{2}} \right)^2 + \left( R \sin \theta - \frac{R}{\sqrt{2}} \right)^2 }
   \]
   
4. **Distance \( PD \):**
   \[
   PD = \sqrt{ \left( R \cos \theta - \frac{R}{\sqrt{2}} \right)^2 + \left( R \sin \theta + \frac{R}{\sqrt{2}} \right)^2 }
   \]

**Reflection:**

Calculating each distance separately seems cumbersome. Perhaps there's a more straightforward approach using trigonometric identities or properties of the square and circle.

---

**Step 4: Simplifying the Products \( PA \cdot PC \) and \( PB \cdot PD \)**

Instead of calculating each distance individually, let's consider the products directly, as given in the problem:

1. **Product \( PA \cdot PC = 56 \)**
2. **Product \( PB \cdot PD = 90 \)**

**Idea:**

Notice that \( PA \) and \( PC \) are distances to opposite vertices \( A \) and \( C \). Similarly, \( PB \) and \( PD \) are distances to the other pair of opposite vertices \( B \) and \( D \).

I recall that for any two points \( X \) and \( Y \) on a circle, the product of distances from a third point \( P \) on the circle to \( X \) and \( Y \) can be related to the circle's properties.

**Alternative Approach: Using the Law of Cosines**

Let’s consider the Law of Cosines in triangle \( PAB \):

However, this might not directly help. Instead, let's think about vectors or complex numbers to represent points on the circle.

**Let’s Try Complex Numbers:**

Let’s represent point \( P \) on the circle as a complex number \( e^{i\theta} \), scaling appropriately with radius \( R \).

But before diving into complex numbers, let's consider another geometric property: **Chords and Inscribed Angles.**

---

**Step 5: Leveraging Chord Lengths and Angles**

Recall that the length of a chord in a circle is related to the central angle it subtends:

\[
\text{Chord length} = 2R \sin\left( \frac{\alpha}{2} \right)
\]

Where \( \alpha \) is the central angle.

**Application:**

In our problem, \( PA \) and \( PC \) are chords subtending angles \( \theta - 45^\circ \) and \( \theta + 135^\circ \), respectively (since vertices \( A \) and \( C \) are at \( 45^\circ \) and \( 225^\circ \) from the positive \( x \)-axis).

But this seems complicated. Perhaps there's a better way.

**Alternative Idea: Using Power of a Point**

Although the traditional Power of a Point theorem applies to points outside or inside the circle, let's explore if a similar concept can be adapted for a point on the circumference.

For a point \( P \) on the circle, the power is zero:

\[
PA \cdot PC = \text{Power of } P \text{ with respect to the circle} = 0
\]

But in our problem, \( PA \cdot PC = 56 \neq 0 \). This suggests that \( P \) is not on the circle, which contradicts the given. Therefore, my initial thought is incorrect.

**Realization:**

Wait! The Power of a Point theorem states that for a point \( P \) and a circle, if \( P \) lies on the circle, then the power is zero, meaning \( PA \cdot PC = 0 \) if \( A \) and \( C \) coincide with \( P \). Since in our problem \( PA \cdot PC \neq 0 \), the point \( P \) must not lie on the circle. But this contradicts the problem statement.

**Confusion:**

This inconsistency suggests that my understanding is flawed. I need to revisit the problem statement carefully.

**Clarification:**

Upon re-reading the problem, I realize that \( P \) is indeed on the circle, and \( PA \cdot PC \) and \( PB \cdot PD \) are given as non-zero values. This means that \( P \) is distinct from the vertices, and the products relate to specific properties of the square and its circumcircle.

---

**Step 6: Revisiting the Coordinate Approach**

Let's return to the coordinate system approach, ensuring accurate calculations.

**Coordinates Setup:**

- Center \( O(0, 0) \)
- Square vertices:
  - \( A \left( \frac{R}{\sqrt{2}}, \frac{R}{\sqrt{2}} \right) \)
  - \( B \left( -\frac{R}{\sqrt{2}}, \frac{R}{\sqrt{2}} \right) \)
  - \( C \left( -\frac{R}{\sqrt{2}}, -\frac{R}{\sqrt{2}} \right) \)
  - \( D \left( \frac{R}{\sqrt{2}}, -\frac{R}{\sqrt{2}} \right) \)

Point \( P \) on the circle:

- \( P \left( R \cos \theta, R \sin \theta \right) \)

**Calculating Distances:**

Let's calculate \( PA \) and \( PC \):

1. **Distance \( PA \):**
   \[
   PA = \sqrt{ \left( R \cos \theta - \frac{R}{\sqrt{2}} \right)^2 + \left( R \sin \theta - \frac{R}{\sqrt{2}} \right)^2 }
   \]
   
2. **Expanding \( PA^2 \):**
   \[
   PA^2 = \left( R \cos \theta - \frac{R}{\sqrt{2}} \right)^2 + \left( R \sin \theta - \frac{R}{\sqrt{2}} \right)^2
   \]
   \[
   = R^2 \cos^2 \theta - 2R^2 \cos \theta \cdot \frac{1}{\sqrt{2}} + \frac{R^2}{2} + R^2 \sin^2 \theta - 2R^2 \sin \theta \cdot \frac{1}{\sqrt{2}} + \frac{R^2}{2}
   \]
   \[
   = R^2 (\cos^2 \theta + \sin^2 \theta) - \frac{2R^2}{\sqrt{2}} (\cos \theta + \sin \theta) + R^2
   \]
   \[
   = R^2 (1) - \sqrt{2} R^2 (\cos \theta + \sin \theta) + R^2
   \]
   \[
   = 2R^2 - \sqrt{2} R^2 (\cos \theta + \sin \theta)
   \]

Similarly, calculating \( PC^2 \):

3. **Distance \( PC \):**
   \[
   PC = \sqrt{ \left( R \cos \theta + \frac{R}{\sqrt{2}} \right)^2 + \left( R \sin \theta + \frac{R}{\sqrt{2}} \right)^2 }
   \]
   
4. **Expanding \( PC^2 \):**
   \[
   PC^2 = \left( R \cos \theta + \frac{R}{\sqrt{2}} \right)^2 + \left( R \sin \theta + \frac{R}{\sqrt{2}} \right)^2
   \]
   \[
   = R^2 \cos^2 \theta + 2R^2 \cos \theta \cdot \frac{1}{\sqrt{2}} + \frac{R^2}{2} + R^2 \sin^2 \theta + 2R^2 \sin \theta \cdot \frac{1}{\sqrt{2}} + \frac{R^2}{2}
   \]
   \[
   = R^2 (\cos^2 \theta + \sin^2 \theta) + \frac{2R^2}{\sqrt{2}} (\cos \theta + \sin \theta) + R^2
   \]
   \[
   = R^2 (1) + \sqrt{2} R^2 (\cos \theta + \sin \theta) + R^2
   \]
   \[
   = 2R^2 + \sqrt{2} R^2 (\cos \theta + \sin \theta)
   \]

**Product \( PA \cdot PC \):**

\[
PA^2 \cdot PC^2 = (2R^2 - \sqrt{2} R^2 (\cos \theta + \sin \theta)) \cdot (2R^2 + \sqrt{2} R^2 (\cos \theta + \sin \theta))
\]
\[
= (2R^2)^2 - (\sqrt{2} R^2 (\cos \theta + \sin \theta))^2
\]
\[
= 4R^4 - 2R^4 (\cos \theta + \sin \theta)^2
\]

**Simplifying \( (\cos \theta + \sin \theta)^2 \):**

\[
(\cos \theta + \sin \theta)^2 = \cos^2 \theta + 2 \sin \theta \cos \theta + \sin^2 \theta = 1 + \sin 2\theta
\]

**Substituting Back:**

\[
PA^2 \cdot PC^2 = 4R^4 - 2R^4 (1 + \sin 2\theta) = 4R^4 - 2R^4 - 2R^4 \sin 2\theta = 2R^4 - 2R^4 \sin 2\theta
\]

But we know \( PA \cdot PC = 56 \), so:

\[
PA \cdot PC = \sqrt{PA^2 \cdot PC^2} = \sqrt{2R^4 - 2R^4 \sin 2\theta} = R^2 \sqrt{2(1 - \sin 2\theta)} = 56
\]

**Equation 1:**

\[
R^2 \sqrt{2(1 - \sin 2\theta)} = 56
\]
\[
\sqrt{2(1 - \sin 2\theta)} = \frac{56}{R^2}
\]
\[
2(1 - \sin 2\theta) = \frac{3136}{R^4}
\]
\[
1 - \sin 2\theta = \frac{1568}{R^4}
\]
\[
\sin 2\theta = 1 - \frac{1568}{R^4}
\]

**Similarly, for \( PB \cdot PD = 90 \):**

Following analogous steps, we find:

\[
PB^2 \cdot PD^2 = (2R^2 + \sqrt{2} R^2 (\cos \theta + \sin \theta)) \cdot (2R^2 - \sqrt{2} R^2 (\cos \theta + \sin \theta)) = 4R^4 - 2R^4 (\cos \theta + \sin \theta)^2
\]
\[
= 4R^4 - 2R^4 (1 + \sin 2\theta) = 2R^4 - 2R^4 \sin 2\theta
\]

Thus,

\[
PB \cdot PD = \sqrt{2R^4 - 2R^4 \sin 2\theta} = R^2 \sqrt{2(1 - \sin 2\theta)} = 90
\]

**Equation 2:**

\[
R^2 \sqrt{2(1 - \sin 2\theta)} = 90
\]
\[
\sqrt{2(1 - \sin 2\theta)} = \frac{90}{R^2}
\]
\[
2(1 - \sin 2\theta) = \frac{8100}{R^4}
\]
\[
1 - \sin 2\theta = \frac{4050}{R^4}
\]
\[
\sin 2\theta = 1 - \frac{4050}{R^4}
\]

**Reflection:**

Hmm, both equations express \( \sin 2\theta \) in terms of \( R^4 \). It seems like we can set them equal to each other since both equal \( \sin 2\theta \).

---

**Step 7: Equating the Two Expressions for \( \sin 2\theta \)**

From Equation 1 and Equation 2:

\[
1 - \frac{1568}{R^4} = 1 - \frac{4050}{R^4}
\]

**Simplifying:**

\[
1 - \frac{1568}{R^4} = 1 - \frac{4050}{R^4}
\]
\[
- \frac{1568}{R^4} = - \frac{4050}{R^4}
\]
\[
\frac{1568}{R^4} = \frac{4050}{R^4}
\]

**Wait, this leads to:**

\[
1568 = 4050
\]

**Contradiction:**

This is clearly impossible. This contradiction suggests that there's an error in the previous steps.

**Realization:**

Upon reviewing, I notice that I mistakenly assumed both products \( PA \cdot PC \) and \( PB \cdot PD \) result in the same expression for \( \sin 2\theta \). However, the actual expressions for \( PA \cdot PC \) and \( PB \cdot PD \) should involve different angles or properties.

**Re-evaluation:**

Perhaps I oversimplified the relationship between \( PA \cdot PC \) and \( PB \cdot PD \). Let's think differently.

---

**Step 8: Exploring Another Approach Using Diagonals**

Given that \( ABCD \) is a square, its diagonals are perpendicular and bisect each other at the center \( O \). Moreover, each diagonal is a diameter of the circumcircle.

**Properties:**

- \( AC \) and \( BD \) are diagonals intersecting at \( O \).
- Length of each diagonal \( = s\sqrt{2} \), where \( s \) is the side length of the square.
- Therefore, radius \( R = \frac{s\sqrt{2}}{2} = \frac{s}{\sqrt{2}} \).

**Idea:**

The Power of a Point theorem states that for a point \( P \) on the circle, the product of the distances to two points \( X \) and \( Y \) on the circle that are endpoints of a diameter equals \( R^2 \).

Wait, does this hold?

**Recollection:**

Actually, for any point \( P \) on the circle, the product \( PA \cdot PC \) where \( AC \) is a diameter equals \( R^2 \). Similarly, \( PB \cdot PD = R^2 \).

But in our problem, \( PA \cdot PC = 56 \) and \( PB \cdot PD = 90 \), which are different values. This suggests that \( AC \) and \( BD \) are not both diameters, which contradicts the properties of a square.

**Confusion:**

This inconsistency indicates a misunderstanding. In a square, both diagonals \( AC \) and \( BD \) are diameters of the circumcircle, so for any point \( P \) on the circle:

\[
PA \cdot PC = PB \cdot PD = R^2
\]

But in our problem, \( PA \cdot PC \) and \( PB \cdot PD \) have different values (\(56\) and \(90\)), which shouldn't happen if both are equal to \( R^2 \).

**Realization:**

This suggests that the square might not be regular, but the problem states it's a square. Alternatively, perhaps I misapplied the Power of a Point theorem.

**Clarification:**

Upon re-examining, I recall that for a cyclic quadrilateral (which a square is a special case of), the Power of a Point theorem states that for any point \( P \) on the circumcircle, the product of the lengths of two opposite sides equals the product of the lengths of the other two opposite sides.

But in our case, \( ABCD \) is a square, so opposite sides are equal, but \( PA \cdot PC \) and \( PB \cdot PD \) are products of distances to vertices, not side lengths.

**Alternative Idea:**

Perhaps, instead of applying Power of a Point directly, I should consider angles or trigonometric identities involving \( \theta \) and relate the given products to \( R \).

---

**Step 9: Using Trigonometric Identities**

Let's revisit the earlier approach and correct the mistake.

We had:

\[
PA^2 \cdot PC^2 = 2R^4 - 2R^4 \sin 2\theta = (56)^2 = 3136
\]
\[
PB^2 \cdot PD^2 = 2R^4 - 2R^4 \sin 2\theta = (90)^2 = 8100
\]

Wait, this suggests:

\[
2R^4 - 2R^4 \sin 2\theta = 3136
\]
\[
2R^4 - 2R^4 \sin 2\theta = 8100
\]

**Setting Equations Equal:**

\[
3136 = 8100
\]

This is impossible, indicating a fundamental flaw in the approach.

**Understanding the Mistake:**

I realize that \( PA^2 \cdot PC^2 \) and \( PB^2 \cdot PD^2 \) cannot both equal different constants if they are expressed by the same formula involving \( \sin 2\theta \). This contradiction arises because I mistakenly assumed both products yield the same expression.

**Alternative Approach:**

Let's instead consider that \( PA \cdot PC = 56 \) and \( PB \cdot PD = 90 \) both relate to \( R \) and \( \theta \), and find a relationship between them to solve for \( R \).

---

**Step 10: Introducing Variable Relationships**

Let’s define:

\[
PA \cdot PC = 56 \quad \text{(Equation 1)}
\]
\[
PB \cdot PD = 90 \quad \text{(Equation 2)}
\]

From earlier steps, we have:

\[
PA \cdot PC = R^2 \sqrt{2(1 - \sin 2\theta)} = 56
\]
\[
PB \cdot PD = R^2 \sqrt{2(1 + \sin 2\theta)} = 90
\]

**Let’s Square Both Equations:**

1. **From Equation 1:**
   \[
   (PA \cdot PC)^2 = 56^2 = 3136 = 2R^4 (1 - \sin 2\theta)
   \]
   \[
   1 - \sin 2\theta = \frac{3136}{2R^4} = \frac{1568}{R^4}
   \]
   
2. **From Equation 2:**
   \[
   (PB \cdot PD)^2 = 90^2 = 8100 = 2R^4 (1 + \sin 2\theta)
   \]
   \[
   1 + \sin 2\theta = \frac{8100}{2R^4} = \frac{4050}{R^4}
   \]

**Adding Both Equations:**

\[
(1 - \sin 2\theta) + (1 + \sin 2\theta) = \frac{1568}{R^4} + \frac{4050}{R^4}
\]
\[
2 = \frac{5618}{R^4}
\]
\[
R^4 = \frac{5618}{2} = 2809
\]

**Solving for \( R^2 \):**

\[
R^2 = \sqrt{2809} = 53
\]

**Reflection:**

This seems promising. We've found \( R^2 = 53 \).

**Verifying \( \sin 2\theta \):**

From Equation 1:

\[
1 - \sin 2\theta = \frac{1568}{2809} = \frac{1568}{2809}
\]
\[
\sin 2\theta = 1 - \frac{1568}{2809} = \frac{1241}{2809} \approx 0.442
\]

This is a valid value for \( \sin 2\theta \) since it lies between \(-1\) and \(1\).

**Step 11: Finding the Area of Square \( ABCD \)**

We have \( R^2 = 53 \). Recall that for a square inscribed in a circle:

\[
\text{Diagonal} = 2R
\]
\[
\text{Side length } s = \frac{\text{Diagonal}}{\sqrt{2}} = \frac{2R}{\sqrt{2}} = R \sqrt{2}
\]
\[
\text{Area } A = s^2 = (R \sqrt{2})^2 = 2R^2
\]

**Calculating the Area:**

\[
A = 2R^2 = 2 \times 53 = 106
\]

---

**Conclusion:**

After carefully analyzing the problem, correcting initial misconceptions, and methodically applying geometric and algebraic principles, we've determined that the area of square \( ABCD \) is **106**.

---

**Final Answer:** \( \boxed{106} \)