# Autonomous Robotics Project - Cyberbotics Humanoid Wrestling

## Abstract

In our Autonomous Robotics project, "Cyberbotics Humanoid Wrestling," we dive into the realm of practical robot control for the Cyberbotics Humanoid Wrestling competition. By merging theoretical concepts from sensing, kinematics, path planning, task execution, and vision, our goal is to craft a robust humanoid robot capable of holding its own in the wrestling ring. We draw insights from academic sources on path planning and vision systems to inform our approach.

Key elements include leveraging the Cyberbotics Open Repository, implementing smart sensing techniques, deploying kinematic models for precise control, and incorporating efficient path planning algorithms. Our robot's task execution involves strategic movements and attacks based on opponent identification through computer vision.

Our modular codebase ensures clarity and ease of modification, and the simulation environment provided by Cyberbotics serves as a valuable testing ground. We assume a level playing field with uniform robot styles and fixed arena dimensions.

Results showcase a commendable 68.33% overall win ratio against six opponent controllers. The success lies in our robot's ability to navigate, self-right after falls, estimate opponent distances using vision, and execute effective offensive maneuvers.

Looking ahead, there's room for improvement, perhaps nudging the win ratio closer to 100% with further optimization. 

## Introduction
Welcome to our Autonomous Robotics project repository! In this project, we are combining various concepts from sensing, kinematics, path planning, task execution, and vision to participate in the Cyberbotics Humanoid Wrestling competition. Our goal is to showcase and implement algorithms discussed in our class while exploring and pushing the boundaries of our interests in robotics.

## Related Works

[1] “Robotic Path Planning.” Path Planning, fab.cba.mit.edu/classes/865.21/topics/path_planning/robotic.html. Accessed 6 Dec. 2023.  

[2] Montazeri, Allahyar. “Path Planning.” Path Planning - an Overview | ScienceDirect Topics, www.sciencedirect.com/topics/engineering/path-planning. Accessed 6 Dec. 2023. 

[3] “Understanding What Is a Robot Vision System.” Techman Robot, 19 Nov. 2021, www.tm-robot.com/en/robot-vision-system/. 

[4] Geiger, A, et al. “Vision Meets Robotics: The Kitti Dataset - Sage Journals.” Vision Meets Robotics: The KITTI Dataset, Sage Journals, journals.sagepub.com/doi/full/10.1177/0278364913491297. Accessed 6 Dec. 2023. 

These academic sources provide valuable information related to the project on Robotics algorithms for an autonomous robot wrestling simulation program. The first source provides an introduction to robotic path planning. "Robotic Path Planning" is a relevant source as it discusses the concept of path planning which is essential for the movement and navigation of the robot so that it will stay within the bounds of the simulated wrestling ring and target the other robot. It also discusses map representation which was not directly related to our specific controller but does relate to the class. The second source, "Path Planning - an Overview," provides a broader understanding of path planning and it serves as a comprehensive reference for the project. It also discusses global path planning vs local path planning. In global path planning, the environment is static, and the robot’s global information is known. Local path planning is where the path is generated based off of inputs received from sensors. The environment is always the same for our project. The arena never changes sizes, and our robot always starts in the same spot. Because the environment doesn’t change, we decided to use global path planning. The third source, "Understanding What Is a Robot Vision System," directly relates to the project on our robotics wrestling simulation program by discussing the importance of robot vision systems in understanding and interacting with the environment and identifying obstacles or opponents. The fourth source, "Vision Meets Robotics: The KITTI Dataset," provides insights into the use of vision in robotics and the importance of datasets in training and evaluating vision-based robotic systems. In our project, leveraging the robot’s vision capabilities allow it to identify how far away the opponent is from it and when it should execute an attack. These academic sources provide valuable information that is directly relevant to the project on Robotics algorithms for an autonomous robot wrestling simulation program. The academic sources provided offer valuable insights and information that directly relate to the project on Robotics algorithms for an autonomous robot wrestling simulation program and address key aspects such as path planning, map representation, global versus local path planning, and robot vision systems. These sources provide an overview of robotic path planning and discuss the different methods and algorithms used in this process. They also highlight the importance of understanding the environment and using sensor information for effective path planning and obstacle avoidance. Additionally, the sources emphasize the integration of vision systems and classifiers with navigation technology, path planning, and other algorithms to achieve autonomous operation in new environments. 



