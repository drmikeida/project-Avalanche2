import pyxel

class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height) and tilemap
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")
        
        # Set the initial position of the square
        self.x = 20
        self.y = 20
        self.score = 0

        # Set the initial position of first ball
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2

        #set initial position of second ball. spawn invisible
        self.sprite_a = None
        self.sprite_b = None
        self.sprite_da = 2
        self.sprite_db = 2

        #set initial position of third ball. spawn invisible
        self.sprite2_a = None
        self.sprite2_b = None
        self.sprite2_da = 2
        self.sprite2_db = 2

        #set initial position of fourth ball. spawn invisible
        self.sprite3_a = None
        self.sprite3_b = None
        self.sprite3_da = 2
        self.sprite3_db = 2

        #set initial position of fifth ball. spawn invisible
        self.sprite4_a = None
        self.sprite4_b = None
        self.sprite4_da = 2
        self.sprite4_db = 2
        
        # Start the game loop
        self.game_start = True
        self.game_over = False
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        if pyxel.btn(pyxel.KEY_SPACE):
            self.game_start = False

        #kill when touch wall
        if self.x <= -5 or self.x >= 160:
            self.game_over = True
        if self.y <= -5 or self.y >= 115:
            self.game_over = True

        if self.score<10:
            pyxel.text(50, 40, "GAME START", 8)

        #score increase over time
        if not self.game_over and not self.game_start:
            self.score += 0.5

        # Update the first ball position
        if not self.game_start:
            self.sprite_x += self.sprite_dx
            self.sprite_y += self.sprite_dy

        # Bounce ball 1 off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1

        #check for colllision first ball            
        distance = ((self.x - self.sprite_x) ** 2 + (self.y - self.sprite_y) ** 2) ** 0.5
        if distance < 13:
            self.game_over = True

        #spawn second ball when score is 100
        if self.score >= 100 and self.sprite_a is None:
            self.sprite_a = 100
            self.sprite_b = 80
        
        #allow second ball move
        if self.sprite_a is not None and self.sprite_b is not None:
            self.sprite_a += self.sprite_da
            self.sprite_b += self.sprite_db

            #allow second ball bounce off walls
            if self.sprite_a <= 0 or self.sprite_a >= 160:
                self.sprite_da *= -1
            if self.sprite_b <= 0 or self.sprite_b >= 120:
                self.sprite_db *= -1

        #check for collision second ball
            distance2 = ((self.x - self.sprite_a) ** 2 + (self.y - self.sprite_b) ** 2) ** 0.5
            if distance2 < 13:
                self.game_over = True

        #spawn third ball when score is 200
        if self.score >= 200 and self.sprite2_a is None:
            self.sprite2_a = 80
            self.sprite2_b = 70 

        #allow third ball move
        if self.sprite2_a is not None and self.sprite2_b is not None:
            self.sprite2_a += self.sprite2_da
            self.sprite2_b += self.sprite2_db

            #allow third ball bounce off walls
            if self.sprite2_a <= 0 or self.sprite2_a >= 160:
                self.sprite2_da *= -1
            if self.sprite2_b <= 0 or self.sprite2_b >= 120:
                self.sprite2_db *= -1
                
        #check for collision third ball
            distance3 = ((self.x - self.sprite2_a) ** 2 + (self.y - self.sprite2_b) ** 2) ** 0.5
            if distance3 < 13:
                self.game_over = True

        #spawn fourth ball when score is 300
        if self.score >= 300 and self.sprite3_a is None:
            self.sprite3_a = 90
            self.sprite3_b = 90 

        #allow fourth ball move
        if self.sprite3_a is not None and self.sprite3_b is not None:
            self.sprite3_a += self.sprite3_da
            self.sprite3_b += self.sprite3_db

            #allow fourth ball bounce off walls
            if self.sprite3_a <= 0 or self.sprite3_a >= 160:
                self.sprite3_da *= -1
            if self.sprite3_b <= 0 or self.sprite3_b >= 120:
                self.sprite3_db *= -1

        #check for collision fourth ball
            distance4 = ((self.x - self.sprite3_a) ** 2 + (self.y - self.sprite3_b) ** 2) ** 0.5
            if distance4 < 13:
                self.game_over = True

        #spawn fifth ball when score is 300
        if self.score >= 400 and self.sprite4_a is None:
            self.sprite4_a = 30
            self.sprite4_b = 20 

        #allow fifth ball move
        if self.sprite4_a is not None and self.sprite4_b is not None:
            self.sprite4_a += self.sprite4_da
            self.sprite4_b += self.sprite4_db

            #allow fifth ball bounce off walls
            if self.sprite4_a <= 0 or self.sprite4_a >= 160:
                self.sprite3_da *= -1
            if self.sprite4_b <= 0 or self.sprite4_b >= 120:
                self.sprite3_db *= -1

        #check for collision fifth ball
            distance5 = ((self.x - self.sprite4_a) ** 2 + (self.y - self.sprite4_b) ** 2) ** 0.5
            if distance5 < 13:
                self.game_over = True

    def draw(self):
        if self.game_start:
            pyxel.text(20, 50, "Welcome to Avalanche! Press [SPACE] to Start!", 8)
            pyxel.text(20, 70, "Avoid the snowballs and walls!", 8)

        if self.game_over:
            pyxel.text(50, 40, "GAME OVER", 8)
            pyxel.text(40, 60, f"Final Score: {self.score}", 7)
            return

        if not self.game_start:
            pyxel.cls(0)
            pyxel.blt(self.x, self.y, 0, 0, 0, 9, 7)

            # Clear the screen with black (color 0)
            pyxel.cls(11)

            # Draw a square (color 9)
            pyxel.blt(self.x, self.y, 0, 0, 0, 10, 10)

            # Draw the moving sprite (circle) (color 11)
            pyxel.circ(self.sprite_x, self.sprite_y, 5, 7)

            # Display the score
            pyxel.text(5, 5, f"Score: {self.score}", 7)
                
            if self.sprite_a is not None and self.sprite_b is not None:
                pyxel.circ(self.sprite_a, self.sprite_b, 5, 7)
    
            if self.sprite2_a is not None and self.sprite2_b is not None:
                pyxel.circ(self.sprite2_a, self.sprite2_b, 5, 7)
    
            if self.sprite3_a is not None and self.sprite3_b is not None:
                pyxel.circ(self.sprite3_a, self.sprite3_b, 5, 7)
# Run the game
App()