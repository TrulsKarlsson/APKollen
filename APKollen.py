# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data retrieval
url1 = "https://raw.githubusercontent.com/AlexGustafsson/systembolaget-api-data/main/data/assortment.json"
url2 = "https://raw.githubusercontent.com/AlexGustafsson/systembolaget-api-data/main/data/stores.json"

assortment = pd.read_json(url1)
stores = pd.read_json(url2)

# Feature selection
feature_names = [
    'alcoholPercentage', 
    'price', 
    'isTemporaryOutOfStock', 
    'bottleText', 
    'images',
    'producerName',
    'volumeText',
    'productNameBold'
]

# Filter the DataFrame to include only the relevant columns
df = assortment[feature_names].copy()
df = df[df['alcoholPercentage'] != 0]
df.loc[:, 'alcoholPerSEK'] = df['alcoholPercentage'] / df['price']
df.loc[:, 'sekPerAlcohol'] = df['price'] / df['alcoholPercentage']

# Sort the DataFrame by alcohol per SEK and SEK per alcohol
# The first sort is in descending order (best value first), and the second is in ascending order (cheapest first)
df_sorted = df.sort_values(by=['alcoholPerSEK', 'sekPerAlcohol'], ascending=[False, True])

# Plot
#plt.figure(figsize=(10, 8))
#plt.barh(df_n['productNameBold'], df_n['alcoholPerSEK'])
#plt.xlabel('Alcohol per SEK')
#plt.title('Best Value Alcohol Products')
#plt.gca().invert_yaxis()  # Highest value at top
#plt.tight_layout()
#plt.show()

def get_product_info(product_name):
    """
    Function to get product information based on the product name.
    """
    product_info = df[df['productNameBold'] == product_name]
    if not product_info.empty:
        return product_info.iloc[0]
    else:
        return None
    
# Main menu

def list_top_n_products():
    n = int(input("Enter the number of top products to display: "))
    print(f"\nTop {n} Best Value Alcohol Products (based on alcohol per SEK):\n")
    df_n = df_sorted.head(n)
    for i, row in df_n.iterrows():
        print(f"Item: {row['productNameBold']}\n")
        print(f"      Price: {row['price']} SEK")
        print(f"      Alcohol: {row['alcoholPercentage']}%")
        print(f"      Alcohol per SEK: {row['alcoholPerSEK']}")
        print(f"      SEK per alcohol: {row['sekPerAlcohol']}")
        print(f"      Size: {row['volumeText']}")
        print(f"      Out of stock: {row['isTemporaryOutOfStock']}\n")

def search_product():
    product_name = input("Enter the product name: ")
    product_info = get_product_info(product_name)
    if product_info is not None:
        print(f"\nProduct Information for '{product_name}':\n")
        print(f"Price: {product_info['price']} SEK")
        print(f"Alcohol: {product_info['alcoholPercentage']}%")
        print(f"Alcohol per SEK: {product_info['alcoholPerSEK']}")
        print(f"SEK per alcohol: {product_info['sekPerAlcohol']}")
        print(f"Size: {product_info['volumeText']}")
        print(f"Out of stock: {product_info['isTemporaryOutOfStock']}\n")
    else:
        print("Product not found.")

def show_menu():
    print("\nMenu:")
    print("1. Show top N best value alcohol products")
    print("2. Get product information by name")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        list_top_n_products()
    
    elif choice == '2':
        search_product()
    
    elif choice == '3':
        exit()
    
    else:
        print("Invalid choice. Please try again.")

while True:
    show_menu()