import os
import time
import shutil
import random

def unpack():
    item_to_category = {
        "aerosol_cans": "Metal",
        "aluminum_food_cans": "Metal",
        "aluminum_soda_cans": "Metal",
        "cardboard_boxes": "Paper_and_Cardboard",
        "cardboard_packaging": "Paper_and_Cardboard",
        "clothing": "Textiles",
        "coffee_grounds": "Organic_Waste",
        "disposable_plastic_cutlery": "Plastic",
        "eggshells": "Organic_Waste",
        "food_waste": "Organic_Waste",
        "glass_beverage_bottles": "Glass",
        "glass_cosmetic_containers": "Glass",
        "glass_food_jars": "Glass",
        "magazines": "Paper_and_Cardboard",
        "newspaper": "Paper_and_Cardboard",
        "office_paper": "Paper_and_Cardboard",
        "paper_cups": "Paper_and_Cardboard",
        "plastic_cup_lids": "Plastic",
        "plastic_detergent_bottles": "Plastic",
        "plastic_food_containers": "Plastic",
        "plastic_shopping_bags": "Plastic",
        "plastic_soda_bottles": "Plastic",
        "plastic_straws": "Plastic",
        "plastic_trash_bags": "Plastic",
        "plastic_water_bottles": "Plastic",
        "shoes": "Textiles",
        "steel_food_cans": "Metal",
        "styrofoam_cups": "Plastic",
        "styrofoam_food_containers": "Plastic",
        "tea_bags": "Organic_Waste",
    }
    print("UNPACKING: STARTED...")
    start = time.perf_counter()
    path = "C:\\Users\\frkho\\Downloads\\archive\\images\\images"
    output = "C:\\Users\\frkho\\Downloads\\archive\\jumbledData"
    if os.path.exists(output):
        shutil.rmtree(output)
        os.mkdir(output)
        print("UNPACKING: FOLDER RENEWED")
    else:
        os.mkdir(output)
        print("UNPACKING: FOLDER CREATED")
    print("CREATING SUBFOLDERS...")
    for val in set(item_to_category.values()):
        os.mkdir(f'{output}\\{val}')
        print(f'SUBFOLDER {val} MADE.')
    print("CREATING SUBFOLDERS DONE...")
    c = 0
    for category in os.listdir(path):
        destPath = f'{output}\\{item_to_category[category]}'
        for sub in ['default','real_world']:
            for img in os.listdir(f'{path}\\{category}\\{sub}'):
                shutil.copy(f'{path}\\{category}\\{sub}\\{img}',f'{destPath}\\{img}')
                c += 1
    end = time.perf_counter()
    print(f"UNPACKING: COMPLETED IN {end - start:.4f} SECONDS. {c} FILES PROCESSED.")

def split():
    item_to_category = {
            "aerosol_cans": "Metal",
            "aluminum_food_cans": "Metal",
            "aluminum_soda_cans": "Metal",
            "cardboard_boxes": "Paper_and_Cardboard",
            "cardboard_packaging": "Paper_and_Cardboard",
            "clothing": "Textiles",
            "coffee_grounds": "Organic_Waste",
            "disposable_plastic_cutlery": "Plastic",
            "eggshells": "Organic_Waste",
            "food_waste": "Organic_Waste",
            "glass_beverage_bottles": "Glass",
            "glass_cosmetic_containers": "Glass",
            "glass_food_jars": "Glass",
            "magazines": "Paper_and_Cardboard",
            "newspaper": "Paper_and_Cardboard",
            "office_paper": "Paper_and_Cardboard",
            "paper_cups": "Paper_and_Cardboard",
            "plastic_cup_lids": "Plastic",
            "plastic_detergent_bottles": "Plastic",
            "plastic_food_containers": "Plastic",
            "plastic_shopping_bags": "Plastic",
            "plastic_soda_bottles": "Plastic",
            "plastic_straws": "Plastic",
            "plastic_trash_bags": "Plastic",
            "plastic_water_bottles": "Plastic",
            "shoes": "Textiles",
            "steel_food_cans": "Metal",
            "styrofoam_cups": "Plastic",
            "styrofoam_food_containers": "Plastic",
            "tea_bags": "Organic_Waste",
        }
    print("SPLITTING: STARTED...")
    start = time.perf_counter()
    path = "C:\\Users\\frkho\\Downloads\\archive\\jumbledData"
    output = "C:\\Users\\frkho\\Downloads\\archive\\splitData"
    if os.path.exists(output):
        shutil.rmtree(output)
        os.mkdir(output)
        os.mkdir(output + '\\' + 'train')
        os.mkdir(output + '\\' + 'val')
        print("SPLITTING: FOLDER RENEWED")
    else:
        os.mkdir(output)
        os.mkdir(output + '\\' + 'train')
        os.mkdir(output + '\\' + 'val')
        print("SPLITTING: FOLDER CREATED")
    print("CREATING SUBFOLDERS... in JUMBLEDDATA")
    for val in set(item_to_category.values()):
        os.mkdir(f'{output}\\{val}')
        print(f'SUBFOLDER {val} MADE.')
    print("CREATING SUBFOLDERS DONE...")
    random.seed(42)
    images = os.listdir(path)
    random.shuffle(images)
    valSize = 0.15
    splitIndex = int(len(images) * (1 - valSize))
    valImages = images[splitIndex:]
    trainImages = images[:splitIndex]
    for img in valImages:
        shutil.copy(path + '\\' + img, output + "\\val\\" + img)
    for img in trainImages:
        shutil.copy(path + '\\' + img, output + "\\train\\" + img)
    end = time.perf_counter()
    print(f"SPLITTING: COMPLETED IN {end - start:.4f} SECONDS. {len(valImages)} VAL / {len(trainImages)} TRAIN.")

if __name__ == "__main__":
    unpack()
    split()
    print("SCRIPT COMPLETED.")
