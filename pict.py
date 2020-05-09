"""list_pdf = half cardboard oar
baby-sitter drip shampoo
point time machine yardstick
think lace darts
world avocado bleach
shower curtain extension cord dent
birthday lap sandbox
bruise quicksand fog
gasoline pocket honk
sponge rim bride
wig zipper wag
letter opener fiddle water buffalo
pilot brand pail
baguette rib mascot
fireman pole zoo sushi
fizz ceiling fan bald
banister punk post office
season Internet chess
puppet chime ivy
full koala dentist
Copyright
baseboards ping pong bonnet
mast hut welder
dryer sheets sunburn houseboat
sleep kneel crust
grandpa speakers cheerleader
dust bunny salmon cabin
handle swamp cruise
wedding cake crow's nest macho
drain foil orbit
dream recycle raft
gold plank cliff
sweater vest cape safe
picnic shrink ray leak
boa constrictor deep mold
CD tiptoe hurdle
knight loveseat cloak
bedbug bobsled hot tub
firefighter cell phone charger beanstalk
nightmare coach moth
sneeze wooly mammoth pigpen
swarm goblin chef
applause wax sheep dog
s'mores plow runt
Bug
Slide
Swing
Coat
Shoe
Ocean
Dog
Mouth
Milk
Duck
Skateboard
Bird
Mouse
Whale
Jacket
Shirt
Hippo
Beach
Egg
Cookie
Cheese
Skip
Drum
Worm
Spider
Bridge
Bell
Jellyfish
Bunny
Truck
Monkey
Bread
Bracelet
Alligator
Bat
Clock
Lollipop
Moon
Doll
Basketball
Bike
Seashell
Rocket
Bear
Corn
Chicken
Purse
Glasses
Blocks
Turtle
Horse
Dinosaur
Head
Lamp
Snowman
Ant
Giraffe
Cupcake
Chair
Bunk Bed
Snail
Baby
Cherry
Crab
Branch
Robot
Song
Trip
Backbone
Bomb
Treasure
Garbage
Park
Pirate
Ski
Whistle
State
Baseball
Coal
Queen
Photograph
Computer
Hockey
Hot Dog
Salt and Pepper
iPad
Frog
Lawnmower
Mattress
Pinwheel
Cake
Circus
Battery
Mailman
Cowboy
Password
Bicycle
Skate
Electricity
Thief
Teapot
Deep
Spring
Nature
Shallow
Outside
America
Bow tie
Wax
Light Bulb
Music
Popsicle
Brain
Birthday Cake
Knee
Pineapple
Tusk
Sprinkler
Money
Pool
Lighthouse
Doormat
Face
Flute
Rug
Snowball
Purse
Owl
Gate
Suitcase
Stomach
Doghouse
Pajamas
Bathroom
Scale
Peach
Newspaper
Watering Can
Hook
School
French Fries
Beehive
Artist
Flagpole
Camera
Hair Dryer
Mushroom
TV
Quilt
Chalk
Cardboard
Oar
Drip
Shampoo
Time Machine
Yardstick
Think
Lace
Darts
Avocado
Bleach
Curtain
Extension Cord
Dent
Birthday
Lap
Sandbox
Bruise
Fog
Sponge
Wig
Pilot
Mascot
Fireman
Zoo
Sushi
Fizz
Ceiling
Post Office
Season
Internet
Chess
Puppet
Chime
Koala
Dentist
Ping Pong
Bonnet
Sheets
Sunburn
Houseboat
Sleep
Kneel
Crust
Speakers
Cheerleader
Dust
Salmon
Cabin
Handle
Swamp
Cruise
Pharmacist
Dream
Raft
Plank
Cliff
Sweater
Safe
Picnic
Shrink
Ray
Leak
Deep
Tiptoe
Hurdle
Knight
Cloak
Bedbug
Hot Tub
Firefighter
Charger
Nightmare
Coach
Sneeze
Goblin
Chef
Applause
Golden Retriever
Joke
Comedian
Cupcake
Baker
Facebook
Convertible
Giant
Garden
Diving
Hopscotch
Stingray

list_pdf_split = list_pdf.split('\n')
full_list= []
for line in list_pdf_split:
    [full_list.append(word) for word in line.split()]
    
import pickle
with open('/home/sam/Documents/full_list.pkl', 'wb') as f:
    pickle.dump(full_list, f)
"""

import tkinter as tk
from tkinter import messagebox
import random
import pickle

with open('/home/sam/Documents/full_list.pkl', 'rb') as f:
    full_list = pickle.load(f)

if __name__ == "__main__":
    rand_word = random.choice(full_list)
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Your word is--------------------------------->", rand_word)
    full_list.remove(rand_word)
    with open('/home/sam/Documents/full_list.pkl', 'wb') as f:
        pickle.dump(full_list, f)
