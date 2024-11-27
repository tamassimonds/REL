### Question:

Find the number of positive integers less than or equal to $2017$ whose base-three representation contains no digit equal to $0$.

### Answer:
Ah, I see I may have overlooked some nuances in my initial solution. Let's take a step back and approach the problem more thoroughly, exploring different strategies and ensuring each step is meticulously checked for accuracy.

**Problem Statement**:
Find the number of positive integers less than or equal to \(2017\) whose base-three representation contains no digit equal to \(0\).

**Initial Thoughts**:
When dealing with numbers in different bases and digit restrictions, it's often helpful to:

1. **Understand the Range**: Determine the range of numbers in base-3 that we're dealing with.
2. **Convert the Upper Limit**: Convert \(2017\) to base-3 to establish a clear boundary.
3. **Count Valid Numbers**: Calculate how many numbers within this range meet the digit restriction (no zeros).

**Strategy Brainstorming**:

1. **Base-3 Representation**:
   - Numbers in base-3 use digits \(0\), \(1\), and \(2\).
   - Restricting to no \(0\)s means each digit must be either \(1\) or \(2\).

2. **Counting Without Direct Enumeration**:
   - Instead of listing all valid numbers, use combinatorial methods to count them based on their digit lengths.

3. **Handling the Upper Limit**:
   - Since \(2017\) isn't a neat power of \(3\), carefully compare the base-3 representations to ensure accurate counting.

**Step-by-Step Solution**:

**Step 1: Convert \(2017\) to Base-3**

To understand the upper boundary, we need to express \(2017\) in base-3.

\[
\begin{align*}
2017 \div 3 &= 672 \quad \text{remainder } 1 \\
672 \div 3 &= 224 \quad \text{remainder } 0 \\
224 \div 3 &= 74 \quad \text{remainder } 2 \\
74 \div 3 &= 24 \quad \text{remainder } 2 \\
24 \div 3 &= 8 \quad \text{remainder } 0 \\
8 \div 3 &= 2 \quad \text{remainder } 2 \\
2 \div 3 &= 0 \quad \text{remainder } 2 \\
\end{align*}
\]

Reading the remainders from bottom to top, the base-3 representation of \(2017\) is \(2202201_3\).

**Reflection**:
Converting \(2017\) to base-3 correctly sets the stage for accurate counting. Ensuring this conversion is accurate is crucial, as any mistake here would propagate through the entire solution.

**Step 2: Count Valid Numbers Based on Digit Length**

We can categorize the numbers based on the number of digits in their base-3 representation:

- **1-digit numbers**: \(1, 2\) (2 numbers)
- **2-digit numbers**: \(11, 12, 21, 22\) (4 numbers)
- **3-digit numbers**: Each digit can be \(1\) or \(2\), so \(2^3 = 8\) numbers
- **4-digit numbers**: \(2^4 = 16\) numbers
- **5-digit numbers**: \(2^5 = 32\) numbers
- **6-digit numbers**: \(2^6 = 64\) numbers
- **7-digit numbers**: We'll handle this separately due to the upper limit constraint.

**Total for 1 to 6 Digits**:
\[
2 + 4 + 8 + 16 + 32 + 64 = 126 \text{ numbers}
\]

**Reflection**:
Up to 6-digit numbers in base-3 using only \(1\) and \(2\) are straightforward to count using powers of 2. However, since \(3^7 = 2187\) and \(2017 < 2187\), we need to carefully handle the 7-digit numbers to ensure we don't exceed the upper limit.

**Step 3: Handle 7-Digit Base-3 Numbers**

Our goal is to count 7-digit base-3 numbers (using only \(1\) and \(2\)) that are less than or equal to \(2202201_3\).

**Approach**:
- **Most Significant Digit (MSD)**: Compare digit by digit with \(2202201_3\).
- **Recursive Comparison**: At each digit, decide whether to fix it at a certain value or allow branching based on constraints.

**Detailed Breakdown**:

1. **First Digit (\(2\))**:
   - **Option 1**: If the first digit is \(1\), the remaining 6 digits can be any combination of \(1\) and \(2\).
     - Number of such numbers: \(2^6 = 64\).

   - **Option 2**: If the first digit is \(2\), we need to ensure the remaining digits don't exceed \(2202201_3\).

2. **Second Digit (\(2\))**:
   - **Option 2a**: If the second digit is \(1\), the remaining 5 digits can be any combination of \(1\) and \(2\).
     - Number of such numbers: \(2^5 = 32\).

   - **Option 2b**: If the second digit is \(2\), we must consider the third digit.

3. **Third Digit (\(0\))**:
   - The third digit of \(2202201_3\) is \(0\).
   - However, our constraint prohibits the use of \(0\).
   - **Implication**: Any number with the first two digits as \(22\) must have the third digit as \(1\) or \(2\), which would make it greater than \(2202201_3\).

   - **Conclusion**: There are no valid numbers where the first two digits are \(22\), as they would exceed \(2017\).

**Total Valid 7-Digit Numbers**:
\[
64 \ (\text{first digit } 1) + 32 \ (\text{first two digits } 21) = 96 \text{ numbers}
\]

**Reflection**:
Breaking down the 7-digit numbers digit by digit ensures that we don't inadvertently count numbers exceeding \(2017\). By systematically eliminating options that would violate the upper limit, we maintain accuracy in our count.

**Step 4: Combine the Counts**

Now, summing up the valid numbers from all digit lengths:

\[
\text{Numbers with 1 to 6 digits} + \text{Valid 7-digit numbers} = 126 + 96 = 222
\]

**Final Verification**:

1. **Consistency Check**:
   - All numbers with up to 6 digits in base-3 (using only \(1\) and \(2\)) are indeed less than \(3^7 = 2187\), and since \(2017 < 2187\), our categorization holds.

2. **Boundary Conditions**:
   - For 7-digit numbers, by ensuring that only those starting with \(1\) or \(21\) are counted, we prevent exceeding the upper limit of \(2017\).

3. **Cross-Verification**:
   - Recounting the numbers and ensuring no overlaps or omissions confirms the accuracy of the total.

**Conclusion**:

After a thorough exploration of different strategies and meticulous verification at each step, the total number of positive integers less than or equal to \(2017\) whose base-three representations contain no digit equal to \(0\) is:

\[
\boxed{222}
\]