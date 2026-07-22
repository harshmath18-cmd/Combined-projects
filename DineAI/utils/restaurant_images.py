def get_restaurant_image(name, cuisine=""):

    name = str(name).lower()
    cuisine = str(cuisine).lower()

    # ---------- Brand Logos ----------

    if "pizza hut" in name:
        return "images/restaurants/brands/pizzahut.jpg"

    elif "domino" in name:
        return "images/restaurants/brands/dominos.jpg"

    elif "burger king" in name:
        return "images/restaurants/brands/burgerking.jpg"

    elif "mcd" in name or "mcdonald" in name:
        return "images/restaurants/brands/mcd.jpg"

    elif "kfc" in name:
        return "images/restaurants/brands/kfc.jpg"

    elif "starbucks" in name:
        return "images/restaurants/brands/starbucks.jpg"

    elif "subway" in name:
        return "images/restaurants/brands/subway.jpg"

    # ---------- Cuisine Images ----------

    elif "north indian" in cuisine:
        return "images/restaurants/north_indian.jpg"

    elif "south indian" in cuisine:
        return "images/restaurants/south_indian.jpg"

    elif "indian" in cuisine:
        return "images/restaurants/indian.jpg"

    elif "chinese" in cuisine:
        return "images/restaurants/chinese.jpg"

    elif "italian" in cuisine:
        return "images/restaurants/italian.jpg"

    elif "pizza" in cuisine:
        return "images/restaurants/pizza.jpg"

    elif "burger" in cuisine:
        return "images/restaurants/burger.jpg"

    elif "cafe" in cuisine:
        return "images/restaurants/cafe.jpg"

    elif "bakery" in cuisine:
        return "images/restaurants/bakery.jpg"

    elif "dessert" in cuisine:
        return "images/restaurants/dessert.jpg"

    elif "ice cream" in cuisine:
        return "images/restaurants/ice_cream.jpg"

    elif "street food" in cuisine:
        return "images/restaurants/street_food.jpg"

    elif "biryani" in cuisine:
        return "images/restaurants/biryani.jpg"

    elif "seafood" in cuisine:
        return "images/restaurants/seafood.jpg"

    elif "mughlai" in cuisine:
        return "images/restaurants/mughlai.jpg"

    elif "mexican" in cuisine:
        return "images/restaurants/mexican.jpg"

    elif "thai" in cuisine:
        return "images/restaurants/thai.jpg"

    elif "japanese" in cuisine:
        return "images/restaurants/japanese.jpg"

    elif "korean" in cuisine:
        return "images/restaurants/korean.jpg"

    elif "bbq" in cuisine or "barbecue" in cuisine:
        return "images/restaurants/bbq.jpg"

    elif "vegetarian" in cuisine or "pure veg" in cuisine:
        return "images/restaurants/vegetarian.jpg"

    elif "healthy" in cuisine:
        return "images/restaurants/healthy.jpg"

    elif "beverages" in cuisine:
        return "images/restaurants/beverages.jpg"

    else:
        return "images/restaurants/default.jpg"