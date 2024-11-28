### Question:
A plane contains $40$ lines, no $2$ of which are parallel. Suppose that there are $3$ points where exactly $3$ lines intersect, $4$ points where exactly $4$ lines intersect, $5$ points where exactly $5$ lines intersect, $6$ points where exactly $6$ lines intersect, and no points where more than $6$ lines intersect. Find the number of points where exactly $2$ lines intersect.


### Answer:

Alright, let's tackle this problem step by step, just as I would approach it in real life. I'll start by understanding the problem, brainstorming possible strategies, trying them out, and adjusting my approach as needed.

---

**Problem Statement:**

A plane contains **40 lines**, no two of which are parallel. There are:
- **3 points** where exactly **3 lines** intersect,
- **4 points** where exactly **4 lines** intersect,
- **5 points** where exactly **5 lines** intersect,
- **6 points** where exactly **6 lines** intersect.

No points have more than **6 lines** intersecting. **Find the number of points where exactly 2 lines intersect.**

---

**Step 1: Understanding the Problem**

We have 40 lines in a plane with no two parallel. Normally, if no three lines intersect at a single point, each pair of lines would intersect exactly once. However, in this problem, there are specific points where multiple lines intersect. Our goal is to find how many intersection points involve exactly two lines.

**Key Points:**
- Total number of lines: 40
- No two lines are parallel
- Multiple lines intersect at specific points

---

**Step 2: Brainstorming Strategies**

To find the number of points where exactly two lines intersect, I can consider the following approaches:

1. **Total Intersection Points Without Multiplicity:**
   - Calculate the total number of intersections if no three lines meet at a single point.
   
2. **Adjust for Multiple Intersections:**
   - Subtract the overcounted intersections due to points where more than two lines intersect.

3. **Use Combinatorics:**
   - Utilize combinations to count the number of intersecting pairs.

I think combining these strategies would be effective. First, find the total possible intersections without considering multiple lines intersecting at the same point, then adjust this number based on the given multiple intersections.

---

**Step 3: Calculating Total Intersection Points Without Multiplicity**

If no two lines are parallel and no three lines intersect at a single point, the number of intersection points is simply the number of ways to choose 2 lines out of 40:

\[
\text{Total intersections} = \binom{40}{2} = \frac{40 \times 39}{2} = 780
\]

So, there would be **780** intersection points if every pair of lines intersected uniquely.

**Reflection:**
This is our starting point. However, the problem specifies that some points have more than two lines intersecting, so we need to adjust this total.

---

**Step 4: Adjusting for Multiple Intersections**

Each point where **k** lines intersect represents \(\binom{k}{2}\) intersections that occur at the same point. Therefore, these points cause an overcount in our initial total.

Given:
- **3 points** with **3 lines** each:
  - Each such point accounts for \(\binom{3}{2} = 3\) intersections.
  - Total for these points: \(3 \times 3 = 9\)

- **4 points** with **4 lines** each:
  - Each such point accounts for \(\binom{4}{2} = 6\) intersections.
  - Total for these points: \(4 \times 6 = 24\)

- **5 points** with **5 lines** each:
  - Each such point accounts for \(\binom{5}{2} = 10\) intersections.
  - Total for these points: \(5 \times 10 = 50\)

- **6 points** with **6 lines** each:
  - Each such point accounts for \(\binom{6}{2} = 15\) intersections.
  - Total for these points: \(6 \times 15 = 90\)

**Total Overcounted Intersections:**
\[
9 + 24 + 50 + 90 = 173
\]

**Reflection:**
Wait a minute—this seems like the total number of intersections at these special points. But we need to consider that in our initial total (780), each of these intersections was counted separately, but they actually occur at a single point. So, we need to adjust our total by subtracting the overcounts.

Each point where **k** lines intersect should contribute **1** to the count of intersection points, but we've initially counted \(\binom{k}{2}\) intersections for it.

So, for each special point, the overcount is \(\binom{k}{2} - 1\).

Let's recalculate the overcounts accordingly.

---

**Step 5: Recalculating Overcounts Correctly**

**Correct Overcount Calculation:**

For each special point where **k** lines intersect, the overcount is:
\[
\text{Overcount} = \binom{k}{2} - 1
\]

Applying this to each set of special points:

1. **3 points** with **3 lines** each:
   \[
   \binom{3}{2} - 1 = 3 - 1 = 2 \text{ overcounts per point}
   \]
   Total overcount: \(3 \times 2 = 6\)

2. **4 points** with **4 lines** each:
   \[
   \binom{4}{2} - 1 = 6 - 1 = 5 \text{ overcounts per point}
   \]
   Total overcount: \(4 \times 5 = 20\)

3. **5 points** with **5 lines** each:
   \[
   \binom{5}{2} - 1 = 10 - 1 = 9 \text{ overcounts per point}
   \]
   Total overcount: \(5 \times 9 = 45\)

4. **6 points** with **6 lines** each:
   \[
   \binom{6}{2} - 1 = 15 - 1 = 14 \text{ overcounts per point}
   \]
   Total overcount: \(6 \times 14 = 84\)

**Total Correct Overcount:**
\[
6 + 20 + 45 + 84 = 155
\]

**Reflection:**
Initially, I miscalculated the overcount by not subtracting 1 for each special point. Now, with the correct overcount of 155, I can adjust the total number of intersections.

---

**Step 6: Adjusting the Total Number of Intersection Points**

Starting with the initial total of 780 intersections, we need to subtract the overcounts:

\[
\text{Adjusted total intersections} = 780 - 155 = 625
\]

**Interpretation:**
This adjusted total of **625** represents the number of unique intersection points considering the multiple-line intersections specified.

However, the problem asks for the number of points where **exactly two lines** intersect. So, the 625 includes all intersection points, both those where exactly two lines intersect and those where more than two lines intersect.

---

**Step 7: Calculating Points with Exactly Two Lines Intersecting**

To find the number of points where exactly two lines intersect, we need to subtract the number of special intersection points (where more than two lines intersect) from the adjusted total.

Given:
- **3 points** with **3 lines** intersecting
- **4 points** with **4 lines** intersecting
- **5 points** with **5 lines** intersecting
- **6 points** with **6 lines** intersecting

Total number of special points:
\[
3 + 4 + 5 + 6 = 18
\]

**Number of Points with Exactly Two Lines Intersecting:**
\[
\text{Points with exactly two lines} = \text{Adjusted total intersections} - \text{Special points} = 625 - 18 = 607
\]

---

**Step 8: Final Answer**

After carefully accounting for overcounts due to multiple-line intersections and adjusting the total number of intersection points accordingly, we find that there are **607** points where exactly two lines intersect.

\(\boxed{607}\)

---

**Final Reflection:**

Throughout the problem, it was crucial to accurately account for the overcounting caused by multiple lines intersecting at a single point. Initially, I overlooked subtracting 1 for each special point, which led to an incorrect overcount. By revisiting the overcount calculation and ensuring that only the excess intersections were subtracted, I arrived at the correct number of points where exactly two lines intersect.