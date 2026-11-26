
import numpy as np

print("NumPy version:", np.__version__)

# ================= TASK 1 =================
print("\n=== Task 1 ===")

# 1a
temps = np.array([31, 28, 35, 30, 33, 29, 36])
print("Temperatures:", temps)
print("Data type:", temps.dtype)
print("Shape:", temps.shape)
print("Size:", temps.size)

# 1b
months = np.arange(1, 13).reshape(3, 4)
print("Months:\n", months)
print("Months shape:", months.shape)

# 1c
print("Five zeros:", np.zeros(5))
print("2 x 3 ones:\n", np.ones((2, 3)))

# 1d
rng = np.random.default_rng(42)
dice = rng.integers(1, 7, size=10)
print("Dice rolls:", dice)


# ================= TASK 2 =================
print("\n=== Task 2 ===")

# 2a
print("First temperature:", temps[0])
print("Last temperature:", temps[-1])

# 2b
print("Weekend temperatures:", temps[-2:])

# 2c
print("Reverse temperatures:", temps[::-1])

# 2d
hot_days = temps[temps > 32]
print("Hot days:", hot_days)
print("Number of hot days:", hot_days.size)
print("Average of hot days:", hot_days.mean())

# 2e
selected_temps = temps[(temps >= 29) & (temps <= 33)]
print("Temperatures from 29 to 33:", selected_temps)

# 2f
day_labels = np.where(temps >= 33, "Hot", "OK")
print("Day labels:", day_labels)


# ================= TASK 3 =================
print("\n=== Task 3 ===")

names = np.array(["Ali", "Sara", "Usman", "Hina", "Bilal"])

marks = np.array([
    [78, 85, 62, 90],
    [92, 88, 95, 79],
    [45, 60, 48, 70],
    [88, 94, 91, 85],
    [65, 42, 75, 58]
])

# 3a
print("Marks shape:", marks.shape)

# 3b
print("Usman's marks:", marks[2])
print("Subject 3 marks:", marks[:, 2])

# 3c
subject_averages = np.mean(marks, axis=0)
student_averages = np.mean(marks, axis=1)

print("Average of each subject:", subject_averages)
print("Average of each student:", student_averages)

# 3d
best_student_index = np.argmax(student_averages)
print("Student with highest average:", names[best_student_index])

# 3e
weights = np.array([0.3, 0.3, 0.2, 0.2])
weighted_totals = np.sum(marks * weights, axis=1)
print("Weighted totals:", np.round(weighted_totals, 1))

# 3f
new_marks = np.clip(marks + 5, 0, 100)
print("New marks after grace marks:\n", new_marks)

# 3g
failed_counts = np.sum(marks < 50, axis=0)
print("Failed students in each subject:", failed_counts)


# ================= TASK 4 =================
print("\n=== Task 4 ===")

img = np.array([
    [10, 10, 200, 10, 10],
    [10, 10, 220, 10, 10],
    [210, 230, 250, 230, 210],
    [10, 10, 220, 10, 10],
    [10, 10, 200, 10, 10]
])

# 4a
print("Image shape:", img.shape)
print("Darkest value:", img.min())
print("Brightest value:", img.max())

# 4b
inverted_img = 255 - img
print("Inverted image:\n", inverted_img)

# 4c
black_white_img = (img > 128).astype(int)
print("Black-and-white image:\n", black_white_img)

# 4d
normalized_row = np.round(img[2] / 255, 2)
print("Normalized row 2:", normalized_row)

# 4e
centre = img[1:4, 1:4]
print("Centre 3 x 3:\n", centre)
