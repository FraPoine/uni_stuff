- OpenCV
- b, g, r = cv2.split(input_image)
- merged = cv2.merge([r, g, b])

## RGB Color Space

RGB color space has *3* color channels: Red, Green, Blue.

The RGB color space is the most common one, as used by many (or all) camera devices during the camera acquisition process.

Specifically, RGB is a consequence of the Color Filter Array (CFA). This latter implement a *Bayer filter*, place over the sensor, aimed at capturing red, green and blue light (all characterized by different wavelength). Filters devoted at capturing green light are twice as many as red and blue.

*WHY?*

1. dont use rgb for watermark
2. if used use the best layer


### Convert into YCbCr color space

focus always in the channel in which u have more information
color redundancy is a thing 
more easy to hide a watermark in the less color redundancy image


some simple extracting color component


## Masking Operations
most important thing is that it need to be converted in a matrix so u can play with indexes

Crop and slice

image composition

localize an attack is better to try to do it globally


size of the watermark [|x|024]

other operation
## Rotation, Flip and Basic Operations

there are some thing that u might want to touch 


## Edge Dection

For a lot of time "modern" computer vision techniques were based on edge detection functions as a building block. Much edge detection actually works by **convolution**, and indeed **convolutional neural networks** are absolutely the flavour of the month in some parts of computer vision. Sobel's edge detector was one of the first truly successful edge detection (enhancement) technique and that involves convolution at its core. You can read more about the background to Sobel here in the OpenCV docs [here](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_gradients/py_gradients.html).

Edge Detection techniques permit to detect and spot suitable position to embed your watermark. As we will learn, edges often corresponds to textures, textures corresponds to high frequencies and... high frequencies to .

if u have higher variability its easier to hide because with lower is easier to noted if something change

### Canny Edge Detection

in this case u dont want just to find an edge but to find something in the edge

---
# Image processing
In this section we see the image processings you are allowed to use for the challenge!

## AWGN
AWGN (Additive White Gaussian Noise), as the name suggests, is used to add a normally distributed noise to a signal, in our case an image.

the std can destroy the image

## Blurring through GAUSSIAN FILTER

The Gaussian Filter is used to "remove" or attenute high-frequencies information contained in images related to textures and noise like AWGN.

The filter applies a Gaussian function to image (or single image channel/components) weighting the values of neighboring pixels based on their distance from the central point (more weight to nearby points and less weight to distant points).

Basically, it smooth your image.

![gaussian_filter.gif](attachment:gaussian_filter.gif)

When could it be useful in your watermarking challenge? (TAKE NOTE)
set parameter is important because u can destroy the watermark 

The standard deviations (sigma) of the Gaussian filter, which affects the strenght of the filter, can be an integer or a list of two integers. [check this](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html)

## Sharpening
The sharpening filter is the inverse of blurring. It is used to enhance details in an image by exaggerating the brightness difference along edges within an image.

still gautian filter

## Median filtering

The median filter is a digital filtering technique often used to remove noise from an image PRESERVING EDGES. It is very effective on salt and pepper noise while is less effective on others. It use convolutional operations similar to the Gaussian Filter (blur), but implement a different kernel. Also useful during edge detection operation.

is something that we would like to use

all this filter we can applied it to filters and that are more effective

## RESIZING
Resizing is a common operation that can be performed on images.

When an image is downscaled and then upscaled, some information will be lost (similarly to low-pass filtering but avoiding blurring effects) as the final image willcontain less pixels.

In fact, when upscaled the values of the new pixels are estimated using interpolation.

weakest watermarking tecnique

## JPEG Compression
one of the most powerful legal technique 

Images require a lot of bandwidth and storage capacity. Compression is aimed at reducing the amount of data to be transmitted. One of the main standards is JPEG.

The JPEG is a lossy scheme, i.e. some information is lost during the process.

By increasing the compression rate, artifacts appear: blocking, blurring, chromatic aberrations.

In Python we can specify the Quality Factor (QF $\in$ [0, 100]$). They lower the QF the higher the compression rate.

first split the image and then do something 
pretty power 
there is a quatization
encoding
and something

during all operation we have an image in which with every operation we lost information that we are no more able to recover.
is not possible to work backword 

this for sure is needed to be applied globally


