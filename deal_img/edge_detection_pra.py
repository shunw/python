from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from skimage import data, io, filters, color
from skimage.filters import threshold_local
from skimage.feature import peak_local_max
from skimage.feature import canny
import skimage.color as skcolor

from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label

def get_threshold(d_array): 
    '''
    input: d_array
    output: lower & upper threshold
    '''
    # print (d_array)
    sort_d = sorted(d_array.flatten())
    
    mini = sort_d[0]
    maxima = sort_d[-1]

    max_diff = 0
    mini_mid = None

    for ind in range(1, len(sort_d)):
    
        if sort_d[ind] - sort_d[ind - 1] > max_diff: 
            max_diff = sort_d[ind] - sort_d[ind - 1]
            mini_mid = sort_d[ind - 1]
            max_mid = sort_d[ind]
    # print(mini, maxima, mini_mid, max_mid)
    # print (set((mini, maxima, mini_mid, max_mid)))
    # if len(set((mini, maxima, mini_mid, max_mid))) <= 3: 
    #     print (mini, maxima, mini_mid, max_mid)
    #     print ('only three data, something wrong with the threshold. please check')
    #     return None
    if mini_mid is None: 
        return None
    lower_threshold = mini_mid / max_mid
    upper_threshold = mini / maxima
    
    return lower_threshold, upper_threshold


class try_skimage(object):
    '''
    reference from: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4081273/
    '''
    def __init__(self, fl_name):
        self.image_coin = data.coins()
        self.fl_name = fl_name

        # convert to grey scale
        self.image = color.rgb2gray(io.imread(self.fl_name))

        
    
    def show_ini_image(self):
        self.edges = filters.sobel(self.image)
        io.imshow(self.edges)
        plt.show()

    def letter_detect_hist(self):

        values, bins = np.histogram(self.image, bins = np.arange(256))
        plt.plot(bins[:-1], values, lw = 2, c = 'k')
        plt.show()

    def letter_detect(self):
        # self.image = self.image[100: 285, 320: 570]
        self.image = self.image * 256
        
        fig, axes = plt.subplots(ncols = 2, nrows = 3)
        ax0, ax1, ax2, ax3, ax4, ax5 = axes.flat

        # small part image
        ax0.imshow(self.image, cmap = plt.cm.gray)
        ax0.set_title('Original', fontsize = 24)
        ax0.axis('off')

        # make the histogram
        values, bins = np.histogram(self.image, bins = np.arange(256))
        ax1.plot(bins[:-1], values, lw = 2, c = 'k')
        ax1.set_xlim(xmax = 256)
        ax1.set_yticks([0, 400])
        # ax1.set_aspect(.2)
        ax1.set_title('Histogram', fontsize = 24)

        # apply threshold
        bw = threshold_local(self.image, 95, offset = -15)

        ax2.imshow(bw,cmap = plt.cm.gray)
        ax2.set_title('Adaptive threshold', fontsize = 24)
        ax2.axis('off')

        # find maxima
        coordinates = peak_local_max(self.image, min_distance = 10)

        upper_threshold = 0
        lower_threshold = 1
        for ind in coordinates: 
            data_block_size = 1
            
            t = self.image[ind[0] - data_block_size:ind[0] + data_block_size + 1, ind[1] - data_block_size:ind[1] + data_block_size + 1]
            if get_threshold(t) is not None: 
                upper_threshold_temp, lower_threshold_temp = get_threshold(t)

            if upper_threshold < upper_threshold_temp: 
                upper_threshold = upper_threshold_temp
            if lower_threshold > lower_threshold_temp: 
                lower_threshold = lower_threshold_temp
        
        ax3.imshow(self.image, cmap = plt.cm.gray)
        ax3.autoscale(False)
        ax3.plot(coordinates[:, 1], coordinates[:, 0], 'r.')
        ax3.set_title('Peak local maxima', fontsize = 24)
        ax3.axis('off')

        # detect edges
        # edges = canny(self.image_part, sigma = 3, low_threshold = 10, high_threshold = 80) # original
        edges = canny(self.image, sigma = 3, low_threshold = lower_threshold *100, high_threshold = upper_threshold * 100)

        ax4.imshow(edges, cmap = plt.cm.gray)
        ax4.set_title('Edges', fontsize = 24)
        ax4.axis('off')

        # # Label image regions
        # label_image = label(edges)

        # ax5.imshow(self.image, cmap = plt.cm.gray)
        # ax5.set_title('Labeled items', fontsize = 24)
        # ax5.axis('off')

        # for region in regionprops(label_image):
        #     # Draw rectangle around segmented coins.
        #     minr, minc, maxr, maxc = region.bbox
        #     # print (minr, minc, maxr, maxc)
        #     rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill = False, edgecolor = 'red', linewidth = .5)
        #     ax5.add_patch(rect)

        plt.tight_layout()
        plt.show()



    def final_run(self):
        self.letter_detect()

if __name__ == '__main__':  
    
    fl_name = 'vivian.jpg'
    test = try_skimage(fl_name)
    # test.show_ini_image()
    test.final_run()
    
    

    '''
    reference: 
        - convert RGB -> grey scale: 
            https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python

        - circle detection example: 
            https://scikit-image.org/docs/dev/auto_examples/edges/plot_circular_elliptical_hough_transform.html#sphx-glr-auto-examples-edges-plot-circular-elliptical-hough-transform-py
    '''