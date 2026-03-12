# Block Ciphers: Overview, DES & AES

Shannon's Design Principles

- **Diffusion**
	- The ciphertext statistics should depend on the plaintext statistics in a manner too complicated to be exploited by the cryptanalyst
	- *Permutations creates diffusion*
- **Confusion**
	- Each digit of the plaintext and each digit of the secret key should influence many digits of the ciphertext
	- Substitution creates confusion
- **Modern block ciphers** are typically obtained by **mixing substitutions and permutations** to obtain both confusion and diffusion

# Anatomy of Block Ciphers
### Overview
**A block cipher is a keyed family of pseudorandom permutations**
- for each key, we have a single permutation that is independent of all the others 
- Design ways to choose 2^K permutations uniformly at random from the set of all (2^N)! permutations
- **Goal** 
	- for a block cipher to be good, Eve should not be able to recover the key even using multiple plaintext-ciphertext pairs

Key design principles
- **Diffusion**
	- If a plaintext bit changes, several ciphertext bits should change
- **Confusion**
	- Every bit of the ciphertext should depend on several bits in the key

#### On Diffusion
- ***Diffusion*** means that the output bits should depend on the input bits in a very complex way
- ***Avalanche criterion***
	- Flipping a fixed set of bits should change each output bit with probability one half
- ***Strict avalanche criterion***
	- For a randomly chosen input, if one flips the i-th bit, then the probability that the j-th output bit will change should be one half, for any i and j

#### On Confusion
- ***Confusion*** refers to making the relationship between the key and the ciphertext as complex and involved as possible
- ***Goal***: make it very hard to find the key even if one has a large number of plaintext- ciphertext pairs produced with the same key
- Each bit of the ciphertext should depend on the entire key, and in different ways on different bits of the key, changing one bit of the key should change the ciphertext completely.

---
### Substitution-Permutation Network
- *The simplest way to achieve both diffusion and confusion*
	- The plaintext and the key often have a very similar role in producing the output, hence it is the same mechanism that ensures both diffusion and confusion
- It takes a block of the plaintext and the key as inputs, and to produce the ciphertext block applies several alternating "**rounds**" or "**layers**" of
	- substitution boxes (S-boxes) and
	- permutation boxes (P-boxes)
- S-boxes and P-boxes transform (sub-)blocks of input bits into output bits
- it is common for these transformation to be operations that are efficient to perform in hardware, such as xor and bitwise rotation
- The key is introduced in each round, usually in the form of "round keys" derived from it
- Decryption is done by simply reversing the process 

### S-Box
- It substitutes a small block of bits by another block of bits
- This substitution should be one-to-one, to ensure invertibility (hence decryption) 
	- There are exceptions as we will see for DES 
- In many cases, the length of the output is the same as the length of the input 
	- In general, this is not always the case as in the case of DES (Data Encryption Standard) 
- An S-box is usually not just a permutation of the bits 
- Rather, a good S-box will have the property that changing one input bit will change about half of the output bits (with an avalanche effect)
- It will also have the property that each output bit will depend on every input bit

### P-Box
- It is a permutation of all the bits
- It takes the output of all the S-boxes of one round, permutes the bits, and feeds them into the S-boxes of the next round
- A good P-box has the property that the output bits of any S-box are distributed to as many S-box inputs as possible

---

# Data Encryption Standard (DES)
- **Feistel Structure**
- it use the same basic algorithm for both encryption and decryption
- It consists of multiple rounds of processing of the plaintext, with each round consisting of a substitution step followed by a permutation step
- In each round 
	- the right half of the block, R, goes through unchanged 
	- he left half, L, goes through an operation that depends on R and the encryption key 
	- the operation carried out on the left half L is referred to as the Feistel Function F 
	- he permutation step consists of swapping the modified L and R
- Decryption is exactly the same as the encryption with the only difference that the round keys are used in the reverse order

