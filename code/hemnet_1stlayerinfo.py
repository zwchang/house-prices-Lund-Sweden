# This script scrapes first-layer info (features directly from body tag)
# as domostrated in the hemnet_1stLayerinfo_demo.ipynb

# Import necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import glob
import re

# Generate CSV file for each downloaded Hemnet page (50 in total)

for p in range(50):

    page = "hemnet_page" + str(p + 1) + ".html"
    with open(page, "r") as html_file:
        soup = BeautifulSoup(html_file, "html.parser")
    body = soup.find("body")

    # links
    link_info = body.select("li.sold-results__normal-hit a")
    links = [link["href"] for link in link_info]

    # addresses
    str_addresses = body.select("li.sold-results__normal-hit h2")
    addresses = [
        address.get_text().replace("\n", "").strip() for address in str_addresses
    ]

    # building type
    str_types = body.select("li.sold-results__normal-hit title")
    types = [type.get_text() for type in str_types]

    # 3 pieces of info: living area, # of rooms, and sold price embedded
    info_3piece = body.select("div.sold-property-listing__subheading")
    info = [
        item.get_text().replace("\n", "").replace("\xa0", "").strip()
        for item in info_3piece
    ]

    # Apparently there's some exceptions for "area" which gives None value. These elements
    # all have the room type as "Gård/Skog".

    # area
    area = [None for _ in range(50)]
    for i in range(len(info) // 2):
        n = re.search(r"(.*?)m²", info[2 * i])
        if n:
            area[i] = n.group(1).replace("                                 ", "")

    # price and room count
    prices = [0 for _ in range(50)]
    number_of_rooms = [None for _ in range(50)]
    for i in range(len(info) // 2):
        prices[i] = int(
            int(re.search(r"Slutpris(.*?)kr", info[2 * i + 1]).group(1)) / 1000
        )
        m = re.search(r"m²                          (.*?)rum", info[2 * i])
        if m:
            number_of_rooms[i] = float(m.group(1).replace(",", ".").strip())

    # sold dates
    dates = body.select("div.sold-property-listing__sold-date")
    sold_date = [
        date.get_text().replace("\n", "").replace("Såld", "").strip() for date in dates
    ]

    # There are also 3 pieces info embeded in the div class=sold-property-listing__size
    # which we only need the monthly fees (avgift)
    sizes = body.select("div.sold-property-listing__size")
    size_and_avgift = [
        size.get_text().replace("\n", "").replace("\xa0", "").strip() for size in sizes
    ]

    avgift = [None for _ in range(50)]
    for i in range(len(size_and_avgift)):
        n = re.search(r"rum        (.*?)kr/mån", size_and_avgift[i])
        if n:
            avgift[i] = int(n.group(1).strip())

    # create data frame
    d = {
        "Addresses": addresses,
        "Types": types,
        "Area": area,
        "RoomCount": number_of_rooms,
        "Avgift": avgift,
        "SoldDate": sold_date,
        "Links": links,
        "Prices": prices,
    }

    df = pd.DataFrame(data=d)

    # Merge into one CSV file
    filename = "hemnet" + str(p + 1) + ".csv"
    df.to_csv(filename, index=False)

# Merge 50 csv files into one

# filenames = [str(f"hemnet{i}.csv") for i in range(1, 51)]
filenames = glob.glob("*.csv")

li = []

for filename in filenames:
    df_page = pd.read_csv(filename, index_col=None, header=0)
    li.append(df_page)

df_temp = pd.concat(li, axis=0, ignore_index=True)
df_temp.to_csv("hemnet_withLinks.csv", index=False)


# Generate csv file with housing type == apartment

df_apartment = df_temp[df_temp["Types"] == "Lägenhet"]
df_apartment = df_apartment.drop(columns=["Types"])
df_apartment.to_csv("apartment_withLinks.csv", index=False)
