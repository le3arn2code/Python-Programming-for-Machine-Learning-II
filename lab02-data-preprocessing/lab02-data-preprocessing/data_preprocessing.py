import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def main():
    # 1) Load dataset
    url = "iris.csv"  # keep in same folder
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
    df = pd.read_csv(url, header=None, names=column_names)
    print("=== Head ===")
    print(df.head())

    # 2) Simulate and handle missing values
    # Simulate
    df.loc[2, "sepal_length"] = None
    df.loc[5, "petal_width"] = None
    print("\n=== Dataset with missing values (sample) ===")
    print(df.loc[[0,1,2,3,4,5]])  # show a small slice incl. the NaNs

    # Handle: fill with mean (DataFrame-level to avoid FutureWarning on Series inplace)
    df.fillna({
        "sepal_length": df["sepal_length"].mean(),
        "petal_width": df["petal_width"].mean()
    }, inplace=True)

    print("\n=== After handling missing values (sample) ===")
    print(df.loc[[0,1,2,3,4,5]])

    # 3) Normalize numerical data (Min-Max 0..1)
    numerical_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    scaler = MinMaxScaler()
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    print("\n=== After normalization (head) ===")
    print(df.head())

    # 4) Split dataset into train/test
    X = df[numerical_columns]
    y = df["class"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print("\nTraining data shape:", X_train.shape)
    print("Testing data shape:", X_test.shape)

if __name__ == "__main__":
    main()