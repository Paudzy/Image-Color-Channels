import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def linecutColumn(file, col):
    
    # Extract pixels of line cut
    img = Image.open(file)
    M = np.asarray(img)
    linecut = M[:,col]
    aspect_ratio = np.shape(M)[1]/np.shape(M)[0]
    
    # Plot image
    plt.figure(figsize=(18, 18*aspect_ratio))
    plt.tight_layout()
    
    # Plot color channels for full image
    plt.subplot(421)
    plt.imshow(M)
    plt.axvline(x=col, color='white', ls='--', alpha=0.2)
    plt.title('Raw Image')
    plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    
    plt.subplot(423)
    plt.imshow(M[:, :, 0], cmap='Greens', vmin=0, vmax=255)
    plt.axvline(x=col, color='black', ls='--', alpha=0.2)
    plt.title("Red Channel")
    plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    
    plt.subplot(425)
    plt.imshow(M[:, :, 1], cmap='Blues', vmin=0, vmax=255)
    plt.axvline(x=col, color='black', ls='--', alpha=0.2)
    plt.title("Green Channel")
    plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    
    plt.subplot(427)
    plt.imshow(M[:, :, 2], cmap='Reds', vmin=0, vmax=255)
    plt.axvline(x=col, color='black', ls='--', alpha=0.2)
    plt.title("Blue Channel")
    plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    
    # Extract color channels for linecut
    
    pixels = np.arange(0, len(np.asarray(img)[:,col]))
    
    red = [linecut[i][0] for i in range(len(pixels))]
    
    green = [linecut[i][1] for i in range(len(pixels))]
    
    blue = [linecut[i][2] for i in range(len(pixels))]
    
    # Plot line cuts
    plt.subplot(422)
    plt.plot(green, pixels, color='green', lw=1)
    plt.plot(blue, pixels, color='blue', lw=1)
    plt.plot(red, pixels, color='red', lw=1)
    plt.xlabel('Intensity')
    plt.ylabel('Column Pixel')
    plt.xlim(-25,275)
    plt.gca().invert_yaxis()
    plt.gca().set_box_aspect(1/aspect_ratio)
    plt.grid()
    
    plt.subplot(424)
    plt.plot(green, pixels, color='green')
    plt.xlabel('Intensity')
    plt.ylabel('Column Pixel')
    plt.xlim(-25,275)
    plt.gca().invert_yaxis()
    plt.gca().set_box_aspect(1/aspect_ratio)
    plt.grid()
    
    plt.subplot(426)
    plt.plot(blue, pixels, color='blue')
    plt.xlabel('Intensity')
    plt.ylabel('Column Pixel')
    plt.xlim(-25,275)
    plt.gca().invert_yaxis()
    plt.gca().set_box_aspect(1/aspect_ratio)
    plt.grid()
    
    plt.subplot(428)
    plt.plot(red, pixels, color='red')
    plt.xlabel('Intensity')
    plt.ylabel('Column Pixel')
    plt.xlim(-25,275)
    plt.gca().invert_yaxis()
    plt.gca().set_box_aspect(1/aspect_ratio)
    plt.grid()
    
    plt.show()