from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('models/best.pt')

# Run the prediction on the video and save the results
results = model.predict('input_videos/08fd33_4.mp4', save=True)

# Print the first result
print(results[0])
print('======================================')
for box in results[0].boxes:
    print(box)
    