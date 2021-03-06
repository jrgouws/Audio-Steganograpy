import ResultsAndTesting as RT
import dwtEncrypt
import fileprocessing as fp
import numpy as np
import matplotlib.pyplot as plt

import scipy.io.wavfile as scWave
from copy import deepcopy
import time
import os
import AES

textMessage = True
originalDecSamples = []
totalNoiseSNR = 0
allPaths = []

OBHs = [0]
#OBHs = [0,1,2]
coverFiles = ['C:/Users/Johan Gouws/Desktop/Survey/A_Alternative_kite-as_worlds_collide.wav',
              'C:/Users/Johan Gouws/Desktop/Survey/A_Blues_Big_Steve___the_Trainwreck-Sorry_.wav',
              'C:/Users/Johan Gouws/Desktop/Survey/A_Electronic_Effective_Now-Complete.wav',
              'C:/Users/Johan Gouws/Desktop/Survey/A_Jazz_Akbar_Muhammad_Quartet-Ebony_Beauty.wav',
              'C:/Users/Johan Gouws/Desktop/Survey/A_Pop_Arthur_Yoria-P_S_A_.wav',
              'C:/Users/Johan Gouws/Desktop/Survey/A_Rock_April_Sixth-Bring_Me_Down.wav']         

audioOrText = True

for t in range(0,len(coverFiles)):
      for OBH_index in range(0, len(OBHs)):
            AESkeyEncode = "THIS_IS_THE_KEY_USED_FOR_AES_ENCRYPTION"
            
            samplesOne, samplesTwo, rate = fp.getWaveSamples(coverFiles[t])
                                
            message = ""
                    
            
            messageObject = open('C:/Users/Johan Gouws/Desktop/Audio-Steganograpy/src/Media/text.txt', "r")
                
            # Extract the message as a string of characters
            message = messageObject.read()
            messageObject.close()
            
           
            originalCoverSamples = deepcopy(samplesOne) 
                              
            currentTime = time.time()
            stegoSamples, samplesUsed, capacityWarning = dwtEncrypt.dwtEncryptEncode(samplesOne, message, 512, '.txt')   
            
            stegoSamples = np.asarray(stegoSamples, dtype=np.float32, order = 'C')/ 32768.0
            
            
            fileLoc = ''
            if (t == 0):
                  scWave.write("C:/Users/Johan Gouws/Desktop/Survey/encode_alt_txt.wav", rate, stegoSamples)
                  fileLoc = "C:/Users/Johan Gouws/Desktop/Survey/encode_alt_txt.wav"
            elif(t==1):
                  scWave.write("C:/Users/Johan Gouws/Desktop/Survey/encode_blu_txt.wav", rate, stegoSamples)
                  fileLoc = "C:/Users/Johan Gouws/Desktop/Survey/encode_blu_txt.wav"
            elif(t==2):
                  scWave.write("C:/Users/Johan Gouws/Desktop/Survey/encode_ele_txt.wav", rate, stegoSamples)
                  fileLoc = "C:/Users/Johan Gouws/Desktop/Survey/encode_ele_txt.wav"
            elif(t==3):
                  scWave.write("C:/Users/Johan Gouws/Desktop/Survey/encode_jzz_txt.wav", rate, stegoSamples)
                  fileLoc = "C:/Users/Johan Gouws/Desktop/Survey/encode_jzz_txt.wav"
            elif(t==4):
                  scWave.write("C:/Users/Johan Gouws/Desktop/Survey/encode_pop_txt.wav", rate, stegoSamples)
                  fileLoc = "C:/Users/Johan Gouws/Desktop/Survey/encode_pop_txt.wav"
            elif(t==5):
                  scWave.write("C:/Users/Johan Gouws/Desktop/Survey/encode_rock_txt.wav", rate, stegoSamples)   
                  fileLoc = "C:/Users/Johan Gouws/Desktop/Survey/encode_rock_txt.wav"
            # Get the characteristics of the stego file
            
            stegoSamplesOne, stegoSamplesTwo, rate = fp.getWaveSamples(fileLoc)
            stegoSamples = np.asarray(stegoSamplesOne, dtype=np.float32, order = 'C') * 32768.0
            
            SNR = RT.getSNR(originalCoverSamples[0:samplesUsed], stegoSamples[0:samplesUsed] )
            
            print(SNR)