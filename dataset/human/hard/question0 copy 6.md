### Question:

Let $P$ be a point on the circle circumscribing square $ABCD$ that satisfies $PA \cdot PC = 56$ and $PB \cdot PD = 90.$ Find the area of $ABCD.$


### Answer:

Alright, let's tackle this problem step by step. I'll walk through my thought process, exploring different strategies, checking for correctness along the way, and adjusting my approach as needed.

**Problem Statement Recap:**
We have a square \(ABCD\) with a circumscribed circle. Point \(P\) lies on this circle such that:
- \(PA \cdot PC = 56\)
- \(PB \cdot PD = 90\)

We need to find the area of square \(ABCD\).

**First Thoughts:**
When dealing with squares and their circumscribed circles, symmetry is a powerful tool. The fact that \(P\) lies on the circumcircle suggests that properties related to cyclic quadrilaterals or power of a point might be useful. The given products \(PA \cdot PC\) and \(PB \cdot PD\) hint towards the Power of a Point theorem, which relates these products to the circle's properties.

**Strategy Exploration:**

1. **Power of a Point Theorem:**
   The Power of a Point theorem states that for a point \(P\) on a circle, the product of the lengths of the segments from \(P\) to two points on the circle is constant for any chord through \(P\). Here, \(PA \cdot PC\) and \(PB \cdot PD\) are such products.

   - **Reflection:** This seems promising because it directly relates the given products to the circle and, by extension, to the square's properties.

2. **Coordinate Geometry Approach:**
   Placing the square on a coordinate system might help visualize and calculate distances more concretely.

   - **Reflection:** This could complicate things with coordinates and algebra, but it might offer a clear path if the Power of a Point doesn't directly yield the area.

3. **Using Trigonometry:**
   Since \(P\) lies on the circumcircle, angles and trigonometric identities might relate the given products to the square's side length.

   - **Reflection:** This could be useful, especially if we can relate angles subtended by the square's sides at \(P\).

**Choosing a Strategy:**
I'll start with the Power of a Point theorem since it directly involves the given products. If I hit a roadblock, I'll consider switching to a trigonometric or coordinate-based approach.

**Applying Power of a Point:**

Let's denote:
- \(s\) as the side length of square \(ABCD\).
- \(R\) as the radius of the circumscribed circle.

For a square, the diagonal is \(s\sqrt{2}\), so the radius \(R\) is half the diagonal:
\[
R = \frac{s\sqrt{2}}{2} = \frac{s}{\sqrt{2}}
\]
\[
R^2 = \frac{s^2}{2}
\]

**Understanding the Products:**

Given that \(PA \cdot PC = 56\) and \(PB \cdot PD = 90\), and knowing that \(P\) lies on the circumcircle, we can think of \(PA\), \(PB\), \(PC\), and \(PD\) as chords intersecting at \(P\).

However, since \(ABCD\) is a square, the positions of \(A\), \(B\), \(C\), and \(D\) are symmetric. This symmetry might imply certain relationships between the products \(PA \cdot PC\) and \(PB \cdot PD\).

**Exploring Relationships:**

Let's consider the diagonals \(AC\) and \(BD\). These diagonals intersect at the center of the square, which is also the center of the circumscribed circle.

If \(P\) is any point on the circumcircle, the products \(PA \cdot PC\) and \(PB \cdot PD\) are related to the position of \(P\) relative to the square's vertices.

**Possible Approach:**

One approach is to express \(PA\), \(PB\), \(PC\), and \(PD\) in terms of \(R\) and the angles they make with the square's vertices. However, this might lead to complicated trigonometric expressions.

Instead, let's think about the average of the two products. Since \(PA \cdot PC = 56\) and \(PB \cdot PD = 90\), their average is:
\[
\frac{56 + 90}{2} = 73
\]
I wonder if this average has any geometric significance related to the square's properties.

**Alternative Idea:**

Wait a minute—since the square has rotational symmetry, perhaps there's a way to relate these products without delving deep into angles. Maybe by considering that the sum of these products is somehow connected to the square's area or the circle's radius.