----
# The Feistel Function
- The 32-bit right half of the 64-bit input data block is expanded into a 48-bit block 
- Expansion permutation step 
	1. divide the 32-bit block into eight 4-bit words 
	2. attach an additional bit on the left to each 4- bit word that is the last bit of the previous 4- bit word 
	3. attach an additional bit to the right of each 4- bit word that is the beginning bit of the next 4-bit word
- The 56-bit key is divided into two halves, each half shifted separately, and the combined 56-bit key permuted/contracted to yield a 48-bit round key

- ***Purpose***: The Feistel structure allows for the construction of a permutation (i.e., a one-to-one mapping over a set of input blocks)
	- This is crucial for block ciphers, which must be invertible to enable decryption.
- ***Basic Operation***: It takes a data input divided into two halves (e.g., x and y) and applies a specific transformation. One half is combined (typically via XOR) with the output of an arbitrary function F that operates on the other half.
	- The transformation of a single "Feistel permutation" is defined as π(x, y) := (y, x ⊕ F(y)).
- ***Simplified Decryption***: A key advantage of the Feistel structure is that its inverse function π⁻¹(u, v) = (v ⊕ F(u), u) is almost identical to the function itself. This means that the same hardware or software logic can be used for both encryption and decryption, making the implementation more efficient. The result is independent of the definition of the Feistel function F
- ***Application in DES***: In the Data Encryption Standard (DES), the cipher is a 16-round Feistel cipher structure. Each round uses a specific function f, defined as f(x) := F(ki, x), where ki is a 48-bit key for that round, and F is the "DES round function". The DES function F uses several auxiliary functions like E (bit expansion, which expands a 32-bit input to a 48-bit output by rearranging and replicating bits), P (permutation), and the crucial S-boxes (substitution boxes), which introduce non-linearity and confusion/diffusion into the encryption process. DES was adopted by NIST in 1977 and was based on the Lucifer cipher developed earlier by IBM
- ***Round Keys***: The round keys (Ki) are derived from the main encryption key and are used in reverse order for decryption.


### Feistel S-Box
- The 48-bit input word is divided into eight 6-bit word.
- Each 6-bit word fed into a separate S-box
- Each S-box produces a 4-bit output
- The 8 S-boxes together generate a 32-bit output
- Recall that the input 48 bits are obtained by xor-ing the output from the expansion permutation step with the round key
- Each of the eight S-boxes consists of a 4 × 16 table lookup for an output 4-bit word
- The first and the last bit of the 6-bit input word are decoded into one of 4 rows and the middle 4 bits decoded into one of 16 columns for the table lookup
- The goal of the substitution carried out by an S-box is to enhance diffusion
- The expansion-permutation step expands a 32-bit block into a 48-bit block by attaching a bit at the beginning and a bit at the end of each 4-bit sub-block
- Note that the row lookup for each of the eight S-boxes becomes a function of the input bits for the previous S-box and the next S-box


### Digression On Differential Attacks 
- S-boxes tuned to enhance resistance to DES **differential attacks**
	- instance of *chosen plain-text attacks*
- Differential cryptanalysis of block ciphers consists of presenting to the encryption algorithm pairs of plain-text bit patterns with known differences between them and examining the differences between the corresponding cipher-texts
- typically notion of difference between two plain-texts of cipher-texts is the XOR of the bits performed position-wise
- X1 and X2 two plaintext releted with ∆X = X1 + X2, where + is the bitwise xor operator
- The attacker computes the difference ∆Y = Y1 + Y2 of the ciphertexts Y1 and Y2 corresponding to the plaintexts X1 and X2, respectively


## Feistel: P-Box
- table at slide 35 :)))

---
# Key Scheduling 

## Des Key Scheduling 
- The 56-bit encryption key is represented by 8 bytes
- The relevant 56 bits are subject to a permutation before any round keys are generated
- The bit indexing is based on using the range 0-63 for addressing the bit positions in an 8-byte bit pattern in which the last bit of each byte is used as a parity bit.


- end with key permutation, 


