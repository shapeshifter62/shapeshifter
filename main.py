# I chose these import statements just to make my code look cleaner
# For this to work you would just need to import cocos and then add the subdirectory after
# Ex: self.label = Label(...) would be self.label = cocos.text.Label(...)

import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.director import director
from cocos.menu import Menu, CENTER, MenuItem, shake, shake_back
from cocos.scene import Scene
from pyglet.app import exit
from cocos.sprite import Sprite

class Actors(Layer):
    def __init__(self, width, height):
        super(Actors, self).__init__()

        self.width = width
        self.height = height
        # Here is where the code starts to get different
        # Instead of text, I create a sprite object
        # Also unlike last time, I added the sprite to the object instead of making it local
        # This is useful if you want to access it in other functions, like I will show in the next tutorial
        self.actor = Sprite('art/stefana.png')
        self.background = Sprite('art/level1.png')
        # Then I add it to the layer, similar to the text
        self.actor.position = 320, 240

        self.background.position = self.width//2, self.height//2
        self.background.scale = 1.0

        # And lastly I add it to the layer. Standard stuff
        self.add(self.background)
        self.add(self.actor)



# This code is an explained version of the Hello World example from the Cocos2D Python documentation
# We will be making a simple game that displays the text "Hello World!"




# From here the code is pretty typical for a Cocos2D application
# First I need to initialize the cocos director
# The director is the part of cocos that "directs" the scenes. Cocos is pretty partial to this type of film language
director.init(fullscreen=True, width=1024, height=768)
# Lastly I run the scene. This line of code is pretty long compared to the others, so I'll explain what each part does
# To begin I call the director's run function, which allows it to run the scene by placing layers within
# Next I create a Scene object that allows me to string the layers together. In this case I only have 1 layer
main_scene = scene.Scene(
    # And lastly I create the layer that we made above inside of the new scene
    Actors(director.get_window_size()[0], director.get_window_size()[1])
)
# main_scene.anchor = 0, 0
# main_scene.position = 0, 0
director.run(
    main_scene
)

# That's it! Run it and see what happens

