#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on abril 18, 2022, at 08:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'Entr-workshop'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Natasha\\Documents\\PsychoPy\\Entrenamiento-Workshop\\Entr-workshop_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1360, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Inicio"
InicioClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='1°Bloque:\nFunciones Simples',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Instruccion = visual.TextStim(win=win, name='Instruccion',
    text='Deberá presionar las siguientes teclas según sea el sonido que escuchó:\n\nArriba --> Creciente\n\nAbajo --> Decreciente\n\nIzquierda --> Senoidal\n\nDerecha --> Cuadrada',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "bloque1"
bloque1Clock = core.Clock()
sound1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound1')
sound1.setVolume(1.0)
image = visual.ImageStim(
    win=win,
    name='image', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(9, 3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='Usted escuchó una función:\n\nArriba --> Creciente\n\nAbajo --> Decreciente\n\nIzquierda --> Senoidal\n\nDerecha --> Cuadrada',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "feed"
feedClock = core.Clock()
feedback = visual.TextStim(win=win, name='feedback',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "inicio_2"
inicio_2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='2°Bloque:\nLíneas de Absorción y Emisión',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Deberá identificar si lo que escucho es una línea de absorción, de emisión o ruido, presionando la tecla indicada.\n\nPara línea de Emisión --> Arriba\n\nPara línea de Absorción --> Abajo\n\nPara Ruido -->Izquierda',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "bloque2"
bloque2Clock = core.Clock()
sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
text1 = visual.TextStim(win=win, name='text1',
    text='Para línea de Emisión --> Arriba\n\nPara línea de Absorción --> Abajo\n\nPara Ruido --> Izquierda',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "inicio_3"
inicio_3Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='3°Bloque:\nLineas de Absorción y Emisión con sonido e imagen',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='Deberá identificar si lo que escucho y vio es una línea de absorción, de emisión o ruido.\n\nPara línea de Emisión --> Arriba\n\nPara línea de Absorción --> Abajo\n\nPara Ruido --> Izquierda',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "bloque3"
bloque3Clock = core.Clock()
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(12, 5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text2 = visual.TextStim(win=win, name='text2',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
resp_2 = keyboard.Keyboard()

# Initialize components for Routine "feed2"
feed2Clock = core.Clock()
fb = visual.TextStim(win=win, name='fb',
    text='',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Fin"
FinClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Entrenamiento concluido',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Inicio"-------
continueRoutine = True
routineTimer.add(12.100000)
# update component parameters for each repeat
# keep track of which components have finished
InicioComponents = [text_2, Instruccion]
for thisComponent in InicioComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InicioClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Inicio"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InicioClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InicioClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *Instruccion* updates
    if Instruccion.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
        # keep track of start time/frame for later
        Instruccion.frameNStart = frameN  # exact frame index
        Instruccion.tStart = t  # local t and not account for scr refresh
        Instruccion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruccion, 'tStartRefresh')  # time at next scr refresh
        Instruccion.setAutoDraw(True)
    if Instruccion.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instruccion.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            Instruccion.tStop = t  # not accounting for scr refresh
            Instruccion.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instruccion, 'tStopRefresh')  # time at next scr refresh
            Instruccion.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InicioComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inicio"-------
for thisComponent in InicioComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('Instruccion.started', Instruccion.tStartRefresh)
thisExp.addData('Instruccion.stopped', Instruccion.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bloque1.xlsx'),
    seed=None, name='loop1')
thisExp.addLoop(loop1)  # add the loop to the experiment
thisLoop1 = loop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
if thisLoop1 != None:
    for paramName in thisLoop1:
        exec('{} = thisLoop1[paramName]'.format(paramName))

for thisLoop1 in loop1:
    currentLoop = loop1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
    if thisLoop1 != None:
        for paramName in thisLoop1:
            exec('{} = thisLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "bloque1"-------
    continueRoutine = True
    routineTimer.add(15.100000)
    # update component parameters for each repeat
    sound1.setSound(Sonido, secs=5.0, hamming=True)
    sound1.setVolume(1.0, log=False)
    image.setImage(Img)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    bloque1Components = [sound1, image, text, key_resp]
    for thisComponent in bloque1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    bloque1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "bloque1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = bloque1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=bloque1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound1
        if sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound1.frameNStart = frameN  # exact frame index
            sound1.tStart = t  # local t and not account for scr refresh
            sound1.tStartRefresh = tThisFlipGlobal  # on global time
            sound1.play(when=win)  # sync with win flip
        if sound1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound1.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                sound1.tStop = t  # not accounting for scr refresh
                sound1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound1, 'tStopRefresh')  # time at next scr refresh
                sound1.stop()
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 5.1-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 5.1-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['up','down','left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bloque1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "bloque1"-------
    for thisComponent in bloque1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound1.stop()  # ensure sound has stopped at end of routine
    loop1.addData('sound1.started', sound1.tStartRefresh)
    loop1.addData('sound1.stopped', sound1.tStopRefresh)
    loop1.addData('image.started', image.tStartRefresh)
    loop1.addData('image.stopped', image.tStopRefresh)
    loop1.addData('text.started', text.tStartRefresh)
    loop1.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for loop1 (TrialHandler)
    loop1.addData('key_resp.keys',key_resp.keys)
    loop1.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        loop1.addData('key_resp.rt', key_resp.rt)
    loop1.addData('key_resp.started', key_resp.tStartRefresh)
    loop1.addData('key_resp.stopped', key_resp.tStopRefresh)
    
    # ------Prepare to start Routine "feed"-------
    continueRoutine = True
    routineTimer.add(2.200000)
    # update component parameters for each repeat
    # If a key response component has been added and feedback is functioning.
    # 1. remove lines 12, 13, 15, 22 and 23.
    # 2. dedent lines 16 to 21
    
    if key_resp.corr:
            fdb1_text = 'Correcto!'
            fdb1_col = 'green'
    else:
            fdb1_text = 'Incorrecto'
            fdb1_col = 'red'
    feedback.setColor(fdb1_col, colorSpace='rgb')
    feedback.setText(fdb1_text)
    # keep track of which components have finished
    feedComponents = [feedback]
    for thisComponent in feedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feed"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback* updates
        if feedback.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            feedback.frameNStart = frameN  # exact frame index
            feedback.tStart = t  # local t and not account for scr refresh
            feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
            feedback.setAutoDraw(True)
        if feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback.tStop = t  # not accounting for scr refresh
                feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback, 'tStopRefresh')  # time at next scr refresh
                feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feed"-------
    for thisComponent in feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop1.addData('feedback.started', feedback.tStartRefresh)
    loop1.addData('feedback.stopped', feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop1'

# get names of stimulus parameters
if loop1.trialList in ([], [None], None):
    params = []
else:
    params = loop1.trialList[0].keys()
# save data for this loop
loop1.saveAsExcel(filename + '.xlsx', sheetName='loop1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
loop1.saveAsText(filename + 'loop1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "inicio_2"-------
continueRoutine = True
routineTimer.add(12.100000)
# update component parameters for each repeat
# keep track of which components have finished
inicio_2Components = [text_3, text_4]
for thisComponent in inicio_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inicio_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inicio_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = inicio_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inicio_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inicio_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inicio_2"-------
for thisComponent in inicio_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bloque2.xlsx'),
    seed=None, name='loop2')
thisExp.addLoop(loop2)  # add the loop to the experiment
thisLoop2 = loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
if thisLoop2 != None:
    for paramName in thisLoop2:
        exec('{} = thisLoop2[paramName]'.format(paramName))

for thisLoop2 in loop2:
    currentLoop = loop2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
    if thisLoop2 != None:
        for paramName in thisLoop2:
            exec('{} = thisLoop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "bloque2"-------
    continueRoutine = True
    routineTimer.add(23.100000)
    # update component parameters for each repeat
    sound_2.setSound(sonido, secs=13.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    bloque2Components = [sound_2, text1, key_resp_3]
    for thisComponent in bloque2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    bloque2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "bloque2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = bloque2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=bloque2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 13.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # *text1* updates
        if text1.status == NOT_STARTED and tThisFlip >= 13.1-frameTolerance:
            # keep track of start time/frame for later
            text1.frameNStart = frameN  # exact frame index
            text1.tStart = t  # local t and not account for scr refresh
            text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
            text1.setAutoDraw(True)
        if text1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text1.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                text1.tStop = t  # not accounting for scr refresh
                text1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text1, 'tStopRefresh')  # time at next scr refresh
                text1.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 13.1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['up','down','left'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # was this correct?
                if (key_resp_3.keys == str(corrAns2)) or (key_resp_3.keys == corrAns2):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bloque2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "bloque2"-------
    for thisComponent in bloque2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    loop2.addData('sound_2.started', sound_2.tStartRefresh)
    loop2.addData('sound_2.stopped', sound_2.tStopRefresh)
    loop2.addData('text1.started', text1.tStartRefresh)
    loop2.addData('text1.stopped', text1.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(corrAns2).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for loop2 (TrialHandler)
    loop2.addData('key_resp_3.keys',key_resp_3.keys)
    loop2.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        loop2.addData('key_resp_3.rt', key_resp_3.rt)
    loop2.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    loop2.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop2'

# get names of stimulus parameters
if loop2.trialList in ([], [None], None):
    params = []
else:
    params = loop2.trialList[0].keys()
# save data for this loop
loop2.saveAsExcel(filename + '.xlsx', sheetName='loop2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
loop2.saveAsText(filename + 'loop2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "inicio_3"-------
continueRoutine = True
routineTimer.add(12.100000)
# update component parameters for each repeat
# keep track of which components have finished
inicio_3Components = [text_5, text_6]
for thisComponent in inicio_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inicio_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inicio_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = inicio_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inicio_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
            text_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inicio_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inicio_3"-------
for thisComponent in inicio_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Bloque3.xlsx'),
    seed=None, name='loop3')
thisExp.addLoop(loop3)  # add the loop to the experiment
thisLoop3 = loop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
if thisLoop3 != None:
    for paramName in thisLoop3:
        exec('{} = thisLoop3[paramName]'.format(paramName))

for thisLoop3 in loop3:
    currentLoop = loop3
    # abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
    if thisLoop3 != None:
        for paramName in thisLoop3:
            exec('{} = thisLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "bloque3"-------
    continueRoutine = True
    routineTimer.add(23.100000)
    # update component parameters for each repeat
    sound_1.setSound(sonido, secs=13.0, hamming=True)
    sound_1.setVolume(1.0, log=False)
    image_2.setImage(img)
    text2.setText('Para línea de Emisión --> Arriba\n\nPara línea de Absorción --> Abajo\n\nPara Ruido --> Izquierda')
    resp_2.keys = []
    resp_2.rt = []
    _resp_2_allKeys = []
    # keep track of which components have finished
    bloque3Components = [sound_1, image_2, text2, resp_2]
    for thisComponent in bloque3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    bloque3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "bloque3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = bloque3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=bloque3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 13.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 13.0-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *text2* updates
        if text2.status == NOT_STARTED and tThisFlip >= 13.1-frameTolerance:
            # keep track of start time/frame for later
            text2.frameNStart = frameN  # exact frame index
            text2.tStart = t  # local t and not account for scr refresh
            text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text2, 'tStartRefresh')  # time at next scr refresh
            text2.setAutoDraw(True)
        if text2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                text2.tStop = t  # not accounting for scr refresh
                text2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text2, 'tStopRefresh')  # time at next scr refresh
                text2.setAutoDraw(False)
        
        # *resp_2* updates
        waitOnFlip = False
        if resp_2.status == NOT_STARTED and tThisFlip >= 13.1-frameTolerance:
            # keep track of start time/frame for later
            resp_2.frameNStart = frameN  # exact frame index
            resp_2.tStart = t  # local t and not account for scr refresh
            resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_2, 'tStartRefresh')  # time at next scr refresh
            resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                resp_2.tStop = t  # not accounting for scr refresh
                resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_2, 'tStopRefresh')  # time at next scr refresh
                resp_2.status = FINISHED
        if resp_2.status == STARTED and not waitOnFlip:
            theseKeys = resp_2.getKeys(keyList=['up','down','left'], waitRelease=False)
            _resp_2_allKeys.extend(theseKeys)
            if len(_resp_2_allKeys):
                resp_2.keys = _resp_2_allKeys[-1].name  # just the last key pressed
                resp_2.rt = _resp_2_allKeys[-1].rt
                # was this correct?
                if (resp_2.keys == str(corrAns2)) or (resp_2.keys == corrAns2):
                    resp_2.corr = 1
                else:
                    resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bloque3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "bloque3"-------
    for thisComponent in bloque3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    loop3.addData('sound_1.started', sound_1.tStartRefresh)
    loop3.addData('sound_1.stopped', sound_1.tStopRefresh)
    loop3.addData('image_2.started', image_2.tStartRefresh)
    loop3.addData('image_2.stopped', image_2.tStopRefresh)
    loop3.addData('text2.started', text2.tStartRefresh)
    loop3.addData('text2.stopped', text2.tStopRefresh)
    # check responses
    if resp_2.keys in ['', [], None]:  # No response was made
        resp_2.keys = None
        # was no response the correct answer?!
        if str(corrAns2).lower() == 'none':
           resp_2.corr = 1;  # correct non-response
        else:
           resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for loop3 (TrialHandler)
    loop3.addData('resp_2.keys',resp_2.keys)
    loop3.addData('resp_2.corr', resp_2.corr)
    if resp_2.keys != None:  # we had a response
        loop3.addData('resp_2.rt', resp_2.rt)
    loop3.addData('resp_2.started', resp_2.tStartRefresh)
    loop3.addData('resp_2.stopped', resp_2.tStopRefresh)
    
    # ------Prepare to start Routine "feed2"-------
    continueRoutine = True
    routineTimer.add(2.200000)
    # update component parameters for each repeat
    # If a key response component has been added and feedback is functioning.
    # 1. remove lines 12, 13, 15, 22 and 23.
    # 2. dedent lines 16 to 21
    
    
    if resp_2.corr:
            fdb2_text = 'Correcto!'
            fdb2_col = 'green'
    else:
            fdb2_text = 'Incorrecto'
            fdb2_col = 'red'
    fb.setColor(fdb2_col, colorSpace='rgb')
    fb.setText(fdb2_text)
    # keep track of which components have finished
    feed2Components = [fb]
    for thisComponent in feed2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feed2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feed2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feed2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feed2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fb* updates
        if fb.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            fb.frameNStart = frameN  # exact frame index
            fb.tStart = t  # local t and not account for scr refresh
            fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fb, 'tStartRefresh')  # time at next scr refresh
            fb.setAutoDraw(True)
        if fb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fb.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fb.tStop = t  # not accounting for scr refresh
                fb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fb, 'tStopRefresh')  # time at next scr refresh
                fb.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feed2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feed2"-------
    for thisComponent in feed2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop3.addData('fb.started', fb.tStartRefresh)
    loop3.addData('fb.stopped', fb.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop3'

# get names of stimulus parameters
if loop3.trialList in ([], [None], None):
    params = []
else:
    params = loop3.trialList[0].keys()
# save data for this loop
loop3.saveAsExcel(filename + '.xlsx', sheetName='loop3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
loop3.saveAsText(filename + 'loop3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Fin"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
FinComponents = [text_7]
for thisComponent in FinComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Fin"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin"-------
for thisComponent in FinComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='tab')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
