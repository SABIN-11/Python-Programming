import cv2
import numpy as np

# Define two red color ranges in HSV
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create a black canvas for painting
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for mirror view
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create two masks and combine them
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour
        largest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest) > 1000:
            (x, y), radius = cv2.minEnclosingCircle(largest)
            center = (int(x), int(y))

            # Draw on frame and canvas
            cv2.circle(frame, center, 10, (0, 0, 255), -1)  # Red dot on frame
            cv2.circle(canvas, center, 10, (0, 0, 255), -1)  # Red dot on canvas

    # Combine camera frame and canvas
    combined = cv2.add(frame, canvas)

    # Show the results
    cv2.imshow("Virtual Painter (Red)", combined)
    cv2.imshow("Mask (Red Detection)", mask)

    key = cv2.waitKey(1)
    if key == ord('c'):
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
