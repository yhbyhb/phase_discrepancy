clear; close all;

img1 = imread('helmet_mkv_0000000000.jpg');
img2 = imread('helmet_mkv_0000000004.jpg');
Frame1 = rgb2gray(img1);
Frame2 = rgb2gray(img2);

FFT1=fft2(Frame1);
FFT2=fft2(Frame2);
Amp1=abs(FFT1);
Amp2=abs(FFT2);
Phase1=angle(FFT1);
Phase2=angle(FFT2);
mMap1=abs(ifft2((Amp2-Amp1).*exp(i*Phase1)));
mMap2=abs(ifft2((Amp2-Amp1).*exp(i*Phase2)));
mMap=mat2gray(mMap1.*mMap2);

figure, imshow(img1), title('image1');
figure, imshow(img2), title('image2');

figure, imshow(mat2gray(mMap1)), title('saliency map1');
figure, imshow(mat2gray(mMap2)), title('saliency map2');
figure, imshow(mMap), title('final saliency map');
