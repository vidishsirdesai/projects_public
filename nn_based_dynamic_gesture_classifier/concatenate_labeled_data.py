import pandas as pd

df_lift = pd.read_csv("data/subject_all_labeled/lift.csv")
df_roll_left = pd.read_csv("data/subject_all_labeled/roll_left.csv")
df_roll_right = pd.read_csv("data/subject_all_labeled/roll_right.csv")
df_tilt_down = pd.read_csv("data/subject_all_labeled/tilt_down.csv")
df_tilt_up = pd.read_csv("data/subject_all_labeled/tilt_up.csv")
df_yaw_left = pd.read_csv("data/subject_all_labeled/yaw_left.csv")
df_yaw_right = pd.read_csv("data/subject_all_labeled/yaw_right.csv")

df = pd.concat([df_lift, df_roll_left, df_roll_right, df_tilt_down, df_tilt_up, df_yaw_left, df_yaw_right])

df.to_csv("data/final.csv")
