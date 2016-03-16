#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.03), Sun Jan 31 12:22:50 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'switch_task'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()

trial_fixation = visual.TextStim(win=win, ori=0, name='trial_fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
trial_leftShape = visual.Rect(win=win, name='trial_leftShape',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[-0.5, 0],
    lineWidth=1, lineColor=[0,1, 0], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0,depth=-3.0, 
interpolate=True)
trial_rightShape = visual.Rect(win=win, name='trial_rightShape',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0.5, 0],
    lineWidth=1, lineColor=[0,1,0], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0,depth=-4.0, 
interpolate=True)
trial_debugtxt = visual.TextStim(win=win, ori=0, name='trial_debugtxt',
    text='default text',    font='Arial',
    pos=[0, .75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
leftimg_opacity = 0
rightimg_opacity = 0

trial_duration = 2 if random()<=0.5 else 3
trial_starttime = trialClock.GetTime()
trial_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
trial_response.status = NOT_STARTED
# keep track of which components have finished
trialComponents = []
trialComponents.append(trial_fixation)
trialComponents.append(trial_response)
trialComponents.append(trial_leftShape)
trialComponents.append(trial_rightShape)
trialComponents.append(trial_debugtxt)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    debugtext = trial_response.keys
    
    leftimg_opacity = 0
    rightimg_opacity = 0
    if trial_response.keys == "left":
        leftimg_opacity = 1
    elif trial_response.keys == "right":
        rightimg_opacity = 1
    
    if trialClock.GetTime()
    
    # *trial_fixation* updates
    if t >= 0.0 and trial_fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        trial_fixation.tStart = t  # underestimates by a little under one frame
        trial_fixation.frameNStart = frameN  # exact frame index
        trial_fixation.setAutoDraw(True)
    
    # *trial_response* updates
    if t >= 0.0 and trial_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        trial_response.tStart = t  # underestimates by a little under one frame
        trial_response.frameNStart = frameN  # exact frame index
        trial_response.status = STARTED
        # keyboard checking is just starting
        trial_response.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if trial_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['left', 'right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            trial_response.keys = theseKeys[-1]  # just the last key pressed
            trial_response.rt = trial_response.clock.getTime()
    
    # *trial_leftShape* updates
    if t >= 0.0 and trial_leftShape.status == NOT_STARTED:
        # keep track of start time/frame for later
        trial_leftShape.tStart = t  # underestimates by a little under one frame
        trial_leftShape.frameNStart = frameN  # exact frame index
        trial_leftShape.setAutoDraw(True)
    if trial_leftShape.status == STARTED:  # only update if being drawn
        trial_leftShape.setOpacity(leftimg_opacity, log=False)
    
    # *trial_rightShape* updates
    if t >= 0.0 and trial_rightShape.status == NOT_STARTED:
        # keep track of start time/frame for later
        trial_rightShape.tStart = t  # underestimates by a little under one frame
        trial_rightShape.frameNStart = frameN  # exact frame index
        trial_rightShape.setAutoDraw(True)
    if trial_rightShape.status == STARTED:  # only update if being drawn
        trial_rightShape.setOpacity(rightimg_opacity, log=False)
    
    # *trial_debugtxt* updates
    if t >= 0.0 and trial_debugtxt.status == NOT_STARTED:
        # keep track of start time/frame for later
        trial_debugtxt.tStart = t  # underestimates by a little under one frame
        trial_debugtxt.frameNStart = frameN  # exact frame index
        trial_debugtxt.setAutoDraw(True)
    if trial_debugtxt.status == STARTED:  # only update if being drawn
        trial_debugtxt.setText(debugtext, log=False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if trial_response.keys in ['', [], None]:  # No response was made
   trial_response.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('trial_response.keys',trial_response.keys)
if trial_response.keys != None:  # we had a response
    thisExp.addData('trial_response.rt', trial_response.rt)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

win.close()
core.quit()
