import pandas as pd
import os, sys


class data:
    """Classe de collecte des données relative à la base de données du projet
    
    Keyword arguments:
    data -- données utiles
    Return: return_description
    """
    def __init__(self):
        self.data_dir = "../data/dataset/ml-latest-small"
        self.movies_df =  pd.read_csv(os.path.join(self.data_dir + "/"+ "movies.csv"))
        self.ratings_df = pd.read_csv(os.path.join(self.data_dir + "/"+ "ratings.csv"))
        self.model_dir = "../data/model_dir"
        self.database_dir = "../data/database"
    
    def filter(self):
        """Fonction permettant de traiter les données"""
        self.users = self.ratings_df["userId"]
        self.movies_title = self.movies_df["title"]
        self.genres = self.movies_df["genres"]
        return (self.genres , self.movies_df , self.users)

data = data()
print(data.filter())