#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on abril 12, 2022, at 18:58
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
    originPath='C:\\Users\\Natasha\\Documents\\PsychoPy\\Entrenamiento-Workshop\\Entr-workshop.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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
    text='Deberá presionar los siguientes botones según sea el sonido que escuchó:\n\nUp --> Creciente\n\nDown --> Decreciente\n\nLeft --> Senoidal\n\nRight --> Cuadrada',
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
text = visual.TextStim(win=win, name='text',
    text='Usted escuchó una función:\n\nUp --> Creciente\n\nDown --> Decreciente\n\nLeft --> Senoidal\n\nRight --> Cuadrada',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
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

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Inicio"-------
continueRoutine = True
routineTimer.add(6.100000)
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
        if tThisFlipGlobal > Instruccion.tStartRefresh + 4.0-frameTolerance:
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
loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bloque1.xlsx'),
    seed=None, name='loop')
thisExp.addLoop(loop)  # add the loop to the experiment
thisLoop = loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
if thisLoop != None:
    for paramName in thisLoop:
        exec('{} = thisLoop[paramName]'.format(paramName))

for thisLoop in loop:
    currentLoop = loop
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "bloque1"-------
    continueRoutine = True
    routineTimer.add(10.100000)
    # update component parameters for each repeat
    sound1.setSound(Sonido, secs=5.0, hamming=True)
    sound1.setVolume(1.0, log=False)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    bloque1Components = [sound1, text, key_resp]
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
            if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
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
            if tThisFlipGlobal > key_resp.tStartRefresh + 5-frameTolerance:
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
    loop.addData('sound1.started', sound1.tStartRefresh)
    loop.addData('sound1.stopped', sound1.tStopRefresh)
    loop.addData('text.started', text.tStartRefresh)
    loop.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for loop (TrialHandler)
    loop.addData('key_resp.keys',key_resp.keys)
    loop.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        loop.addData('key_resp.rt', key_resp.rt)
    loop.addData('key_resp.started', key_resp.tStartRefresh)
    loop.addData('key_resp.stopped', key_resp.tStopRefresh)
    
    # ------Prepare to start Routine "feed"-------
    continueRoutine = True
    routineTimer.add(2.200000)
    # update component parameters for each repeat
    # Check if the key press was correct or not.
    # This routine will need to follow another routine with a 
    # key response component in it called "key_resp" 
    # and the "store correct" option enabled. 
    # If your experiment is missing that you will 
    # not receive feedback and an error message will be displayed.
    
    # If a key response component has been added and feedback is functioning.
    # 1. remove lines 12, 13, 15, 22 and 23.
    # 2. dedent lines 16 to 21
    
    text = 'no key_resp'
    col = 'black'
    
    try:
        if key_resp.corr:
            fdb_text = 'Correct!'
            fdb_col = 'green'
        else:
            fdb_text = 'Incorrect'
            fdb_col = 'red'
    except:
        print('\n1. a routine with a keyboard component in it called "key_resp"\n 2. In the key_Resp component in the "data" tab select "Store Correct".\n in the "Correct answer" field use "$corrAns" (where corrAns is a column header in your conditions file indicating the correct key press')
    
    feedback.setColor(fdb_col, colorSpace='rgb')
    feedback.setText(fdb_text)
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
    thisExp.addData('feedback.started', feedback.tStartRefresh)
    thisExp.addData('feedback.stopped', feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
