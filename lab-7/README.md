# 🧪 Lab 7 – Sliding Window & Prefix Sum Techniques

## 📌 Overview

This lab focuses on advanced problem-solving techniques such as **Sliding Window**, **Prefix Sum**, and **Matrix-based computations**. These approaches help in optimizing time complexity and are widely used in real-world applications and coding interviews.

---

## 🔢 Questions & Solutions

### ✅ Q1. Maximum Average Subarray

📄 

**Problem:**
Find the maximum average of a subarray of size `k`.

**Approach:**

* Use sliding window
* Maintain window sum
* Update sum efficiently by removing old element and adding new one

**Example:**
Input: `[1,12,-5,-6,50,3], k=4`
Output: `12.75`

---

### ✅ Q2. First Negative in Every Window

📄 

**Problem:**
Find first negative number in every window of size `k`.

**Approach:**

* Use deque to store indices of negative numbers
* Slide window and update deque

---

### ✅ Q3. Range Sum Query (Prefix Sum)

📄 

**Problem:**
Answer multiple range sum queries efficiently.

**Approach:**

* Precompute prefix sum array
* Use formula: `sum(L,R) = prefix[R] - prefix[L-1]`

---

### ✅ Q4. Range Updates (Difference Array)

📄 

**Problem:**
Perform multiple range updates efficiently.

**Approach:**

* Use difference array
* Apply updates in O(1)
* Build final array using prefix sum

---

### ✅ Q5. Subarray Sum Equals K

📄 

**Problem:**
Count number of subarrays whose sum equals `k`.

**Approach:**

* Use prefix sum + hashmap
* Store frequency of sums
* Check `(current_sum - k)`

---

### ✅ Q6. 2D Prefix Sum (Matrix Region Sum)

📄 

**Problem:**
Find sum of elements in a submatrix.

**Approach:**

* Build 2D prefix sum matrix
* Use inclusion-exclusion principle

---

### ✅ Q7. Maximum Submatrix Sum

📄 

**Problem:**
Find maximum sum of any rectangular submatrix.

**Approach:**

* Fix column boundaries
* Compress rows
* Apply Kadane’s algorithm

---

## 🛠️ Concepts Used

* Sliding Window
* Prefix Sum (1D & 2D)
* HashMap (Dictionary)
* Kadane’s Algorithm

---

## 🎯 Learning Outcomes

* Efficient handling of range queries
* Optimization from O(n²) to O(n) / O(n log n)
* Strong foundation for advanced DSA problems

---

## 📌 Conclusion

Lab 7 covers highly optimized techniques that are crucial for solving real-world and interview-level problems efficiently. Mastery of these concepts significantly improves problem-solving speed and performance.

---