----
# TRANSFORM DOMAIN

Details in images are generally found in
* high frequencies
* very rapid alterations of dark and brigh areas
One of the possibilities to determine how much detail we want in a picture is to change the domain of analysis.

To move from the spatial domain (pixels) to the frequency domain we use **transforms**.

A transform is a class of unary matrices that are used to represent signals
* A 1-D signal can be expressed as the combination of a number of orthonormal basis functions  
* A 2-D signal can be expressed as the combination of a number of basis matrices called basis images

we will just work with the rgb domain

u have frequencies in the space domain 

## Fourier Transform
u have the dc transformer 

transform = np.fft.fftshift(np.fft.fft2(im)) --> for put the watermark in the center of the corner 

do not touch the bright area

## Inverse FFT
it became very useful 
it might be that our group use a redundant something 


# Discrete Cosine Transform DCT
JPEG compression

compress an image into a series of sin and cos
its good for data optimization and prcession

how am i suppose to use it?

bright area on top, dont touch the light, u can touch the rest.

embed the watermark in a specific region

## Inverse DCT
u can always come back to the base image

finally

# Wavelet transform

high and low frequencies

## Wavelet decomposition

its good for redundancy, u can adding some redundancy to the watermark 

more time u embed ur watermark less invisible it became


---
## TRANSFORM DOMAIN
### Fourier Transform FFT
- La **Trasformata di Fourier** scompone un segnale (spaziale o temporale) nelle sue **componenti di frequenza**.
- Nel contesto delle immagini, mostra “quanto” di ciascuna frequenza è presente.
	`transform = np.fft.fftshift(np.fft.fft2(im))`

### Inverse FFT
```
transform = (np.fft.fft2(im))

plt.imshow(np.real(np.fft.ifft2(transform)), 'gray')
```
- Serve per **ricostruire l’immagine originale** a partire dallo spettro di Fourier.

### Discrete Cosine Transform DCT
La **Trasformata Discreta del Coseno** rappresenta un segnale come somma di funzioni **coseno** (e non seno).
Vantaggi:
- È **reale e ortogonale**, quindi la matrice inversa è semplicemente la trasposta.
- È **efficiente e veloce** da calcolare.
- **Concentra l’energia** nelle prime componenti: la maggior parte dell’informazione è nelle basse frequenze.
- Utile anche per **watermarking** (inserimento o estrazione di segnali nascosti).
- È alla base di **quasi tutte le tecnologie di compressione multimediale moderne**.

### Inverse DCT
```
idct2 = np.uint8(idct(idct(transform,axis=1, norm='ortho'),axis=0, norm='ortho'))

plt.imshow(idct2, 'gray')
```

# Wavelet transform
- Può essere **continua** o **discreta.** Per le immagini usiamo tipicamente la discreta. La **Discreta walvet Transform (DWT)**, that use different filters to analyze the signal at different levels.
	* high-pass filters to analyse high frequencies
	* low-pass filters to analyse low frequencies
```
import pywt
coeffs2 = pywt.dwt2(im, 'haar')
LL, (LH, HL, HH) = coeffs2

# Show components
blank_image = np.zeros((512,512), np.float32)
blank_image[:256, :256] = LL
blank_image[:256, 256:] = LH
blank_image[256:, :256] = HL
blank_image[256:, 256:] = HH

plt.imshow(blank_image, 'gray')
```

### Inverse DWT
```
IDWT = pywt.idwt2((LL, (LH, HL, HH)), 'haar')
plt.imshow(IDWT, 'gray')
```

#### Something curios like Giorge
DWT allows to further decompose the DC component. You can exploit this to "play" some sort "matrioska" game to hide your watermark.

```
import pywt
coeffs2_2 = pywt.dwt2(LL, 'haar')
LL2, (LH2, HL2, HH2) = coeffs2_2

blank_image = np.zeros((512,512), np.float32)
blank_image[:128, :128] = LL2
blank_image[:128, 128:256] = LH2
blank_image[128:256, :128] = HL2
blank_image[128:256, 128:256] = HH2
blank_image[:256, 256:] = LH
blank_image[256:, :256] = HL
blank_image[256:, 256:] = HH

# Show components
plt.imshow(blank_image, 'gray')
```