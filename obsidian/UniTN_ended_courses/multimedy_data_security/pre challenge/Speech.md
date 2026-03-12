Circa 2 minuti

## Titolo
this is the presentation on the work made by the ecorp team, 
## Paper Implementation
At the very start of the work we were a little lost, until we found the paper named “Robust Digital Image Watermarking Based on Joint DWT-DCT” by Saeed Kasmani, on which we based our implementation strategy.

the paper decompose a little logo/image in 1024 bits and embed an image with that watermark using, **precisely**, joint DWT-DCT. In our case the the watermark wast already 1024 bits so it instantly sound nice for our work.

In particular we had follow 4 steps to implement the watermark in the challenge's image

We start the implementation by applying a **three-level DWT** to the image.  
This allows us to separate the information into different frequency bands.  
we choose the HL and LH sub-bands from levels 2 and 3, since they correspond to mid-frequency regions: they are **not very visible** and quite enough stable.

Each selected sub-band is divided into 4×4 blocks, and a DCT is applied to each block.  
we then use only **seven mid-band coefficients**, the optimal frequencies for embedding the watermark without introducing visible artifacts.

Each block is associated with one bit of the watermark.  
**Two pseudorandom sequences, one for 0 and one for 1** are added to the selected **DCT coefficients** with a scaling factor α, so each block carries an imperceptible signal that, taken together, encodes the entire watermark.

Finally, **I place the modified sub-bands back into the wavelet domain** and apply the inverse DWT, obtaining an image visually identical to the original but containing 1024 bits spread across the DWT–DCT domain.

At the and of this implementation we found that the implementation work well but every implemented image score a  wpsnr around 57 db, and modifying it to obtain a wpsnr of 58 db make the implementation weaker and softer. It dosen't match our hope. So we decide to change our goal.

## Embedding Improvement 
The new goal became:
obtain the most robust watermark embedding possible, maintaining a WPSNR above 54 dB. we decide to trade 1 of our secure points on order to obtain a more robust watermark.

First, instead of using a fixed embedding strength, we used an **adaptive α for each block**, based on the local texture.  

tagliabile
*This means that in detailed areas the watermark is stronger, and in smooth areas it’s weaker, so it stays less visible.*

Then, we added a **block equalization step**, which normalizes each block by its local variance.  
This helps keep the watermark effect more uniform across the image, even if the contrast changes.

**we also used an HVS weighting mask on the DCT coefficients**, so the embedding follows the human visual system  

tagliabile
stronger where the eye is less sensitive and weaker where it’s more sensitive.

Finally, we implement an **automatic κ tuning**, which adjusts the overall strength until the watermarked image reaches the target visual quality, measured with WPSNR.

Together, these changes make the watermark more invisible, more consistent, and automatically adapted to each image.