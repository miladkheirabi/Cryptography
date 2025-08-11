# Cryptography & Applied Security Challenges

This repository contains a collection of practical exercises and challenges related to cryptography, cybersecurity, and applied security concepts.  
The challenges are inspired by the **Applied Cryptography** course, as well as self-designed CTF-style problems for hands-on learning.  

More exercises will be added regularly.

---

## 📂 Applied Cryptography Challenges

### 1. XOR Image Decryption  
**Description:** Two PNG images are encrypted with the same random image key using the XOR method. Recover the flag using known-plaintext properties.  
**Skills:** Bitwise operations, image processing, cryptanalysis  
[View Challenge](Applied%20Cryptography/2ndSemester/HW1)  

---

### 2. Flimsy Numbers: A Cryptographer’s Playground  
**Description:** Weak number generation combined with obfuscation. Analyze the provided code, detect weaknesses, and recover the flag.  
**Skills:** Reverse engineering Python code, RNG attacks, XOR  
[View Challenge](Applied%20Cryptography/2ndSemester/HW2)  

---

### 3. Hidden in Compression (AES-CTR)  
**Description:** Demonstrates why compressing data before encryption can be dangerous when patterns exist. Interact with the provided online lab.  
**Lab Link:** [miladsaleh.pythonanywhere.com](https://miladsaleh.pythonanywhere.com)  
**Skills:** Stream cipher vulnerabilities, compression attacks  
[View Challenge](Applied%20Cryptography/2ndSemester/HW3)  

---

### 4. Weak Keys in 3DES  
**Description:** Explore weak-key vulnerabilities in Triple DES using an interactive web interface.  
**Lab Link:** [miladkheirabi.pythonanywhere.com](https://miladkheirabi.pythonanywhere.com)  
**Skills:** Symmetric cryptography, key schedule weaknesses  
[View Challenge](Applied%20Cryptography/2ndSemester/HW4)  

---

### 5. ECC with Weak Curve Parameters  
**Description:** Analyze an elliptic curve with weak parameters and recover the shared secret using discrete log algorithms.  
**Skills:** ECC cryptanalysis, Pohlig–Hellman, Baby-step giant-step, SageMath  
[View Challenge](Applied%20Cryptography/2ndSemester/HW5)  

---

## 🛠 Technologies & Skills
- **Languages:** Python  
- **Libraries:** PyCryptodome, Flask, SageMath  
- **Topics:** Symmetric & Asymmetric Cryptography, Cryptanalysis, CTF-style problem solving  

---

## 📌 Notes
- These challenges are for **educational purposes only**.  
- All flags follow the format `MERCER{...}` or `flag{...}`.  
- Designed for hands-on exploration of cryptographic vulnerabilities.

---
