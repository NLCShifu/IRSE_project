from data import dataset

# main entry point for the application
if __name__ == "__main__":
    print("Hello world!")
    print(f"Loaded dataset with {len(dataset)} records.")
    print(f"First record: {dataset[0]}")
    print("One document:")
    for example in dataset:
        for k,v in example.items():
            print(f"'{k}' = {v}\n")
        break
