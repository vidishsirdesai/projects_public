import pandas as pd

df_lift = pd.read_csv("data/subject_all/lift.csv")
df_lift["gesture_name"] = "Lift"
df_lift.to_csv("data/subject_all_labeled/lift.csv")

df_roll_left = pd.read_csv("data/subject_all/roll_left.csv")
df_roll_left["gesture_name"] = "Roll Left"
df_roll_left.to_csv("data/subject_all_labeled/roll_left.csv")

df_roll_right = pd.read_csv("data/subject_all/roll_right.csv")
df_roll_right["gesture_name"] = "Roll Right"
df_roll_right.to_csv("data/subject_all_labeled/roll_right.csv")

df_tilt_down = pd.read_csv("data/subject_all/tilt_down.csv")
df_tilt_down["gesture_name"] = "Tilt Down"
df_tilt_down.to_csv("data/subject_all_labeled/tilt_down.csv")

df_tilt_up = pd.read_csv("data/subject_all/tilt_up.csv")
df_tilt_up["gesture_name"] = "Tilt Up"
df_tilt_up.to_csv("data/subject_all_labeled/tilt_up.csv")

df_yaw_left = pd.read_csv("data/subject_all/yaw_left.csv")
df_yaw_left["gesture_name"] = "Yaw Left"
df_yaw_left.to_csv("data/subject_all_labeled/yaw_left.csv")

df_yaw_right = pd.read_csv("data/subject_all/yaw_right.csv")
df_yaw_right["gesture_name"] = "Yaw Right"
df_yaw_right.to_csv("data/subject_all_labeled/yaw_right.csv")
