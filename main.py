"""the main file to be called"""
from load.load_data import insert_data
from transform.transform_data import blog_data

if __name__ == "__main__":
    insert_data(blog_data)