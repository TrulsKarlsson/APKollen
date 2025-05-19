# 🥂 APKollen – Find the Best Value at Systembolaget

**APKollen** is a Python-based tool that helps you discover which alcoholic beverages at [Systembolaget](https://www.systembolaget.se/) offer the best value based on **alcohol per SEK (APK)**.  
It fetches real-time product data from the [Systembolaget API Data Mirror](https://github.com/AlexGustafsson/systembolaget-api-data) and lets you explore, rank, and analyze products interactively.

---

## 🚀 Features

- 💰 **Top value ranking**: Sort products by alcohol content per krona (APK)
- 🔎 **Search**: Look up product details by name
- 📊 **Visualizations** *(coming soon)*: Bar and scatter plots to compare prices, alcohol %, and APK
- ✅ Filters out non-alcoholic products and handles edge cases

---

## 🧪 Example

```
Top 5 Best Value Alcohol Products:

Item: Fernet-Branca

      Price: 59.0 SEK
      Alcohol: 39.0%
      Alcohol per SEK: 0.6610169491525424
      SEK per alcohol: 1.5128205128205128
      Size: 3 fl à 20 ml
      Out of stock: False

Item: Arboga 7,3

      Price: 13.5 SEK
      Alcohol: 7.3%
      Alcohol per SEK: 0.5407407407407407
      SEK per alcohol: 1.8493150684931507
      Size: 330 ml
      Out of stock: False

...
```

# 📦 Installation
## 1. Clone the repo
```
git clone https://github.com/yourusername/APKollen.git
cd APKollen
```

## 2. Install dependencies
Make sure you have Python 3 and pip installed. Then run:
```
pip install pandas matplotlib
```

# ▶️ Usage
Run the program using:
```
python3 APKollen.py
```

# 📊 Data Source
APKollen uses live data from Alex Gustafsson’s Systembolaget data mirror, which provides regular JSON snapshots of the official Systembolaget assortment and store database. Link: https://github.com/alexgustafsson/systembolaget-api-data

## 📌 To-Do

- [ ] Add filtering by beverage category (e.g., beer, wine, spirits)
- [ ] Visual charts (bar chart, scatter plot)
- [ ] Add option to export results to CSV
- [ ] Build an interactive web version

---

## 🧑‍💻 Author

Created by **Truls Karlsson**  
[LinkedIn](https://www.linkedin.com/in/trulskarlsson/) • [GitHub](https://github.com/trulskarlsson)

---

## 📄 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it — contributions are welcome!
