# Read binary frames from file
with open("binary_frames.txt", 'r') as f:
    binary_frames = f.readlines()

# Convert binary frames to arrays of arrays
c_style_arrays = []
for binary_frame_index, binary_frame in enumerate(binary_frames):
    binary_frame = binary_frame.strip()
    array = []
    for i in range(18):
        row = []
        for j in range(20):
            row.append(int(binary_frame[i * 20 + j]))
        array.append(row)
    c_style_arrays.append(array)

# Write arrays to output assembly file
with open("frames.asm", 'w') as f:
    f.write("frames:\n")

    for array_index, array in enumerate(c_style_arrays):
        for row_index, row in enumerate(array):
            f.write("    .db ")
            for i, value in enumerate(row):
                f.write(str(value))
                if i < 19:
                    f.write(",")
            f.write("\n")
        if array_index < len(c_style_arrays) - 1:
            f.write("\n")
