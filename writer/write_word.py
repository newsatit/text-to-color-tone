'''
Defines a function that a file that contains the color tone
of the information of a given word.
'''

from process.get_color_tone import get_clusters_from_text
# Note that the centroid histogram function just creates an
# np.array with values corresponding to the % of the appearance
# of that color
from process.plot_utils import centroid_histogram

def print_info(text, folderpath='./assets/info/') :
    '''
    Print the detailed color tone information of the
    text to two seperate files in assets/info.
    '''
    # Get the centers of the cluster
    clusters = get_clusters_from_text(text)
    centers = clusters.cluster_centers_