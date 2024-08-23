"""Prototype of Sund Controling software
The Idea: It's nescessary to control the sound level in noise sensitive area. Government has taken Quite a few measure to stop the sound but there are
still some peoplke who don't foloow the rules. The role of the software will be to detect the decible unit of the sound being played through the microphone 
of the speaker and according to the input given by the user in the limit box, it will stop the sound by itself if the sound goes above the limit set."""



import tkinter as tk
import sounddevice as sd
import numpy as np
import threading

class NoiseCutoffApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Noise Cutoff App")

        self.threshold_label = tk.Label(master, text="Threshold (dB):")
        self.threshold_label.pack()

        self.threshold_entry = tk.Entry(master)
        self.threshold_entry.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.recording = False
        self.stream = None

    def validate_threshold(self):
        try:
            threshold = float(self.threshold_entry.get())
            return threshold
        except ValueError:
            self.status_label.config(text="Invalid threshold value. Please enter a valid number.")
            return None

    def start_recording(self):
        threshold = self.validate_threshold()
        if threshold is None:
            return

        self.status_label.config(text="Recording...")

        def callback(indata, frames, time, status):
            if status:
                print(f"Error: {status}")
            volume_norm = np.linalg.norm(indata) * 10
            if volume_norm > threshold:
                self.status_label.config(text="Noise threshold crossed. Stopping recording.")
                self.stop_recording()

        self.stream = sd.InputStream(callback=callback)
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        recording_thread = threading.Thread(target=self.run_recording)
        recording_thread.start()

    def run_recording(self):
        with self.stream:
            sd.sleep(1000000)

    def stop_recording(self):
        self.status_label.config(text="")
        self.recording = False
        if self.stream:
            self.stream.stop()
            self.stream.close()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoiseCutoffApp(root)
    root.mainloop()
