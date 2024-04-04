import cv2 as cv
import numpy as np
import os

def find_needle_in_haystack(haystack_path, needle_paths, threshold=0.17):
    # Load the haystack image
    haystack_img = cv.imread(haystack_path, cv.IMREAD_UNCHANGED)

    # Check if the haystack image was loaded successfully
    if haystack_img is None:
        print(f"Error: Couldn't load the haystack image from {haystack_path}")
        return

    # Iterate over each needle image
    for needle_path in needle_paths:
        # Load the needle image
        needle_img = cv.imread(needle_path, cv.IMREAD_UNCHANGED)

        # Check if the needle image was loaded successfully
        if needle_img is None:
            print(f"Error: Couldn't load the needle image from {needle_path}")
            continue

        # Perform template matching
        result = cv.matchTemplate(haystack_img, needle_img, cv.TM_SQDIFF_NORMED)

        # Find locations where the match is below the threshold
        locations = np.where(result <= threshold)
        locations = list(zip(*locations[::-1]))

        if locations:
            print(f'Found needle in {needle_path}.')

            # Get dimensions of the needle image
            needle_w = needle_img.shape[1]
            needle_h = needle_img.shape[0]
            line_color = (255, 0, 64)
            line_type = cv.LINE_4

            # Loop over all the locations and draw rectangles
            for loc in locations:
                # Determine the box positions
                top_left = loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
                # Draw the box
                cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

    # Resize the output image
    resized_img = cv.resize(haystack_img, (800, 600))

    cv.imshow('Matches_Output', resized_img)
    cv.waitKey()

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Paths to haystack and needle images
# haystack_path = 'albion_farm.jpg'
haystack_path = 'Aibooster.jpg'
# needle_paths = ['albion_ilist_1.jpg', 'albion_ilist_2.jpg', 'albion_ilist_3.jpg']
needle_paths = ['Aim1.jpg', 'Aim2.jpg', 'Aim3.jpg']

# Call the function to find the needles in the haystack
find_needle_in_haystack(haystack_path, needle_paths)
