#!/usr/bin/python3

# Copyright 1996-2023 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Minimalist controller example for the Robot Wrestling Tournament.
   Demonstrates how to play a simple motion file."""

from controller import Robot
import sys
import cv2

# We provide a set of utilities to help you with the development of your controller. You can find them in the utils folder.
# If you want to see a list of examples that use them, you can go to https://github.com/cyberbotics/wrestling#demo-robot-controllers
sys.path.append('..')
from utils.motion_library import MotionLibrary
from utils.image_processing import ImageProcessing as IP
from utils.camera import Camera
from utils.running_average import RunningAverage
from utils.fall_detection import FallDetection


class Wrestler (Robot):
    
    
    def run(self):
        # to load all the motions from the motions folder, we use the MotionLibrary class:
        self.library = MotionLibrary()
        # retrieves the WorldInfo.basicTimeTime (ms) from the world file
        self.time_step = int(self.getBasicTimeStep())
        self.camera = Camera(self)
        self.image = IP()
        self.fall = FallDetection(self.time_step, self)
        
        start = True
        found = False
        doneForward = 0
        steps = 8
        walk = 1
        
        while self.step(self.time_step) != -1:
            
            self.fallDectection()
            
            position = self.opponent_distance()
            if found == True:
                walk = 3
                self.attack_opponent()
            #self.opponent_position = RunningAverage(dimensions=1)
            if position < 0.60 and found == False:
                print("OH NO HE'S CLOSE")
                print(position)
                found = True
            if start == True:
                if doneForward == 0:
                    self.library.play('Forwards')
                    doneForward += 1
                elif self.library.get('Forwards').isOver() and doneForward < 5:
                    self.library.play('Forwards')
                    doneForward += 1
                elif self.library.get('Forwards').isOver() and doneForward >= 5:
                    self.library.play('SideStepLeft')
                    start = False     
            elif self.library.get('SideStepLeft').isOver():
                if walk == 1:
                    steps = self.walk1(steps)
                    if steps == 0:
                        walk = 2
                if walk == 2:
                    steps = self.walk2(steps)
                    if steps == 0:
                        walk = 1
                #print(steps)
          
    #ChatGPT helped start positions, but we perfected it and made the arms swing
    def attack_opponent(self):
        self.library.play('Squat')
             
    def opponent_distance(self):
        image = self.camera.get_image()
        opponent_location = self.image.locate_opponent(image)
        largest_contour = opponent_location[0]
        estimated_distance = 10
        if largest_contour is not None:
            # Get the bounding rectangle of the largest contour
            x, y, w, h = cv2.boundingRect(largest_contour)
            
            # Assume a constant size for the opponent (adjust this based on your scenario)
            known_opponent_size = 50  # Example value, adjust based on your case

            #ChatGPT helped with this part
            # Estimate distance based on the ratio of known size to observed size
            estimated_distance = known_opponent_size / w
            
        return estimated_distance
        
                
    def fallDectection(self):
        self.fall.check()
    
    #Walk1 turns wide            
    def walk1(self, totalSteps):
        if self.library.get('SideStepLeft').isOver() and totalSteps < 18:
            self.library.play('SideStepLeft')
            totalSteps += 1
            #print("Step left")
        elif totalSteps == 18:
            if self.library.get('SideStepLeft').isOver():
                self.library.play('TurnRight20')
                totalSteps += 1
                #print("It equals 4 right now")
        elif totalSteps < 23 and totalSteps > 18:
            if self.library.get('TurnRight20').isOver():
                self.library.play('TurnRight20')
                totalSteps += 1
                #print("We shouldn't be getting in here super fast")
        elif totalSteps == 23:
            if self.library.get('TurnRight20').isOver():
                totalSteps = 0
                #print("END")
        return totalSteps
    
    #Walk2 turns narrow, corrects wide turn in walk1
    def walk2(self, totalSteps):
        if self.library.get('SideStepLeft').isOver() and totalSteps < 18:
            self.library.play('SideStepLeft')
            totalSteps += 1
            #print("Step left")
        elif totalSteps == 18:
            if self.library.get('SideStepLeft').isOver():
                self.library.play('TurnRight20')
                totalSteps += 1
                #print("It equals 4 right now")
        elif totalSteps < 24 and totalSteps > 18:
            if self.library.get('TurnRight20').isOver():
                self.library.play('TurnRight20')
                totalSteps += 1
                #print("We shouldn't be getting in here super fast")
        elif totalSteps == 24:
            if self.library.get('TurnRight20').isOver():
                totalSteps = 0
                #print("END")
        return totalSteps          
        


# create the Robot instance and run main loop
wrestler = Wrestler()
wrestler.run()

