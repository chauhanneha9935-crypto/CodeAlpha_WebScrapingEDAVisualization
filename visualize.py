import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize_data():
    # Get base project directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Input cleaned file path
    input_path = os.path.join(base_dir, "data", "processed", "quotes_cleaned.csv")

    # Output folder path
    output_folder = os.path.join(base_dir, "outputs", "figures")
    os.makedirs(output_folder, exist_ok=True)

    # Output image path
    output_path = os.path.join(output_folder, "top_authors.png")

    # Read cleaned data
    df = pd.read_csv(input_path)

    # Count top 10 authors
    author_counts = df['author'].value_counts().head(10)

    # Create bar chart
    plt.figure()
    author_counts.plot(kind='bar')
    plt.title("Top 10 Authors by Quote Count")
    plt.xlabel("Author")
    plt.ylabel("Number of Quotes")
    plt.tight_layout()

    # Save figure
    plt.savefig(output_path)
    plt.show()

    print(f"\nVisualization saved at:\n{output_path}")


if __name__ == "__main__":
    visualize_data()