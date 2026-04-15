# 🧪 Lab 2 – Number Theory & Basic Operations

## 📌 Overview

This lab focuses on fundamental number theory concepts such as GCD, divisibility, and co-prime numbers. It also introduces efficient algorithms and iterative problem-solving techniques.

---

## 🔢 Questions & Solutions

### ✅ Q1. GCD (Basic Method)

📄 

**Problem:**
Find the Greatest Common Divisor (GCD) of two numbers using a basic approach.

**Approach:**

* Iterate from 1 to minimum of both numbers
* Check common divisors
* Store the greatest one

**Example:**
Input: `12 18`
Output: `6`

---

### ✅ Q2. GCD (Euclidean Algorithm)

📄 

**Problem:**
Find GCD using the efficient Euclidean Algorithm.

**Approach:**

* Repeatedly replace `(a, b)` with `(b, a % b)`
* Continue until `b = 0`

**Example:**
Input: `12 18`
Output: `6`

---

### ✅ Q3. Count Divisors

📄 

**Problem:**
Count total number of divisors of a number.

**Approach:**

* Loop from 1 to N
* Count numbers that divide N completely

**Example:**
Input: `6`
Output: `4`

---

### ✅ Q4. Co-Prime Numbers

📄 

**Problem:**
Check whether two numbers are co-prime.

**Approach:**

* Find GCD using Euclidean method
* If GCD = 1 → Co-prime

**Example:**
Input: `8 15`
Output: `Co-Prime`

---

### ✅ Q5. Digit Product Reduction

📄 

**Problem:**
Multiply digits repeatedly until a single digit remains.

**Approach:**

* Concatenate number K times
* Multiply digits
* Repeat until single digit

**Example:**
Input: `N=39, K=2`
Output: `4`

---

## 🛠️ Concepts Used

* GCD & Euclidean Algorithm
* Divisibility rules
* Loops and conditions
* String and number manipulation

---

## 🎯 Learning Outcomes

* Understanding of efficient algorithms (Euclidean method)
* Strong grasp of divisibility and factors
* Improved optimization thinking

---

## 📌 Conclusion

Lab 2 strengthens the foundation of number theory and introduces optimized approaches, which are essential for solving complex computational problems.

---
