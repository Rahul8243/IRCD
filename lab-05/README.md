# 🧪 Lab 5 – Bit Manipulation & Array Partitioning

## 📌 Overview

This lab introduces bit manipulation techniques and array partitioning concepts. It focuses on efficient problem-solving using XOR operations and conditional partitioning of arrays.

---

## 🔢 Questions & Solutions

### ✅ Q1. Unique Element using XOR

📄 

**Problem:**
Find the unique element in an array where every other element appears twice.

**Approach:**

* Use XOR operation (`^`)
* Property: `a ^ a = 0` and `a ^ 0 = a`
* XOR all elements → result is the unique element

**Example:**
Input: `[2, 3, 5, 3, 2]`
Output: `5`

---

### ✅ Q2. XOR of Range [L, R]

📄 

**Problem:**
Find XOR of all numbers in range `[L, R]`.

**Approach:**

* Use pattern-based XOR calculation
* XOR(1 to n) follows repeating pattern (n % 4)
* Compute: `xor(R) ^ xor(L-1)`

**Example:**
Input: `L=3, R=6`
Output: `4`

---

### ✅ Q3. Array Partition into Three Parts

📄 

**Problem:**
Divide array into three parts based on two values (a and b):

* Less than `a`
* Between `a` and `b`
* Greater than `b`

**Approach:**

* Traverse array once
* Use three separate lists to store elements

**Example:**
Input: `arr = [1..10], a=5, b=9`
Output: `[1-4], [6-8], [10]`

---

## 🛠️ Concepts Used

* Bit Manipulation (XOR)
* Pattern recognition
* Array traversal
* Conditional partitioning

---

## 🎯 Learning Outcomes

* Understanding XOR properties and applications
* Efficient computation using mathematical patterns
* Improved array handling and classification techniques

---

## 📌 Conclusion

Lab 5 introduces optimized techniques like XOR operations and structured array partitioning, which are commonly used in coding interviews and competitive programming.

---
