# Least Significant Bit (LSB) Watermarking

IDEA: embed the watermark most significant bit (MSB) (if you use an array of N elements they are all significant) to the image pixels Less Significant Bit (LSB).

watermark size --> N = 1024 
## Quality
$PSNR = 10 \cdot log_{10} \frac{V_{max}^2}{MSE}$
#### WPSNR
However, for our challenge we are going to use the Weighted Peak Signal to Noise Ration (WPSNR), a variant of PSNR that takes into account the human visual system (HVS), more sensitive to luminance and contrast variations in certain regions. Thus, WPSNR applies weights to the different pixel locations to account for this sensitivity.
- $\text{WPSNR} = 10 \cdot \log_{10} \left( \frac{V_{max}^2}{\text{WMSE}} \right)$
where:
- $\text{WMSE} = \frac{1}{mn} \sum_{i=0}^{m-1} \sum_{j=0}^{n-1} w(i,j) \left( I(i,j) - K(i,j) \right)^2$


we need to memorize that lsb is not a good based for implement our defense, 
its difficult to detect but easy to erase 

## LSB Detection
blind tecnique
u only need the image with the watermark

## Similarity between the Extracted Watermark and the Original Watermark

This is a simple script to measure how similar the extracted watermark is with the original one.

You can use compute_thr() to estimate a threshold to detect the presence of the watermark, however, this is not how we will estimate the threshold for the challenge.

To estimate the similarity between $x$ (the watermark extracted from the watermarked image) and $x^\prime$ (the watermark extracted from the attacked watermarked image), we will use:

$sim(x,x^\prime)=\frac{x\cdot x^\prime}{||x||\cdot||x^\prime||}$

we will not use the watermark we extract from the watermarked image

day of the challenge
- we will have 
	- w --> our watermark
	- I --> N blackbox M
	- we will use our embedded technique
	- and we will have $I_w$
---
# Spread Spectrum Watermarking
Spread Spectrum Watermarking is a robust, **NON-BLIND** watermarking technique distributing the watermark's signal over a wide range of frequencies (like in spread spectrum communication techniques).

This method makes the watermark harder to detect, remove, or interfere with, which is especially useful for copyright protection, content authentication, and other security applications.
### Key Concepts:
1. Spread watermark on a broad frequency band (much larger than the one needed to embed the entire watermark);
2. Very Robust and Resilient to different types of attacks;
3. Watermark embedded spreading its energy across the frequency spectrum;
4. During the embedding the watermark can be modulated (or weighted), using $\alpha$ to improve its invisibility.

its an optimal starting point because its easy to implement and very solid

the pipeline at the image is good for implementing every frequency

important to try on high frequencies


embedded strategy is pretty useful for starting exercises 

---
# How to set the threshold using the Receiver operating characteristic (ROC) Curve

What is it?
* A graphic scheme for binary classification.

What it represent?
* On the x-axis you have the False Positive Rate (FPR)
* On the y-axis the True Positive Rate (TPR)
* Each point of the curve is associated to a possible threshold  

How do I choose the threshold?
* You can choose the threshold you prefer as a trade-off between the TPR and the FPR. However, **we will focus on FPR$<0.1$**

How can I generate the ROC?
* **To generate the ROC curve you need two arrays**: score and label
* These two arrays contains informations on the classifier positive and negative decision, respectively: H1 (similarity estimated between the same watermark) and H0 (similarity estimated between two different watermark).
* **In the score array**, goes the similarity values between the watemark extracted from the watermarked image and those extracted from the attacked one.  
* **In the label array**, goes values equals either to 1 or 0. We put 1 if the watermarks extracted from the watermarked image and the attacked image, to estimate the corresponding similarity, are the same (H1 hypothesis). Otherwise, we put 0 (H0 hyphotesis).
##### during the challenge we cant have more than 0.1 of false positive

**we need to motivate our decision** 
