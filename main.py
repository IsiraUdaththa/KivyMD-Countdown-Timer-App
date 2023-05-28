from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.core.window import Window
import pygame
from playsound import playsound

Window.size = (1000, 1000)

class MainApp(MDApp):
    started = False
    seconds = 0
    count_time = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Countdown Timer'
        Clock.schedule_interval(self.update_time, 0)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.root.ids.start_stop.disabled = True if self.seconds == 0 else False

    def update_time(self, obj):
        if self.started:
            self.seconds -= obj
        minutes, seconds = divmod(self.seconds, 60)
        part_seconds = seconds * 100 % 100

        if self.seconds < 0:
            self.root.ids.stopwatch.color = "red"
            self.seconds = 0
        else:
            self.root.ids.stopwatch.color = "black"
            self.root.ids.stopwatch.text = (
                f'[size=150]{int(minutes):02}[/size]'
                f'[size=75]:[/size]'
                f'[size=150]{int(seconds):02}[/size]'
                f'[size=75].[/size]'
                f'[size=75] {int(part_seconds):02}[/size]'
            )
        self.root.ids.progress_bar.value = (self.seconds / self.count_time) * 100

    def start_stop(self):
        self.root.ids.start_stop.text = 'START' if self.started else 'STOP'
        self.started = not self.started
        self.root.ids.reset.disabled = True if self.started else False
        self.root.ids.sound.disabled = True if self.started else False
        self.root.ids.min4.disabled = True if self.started else False
        self.root.ids.min5.disabled = True if self.started else False

    def sound(self):

        sound_file = 'audio/bell.mp3'
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            

        except Exception as e:
            print(f"Failed to load or play the audio file: {sound_file}")
            rint("Error message:", e)

    def resume_app(self):
    # Resume your application logic here after the sound finishes playing
   	 pass


               
	    
    def min4(self):
        self.seconds = 60*4
        self.count_time = self.seconds
        if self.seconds==0:
                playsound('audio/bell.mp3')
        self.root.ids.start_stop.disabled = True if self.seconds == 0 else False
        

    def min5(self):
        self.seconds = 60*5 
        self.count_time = self.seconds
        self.root.ids.start_stop.disabled = True if self.seconds == 0 else False
        

    def reset(self):
        self.seconds = 0
        self.root.ids.start_stop.disabled = True if self.seconds == 0 else False


if __name__ == '__main__':
    MainApp().run()