**Considering the Circle's Radius:**

Given \(R = \frac{s}{\sqrt{2}}\), we have \(R^2 = \frac{s^2}{2}\). Maybe \(PA \cdot PC + PB \cdot PD\) relates to \(R^2\).

Calculating:
\[
PA \cdot PC + PB \cdot PD = 56 + 90 = 146
\]
Is \(146\) related to \(2R^2\)?

Given \(R^2 = \frac{s^2}{2}\), then:
\[
2R^2 = s^2
\]
If \(146 = s^2\), then the area of the square would be \(146\).

But wait, in the initial approach, the answer was \(106\), not \(146\). There's a discrepancy here. This suggests that simply adding the products isn't directly giving \(s^2\).

**Re-evaluating:**

Perhaps the relationship isn't a direct sum. Let's think back to the Power of a Point theorem.

The Power of a Point theorem for point \(P\) with respect to the circle gives:
\[
PA \cdot PC = PB \cdot PD
\]
But in our problem, \(PA \cdot PC = 56\) and \(PB \cdot PD = 90\), which are not equal. This suggests that \(P\) is not just any point on the circle but has a specific position relative to the square's vertices.

**Alternate Approach Using Trigonometry:**

Let's consider the angles subtended by the square's sides at point \(P\).

Assume that point \(P\) makes an angle \(\theta\) with side \(AB\). Due to the square's symmetry, the angles subtended by \(PA\), \(PB\), \(PC\), and \(PD\) will be related.

Using the Law of Cosines in the triangles formed by \(P\) and the square's vertices could relate the products \(PA \cdot PC\) and \(PB \cdot PD\) to the side length \(s\).

However, this seems quite involved. Let's pause and consider if there's a simpler geometric property or theorem that can be applied.

**Insight from Previous Attempt:**

Earlier, I thought about \(PA \cdot PC + PB \cdot PD = 146\) and how it might relate to \(s^2\). Given that \(s^2\) represents the area of the square, and considering the initial answer was \(106\), perhaps there's a different way these products relate to the area.

**Revisiting Power of a Point:**

The Power of a Point for \(P\) with respect to the circle can be expressed as:
\[
PA \cdot PC = PB \cdot PD
\]
But in our problem, \(PA \cdot PC \neq PB \cdot PD\), which indicates that \(P\) does not lie on both chords \(AC\) and \(BD\) simultaneously, but rather at a position where these products differ.

This suggests that \(P\) is positioned such that the angles subtended by \(PA\) and \(PB\) are not equal, breaking the symmetry.

**Alternative Idea:**

Maybe instead of adding the products, we can consider them as part of a system of equations to solve for \(s\).

Given:
\[
PA \cdot PC = 56 \quad (1)
\]
\[
PB \cdot PD = 90 \quad (2)
\]

And knowing that \(PA\), \(PB\), \(PC\), and \(PD\) are related through the circle's radius \(R\), which in turn is related to the square's side length \(s\).

Let’s assume \(PA = a\), \(PB = b\), \(PC = c\), and \(PD = d\). Then:
\[
a \cdot c = 56 \quad (1)
\]
\[
b \cdot d = 90 \quad (2)
\]

But we need more relationships to connect these variables to \(s\).

**Connecting to the Square's Diagonals:**

The diagonals of the square intersect at the center of the circle, and each diagonal has length \(s\sqrt{2}\). Therefore, the radius \(R\) is \(\frac{s\sqrt{2}}{2}\).

From the Power of a Point theorem, for point \(P\) on the circle:
\[
PA \cdot PC = PB \cdot PD = R^2
\]
But in our case, \(PA \cdot PC \neq PB \cdot PD\), implying that point \(P\) is not aligned symmetrically with both diagonals. This discrepancy suggests that perhaps my initial assumption about the Power of a Point is incomplete or misapplied.

**Reassessing the Approach:**

