### Question:
Find the number of positive integers less than $1000$ that can be expressed as the difference of two integral powers of $2.$


### Answer:

To find the number of positive integers less than 1000 that can be expressed as the difference of two integral powers of 2, we start by considering the general form of such numbers:

\[ n = 2^k - 2^j \quad \text{for integers } k > j \geq 0. \]

This can be rewritten as:

\[ n = 2^j (2^{k-j} - 1). \]

Let \( m = k - j \geq 1 \), so the expression becomes:

\[ n = 2^j (2^m - 1). \]

We observe that \( 2^m - 1 \) is always an odd number for \( m \geq 1 \). Therefore, \( n \) is the product of a power of 2 and an odd number.

Now, we can list \( s = 2^m - 1 \) for \( m \) from 1 to 9 (since \( 2^{10} - 1 = 1023 > 1000 \)):

- \( m = 1 \): \( s = 1 \)
- \( m = 2 \): \( s = 3 \)
- \( m = 3 \): \( s = 7 \)
- \( m = 4 \): \( s = 15 \)
- \( m = 5 \): \( s = 31 \)
- \( m = 6 \): \( s = 63 \)
- \( m = 7 \): \( s = 127 \)
- \( m = 8 \): \( s = 255 \)
- \( m = 9 \): \( s = 511 \)

For each \( s \), we multiply by powers of 2 (\( 2^j \)) until the product exceeds 1000:

1. For \( s = 1 \):
   - \( n = 1 \times 2^j \) for \( j = 0 \) to 9 (n = 1, 2, 4, 8, 16, 32, 64, 128, 256, 512)

2. For \( s = 3 \):
   - \( n = 3 \times 2^j \) for \( j = 0 \) to 8 (n = 3, 6, 12, 24, 48, 96, 192, 384, 768)

3. Repeat this process for \( s = 7, 15, 31, 63, 127, 255, 511 \).

After listing all such numbers less than 1000 and removing duplicates, we find that there are exactly 50 distinct positive integers that can be expressed as the difference of two integral powers of 2:

1. 1
2. 2
3. 3
4. 4
5. 6
6. 7
7. 8
8. 12
9. 14
10. 15
11. 16
12. 24
13. 28
14. 30
15. 31
16. 32
17. 48
18. 56
19. 60
20. 62
21. 63
22. 64
23. 96
24. 112
25. 120
26. 124
27. 126
28. 127
29. 128
30. 192
31. 224
32. 240
33. 248
34. 252
35. 254
36. 255
37. 256
38. 384
39. 448
40. 480
41. 496
42. 504
43. 508
44. 510
45. 511
46. 512
47. 768
48. 896
49. 960
50. 992

**Answer: 50**