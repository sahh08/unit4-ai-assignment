# Create a function that recommends a movie based on mood
def recommend_movie(mood):
    recommendations = {
        "happy": "The Pursuit of Happyness",
        "sad": "The Shawshank Redemption",
        "adventurous": "Indiana Jones: Raiders of the Lost Ark",
        "romantic": "The Notebook",
        "thrilled": "Inception"
    }
    
    return recommendations.get(mood.lower(), "Sorry, I don't have a recommendation for that mood.")