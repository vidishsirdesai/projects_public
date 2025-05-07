import pandas as pd

all_dfs = []

for number in range(1, 7):
    file_path = f"data/subject_{number}/lift.csv"

    df = pd.read_csv(file_path)

    df["subject"] = str(number)

    all_dfs.append(df)


df = pd.concat(all_dfs)
df.to_csv("data/subject_all/lift.csv")

all_dfs = []

for number in range(1, 7):
    file_path = f"data/subject_{number}/roll_left.csv"

    df = pd.read_csv(file_path)

    df["subject"] = str(number)

    all_dfs.append(df)


df = pd.concat(all_dfs)
df.to_csv("data/subject_all/roll_left.csv")

all_dfs = []

for number in range(1, 7):
    file_path = f"data/subject_{number}/roll_right.csv"

    df = pd.read_csv(file_path)

    df["subject"] = str(number)

    all_dfs.append(df)


df = pd.concat(all_dfs)
df.to_csv("data/subject_all/roll_right.csv")

all_dfs = []

for number in range(1, 7):
    file_path = f"data/subject_{number}/tilt_down.csv"

    df = pd.read_csv(file_path)

    df["subject"] = str(number)

    all_dfs.append(df)


df = pd.concat(all_dfs)
df.to_csv("data/subject_all/tilt_down.csv")

all_dfs = []

for number in range(1, 7):
    file_path = f"data/subject_{number}/tilt_up.csv"

    df = pd.read_csv(file_path)

    df["subject"] = str(number)

    all_dfs.append(df)


df = pd.concat(all_dfs)
df.to_csv("data/subject_all/tilt_up.csv")

all_dfs = []

for number in range(1, 7):
    file_path = f"data/subject_{number}/yaw_left.csv"

    df = pd.read_csv(file_path)

    df["subject"] = str(number)

    all_dfs.append(df)


df = pd.concat(all_dfs)
df.to_csv("data/subject_all/yaw_left.csv")

all_dfs = []

for number in range(1, 7):
    file_path = f"data/subject_{number}/yaw_right.csv"

    df = pd.read_csv(file_path)

    df["subject"] = str(number)

    all_dfs.append(df)


df = pd.concat(all_dfs)
df.to_csv("data/subject_all/yaw_right.csv")
