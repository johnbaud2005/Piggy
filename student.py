#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1100  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "w": ("Wall", self.wall),
                "l": ("Wallloop", self.wallloop),
                "a": ("Aroundbox", self.aroundbox),
                "b": ("Box", self.box),
                "m": ("Maze", self.maze),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "j": ("John", self.john)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''
    def john(self):
      self.scan()
      print (self.scan_data)
      
    def dance(self):
     if self.safe_to_dance():
        self.fwd()
        time.sleep(2)
        self.stop()

        self.right()
        time.sleep(3)
        self.stop()

        self.left()
        time.sleep(3)
        self.stop
        
        self.fwd()
        time.sleep(1)
        self.stop()
          
        
        # TODO: check to see if it's safe before dancing
        
        # lower-ordered example...
        self.right(primary=50, counter=50)
        time.sleep(2)
        self.stop()

    def safe_to_dance(self):
      for c in range(4):
        self.scan()
        for x in self.scan_data:
            if self.scan_data[x] < 300:
              print("Not Safe To Dance")
              return False
        self.right()
        time.sleep(1)
        self.stop()
      print("Safe To Dance")
      return True


    def wall(self):
      while True:
        self.fwd()
        if self.read_distance() < 300:
          self.stop()
          break

    def wallloop(self):
      while True:
        self.fwd()
        if self.read_distance() < 300:
          self.right()
          time.sleep(2)

    def aroundbox(self):
      while True:
        self.fwd()
        if self.read_distance() < 300:
          self.right()
          time.sleep(1)
          self.fwd()
          time.sleep(1)
          self.stop()
          self.left()
          time.sleep(1)
          self.stop()

    def box(self):
      while True:
        self.fwd(30,30)
        self.servo(self.MIDPOINT)
        time.sleep(.5)
        center = self.read_distance()
        self.servo(1500)
        time.sleep(.5)
        left = self.read_distance()
        self.servo(700)
        time.sleep(.5)
        right = self.read_distance()

        if (center < 200):
          if right < left:
            self.left()
            time.sleep(1)
            self.stop()
            self.fwd()
            time.sleep(3)
            self.stop()
            self.right()
            time.sleep(1)
            self.stop()
            self.fwd()
            
          else:
            self.right()
            time.sleep(1)
            self.stop()
            self.fwd()
            time.sleep(3)
            self.stop()
            self.left()
            time.sleep(1)
            self.stop()
            self.fwd()
        elif (right < 200):
          self.fwd(30,80)
          time.sleep(1)
          self.fwd(80,30)
          time.sleep(1.5)
          self.fwd(30,30)
          time.sleep(1)

        elif (left < 200):
          self.fwd(80,30)
          time.sleep(1)
          self.fwd(30,80)
          time.sleep(1.5)
          self.fwd(30,30)
          time.sleep(1)

          
    def maze(self):
        while True:
          self.servo(self.MIDPOINT)
          self.fwd()
          if self.read_distance() < 200:
            self.stop()
            center = self.read_distance()
            self.servo(2000)
            left = self.read_distance()
            self.servo(700)
            time.sleep(.5)
            right = self.read_distance()
            
    
            if (center < 200):
              if right < left:
                self.left()
                time.sleep(.75)
                
              else:
                self.right()
                time.sleep(.75)

  
    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 20):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