##### I will skip the remarks on des :)

---

# Triple DES
- To avoid meet-in-the-middle attacks
- Triple DES uses a key bundle comprising 3 DES keys (K1, K2, K3), each one of 56 bits length
- **Encryption** works as follows
	- Ek3(Dk2(Ek1(plaintext)))
	- perform encryption with K1, followed by a decryption with K2 and then encryption with K3
- **Decryption** is the inverse, namely
	- Dk1(Ek2(Dk3(ciphertext)))
	- perform decryption with K3, followed by an encryption with K2, and then decryption with K1
- **Each triple encryption works on one block** of 64 bits of data

## Choosing Keys 
There are 3 possible options 
1. All three keys are independent 
	- Strongest option, still vulnerable to meet-in-the-middle but requires 2^(2*56) operations 
2. K1 and K2 are independent but K3=K1 
	- Similar to double DES and vulnerable to the same attack with equal complexity, deprecated 
3. All three keys are equal 
	- For backward compatibility with DES, forbidden
- With these restrictions, Triple DES has been reapproved with keying options 1 and 2 only although it is current best practice to use only option 1 as keys should be generated by using random generators


---
# AES Overview

- Block length: 128 bits
- 3 different key lengths:
	- 128
	- 192
	- 256
- for simplicity we will assume the key length to be 128 bits
-  Encryption consists of 
	- 10 rounds for 128-bit keys 
	- 12 rounds for 192-bit keys 
	- 14 rounds for 256-bit keys
- Except for the last round, all other rounds are identical
- Each round includes 
	1. one single-key based substitution step 
	2. a row-wise permutation step 
	3. a column-wise mixing step 
	4. the addition of the round key
- The order of these steps is different for encryption and decryption
- Each round takes an input state array and returns an output state array

## AES vs DES
Key Differences Between AES and DES

***Key Size***
- DES: Uses a 56-bit key
	- This relatively small key size led to it being considered insecure and broken by 1999
- AES: Supports three different key lengths: 128, 192, or 256 bits
	- A larger key space makes brute-force attacks much harder, with AES-256 having a key space of 2^256, currently considered essentially unbreakable by brute-force

***Block Size***
- DES: Operates on 64-bit blocks of data
	- This block size was also identified as problematic for certain applications
- AES: Operates on 128-bit blocks of data
	- Cipher Structure
- DES: Is based on the Feistel cipher structure
	- In a Feistel structure, the input block is divided into two halves, one half passes through unchanged, and the other half goes through a transformation depending on S-boxes and the round key
- AES: Uses a Substitution-Permutation Network (SPN)
	- Unlike Feistel ciphers, AES processes the entire block (matrix) at once in each round, rather than dividing it into halves. AES is also an example of a "key-alternating block cipher," where a diffusion-achieving transformation is applied to the entire block, followed by the application of the round key to the entire block

***Number of Rounds***
- DES: Consists of 16 rounds of processing
- AES: The number of rounds depends on the key length: 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys

***Security Level***
- DES: Is considered less secure than AES due to its small key size and relatively small block size
	- It was broken in 1999. Triple DES (3DES), which applies DES three times, was adopted to increase strength, but it is much slower. Triple DES will be disallowed after December 31, 2023
- AES: Since its introduction in 2001, threats against it remain theoretical, making it essentially unbreakable at the moment by brute force, especially AES-256
	- It is generally considered more secure than DES

***Orientation***
- DES: Is a bit-oriented cipher, requiring bit-level access to the block during substitution
- AES: Is a byte-oriented cipher, meaning all operations are purely byte-level, which is beneficial for fast software implementations

***Round Operations***
- DES: Rounds include Expansion Permutation, XOR, S-box (Substitution Box), P-box (Permutation Box), XOR, and Swap
	- The S-boxes are crucial for introducing non-linearity
