import cv2

def frame_to_binary(frame):
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Resize the frame to 18x20
    resized_frame = cv2.resize(gray_frame, (20, 18))
    # Threshold the frame to get binary representation
    _, binary_frame = cv2.threshold(resized_frame, 128, 255, cv2.THRESH_BINARY)
    # Flatten the binary frame to a 1D array
    binary_data = binary_frame.flatten()
    # Convert the binary data to a string of '1's and '0's
    binary_string = ''.join('1' if pixel > 0 else '0' for pixel in binary_data)
    return binary_string

def main(video_path, output_file):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    # Open the output text file for writing
    with open(output_file, 'w') as f:
        frame_count = 0
        processed_frames = set()  # Set to store processed frames
        # Read frames from the video
        while True:
            ret, frame = cap.read()
            if not ret:
                break  # Break the loop if no more frames are available
            
            # Check if it's time to process this frame
            if frame_count % cap.get(cv2.CAP_PROP_FPS) == 0:
                # Check if the frame has been processed before
                binary_frame = frame_to_binary(frame)
                if binary_frame in processed_frames:
                    continue  # Skip this frame if it's a duplicate
                
                # Write the binary frame to the output file
                f.write(binary_frame + '\n')
                processed_frames.add(binary_frame)  # Add frame to processed frames
                
            frame_count += 1

    # Release the video capture object
    cap.release()

    print("Total frames processed:", frame_count)

if __name__ == "__main__":
    video_path = "videoplayback.mp4"  # Path to your input video file
    output_file = "binary_frames.txt"  # Path to the output text file
    main(video_path, output_file)
