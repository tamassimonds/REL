### Question:
A plane contains $40$ lines, no $2$ of which are parallel. Suppose that there are $3$ points where exactly $3$ lines intersect, $4$ points where exactly $4$ lines intersect, $5$ points where exactly $5$ lines intersect, $6$ points where exactly $6$ lines intersect, and no points where more than $6$ lines intersect. Find the number of points where exactly $2$ lines intersect.



### Answer:
Alright, let's tackle this problem step by step. I'll walk you through my thought process, exploring different strategies, checking along the way, and adjusting my approach as needed.

**Problem Recap:**
We have 40 lines in a plane, no two of which are parallel. There are:
- 3 points where exactly 3 lines intersect,
- 4 points where exactly 4 lines intersect,
- 5 points where exactly 5 lines intersect,
- 6 points where exactly 6 lines intersect,
- No points where more than 6 lines intersect.

We need to find the number of points where exactly 2 lines intersect.

**First Thoughts:**
- **Total Possible Intersections:** If no two lines are parallel and no three lines intersect at the same point, the total number of intersection points would be the combination of 40 lines taken 2 at a time, which is \( C(40, 2) = 780 \) points.
- **But** we have multiple lines intersecting at the same points, which reduces the total number of distinct intersection points.

So, our task is to adjust the total number of intersection points by accounting for these multiple intersections.

**Strategy Brainstorming:**
1. **Calculate Total Pairwise Intersections:** Start with \( C(40, 2) = 780 \) total possible intersections if all intersections are between exactly two lines.
2. **Adjust for Multiple-Line Intersections:** For each point where more than two lines intersect, subtract the extra intersections that would have been counted if they were just pairwise.

**Diving Deeper:**

Let's formalize this:

- **Single Intersection Points (Exactly 2 lines):** These are the points we need to find.
- **Multiple Intersection Points:** Each point where \( k \) lines intersect accounts for \( C(k, 2) \) pairwise intersections.

**Calculations:**

1. **Total Pairwise Intersections Without Overlaps:**
   \[
   \text{Total} = C(40, 2) = \frac{40 \times 39}{2} = 780
   \]

2. **Subtracting Overlaps:**
   - **Points with 3 lines:**
     - Each such point would have \( C(3, 2) = 3 \) pairwise intersections.
     - Since these 3 intersections are all happening at a single point, we’re overcounting by \( 3 - 1 = 2 \) intersections per such point.
     - **Total Overcount for 3-line Points:** \( 3 \times 2 = 6 \)

   - **Points with 4 lines:**
     - \( C(4, 2) = 6 \) pairwise intersections.
     - Overcount per point: \( 6 - 1 = 5 \)
     - **Total Overcount for 4-line Points:** \( 4 \times 5 = 20 \)

   - **Points with 5 lines:**
     - \( C(5, 2) = 10 \) pairwise intersections.
     - Overcount per point: \( 10 - 1 = 9 \)
     - **Total Overcount for 5-line Points:** \( 5 \times 9 = 45 \)

   - **Points with 6 lines:**
     - \( C(6, 2) = 15 \) pairwise intersections.
     - Overcount per point: \( 15 - 1 = 14 \)
     - **Total Overcount for 6-line Points:** \( 6 \times 14 = 84 \)

3. **Total Overcount Across All Multiple-Line Points:**
   \[
   6 (3\text{-line}) + 20 (4\text{-line}) + 45 (5\text{-line}) + 84 (6\text{-line}) = 155
   \]

4. **Adjusting the Total Pairwise Intersections:**
   \[
   \text{Exact Two-Line Intersections} = \text{Total Pairwise} - \text{Total Overcount} = 780 - 155 = 625
   \]

**Wait a Minute...**

Hold on. This result contradicts the initial quick calculation I did earlier (which was 607). Let me check where I might have gone wrong.

**Reviewing the Approach:**

Ah, I see the mistake. When multiple lines intersect at a single point, the total number of pairwise intersections at that point is \( C(k, 2) \), but in the total pairwise count, each of these has been counted separately. Therefore, to find the actual number of distinct intersection points, we should subtract the extra intersections beyond the first.

But here's a more accurate way:

- **Total pairwise intersections:** 780
- **Each multiple-line intersection point accounts for \( C(k, 2) \) pairwise intersections, but it's just one actual intersection point.**

So, to find the actual number of intersection points:
\[
\text{Actual Intersection Points} = \text{Total Pairwise} - \left( \sum [C(k, 2) \times \text{Number of such points}] \right) + \left( \text{Number of multiple-line points} \right)
\]
Wait, this seems convoluted. Maybe another approach would be clearer.

**Alternative Strategy:**

Perhaps it's simpler to calculate the total number of pairwise intersections accounted for by the multiple-line points and then subtract that from the total pairwise intersections to find the remaining intersections that are exactly between two lines.

Let's try that:

1. **Total Pairwise Intersections:** 780

2. **Pairwise Intersections at Multiple-Line Points:**
   - **3-line points:** \( 3 \times C(3, 2) = 3 \times 3 = 9 \)
   - **4-line points:** \( 4 \times C(4, 2) = 4 \times 6 = 24 \)
   - **5-line points:** \( 5 \times C(5, 2) = 5 \times 10 = 50 \)
   - **6-line points:** \( 6 \times C(6, 2) = 6 \times 15 = 90 \)
   - **Total Pairwise at Multiple-Line Points:** \( 9 + 24 + 50 + 90 = 173 \)

3. **Subtracting These from Total Pairwise:**
   \[
   780 (Total) - 173 (Multiple-Line Pairs) = 607
   \]
   
So, the number of points where exactly two lines intersect is **607**.

**Final Check:**

Let's ensure this makes sense. If we add up all the distinct intersection points:

- **Multiple-Line Points:**
  - 3 (3-line) + 4 (4-line) + 5 (5-line) + 6 (6-line) = 18 points
- **Two-Line Points:** 607
- **Total Intersection Points:** \( 607 + 18 = 625 \)

Now, considering that each pair of lines intersects exactly once, and we have \( C(40, 2) = 780 \) total intersections, does \( 607 \times 1 + 18 \times C(k,2) \) equal 780?

Wait, let's re-express that:

Each multiple-line point accounts for \( C(k, 2) \) pairwise intersections.

So, total pairwise intersections are:

\[
607 (\text{two-line points}) \times 1 + 3 \times C(3,2) + 4 \times C(4,2) + 5 \times C(5,2) + 6 \times C(6,2) = 607 + 9 + 24 + 50 + 90 = 780
\]

Perfect! It adds up to the total number of pairwise intersections, confirming that our answer is consistent.

**Answer:**

\(\boxed{607}\)