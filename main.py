from pygame import mixer, _sdl2 as devicer
import os
import configparser
from colorama import Fore as F
from tkinter import filedialog
import keyboard
from time import sleep as timeout
import sys
import sounddevice as sd
import soundfile as sf


class Main():
    def __init__(self):
        self.Setting_File="config.ini"
        self.DefaultDir=""
        self.SelectedSounds=[]
        self.Sounds=[]
        self.Offset=-1
        if os.path.exists(self.Setting_File):


            self.Program()
        else:
            self.SetUp()


    def Back(self):
        try:
            if self.Offset > -1:
                self.Offset-=12
                if self.Offset <=-1:
                    self.Offset=-1
                self.SelectedSounds=[]
                self.SoundBoardSystem()
        except:
            return

    def Front(self):
        try:
            if not len(self.Sounds)<=self.Offset:
                
                
                self.SelectedSounds=[]
                self.SoundBoardSystem()
        except:
            return


    def Program(self):
        # settings
        self.Microphone=self.ReadSetting("DEFAULT","microphone")
        self.id=self.ReadSetting("DEFAULT","id")
        self.DefaultVolume=self.ReadSetting("DEFAULT","volume")
        self.SoundFolder=self.ReadSetting("DEFAULT","sound_folder")
        self.BackB=self.ReadSetting("CONTROLS","back")
        self.Next=self.ReadSetting("CONTROLS","next")
        self.Prev=self.ReadSetting("CONTROLS","prev")
        self.Inter1=self.ReadSetting("CONTROLS","inter1")
        self.Inter2=self.ReadSetting("CONTROLS","inter2")
        self.Inter3=self.ReadSetting("CONTROLS","inter3")
        self.Inter4=self.ReadSetting("CONTROLS","inter4")
        self.Inter5=self.ReadSetting("CONTROLS","inter5")
        self.Inter6=self.ReadSetting("CONTROLS","inter6")
        self.Cancel=self.ReadSetting("CONTROLS","cancel")

        self.DefaultDir=self.SoundFolder
        os.system("cls")
        print(f"""Selected Microphone: {self.Microphone}
Selected Volume: {self.DefaultVolume}
Selected Folder: {self.SoundFolder}""")
        input("\n\nPress Enter to continue...")
        os.system("cls")
        self.MainMenu()

        
    def MainMenu(self):
        print(f"""{F.LIGHTRED_EX}--SOUND{F.MAGENTA}BOARD--{F.WHITE}
{F.LIGHTBLACK_EX}Microphone: {self.Microphone}
Default Volume: {self.DefaultVolume}{F.WHITE}

1: Open SoundBoard

2: Set Up

3: Close
        """)
    
        try:
            Option=int(input("Select Option: "))
        except:
            os.system("cls")
            print("OPTION CANT BE STRING!")
            input()
            self.MainMenu()
    
        if Option == 1:
            self.SoundBoardSystem()
        elif Option == 2:
            self.SetUp()
        elif Option == 3:
            sys.exit(1)
            return

    def PlaySound(self, SoundNumber,Volume):
        try:
            data, fs = sf.read(f"{self.DefaultDir}/{self.SelectedSounds[SoundNumber]}")
            
            sd.play(data, samplerate=fs, device="CABLE In 16ch (VB-Audio Virtual Cable), Windows DirectSound", blocking=False)
            mixer.music.load(f"{self.DefaultDir}/{self.SelectedSounds[SoundNumber]}")
            mixer.music.set_volume(float(Volume))
            mixer.music.play()
        except Exception as e:
            print(e)
            pass

    
        




    def SoundBoardSystem(self):
        mixer.init()
        os.system("cls")
        print(f"""{F.LIGHTRED_EX}--SOUND{F.MAGENTA}BOARD--{F.WHITE}
{F.LIGHTBLACK_EX}Microphone: {self.Microphone}
Default Volume: {self.DefaultVolume}{F.WHITE}
                """)
 
        self.Files=os.listdir(self.SoundFolder)
        self.Sounds=[]
        
        for i in self.Files:
            if i.endswith(".mp3") or i.endswith(".wav"):
                self.Sounds.append(i)
        
        for s in range(6):
            try:
                self.Offset+=1
                self.SelectedSounds.append(self.Sounds[self.Offset])
                print(f"{self.Offset}: {self.Sounds[self.Offset]}\n")
            except:
                continue

        print(f"\n\nPage Section: {self.Offset}")
        
        while True:
            Event=keyboard.read_event()
            if Event.event_type==keyboard.KEY_DOWN:
                if Event.name==self.Prev:
                    self.Back()
                elif Event.name == self.Cancel:
                    mixer.music.stop()
                    mixer.music.unload()
                    sd.stop()
                elif Event.name == self.Next:
                    self.Front()
                elif Event.name == self.Inter1:
                    self.PlaySound(0,self.DefaultVolume)
                elif Event.name == self.Inter2:
                    self.PlaySound(1,self.DefaultVolume)
                elif Event.name == self.Inter3:
                    self.PlaySound(2,self.DefaultVolume)
                elif Event.name == self.Inter4:
                    self.PlaySound(3, self.DefaultVolume)
                elif Event.name == self.Inter5:
                    self.PlaySound(4, self.DefaultVolume)
                elif Event.name == self.Inter6:
                    self.PlaySound(5, self.DefaultVolume)
                elif Event.name==self.BackB:
                    os.system("cls")
                    self.MainMenu()
            timeout(0.001)
                

        

            
        

    def ReadSetting(self, ROOT:str, Variable:str):
        setting=configparser.ConfigParser()
        setting.read(self.Setting_File)
        return setting.get(ROOT,Variable)

    
    def SetUp(self):
        mixer.init()
        os.system("cls")
        self.Microphones=devicer.audio.get_audio_device_names(True)
        localint_=0
        for i in self.Microphones:
            
            print(f"\n{localint_}: {i}\n")
            localint_+=1
        localint_=0

        try:
            self.MicrophoneSelection=int(input("Input Microphone Number: "))
            self.DefaultVolume=float(input("\nInput Default Volume: "))
            self.SoundFolder = filedialog.askdirectory(title='Please choose a Sound Folder.')
            os.system("cls")
            print("Set a Key for 'Back'! (Press, to set a key)")
            self.BackB= keyboard.read_key()
            timeout(1)

            os.system("cls")
            print("Set a Key for 'Next'! (Press, to set a key)")
            self.Next= keyboard.read_key()
            timeout(1)

            os.system("cls")
            print("Set a Key for 'Prev'! (Press, to set a key)")
            self.Prev= keyboard.read_key()
            timeout(1)

            os.system("cls")
            print("Set a Key for 'Inter 1'! (Press, to set a key)")
            self.Inter1= keyboard.read_key()
            timeout(1)

            os.system("cls")
            print("Set a Key for 'Inter 2'! (Press, to set a key)")
            self.Inter2= keyboard.read_key()
            timeout(1)

            os.system("cls")
            print("Set a Key for 'Inter 3'! (Press, to set a key)")
            self.Inter3= keyboard.read_key()
            timeout(1)

            os.system("cls")
            print("Set a Key for 'Inter 4'! (Press, to set a key)")
            self.Inter4= keyboard.read_key()
            timeout(1)

            os.system("cls")                                      
            print("Set a Key for 'Inter 5'! (Press, to set a key)")
            self.Inter5= keyboard.read_key()
            timeout(1)
            
            os.system("cls")                                      
            print("Set a Key for 'Inter 6'! (Press, to set a key)")                       
            self.Inter6= keyboard.read_key()
            timeout(1)

            os.system("cls")                                      
            print("Set a Key for 'Cancel'! (Press, to set a key)")                       
            self.Cancel= keyboard.read_key()
            timeout(1)                       
        except:
            os.system("cls")

            print("Error: Can not be a string")
            return

        self.id=self.MicrophoneSelection

        self.MicrophoneSelection=self.Microphones[self.MicrophoneSelection]

        os.system("cls")
        print(f"The Program Will Configure...")
        config= configparser.ConfigParser()

        config['DEFAULT'] = {"microphone": self.MicrophoneSelection,
                             "id": self.id,
                             "volume": self.DefaultVolume,
                             "sound_folder":self.SoundFolder}

        config['CONTROLS'] = {"back": self.BackB,
                              "next": self.Next,
                              "prev": self.Prev,
                              "inter1": self.Inter1,
                              "inter2": self.Inter2,
                              "inter3": self.Inter3,
                              "inter4": self.Inter4,
                              "inter5": self.Inter5,
                              "inter6": self.Inter6,
                              "cancel": self.Cancel}

        with open(self.Setting_File, "w") as f:
            config.write(f)

        self.Program()


        

if __name__=="__main__":
    
    Main()
    
mixer.quit() 