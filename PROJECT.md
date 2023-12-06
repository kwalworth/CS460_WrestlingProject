# Autonomous Robotics Project - Cyberbotics Humanoid Wrestling
## Introduction
Welcome to our Autonomous Robotics project repository! In this project, we are combining various concepts from sensing, kinematics, path planning, task execution, and vision to participate in the Cyberbotics Humanoid Wrestling competition. Our goal is to showcase and implement algorithms discussed in our class while exploring and pushing the boundaries of our interests in robotics.

## Project Description
### Objective
The primary objective of this project is to develop a robust humanoid robot controller capable of competing in the Cyberbotics Wrestling competition. We aim to demonstrate the integration of theoretical concepts learned in class into a real-world robotics application.

### Key Components
Cyberbotics Open Repository: There are many functions already created for the robots provided by Cyberbotics for this competition. Several of our implementation strategies will utilize these function from Cyberbotics to try and win the competition.

Sensing: Implementing sensing techniques to perceive changes elevation during the wrestling match.

Kinematics: Implementing kinematic models for precise control of our humanoid robot's movements, ensuring both agility and stability.

Path Planning: Developing efficient path planning algorithms to navigate the robot through the wrestling arena, avoiding falling while covering as much ground as possible and strategically positioning itself for offensive and defensive maneuvers.

Task Execution: Integrating task execution mechanisms to translate high-level strategies into low-level motor commands for the robot's actuators.

Vision: Leveraging computer vision to identify opponent's location and determine best time to execute offensive maneuvers.

### Features
Modular Codebase: Our project is organized into modular components, making it easy to understand, modify, and extend. Each key concept is implemented in a separate module for clarity and maintainability.

Simulation Environment: To facilitate testing and development, we use the simulation environment provided by Cyberbotics Humanoid Wrestling competition.

### Results
We successfully implemented all features. Path planning enabled the robot to navigate the map, increasing our score while avoiding falling out of the arena and potential losses. Fall detection functioned correctly, allowing our robot to self-right when it fell. Our vision was able to provide an estimate of how far away the opponent was. The estimate was used to determine when the attack function was called. Once triggered, our bot started squatting up and down while swinging it’s arms in an attempt to get under the other robot and knock it over. These were all implemented together in one controller. 

There were 6 opponent controller’s provided. Our first measure of success was just to implement the controller with all features working. But we also wanted to see how we measured up to the provided opponent controllers. We were able to defeat 5 of the 6 provided controllers. We didn't have a specific target in mind, but we felt beating 5 of the 6 controllers was very good. It demonstrated that our controller works well. 

 ![Alice](https://github.com/kwalworth/CS460_WrestlingProject/assets/116377367/c82c6c26-b416-41cb-91ef-14e99eda2633)
Alice - Victory 

 ![Bob](https://github.com/kwalworth/CS460_WrestlingProject/assets/116377367/2909596a-f9a5-46bf-a9cd-b0616686ec4f)
Bob - Victory 

 

Charlie - Victory 


David – Defeat 

 

Eve – Victory 

 

Fatima – Victory 

 

### Conclusion
The Cyberbotics Humanoid Wrestling competition provides a unique challenge. Not only does a controller have to be able to make a humanoid robot move throughout an environment, it has to be prepared to interact with and compete against other robots. We decided the most important features to implement were path planning, fall detection, vision, and attacking the opponent. The functions were implemented into the controller successfully as we were able to defeat 5 of the 6 provided opponent controllers. 


### Link to Project Video
Here is the link to the presentation [Project Video][link_toYOUTUBE].

[link_toYOUTUBE]: https://youtu.be/Ki5sl57S7JU