## Approach
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

## Assumptions 
We assumed that both competitors are using the same style robot and motion libraries and that the dimensions of the arena stay constant. We also assumed that if we designed a controller that could track the opponent and simultaneously move to cover more ground and attack the robot only when they were close enough for our attack that we would have a controller that would have a win ratio above 50%. 


## Results
We successfully implemented all features. Path planning enabled the robot to navigate the map, increasing our score while avoiding falling out of the arena and potential losses. Fall detection functioned correctly, allowing our robot to self-right when it fell. Our vision was able to provide an estimate of how far away the opponent was. The estimate was used to determine when the attack function was called. Once triggered, our bot started squatting up and down while swinging it’s arms in an attempt to get under the other robot and knock it over. These were all implemented together in one controller. 

There were 6 opponent controller’s provided. Our first measure of success was just to implement the controller with all features working. But we also wanted to see how we measured up to the provided opponent controllers. We managed to get above the 50% win ratio for 5 of the 6 competing controllers with a final overall win ratio of 68.33%.
 ![Alice](https://github.com/kwalworth/CS460_WrestlingProject/assets/116377367/c82c6c26-b416-41cb-91ef-14e99eda2633)

<p align="center">
  <b>Alice: Win Percentage: 70%, Average Time: 2:52, Coverage Score: 1.8522</b>
</p>
 
 | Trial | Win/Loss | Time | Score |
 |:-----:|:--------:|:----:|:-----:|
 | 1 | Win | 3:00 | 1.68 |
 | 2 | Loss | 2:41 | 1.799 |
 | 3 | Win | 3:00 | 1.721 |
 | 4 | Win | 2:46 | 2.087 |
 | 5 | Loss | 2:46 | 2.056 |
 | 6 | Win | 3:00 | 1.74 |
 | 7 | Loss | 2:36 | 1.744 |
 | 8 | Win | 3:00 | 1.901 |
 | 9 | Win | 3:00 | 1.799 |
 | 10 | Win | 3:00 | 1.995 |

 ![Bob](https://github.com/kwalworth/CS460_WrestlingProject/assets/116377367/2909596a-f9a5-46bf-a9cd-b0616686ec4f)

<p align="center">
  <b>Bob: Win Percentage: 60%, Average Time: 2:06, Coverage Score: 1.7739</b>
</p>
 
 | Trial | Win/Loss | Time | Score |
 |:-----:|:--------:|:----:|:-----:|
 | 1 | Win | 2:01 | 2.178 |
 | 2 | Win | 3:00 | 2.036 |
 | 3 | Win | 2:00 | 1.69 |
 | 4 | Win | 2:09 | 2.045 |
 | 5 | Win | 2:04 | 1.841 |
 | 6 | Loss | 1:53 | 1.478 |
 | 7 | Loss | 1:53 | 1.646 |
 | 8 | Loss | 1:59 | 1.358 |
 | 9 | Win | 2:09 | 1.772 |
 | 10 | Loss | 1:59 | 1.695 |
 
![Charlie](https://github.com/kwalworth/CS460_WrestlingProject/assets/116377367/36f54511-b12e-4dd2-96b1-5fa2ab18a591)

<p align="center">
  <b>Charlie: Win Percentage: 100%, Average Time: 0:23, Coverage Score: 0.9026</b>
</p>

 | Trial | Win/Loss | Time | Score |
 |:-----:|:--------:|:----:|:-----:|
 | 1 | Win | 0:25 | 1.155 |
 | 2 | Win | 0:22 | 0.606 |
 | 3 | Win | 0:27 | 0.719 |
 | 4 | Win | 0:22 | 1.038 |
 | 5 | Win | 0:22 | 1.073 |
 | 6 | Win | 0:22 | 1.06 |
 | 7 | Win | 0:22 | 1.046 |
 | 8 | Win | 0:22 | 1.151 |
 | 9 | Win | 0:26 | 0.558 |
 | 10 | Win | 0:23 | 0.62 |

![David1](https://github.com/kwalworth/CS460_WrestlingProject/assets/116377367/2952c8f2-08d9-4848-8797-fcacee0a8a22)

<p align="center">
  <b>David: Win Percentage: 30%, Average Time: 0:58, Coverage Score: 0.8756</b>
</p>

 | Trial | Win/Loss | Time | Score |
 |:-----:|:--------:|:----:|:-----:|
 | 1 | Loss | 0:37 | 1.256 |
 | 2 | Loss | 0:26 | 0.791 |
 | 3 | Win | 0:24 | 0.99 |
 | 4 | Loss | 0:30 | 0.899 |
 | 5 | Loss | 0:34 | 0.88 |
 | 6 | Loss | 3:00 | 0.866 |
 | 7 | Win | 0:32 | 0.71 |
 | 8 | Win | 0:24 | 0.99 |
 | 9 | Loss | 3:00 | 0.603 |
 | 10 | Loss | 0:22 | 0.771 |

 ![Eve](https://github.com/kwalworth/CS460_WrestlingProject/assets/116377367/5e4f4d23-9659-48b5-a9dc-2d2ee045a824)

<p align="center">
  <b>Eve: Win Percentage: 80%, Average Time: 2:32, Coverage Score: 1.6325</b>
</p>
 
 | Trial | Win/Loss | Time | Score |
 |:-----:|:--------:|:----:|:-----:|
 | 1 | Win | 2:03 | 1.487 |
 | 2 | Win | 3:00 | 1.681 |
 | 3 | Win | 2:08 | 1.54 |
 | 4 | Win | 3:00 | 1.681 |
 | 5 | Win | 3:00 | 1.681 |
 | 6 | Win | 2:13 | 1.593 |
 | 7 | Win | 3:00 | 1.681 |
 | 8 | Win | 2:13 | 1.593 |
 | 9 | Win | 2:31 | 1.821 |
 | 10 | Win | 2:12 | 1.567 |

 ![Fatima](https://github.com/kwalworth/CS460_WrestlingProject/assets/116377367/4c0d4c7a-ce22-43ed-9ac8-9ce703b48d71)

<p align="center">
  <b>Alice: Win Percentage: 70%, Average Time: 1:47, Coverage Score: 1.2004</b>
</p>
 
 | Trial | Win/Loss | Time | Score |
 |:-----:|:--------:|:----:|:-----:|
 | 1 | Win | 0:56 | 0.863 |
 | 2 | Win | 0:48 | 0.789 |
 | 3 | Win | 0:44 | 0.741 |
 | 4 | Loss | 1:57 | 1.336 |
 | 5 | Loss | 2:02 | 1.398 |
 | 6 | Loss | 2:29 | 2.068 |
 | 7 | Win | 1:48 | 1.311 |
 | 8 | Win | 1:06 | 0.97 |
 | 9 | Win | 3:00 | 1.264 |
 | 10 | Win | 3:00 | 1.264 |

 

### Conclusion
The Cyberbotics Humanoid Wrestling competition provided a unique challenge. Not only did a controller have to be able to make a humanoid robot move throughout an environment, it had to be prepared to interact with and compete against other robots. We decided the most important features to implement were path planning, fall detection, vision, and attacking the opponent which fell under task execution. The functions were implemented into the controller successfully as we were able to have a greater than 50% overall win ratio with the competing controllers. Looking forward we could improve the win ratio and perhaps get it to near 100% with more time and trials. Our attack algorithm could be more effecient if we lunged the robot forward instead of staying in the same location and just squatting and flailing the arms. Furthermore we believe the competition provided a valuable experience in dealing with autonomous robotics and helped lay the foundation for a interest in this field.


### Link to Project Video
Here is the link to the presentation [Project Video][link_toYOUTUBE].

[link_toYOUTUBE]: https://youtu.be/Ki5sl57S7JU