Given this confusion, let's try a different angle. Perhaps expressing the distances \(PA\), \(PB\), \(PC\), and \(PD\) in terms of trigonometric functions relative to the square's orientation can help establish a relationship.

**Trigonometric Representation:**

Let’s place the square \(ABCD\) on a coordinate plane with its center at the origin \((0,0)\). Let’s assume that point \(P\) makes an angle \(\theta\) with the positive x-axis.

The coordinates of the square's vertices would then be:
\[
A = \left(\frac{s}{2}, \frac{s}{2}\right), \quad B = \left(-\frac{s}{2}, \frac{s}{2}\right), \quad C = \left(-\frac{s}{2}, -\frac{s}{2}\right), \quad D = \left(\frac{s}{2}, -\frac{s}{2}\right)
\]
And the coordinates of point \(P\) on the circumcircle would be:
\[
P = \left(R\cos\theta, R\sin\theta\right)
\]
where \(R = \frac{s}{\sqrt{2}}\).

**Calculating Distances:**

Now, calculate \(PA\), \(PB\), \(PC\), and \(PD\) using the distance formula.

For example:
\[
PA = \sqrt{\left(R\cos\theta - \frac{s}{2}\right)^2 + \left(R\sin\theta - \frac{s}{2}\right)^2}
\]
This seems quite involved. Let’s see if there's a pattern or simplification.

**Simplifying Expressions:**

Given that \(R = \frac{s}{\sqrt{2}}\), let's substitute:
\[
PA = \sqrt{\left(\frac{s}{\sqrt{2}}\cos\theta - \frac{s}{2}\right)^2 + \left(\frac{s}{\sqrt{2}}\sin\theta - \frac{s}{2}\right)^2}
\]
Factor out \(s\):
\[
PA = s \cdot \sqrt{\left(\frac{\cos\theta}{\sqrt{2}} - \frac{1}{2}\right)^2 + \left(\frac{\sin\theta}{\sqrt{2}} - \frac{1}{2}\right)^2}
\]
This still looks complicated. Maybe there's a trigonometric identity that can simplify this expression.

**Using Trigonometric Identities:**

Let’s consider the following identity:
\[
\left(\frac{\cos\theta}{\sqrt{2}} - \frac{1}{2}\right)^2 + \left(\frac{\sin\theta}{\sqrt{2}} - \frac{1}{2}\right)^2
\]
Expanding:
\[
\frac{\cos^2\theta}{2} - \frac{\cos\theta}{\sqrt{2}} + \frac{1}{4} + \frac{\sin^2\theta}{2} - \frac{\sin\theta}{\sqrt{2}} + \frac{1}{4}
\]
Combine like terms:
\[
\frac{\cos^2\theta + \sin^2\theta}{2} - \frac{\cos\theta + \sin\theta}{\sqrt{2}} + \frac{1}{2}
\]
Since \(\cos^2\theta + \sin^2\theta = 1\):
\[
\frac{1}{2} - \frac{\cos\theta + \sin\theta}{\sqrt{2}} + \frac{1}{2} = 1 - \frac{\cos\theta + \sin\theta}{\sqrt{2}}
\]
Therefore:
\[
PA = s \cdot \sqrt{1 - \frac{\cos\theta + \sin\theta}{\sqrt{2}}}
\]
Similarly, we can derive expressions for \(PB\), \(PC\), and \(PD\), but this seems to be getting too algebra-heavy.

**Realization and Simplification:**

Wait, perhaps there's a smarter way. Instead of calculating each distance separately, maybe I can relate the products \(PA \cdot PC\) and \(PB \cdot PD\) directly.

Given the coordinates, \(PA \cdot PC\) and \(PB \cdot PD\) might simplify nicely when multiplied.

**Calculating \(PA \cdot PC\):**

