import random

# Let's assume we have some memes categorized into themes
memes = {
    "animals": ["animal_meme1.jpg", "animal_meme2.jpg", "animal_meme3.jpg"],
    "movies": ["movie_meme1.jpg", "movie_meme2.jpg", "movie_meme3.jpg"],
    "science": ["science_meme1.jpg", "science_meme2.jpg", "science_meme3.jpg"]
}

# Let's assign rarity to each meme, ranging from 1 to 5
memes_rarity = {
    "animal_meme1.jpg": 3,
    "animal_meme2.jpg": 2,
    "animal_meme3.jpg": 5,
    "movie_meme1.jpg": 4,
    "movie_meme2.jpg": 1,
    "movie_meme3.jpg": 3,
    "science_meme1.jpg": 2,
    "science_meme2.jpg": 5,
    "science_meme3.jpg": 4
}

def get_rare_meme(theme):
    if theme not in memes:
        return "Theme not found"
    
    rarest_meme = None
    rarity = 0
    
    # Finding the rarest meme in the selected theme
    for meme in memes[theme]:
        meme_rarity = memes_rarity[meme]
        if meme_rarity > rarity:
            rarest_meme = meme
            rarity = meme_rarity
    
    return rarest_meme

def get_random_meme(theme):
    if theme not in memes:
        return "Theme not found"
    
    return random.choice(memes[theme])

# Example usage of functions
selected_theme = "animals"  # Selecting the theme "animals"
rare_meme = get_rare_meme(selected_theme)
print("The rarest meme in the theme", selected_theme, "is:", rare_meme)

random_meme = get_random_meme(selected_theme)
print("A random meme in the theme", selected_theme, "is:", random_meme)
