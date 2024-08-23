# Python_Baed_projects
Program 1:
Number Guessing Game with a user interactive GUI

 Uses Tkinter module provided by Python to create a user friendly interface for the player to play te game.
 Uses Random module, another module provided by Python which selects a randon number from between the range provided by te coder.
 Uses Simpledialog module to provide simple dialogues boxes in case there is a need to make input prompt to the user to give inputs.
 Uses messagebox module is yet anotther module provided by Pytho which  displayes warnings, success prompts or any other kind of prompts other than input from to the user.

 In the program here, using the above mentioned modules, a game window is created first asking or credentials to login into the gem window and after the game starts the user has to guess the number util he has guessed the number correctly for the game to terminate. 


Program 2:
Sound Controller Softer based on Python.

The provided code is a prototype for a noise control application using Python's Tkinter for the GUI and the `sounddevice` library for audio input. The application allows users to set a noise threshold in decibels. When the "Start" button is pressed, the app begins recording audio through the microphone. If the noise level exceeds the set threshold, the recording stops automatically. The GUI includes input fields for the threshold, start and stop buttons, and a status label to display messages. The recording process runs in a separate thread to keep the GUI responsive. The app uses a callback function to monitor the audio levels in real-time. The `validate_threshold` method ensures the threshold is a valid number. The `start_recording` method initiates the recording process and updates the GUI. The `stop_recording` method stops the recording and resets the GUI. The `run_recording` method keeps the recording active until the threshold is crossed. The main block initializes the Tkinter root and starts the application. This setup allows for effective noise monitoring and control in noise-sensitive areas.