Using the expressions for \(PA\) and \(PC\):
\[
PA \cdot PC = \sqrt{\left(\frac{s}{\sqrt{2}}\cos\theta - \frac{s}{2}\right)^2 + \left(\frac{s}{\sqrt{2}}\sin\theta - \frac{s}{2}\right)^2} \times \sqrt{\left(\frac{s}{\sqrt{2}}\cos\theta + \frac{s}{2}\right)^2 + \left(\frac{s}{\sqrt{2}}\sin\theta + \frac{s}{2}\right)^2}
\]
This product resembles the difference of squares:
\[
(a - b)(a + b) = a^2 - b^2
\]
Let’s set:
\[
a = \left(\frac{s}{\sqrt{2}}\cos\theta\right)^2 + \left(\frac{s}{\sqrt{2}}\sin\theta\right)^2 = \frac{s^2}{2}(\cos^2\theta + \sin^2\theta) = \frac{s^2}{2}
\]
\[
b = \left(\frac{s}{2}\right)^2 + \left(\frac{s}{2}\right)^2 = \frac{s^2}{4} + \frac{s^2}{4} = \frac{s^2}{2}
\]
Wait, this gives:
\[
PA \cdot PC = \sqrt{a - b} = \sqrt{0} = 0
\]
Which contradicts the given \(PA \cdot PC = 56\). Clearly, this approach is flawed.

**Back to the Drawing Board:**

This dead end suggests that directly multiplying \(PA\) and \(PC\) using coordinates isn't the way to go. Let's rethink.

**Alternative Idea Using Cosine Law:**

Maybe instead of coordinates, I can use the Law of Cosines in triangles \(PAB\), \(PBC\), \(PCD\), and \(PDA\).

But given the symmetry and the products \(PA \cdot PC\) and \(PB \cdot PD\), perhaps there's a more elegant geometric relationship.

**Insight from Initial Answer:**

Recalling the initial approach, we set up equations based on the products and solved for \(R^2\), leading to \(s^2 = 106\).

Perhaps the initial oversight was not fully explaining the reasoning behind those steps. Let me revisit that method, ensuring each step is clear and logically connected.

**Reapplying Power of a Point with Correct Assumptions:**

Given point \(P\) on the circumcircle of square \(ABCD\), the Power of a Point theorem still holds:
\[
PA \cdot PC = PB \cdot PD
\]
But in our problem, \(PA \cdot PC = 56\) and \(PB \cdot PD = 90\), which suggests that perhaps there's a misunderstanding or misapplication.

**Correct Understanding:**

Actually, the Power of a Point theorem states that for any point \(P\) on the circumcircle, the product of the lengths of the two intersecting chords is constant. However, in a square, not all pairs of opposite vertices form intersecting chords through \(P\). Only the diagonals \(AC\) and \(BD\) intersect at the center.

Thus, for point \(P\) on the circumcircle:
\[
PA \cdot PC = PB \cdot PD = R^2
\]
But this contradicts our given values unless \(R^2\) can take two different values, which is impossible. Therefore, my initial assumption must be incorrect.

**Realizing the Mistake:**

The error lies in assuming that \(PA \cdot PC = PB \cdot PD\). This equality holds only when \(P\) lies on a specific locus relative to the square, possibly when \(P\) is aligned with the diagonals. However, our given values \(56\) and \(90\) suggest that \(P\) does not lie symmetrically, and thus, the standard Power of a Point doesn't directly apply.

**Alternative Approach: Using Complex Numbers:**

Perhaps representing the points as complex numbers can help exploit the circle's properties.

Let’s assign complex numbers to the square's vertices:
\[
A = \frac{s}{2} + \frac{s}{2}i, \quad B = -\frac{s}{2} + \frac{s}{2}i, \quad C = -\frac{s}{2} - \frac{s}{2}i, \quad D = \frac{s}{2} - \frac{s}{2}i
\]
Let \(P = Re^{i\theta}\), where \(R = \frac{s}{\sqrt{2}}\) is the radius.

Then:
\[
PA = |P - A| = \left| \frac{s}{\sqrt{2}}e^{i\theta} - \left(\frac{s}{2} + \frac{s}{2}i\right) \right|
\]
\[
PC = |P - C| = \left| \frac{s}{\sqrt{2}}e^{i\theta} - \left(-\frac{s}{2} - \frac{s}{2}i\right) \right|
\]
Similarly for \(PB\) and \(PD\).