- AES: Each round typically includes SubBytes (substitution), ShiftRows (row-wise permutation), MixColumns (column-wise mixing), and AddRoundKey (XOR with the round key)
	- The last round (10th for 128-bit keys) omits the MixColumns step

***Decryption***
- DES: Decryption is identical to encryption in terms of the mechanism, but the round keys are applied in reverse order
	- This is a characteristic of Feistel ciphers
- AES: Unlike DES, decryption differs substantially from encryption, even though similar transformations are used

***Performance***
- AES: Is comparatively faster than DES
	- particularly with hardware implementations like AES-NI, which can significantly speed up encryption

In summary, AES was developed as a successor to DES due to DES's aging security parameters and design, offering a more robust, faster, and flexible encryption standard

---
# AES Structure
- The 128 bits key is arranged in the form of an array of 4 * 4 keys (bytes)
- The four column words of the key array are expanded into a schedule of 44 words
- The first 4 words are used for adding to the input state array before any round can begin
- The remaining 40 words are used for the 10 rounds
- The first 4 are mixed with the input blocks (AddRoundKey) 
	- ***Encryption***: the input state array is xor-ed with the first four words of the key schedule. 
	- ***Decryption***: same as above except that the ciphertext state array is xor-ed with the last four words of the key schedule
- The remaining 40 are used in each one of the 10 rounds
	- 4 at a time
### Structure of a round 
***Encryption*** steps: 
1. Substitute bytes 
2. Shift rows 
3. Mix columns 
4. Add round key 
- It consists of xor-ing the output of the previous 3 steps with 4 words from the key expansion/schedule

***Decryption*** steps 
1. Inverse shift rows 
2. Inverse substitute bytes 
3. Add round key 
4. Inverse mix columns

- The **final round for encryption** does not involve the “Mix columns” step
- The **final round for decryption** does not involve the “Inverse mix columns” step
--- 
## Round Step 1

**SubBytes** for byte-by-byte substitution during encryption
**InvSubBytes** for the corresponding substitution during decryption

- It consists of using a 16 × 16 lookup table to find a replacement byte for a given byte in the input state array 
- The entries in the lookup table are created by using the notions of multiplicative inverses in GF(2^8) and bit scrambling to eliminate the bit-level correlations inside each byte

- To find the substitute byte for a given input byte, divide the input byte into two 4-bit patterns, each yielding an integer value between 0 and 15
- One of the hex values is used as a row index and the other as a column index for selecting one cell in a 16 × 16 lookup table

something to say about its creation
### The lookUp Table is the S-Box

---
## Round Step 2
- **ShiftRows** for shifting the rows of the state array during encryption 
- **InvShiftRows** for the corresponding transformation during decryptio
- The goal is to scramble the byte order inside each 128-bit block

---
## Round Step 3
- **MixColumns** for mixing up of the bytes in each column separately during encryption
- **InvMixColumns** for the corresponding transformation during decryption
- The goal is to further scramble up the 128-bit input block

---
## Round Step 4
- **AddRoundKey** for adding the round key to the output of the previous step during encryption
- **AddRoundKey** or InvAddRoundKey for inverse add round key transformation during **decryption**

---
## Key Expansion
- intro
#### Algorithm
- In the same manner as the 128-bit input block is arranged in the form of a state array, the algorithm first arranges the 16 bytes of the encryption key in the form of a 4 × 4 array of bytes 
	- The first four bytes of the encryption key constitute the word w0 
	- The next four bytes the word w1 
	- The next four bytes the word w2 
	- The last four bytes the word w3
- The algorithm subsequently expands the words \[w0, w1, w2, w3] into a 44-word key schedule:
	- w0, w1, w2, w3, ................., w43
- The first four words w0, w1, w2, w3 are bitwise xor-ed with the input block before the round-based processing begins
- The remaining 40 words w4, …, w43 of the key schedule are used 4 words at a time in each of the 10 rounds
###### ***a lot of other things***


----
## Security of AES
So far, researchers have only uncovered theoretical breaks and side channel attacks

- some attacks

## Summary