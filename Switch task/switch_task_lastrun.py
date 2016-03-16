#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.03), Tue Mar 15 14:53:04 2016
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
    originPath=u'/Users/dmf025/Google Drive/Lab/users/David/projects/timing_tasks/experiment/Switch task/switch_task.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
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
short = 2
pshort = 0.5
long = 3
score = 0

block_number = 1
trial_number = 0 

backgroundColor = [0, 0, 0] # mirrors the background, doesn't set it.
responseColor = [0, 1, 0] # sets the response color
trial_fixation = visual.TextStim(win=win, ori=0, name='trial_fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
trial_leftShape = visual.Rect(win=win, name='trial_leftShape',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[-0.5, 0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-3.0, 
interpolate=True)
trial_rightShape = visual.Rect(win=win, name='trial_rightShape',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0.5, 0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
trial_debugtxt = visual.TextStim(win=win, ori=0, name='trial_debugtxt',
    text='default text',    font='Arial',
    pos=[0, .75], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
ISI_ = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_')

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

feedback_leftShape = visual.Rect(win=win, name='feedback_leftShape',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[-0.5, 0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
feedback_rightShape = visual.Rect(win=win, name='feedback_rightShape',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0.5, 0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=30, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    left_img = {"line": backgroundColor, 
                "fill": backgroundColor}
    right_img = {"line": backgroundColor, 
                "fill": backgroundColor}
    
    ISI_duration = 0.5 + random()
    trial_duration = short if random()<=pshort else long
    trial_and_ISI_duration = ISI_duration + trial_duration
    
    nresponses = 0
    trial_number += 1
    trial_starttime = globalClock.getTime()
    last_response = ""
    
    
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    trial_leftShape.setFillColor(left_img["fill"])
    trial_rightShape.setFillColor(right_img["fill"])
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(trial_fixation)
    trialComponents.append(response)
    trialComponents.append(trial_leftShape)
    trialComponents.append(trial_rightShape)
    trialComponents.append(trial_debugtxt)
    trialComponents.append(ISI_)
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
        debugtext = [trial_duration, score]
        
        left_img["line"] = backgroundColor
        right_img["line"] = backgroundColor
        
        if response.keys:
            last_response = response.keys[-1]
            if last_response == "left":
                left_img["line"] = responseColor
            elif last_response == "right":
                right_img["line"] = responseColor
        
        # they have to make a long response so we get
        # the entire distribution
        if t >= trial_and_ISI_duration:
            continueRoutine = False
        
        # *trial_fixation* updates
        if t >= ISI_duration and trial_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_fixation.tStart = t  # underestimates by a little under one frame
            trial_fixation.frameNStart = frameN  # exact frame index
            trial_fixation.setAutoDraw(True)
        
        # *response* updates
        if t >= ISI_duration and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys.extend(theseKeys)  # storing all keys
                response.rt.append(response.clock.getTime())
        
        # *trial_leftShape* updates
        if t >= ISI_duration and trial_leftShape.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_leftShape.tStart = t  # underestimates by a little under one frame
            trial_leftShape.frameNStart = frameN  # exact frame index
            trial_leftShape.setAutoDraw(True)
        if trial_leftShape.status == STARTED:  # only update if being drawn
            trial_leftShape.setLineColor(left_img["line"], log=False)
        
        # *trial_rightShape* updates
        if t >= ISI_duration and trial_rightShape.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_rightShape.tStart = t  # underestimates by a little under one frame
            trial_rightShape.frameNStart = frameN  # exact frame index
            trial_rightShape.setAutoDraw(True)
        if trial_rightShape.status == STARTED:  # only update if being drawn
            trial_rightShape.setLineColor(right_img["line"], log=False)
        
        # *trial_debugtxt* updates
        if t >= ISI_duration and trial_debugtxt.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_debugtxt.tStart = t  # underestimates by a little under one frame
            trial_debugtxt.frameNStart = frameN  # exact frame index
            trial_debugtxt.setAutoDraw(True)
        if trial_debugtxt.status == STARTED:  # only update if being drawn
            trial_debugtxt.setText(debugtext, log=False)
        # *ISI_* period
        if t >= 0 and ISI_.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_.tStart = t  # underestimates by a little under one frame
            ISI_.frameNStart = frameN  # exact frame index
            ISI_.start(ISI_duration)
        elif ISI_.status == STARTED: #one frame should pass before updating params and completing
            ISI_.complete() #finish the static period
        
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
    if response.keys:
        if trial_duration == short and last_response == "left":
            score += 1
            correct = True
        elif trial_duration == long and last_response == "right":
            score += 1
            correct = True
        else:
            correct = False
    else:
        last_response = ""
        response.keys = [np.nan]
        response.rt = [np.nan]
        correct = False
    
    # Record all key presses
    for key, rt in zip(response.keys, response.rt):
        thisExp.addData("response", key)
        thisExp.addData("response_time", rt)
        thisExp.addData("ISI", ISI_duration)
        thisExp.addData("interval", trial_duration)
        thisExp.addData("time", trial_starttime)
        thisExp.addData("block_number", block_number)
        thisExp.addData("trial_number", trial_number) # auto-record is 0-based, I want 1-based
        thisExp.addData("score", score)
        thisExp.addData("correct", correct)
        thisExp.nextEntry()
    # check responses
    if response.keys in ['', [], None]:  # No response was made
       response.keys=None
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    left_img = {"line": backgroundColor, 
                "fill": backgroundColor}
    right_img = {"line": backgroundColor, 
                "fill": backgroundColor}
    
    left_img["line"] = responseColor if last_response ==" left" else backgroundColor
    right_img["line"] = responseColor if last_response == "right" else backgroundColor
    
    if trial_duration == short:
        left_img["fill"] = "green" if correct else "red"
    elif trial_duration == long:
        right_img["fill"] = "green" if correct else "red"
    feedback_leftShape.setFillColor(left_img["fill"])
    feedback_leftShape.setLineColor(left_img["line"])
    feedback_rightShape.setFillColor(right_img["fill"])
    feedback_rightShape.setLineColor(right_img["line"])
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(feedback_leftShape)
    feedbackComponents.append(feedback_rightShape)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback_leftShape* updates
        if t >= 0 and feedback_leftShape.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_leftShape.tStart = t  # underestimates by a little under one frame
            feedback_leftShape.frameNStart = frameN  # exact frame index
            feedback_leftShape.setAutoDraw(True)
        if feedback_leftShape.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            feedback_leftShape.setAutoDraw(False)
        
        # *feedback_rightShape* updates
        if t >= 0 and feedback_rightShape.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_rightShape.tStart = t  # underestimates by a little under one frame
            feedback_rightShape.frameNStart = frameN  # exact frame index
            feedback_rightShape.setAutoDraw(True)
        if feedback_rightShape.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            feedback_rightShape.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 30 repeats of 'trials'



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
