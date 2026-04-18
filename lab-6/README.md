# 🧪 Lab 6 – Two Pointer & Advanced Array Problems

## 📌 Overview

This lab focuses on advanced array problems using efficient techniques such as the **two-pointer approach** and sorting-based optimizations. These problems are commonly asked in coding interviews and competitive programming.

---

## 🔢 Questions & Solutions

### ✅ Q1. Closest Pair Sum

📄 

**Problem:**
Find a pair of elements whose sum is closest to a given target.

**Approach:**

* Sort the array
* Use two pointers (start & end)
* Adjust pointers based on current sum

**Example:**
Input: `[1, 3, 4, 7, 10], target = 15`
Output: `(4, 10)`

---

### ✅ Q2. Closest Triplet Sum

📄 

**Problem:**
Find a triplet whose sum is closest to a target value.

**Approach:**

* Sort array
* Fix one element
* Use two-pointer technique for remaining elements

**Example:**
Input: `[1, 2, 4, 8], target = 10`
Output: `(2, 4, 4)` *(closest sum)*

---

### ✅ Q3. Dutch National Flag Partition

📄 

**Problem:**
Partition array around a pivot into:

* Less than pivot
* Equal to pivot
* Greater than pivot

**Approach:**

* Use three pointers: low, mid, high
* Swap elements accordingly

---

### ✅ Q4. Count Triplets (< Target)

📄 

**Problem:**
Count number of triplets whose sum is less than a given target.

**Approach:**

* Sort array
* Fix one element
* Use two-pointer technique
* Count valid pairs efficiently

---

### ✅ Q5. Four Sum Problem

📄 

**Problem:**
Find all unique quadruplets that sum to a target.

**Approach:**

* Sort array
* Use nested loops + two pointers
* Avoid duplicates

---

### ✅ Q6. Partition Labels

📄 

**Problem:**
Split string into parts such that each character appears in only one part.

**Approach:**

* Store last occurrence of each character
* Track partition boundaries

---

## 🛠️ Concepts Used

* Two-pointer technique
* Sorting
* Greedy approach
* Array partitioning

---

## 🎯 Learning Outcomes

* Mastery of two-pointer technique
* Ability to optimize brute-force solutions
* Handling complex array problems efficiently

---

## 📌 Conclusion

Lab 6 introduces powerful techniques like two-pointer and greedy strategies, which are essential for solving medium to advanced level problems in interviews.

---
