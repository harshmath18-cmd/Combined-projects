from utils.restaurant_images import get_restaurant_image


def assign_images(df):

    df["Image"] = df["Restaurant_Name"].apply(get_restaurant_image)

    return df