# import cv2
# import mediapipe as mp
# import time 
# from mediapipe.tasks.python import vision


# mpDraw = mp.solutions.drawing_utils
# mpPose = mp.solutions.pose
# pose = mpPose.Pose()

# vidfile = "C:/Users/Monter/Projects/squashai/Videos/squash_vide_raw_1.MP4"
# cap = cv2.VideoCapture(vidfile)
# pTime = 0


# while True:
#     success, img = cap.read()
#     results = pose.process(img)
#     print(results.pose_landmarks)

#     if results.pose_landmarks:
#         mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)


#     cTime = time.time()
#     fps = 1/(cTime-pTime)
#     pTime = cTime
    
#     cv2.putText(img, str(int(fps)), (78,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

#     cv2.imshow("Image", img)
#     cv2.waitKey(10)





import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose

# Initialize pose model with multi-person mode enabled
pose = mpPose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    model_complexity=1,  # Model complexity: 0, 1, or 2
    enable_segmentation=True  # Whether to enable person segmentation
)

vidfile = "C:/Users/Monter/Projects/squashai/Videos/IMG_5411.MP4"
cap = cv2.VideoCapture(vidfile)
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        break
    
    # Flip the image horizontally for a more intuitive view
    img = cv2.flip(img, 1)
    
    # Convert the BGR image to RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Detect poses in the image
    results = pose.process(rgb_img)

    if results.pose_landmarks:
        # Draw landmarks and connections for each detected pose
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    # Calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display FPS
    cv2.putText(img, f"FPS: {int(fps)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display image
    cv2.imshow("Image", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
