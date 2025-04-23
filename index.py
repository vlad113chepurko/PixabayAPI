import requests
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Images")
root.geometry("500x500")

PIX_KEY = "49887738-1e7b4592f48c0ba83eb287d53"
url = f"https://pixabay.com/api/?key={PIX_KEY}&q=cat&image_type=photo"
filename = 'images/image.png'

def save_image(filename, image_resp):
    print("Saving image to ./images...")
    with open (filename, 'wb') as f:
        f.write(image_resp.content)
def generate_image(image_url):
    print(f"There your cat: {image_url}")
    try:
       image_resp = requests.get(image_url)
       save_image(filename, image_resp)
    except Exception as e:
        print(f"Error: {e}")

def on_click():
    print("Click")
    response = requests.get(url)
    if response.status_code == 200:
       data = response.json()
       if data['hits']:
          image_url = data["hits"][0]['largeImageURL']
          generate_image(image_url)
       else:
          print("Error")
    else:
     print(f"Error with response: {response.status_code}")

generate_btn = Button(
root,
fg='white',
font=("Helvetica", 13),
bg="#3d3d3d",
text="Generate a cat",
command=on_click)
generate_btn.grid(row=0,column=0)

root.mainloop()
