# This script scrapes features embedded in the individual links
# as domostrated in the hemnet_2ndLayerfeature__demo.ipynb

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Specify header to pass the robot detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0"
}

# df = pd.read_csv("apartment_withLinks.csv") this is a little bit wierd, got figure out how I generated the apart_df.csv previously.
df = pd.read_csv("apart_df.csv")

# Extract 2nd layer info
link_len = len(df["Links"])

feature_0 = [None for _ in range(link_len)]
feature_1 = [None for _ in range(link_len)]
feature_2 = [None for _ in range(link_len)]
feature_3 = [None for _ in range(link_len)]
feature_4 = [None for _ in range(link_len)]
feature_5 = [None for _ in range(link_len)]
feature_6 = [None for _ in range(link_len)]
feature_7 = [None for _ in range(link_len)]
feature_8 = [None for _ in range(link_len)]
feature_9 = [None for _ in range(link_len)]
feature_10 = [None for _ in range(link_len)]
feature_11 = [None for _ in range(link_len)]
feature_12 = [None for _ in range(link_len)]

for link_ind in range(
    link_len
):  # todo this function does not work stably, needs to rewrite it

    r = requests.get(df["Links"][link_ind], headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")

    body = soup.find("body")

    properties1 = body.select("dd.sold-property__attribute-value")
    prop_len = len(properties1)

    feature_0[link_ind] = (
        str(properties1[0])
        .replace('<dd class="sold-property__attribute-value">', "")
        .replace("</dd>", "")
        .replace("\n", "")
        .replace("\xa0", "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', "")
        .strip()
    )
    feature_1[link_ind] = (
        str(properties1[1])
        .replace('<dd class="sold-property__attribute-value">', "")
        .replace("</dd>", "")
        .replace("\n", "")
        .replace("\xa0", "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', "")
        .strip()
    )
    feature_2[link_ind] = (
        str(properties1[2])
        .replace('<dd class="sold-property__attribute-value">', "")
        .replace("</dd>", "")
        .replace("\n", "")
        .replace("\xa0", "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', "")
        .strip()
    )
    feature_3[link_ind] = (
        str(properties1[3])
        .replace('<dd class="sold-property__attribute-value">', "")
        .replace("</dd>", "")
        .replace("\n", "")
        .replace("\xa0", "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', "")
        .strip()
    )
    feature_4[link_ind] = (
        str(properties1[4])
        .replace('<dd class="sold-property__attribute-value">', "")
        .replace("</dd>", "")
        .replace("\n", "")
        .replace("\xa0", "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', "")
        .strip()
    )
    feature_5[link_ind] = (
        str(properties1[5])
        .replace('<dd class="sold-property__attribute-value">', "")
        .replace("</dd>", "")
        .replace("\n", "")
        .replace("\xa0", "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', "")
        .strip()
    )
    feature_6[link_ind] = (
        str(properties1[6])
        .replace('<dd class="sold-property__attribute-value">', "")
        .replace("</dd>", "")
        .replace("\n", "")
        .replace("\xa0", "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', "")
        .strip()
    )
    feature_7[link_ind] = (
        str(properties1[7])
        .replace('<dd class="sold-property__attribute-value">', "")
        .replace("</dd>", "")
        .replace("\n", "")
        .replace("\xa0", "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
        .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', "")
        .strip()
    )

    if prop_len == 9:
        feature_8[link_ind] = (
            str(properties1[8])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
    elif prop_len == 10:
        feature_8[link_ind] = (
            str(properties1[8])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_9[link_ind] = (
            str(properties1[9])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
    elif prop_len == 11:
        feature_8[link_ind] = (
            str(properties1[8])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_9[link_ind] = (
            str(properties1[9])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_10[link_ind] = (
            str(properties1[10])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
    elif prop_len == 12:
        feature_8[link_ind] = (
            str(properties1[8])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_9[link_ind] = (
            str(properties1[9])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_10[link_ind] = (
            str(properties1[10])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_11[link_ind] = (
            str(properties1[11])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
    elif prop_len == 13:
        feature_8[link_ind] = (
            str(properties1[8])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_9[link_ind] = (
            str(properties1[9])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_10[link_ind] = (
            str(properties1[10])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_11[link_ind] = (
            str(properties1[11])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )
        feature_12[link_ind] = (
            str(properties1[12])
            .replace('<dd class="sold-property__attribute-value">', "")
            .replace("</dd>", "")
            .replace("\n", "")
            .replace("\xa0", "")
            .replace('<i class="fa fa-arrow-circle-o-up fa-lg price-icon--up"></i>', "")
            .replace(
                '<i class="fa fa-arrow-circle-o-up fa-lg price-icon--down"></i>', ""
            )
            .strip()
        )

# Save as a csv file which shall be cleaned later
d = {
    "feature_0": feature_0,
    "feature_1": feature_1,
    "feature_2": feature_2,
    "feature_3": feature_3,
    "feature_4": feature_4,
    "feature_5": feature_5,
    "feature_6": feature_6,
    "feature_7": feature_7,
    "feature_8": feature_8,
    "feature_9": feature_9,
    "feature_10": feature_10,
    "feature_11": feature_11,
    "feature_12": feature_12,
}
frame = pd.DataFrame(data=d).T
frame.to_csv("unprocessed_2ndlayer.csv", index=False)

# Broker/Agency info
brokers = [None for _ in range(link_len)]
agencies = [None for _ in range(link_len)]

for link_ind in range(link_len):

    r = requests.get(df["Links"][link_ind], headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    body = soup.find("body")

    properties2 = body.select("div.broker-card__info")
    m = (
        properties2[0]
        .get_text()
        .replace("\n", "")
        .replace("Kontakta mäklarkontoret", "")
        .replace("Kontakta mäklaren", "")
        .replace("Kontakt", "")
        .strip()
        .split("      ")
    )

    # Note that some links only provide agency without broker info.
    if len(m) == 2:
        brokers[link_ind] = m[0]
        agencies[link_ind] = m[1]
    else:
        agencies[link_ind] = m[0]

# Save as a csv file
d = {"Agents": brokers, "Firm": agencies}
agent_df = pd.DataFrame(data=d)
agent_df.to_csv("agency_info.csv", index=False)
