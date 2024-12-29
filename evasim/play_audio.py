import platform
import subprocess
 
import config # Module with the constants and parameters used in other modules.

# I stopped using the Playsound library because it was too much trouble!

# Playsound for Linux
if platform.system() == "Linux":
    # As future work, it would be interesting to use the SOX library as well as in the Audio Module of the physical robot.
    def playsound(audio_file, block = True):
        if block == True:
            play = subprocess.Popen(['play', audio_file], stdout=subprocess.PIPE)
            play.communicate()[0]
        else:
            play = subprocess.Popen(['play', audio_file], stdout=subprocess.PIPE)



