This is a python example that displays the color tone of a text. The process of transforming text to color works as follows:

1. Use Google search API to search images using the text as the query.
2. Obtain from the search thumbnails (6 by default) of the text.
3. Use KNN (K nearest neighbors) algorithm on the thumnails to get colors (3 by default) that best represent the pixel concatenation.
4. Display the colors (called collectively as color tone) using matplotlib.

Python Library Dependencies: opencv(cv2), requests
Built @ May 2018