Calculating these magnitudes and their products could lead to equations involving \(s\) and \(\theta\), which might be solvable. However, this approach seems too algebraically intensive and may not yield a straightforward solution.

**Seeking Simpler Geometric Relationships:**

Given the complexity of previous approaches, let's consider geometric properties unique to squares and circles. Perhaps the areas formed by connecting \(P\) to the square's vertices relate to the given products.

Alternatively, considering that \(ABCD\) is a square inscribed in a circle, there might be a relationship between the products of distances from any point on the circle to the square's vertices and the square's side length.

**Connecting Back to the Initial Solution:**

Given the time invested in exploring different strategies, perhaps the initial approach was on the right track, and the confusion arose from misapplying the Power of a Point theorem.

Let me revisit the initial steps carefully:

1. **Coordinate Setup:**
   - Center the square at the origin.
   - Coordinates:
     \[
     A = \left(\frac{s}{2}, \frac{s}{2}\right), \quad B = \left(-\frac{s}{2}, \frac{s}{2}\right), \quad C = \left(-\frac{s}{2}, -\frac{s}{2}\right), \quad D = \left(\frac{s}{2}, -\frac{s}{2}\right)
     \]
   - Radius \(R = \frac{s}{\sqrt{2}}\).

2. **Expressing Products Using Angles:**
   - Assume \(P\) makes an angle \(\theta\) with the positive x-axis.
   - The angles for vertices \(A\), \(B\), \(C\), and \(D\) are \(45^\circ\), \(135^\circ\), \(225^\circ\), and \(315^\circ\) respectively.

3. **Expressing \(PA \cdot PC\) and \(PB \cdot PD\):**
   - \(PA \cdot PC = 2R^2 \sin \alpha\)
   - \(PB \cdot PD = 2R^2 \cos \alpha\)
   - Where \(\alpha = |\theta - 45^\circ|\)

4. **Setting Up Equations:**
   - Given:
     \[
     2R^2 \sin \alpha = 56 \quad (1)
     \]
     \[
     2R^2 \cos \alpha = 90 \quad (2)
     \]
   - Dividing (1) by (2):
     \[
     \tan \alpha = \frac{56}{90} = \frac{28}{45}
     \]

5. **Solving for \(R^2\):**
   - From equation (1):
     \[
     2R^2 \sin \alpha = 56 \implies R^2 \sin \alpha = 28
     \]
   - From equation (2):
     \[
     2R^2 \cos \alpha = 90 \implies R^2 \cos \alpha = 45
     \]
   - Using \(\tan \alpha = \frac{28}{45}\), we can find \(\sin \alpha\) and \(\cos \alpha\):
     \[
     \sin \alpha = \frac{28}{\sqrt{28^2 + 45^2}} = \frac{28}{53}, \quad \cos \alpha = \frac{45}{53}
     \]
   - Substituting back:
     \[
     R^2 \cdot \frac{28}{53} = 28 \implies R^2 = 53
     \]

6. **Determining the Side Length \(s\):**
   - Since \(R^2 = \frac{s^2}{2}\):
     \[
     \frac{s^2}{2} = 53 \implies s^2 = 106
     \]
   - Therefore, the area of the square \(ABCD\) is \(106\).

**Verification:**

Let’s check if this makes sense.

Given \(R^2 = 53\), then:
\[
PA \cdot PC = 2R^2 \sin \alpha = 2 \times 53 \times \frac{28}{53} = 56
\]
\[
PB \cdot PD = 2R^2 \cos \alpha = 2 \times 53 \times \frac{45}{53} = 90
\]
Both conditions are satisfied, confirming that \(s^2 = 106\) is indeed the correct area.

**Conclusion:**

After exploring various strategies and encountering a few dead ends, revisiting the initial approach with careful consideration clarified the solution. The area of square \(ABCD\) is:

\[
\boxed{106}
\]