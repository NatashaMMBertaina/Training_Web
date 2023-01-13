/*********************** 
 * Entr-Deteccion Test *
 ***********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.5.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Entr-deteccion';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InicioRoutineBegin());
flowScheduler.add(InicioRoutineEachFrame());
flowScheduler.add(InicioRoutineEnd());
const loop1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop1LoopBegin(loop1LoopScheduler));
flowScheduler.add(loop1LoopScheduler);
flowScheduler.add(loop1LoopEnd);
flowScheduler.add(inicio_2RoutineBegin());
flowScheduler.add(inicio_2RoutineEachFrame());
flowScheduler.add(inicio_2RoutineEnd());
const loop2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop2LoopBegin(loop2LoopScheduler));
flowScheduler.add(loop2LoopScheduler);
flowScheduler.add(loop2LoopEnd);
flowScheduler.add(inicio_3RoutineBegin());
flowScheduler.add(inicio_3RoutineEachFrame());
flowScheduler.add(inicio_3RoutineEnd());
const loop3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop3LoopBegin(loop3LoopScheduler));
flowScheduler.add(loop3LoopScheduler);
flowScheduler.add(loop3LoopEnd);
flowScheduler.add(FinRoutineBegin());
flowScheduler.add(FinRoutineEachFrame());
flowScheduler.add(FinRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'archivos/data_3_sound.mp3', 'path': 'archivos/data_3_sound.mp3'},
    {'name': 'archivos/data_3_flux_sound.wav', 'path': 'archivos/data_3_flux_sound.wav'},
    {'name': 'archivos/data4.flux.png', 'path': 'archivos/data4.flux.png'},
    {'name': 'archivos/sinusoidal_sound.mp3', 'path': 'archivos/sinusoidal_sound.mp3'},
    {'name': 'archivos/data5.png', 'path': 'archivos/data5.png'},
    {'name': 'archivos/data1.png', 'path': 'archivos/data1.png'},
    {'name': 'archivos/lineal_up_sound.wav', 'path': 'archivos/lineal_up_sound.wav'},
    {'name': 'archivos/data_1_flux_sound.mp3', 'path': 'archivos/data_1_flux_sound.mp3'},
    {'name': 'archivos/senoidal.png', 'path': 'archivos/senoidal.png'},
    {'name': 'archivos/continua.creciente.png', 'path': 'archivos/continua.creciente.png'},
    {'name': 'archivos/data_2_sound.mp3', 'path': 'archivos/data_2_sound.mp3'},
    {'name': 'archivos/data5.flux.png', 'path': 'archivos/data5.flux.png'},
    {'name': 'archivos/data_5_sound.wav', 'path': 'archivos/data_5_sound.wav'},
    {'name': 'archivos/data_5_sound.mp3', 'path': 'archivos/data_5_sound.mp3'},
    {'name': 'archivos/decrease_sound.wav', 'path': 'archivos/decrease_sound.wav'},
    {'name': 'archivos/data3.png', 'path': 'archivos/data3.png'},
    {'name': 'bloque2.xlsx', 'path': 'bloque2.xlsx'},
    {'name': 'archivos/data2.png', 'path': 'archivos/data2.png'},
    {'name': 'archivos/data_2_flux_sound.mp3', 'path': 'archivos/data_2_flux_sound.mp3'},
    {'name': 'archivos/lineal_up_sound.mp3', 'path': 'archivos/lineal_up_sound.mp3'},
    {'name': 'archivos/data_1_flux_sound.wav', 'path': 'archivos/data_1_flux_sound.wav'},
    {'name': 'archivos/decreciente.png', 'path': 'archivos/decreciente.png'},
    {'name': 'archivos/data_1_sound.mp3', 'path': 'archivos/data_1_sound.mp3'},
    {'name': 'archivos/data3.flux.png', 'path': 'archivos/data3.flux.png'},
    {'name': 'archivos/data_2_sound.wav', 'path': 'archivos/data_2_sound.wav'},
    {'name': 'archivos/square_sound.mp3', 'path': 'archivos/square_sound.mp3'},
    {'name': 'archivos/data_4_flux_sound.mp3', 'path': 'archivos/data_4_flux_sound.mp3'},
    {'name': 'archivos/data4.png', 'path': 'archivos/data4.png'},
    {'name': 'archivos/decrease_sound.mp3', 'path': 'archivos/decrease_sound.mp3'},
    {'name': 'archivos/data_3_sound.wav', 'path': 'archivos/data_3_sound.wav'},
    {'name': 'archivos/data_4_flux_sound.wav', 'path': 'archivos/data_4_flux_sound.wav'},
    {'name': 'archivos/data_4_sound.mp3', 'path': 'archivos/data_4_sound.mp3'},
    {'name': 'bloque1.xlsx', 'path': 'bloque1.xlsx'},
    {'name': 'archivos/sinusoidal_sound.wav', 'path': 'archivos/sinusoidal_sound.wav'},
    {'name': 'archivos/data_4_sound.wav', 'path': 'archivos/data_4_sound.wav'},
    {'name': 'archivos/square.png', 'path': 'archivos/square.png'},
    {'name': 'archivos/data1.flux.png', 'path': 'archivos/data1.flux.png'},
    {'name': 'archivos/data_5_flux_sound.wav', 'path': 'archivos/data_5_flux_sound.wav'},
    {'name': 'archivos/data_1_sound.wav', 'path': 'archivos/data_1_sound.wav'},
    {'name': 'archivos/data_3_flux_sound.mp3', 'path': 'archivos/data_3_flux_sound.mp3'},
    {'name': 'archivos/data2.flux.png', 'path': 'archivos/data2.flux.png'},
    {'name': 'archivos/data_5_flux_sound.mp3', 'path': 'archivos/data_5_flux_sound.mp3'},
    {'name': 'archivos/data_2_flux_sound.wav', 'path': 'archivos/data_2_flux_sound.wav'},
    {'name': 'archivos/square_sound.wav', 'path': 'archivos/square_sound.wav'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var InicioClock;
var text_2;
var Instruccion;
var bloque1Clock;
var sound1;
var image;
var text;
var key_resp;
var feedClock;
var feedback;
var inicio_2Clock;
var text_3;
var text_4;
var bloque2Clock;
var sound_2;
var text1;
var key_resp_3;
var inicio_3Clock;
var text_5;
var text_6;
var bloque3Clock;
var sound_1;
var image_2;
var text2;
var resp_2;
var feed2Clock;
var fb;
var FinClock;
var text_7;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Inicio"
  InicioClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '1°Bloque:\nFunciones Simples',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Instruccion = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruccion',
    text: 'Deberá presionar las siguientes teclas según sea el sonido que escuchó:\n\nArriba --> Creciente\n\nAbajo --> Decreciente\n\nIzquierda --> Senoidal\n\nDerecha --> Cuadrada',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "bloque1"
  bloque1Clock = new util.Clock();
  sound1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound1.setVolume(1.0);
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.8, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Usted escuchó una función:\n\nArriba --> Creciente\n\nAbajo --> Decreciente\n\nIzquierda --> Senoidal\n\nDerecha --> Cuadrada',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feed"
  feedClock = new util.Clock();
  feedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback',
    text: '',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "inicio_2"
  inicio_2Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '2°Bloque:\nLíneas de Absorción y Emisión',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Deberá identificar si lo que escucho es una línea de absorción, de emisión o ruido, presionando la tecla indicada.\n\nPara línea de Emisión --> Arriba\n\nPara línea de Absorción --> Abajo\n\nPara Ruido -->Izquierda',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "bloque2"
  bloque2Clock = new util.Clock();
  sound_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_2.setVolume(1.0);
  text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text1',
    text: 'Para línea de Emisión --> Arriba\n\nPara línea de Absorción --> Abajo\n\nPara Ruido --> Izquierda',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "inicio_3"
  inicio_3Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '3°Bloque:\nLineas de Absorción y Emisión con sonido e imagen',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Deberá identificar si lo que escucho y vio es una línea de absorción, de emisión o ruido.\n\nPara línea de Emisión --> Arriba\n\nPara línea de Absorción --> Abajo\n\nPara Ruido --> Izquierda',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "bloque3"
  bloque3Clock = new util.Clock();
  sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  sound_1.setVolume(1.0);
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.8, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text2',
    text: '',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feed2"
  feed2Clock = new util.Clock();
  fb = new visual.TextStim({
    win: psychoJS.window,
    name: 'fb',
    text: '',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Fin"
  FinClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'Entrenamiento concluido',
    font: 'Open Sans',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var InicioComponents;
function InicioRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Inicio' ---
    t = 0;
    InicioClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(12.100000);
    // update component parameters for each repeat
    // keep track of which components have finished
    InicioComponents = [];
    InicioComponents.push(text_2);
    InicioComponents.push(Instruccion);
    
    for (const thisComponent of InicioComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function InicioRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Inicio' ---
    // get current time
    t = InicioClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    
    // *Instruccion* updates
    if (t >= 2.1 && Instruccion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruccion.tStart = t;  // (not accounting for frame time here)
      Instruccion.frameNStart = frameN;  // exact frame index
      
      Instruccion.setAutoDraw(true);
    }

    frameRemains = 2.1 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Instruccion.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Instruccion.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InicioComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InicioRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Inicio' ---
    for (const thisComponent of InicioComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var loop1;
function loop1LoopBegin(loop1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'bloque1.xlsx',
      seed: undefined, name: 'loop1'
    });
    psychoJS.experiment.addLoop(loop1); // add the loop to the experiment
    currentLoop = loop1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop1 of loop1) {
      snapshot = loop1.getSnapshot();
      loop1LoopScheduler.add(importConditions(snapshot));
      loop1LoopScheduler.add(bloque1RoutineBegin(snapshot));
      loop1LoopScheduler.add(bloque1RoutineEachFrame());
      loop1LoopScheduler.add(bloque1RoutineEnd(snapshot));
      loop1LoopScheduler.add(feedRoutineBegin(snapshot));
      loop1LoopScheduler.add(feedRoutineEachFrame());
      loop1LoopScheduler.add(feedRoutineEnd(snapshot));
      loop1LoopScheduler.add(loop1LoopEndIteration(loop1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var loop2;
function loop2LoopBegin(loop2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'bloque2.xlsx',
      seed: undefined, name: 'loop2'
    });
    psychoJS.experiment.addLoop(loop2); // add the loop to the experiment
    currentLoop = loop2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop2 of loop2) {
      snapshot = loop2.getSnapshot();
      loop2LoopScheduler.add(importConditions(snapshot));
      loop2LoopScheduler.add(bloque2RoutineBegin(snapshot));
      loop2LoopScheduler.add(bloque2RoutineEachFrame());
      loop2LoopScheduler.add(bloque2RoutineEnd(snapshot));
      loop2LoopScheduler.add(loop2LoopEndIteration(loop2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var loop3;
function loop3LoopBegin(loop3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'bloque2.xlsx',
      seed: undefined, name: 'loop3'
    });
    psychoJS.experiment.addLoop(loop3); // add the loop to the experiment
    currentLoop = loop3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop3 of loop3) {
      snapshot = loop3.getSnapshot();
      loop3LoopScheduler.add(importConditions(snapshot));
      loop3LoopScheduler.add(bloque3RoutineBegin(snapshot));
      loop3LoopScheduler.add(bloque3RoutineEachFrame());
      loop3LoopScheduler.add(bloque3RoutineEnd(snapshot));
      loop3LoopScheduler.add(feed2RoutineBegin(snapshot));
      loop3LoopScheduler.add(feed2RoutineEachFrame());
      loop3LoopScheduler.add(feed2RoutineEnd(snapshot));
      loop3LoopScheduler.add(loop3LoopEndIteration(loop3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _key_resp_allKeys;
var bloque1Components;
function bloque1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bloque1' ---
    t = 0;
    bloque1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(14.100000);
    // update component parameters for each repeat
    sound1 = new sound.Sound({
    win: psychoJS.window,
    value: Sonido,
    secs: 4.0,
    });
    sound1.secs=4.0;
    sound1.setVolume(1.0);
    image.setImage(Img);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    bloque1Components = [];
    bloque1Components.push(sound1);
    bloque1Components.push(image);
    bloque1Components.push(text);
    bloque1Components.push(key_resp);
    
    for (const thisComponent of bloque1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function bloque1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bloque1' ---
    // get current time
    t = bloque1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound1
    if (t >= 0.0 && sound1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound1.tStart = t;  // (not accounting for frame time here)
      sound1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound1.play(); });  // screen flip
      sound1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (4.0 > 0.5) {
        sound1.stop();  // stop the sound (if longer than duration)
      }
      sound1.status = PsychoJS.Status.FINISHED;
    }
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    // *text* updates
    if (t >= 4.1 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 4.1 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 4.1 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 4.1 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['up', 'down', 'left', 'right'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp.keys == corrAns) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of bloque1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function bloque1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bloque1' ---
    for (const thisComponent of bloque1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound1.stop();  // ensure sound has stopped at end of routine
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fdb1_text;
var fdb1_col;
var feedComponents;
function feedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feed' ---
    t = 0;
    feedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.200000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from fb_code
    if (key_resp.corr) {
        fdb1_text = "Correcto!";
        fdb1_col = "green";
    } else {
        fdb1_text = "Incorrecto";
        fdb1_col = "red";
    }
    
    feedback.setColor(new util.Color(fdb1_col));
    feedback.setText(fdb1_text);
    // keep track of which components have finished
    feedComponents = [];
    feedComponents.push(feedback);
    
    for (const thisComponent of feedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feed' ---
    // get current time
    t = feedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback* updates
    if (t >= 0.2 && feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback.tStart = t;  // (not accounting for frame time here)
      feedback.frameNStart = frameN;  // exact frame index
      
      feedback.setAutoDraw(true);
    }

    frameRemains = 0.2 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feed' ---
    for (const thisComponent of feedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var inicio_2Components;
function inicio_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'inicio_2' ---
    t = 0;
    inicio_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(12.100000);
    // update component parameters for each repeat
    // keep track of which components have finished
    inicio_2Components = [];
    inicio_2Components.push(text_3);
    inicio_2Components.push(text_4);
    
    for (const thisComponent of inicio_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function inicio_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'inicio_2' ---
    // get current time
    t = inicio_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    
    // *text_4* updates
    if (t >= 2.1 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 2.1 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of inicio_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function inicio_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'inicio_2' ---
    for (const thisComponent of inicio_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var bloque2Components;
function bloque2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bloque2' ---
    t = 0;
    bloque2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(19.100000);
    // update component parameters for each repeat
    sound_2 = new sound.Sound({
    win: psychoJS.window,
    value: sonido,
    secs: 9.0,
    });
    sound_2.secs=9.0;
    sound_2.setVolume(1.0);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    bloque2Components = [];
    bloque2Components.push(sound_2);
    bloque2Components.push(text1);
    bloque2Components.push(key_resp_3);
    
    for (const thisComponent of bloque2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function bloque2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bloque2' ---
    // get current time
    t = bloque2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_2
    if (t >= 0.0 && sound_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_2.tStart = t;  // (not accounting for frame time here)
      sound_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_2.play(); });  // screen flip
      sound_2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 9.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (9.0 > 0.5) {
        sound_2.stop();  // stop the sound (if longer than duration)
      }
      sound_2.status = PsychoJS.Status.FINISHED;
    }
    
    // *text1* updates
    if (t >= 9.1 && text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text1.tStart = t;  // (not accounting for frame time here)
      text1.frameNStart = frameN;  // exact frame index
      
      text1.setAutoDraw(true);
    }

    frameRemains = 9.1 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text1.setAutoDraw(false);
    }
    
    // *key_resp_3* updates
    if (t >= 9.1 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 9.1 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['up', 'down', 'left'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_3.keys == corrAns2) {
            key_resp_3.corr = 1;
        } else {
            key_resp_3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of bloque2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function bloque2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bloque2' ---
    for (const thisComponent of bloque2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound_2.stop();  // ensure sound has stopped at end of routine
    // was no response the correct answer?!
    if (key_resp_3.keys === undefined) {
      if (['None','none',undefined].includes(corrAns2)) {
         key_resp_3.corr = 1;  // correct non-response
      } else {
         key_resp_3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    psychoJS.experiment.addData('key_resp_3.corr', key_resp_3.corr);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var inicio_3Components;
function inicio_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'inicio_3' ---
    t = 0;
    inicio_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(12.100000);
    // update component parameters for each repeat
    // keep track of which components have finished
    inicio_3Components = [];
    inicio_3Components.push(text_5);
    inicio_3Components.push(text_6);
    
    for (const thisComponent of inicio_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function inicio_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'inicio_3' ---
    // get current time
    t = inicio_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    
    // *text_6* updates
    if (t >= 2.1 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    frameRemains = 2.1 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of inicio_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function inicio_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'inicio_3' ---
    for (const thisComponent of inicio_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp_2_allKeys;
var bloque3Components;
function bloque3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bloque3' ---
    t = 0;
    bloque3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(19.100000);
    // update component parameters for each repeat
    sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: sonido,
    secs: 9.0,
    });
    sound_1.secs=9.0;
    sound_1.setVolume(1.0);
    image_2.setImage(img);
    text2.setText('Para línea de Emisión --> Arriba\n\nPara línea de Absorción --> Abajo\n\nPara Ruido --> Izquierda');
    resp_2.keys = undefined;
    resp_2.rt = undefined;
    _resp_2_allKeys = [];
    // keep track of which components have finished
    bloque3Components = [];
    bloque3Components.push(sound_1);
    bloque3Components.push(image_2);
    bloque3Components.push(text2);
    bloque3Components.push(resp_2);
    
    for (const thisComponent of bloque3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function bloque3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bloque3' ---
    // get current time
    t = bloque3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop sound_1
    if (t >= 0.0 && sound_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_1.tStart = t;  // (not accounting for frame time here)
      sound_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
      sound_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 9.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (9.0 > 0.5) {
        sound_1.stop();  // stop the sound (if longer than duration)
      }
      sound_1.status = PsychoJS.Status.FINISHED;
    }
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 9.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_2.setAutoDraw(false);
    }
    
    // *text2* updates
    if (t >= 9.1 && text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text2.tStart = t;  // (not accounting for frame time here)
      text2.frameNStart = frameN;  // exact frame index
      
      text2.setAutoDraw(true);
    }

    frameRemains = 9.1 + 10.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text2.setAutoDraw(false);
    }
    
    // *resp_2* updates
    if (t >= 9.1 && resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_2.tStart = t;  // (not accounting for frame time here)
      resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_2.clearEvents(); });
    }

    frameRemains = 9.1 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_2.status = PsychoJS.Status.FINISHED;
  }

    if (resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_2.getKeys({keyList: ['up', 'down', 'left'], waitRelease: false});
      _resp_2_allKeys = _resp_2_allKeys.concat(theseKeys);
      if (_resp_2_allKeys.length > 0) {
        resp_2.keys = _resp_2_allKeys[_resp_2_allKeys.length - 1].name;  // just the last key pressed
        resp_2.rt = _resp_2_allKeys[_resp_2_allKeys.length - 1].rt;
        // was this correct?
        if (resp_2.keys == corrAns2) {
            resp_2.corr = 1;
        } else {
            resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of bloque3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function bloque3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bloque3' ---
    for (const thisComponent of bloque3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound_1.stop();  // ensure sound has stopped at end of routine
    // was no response the correct answer?!
    if (resp_2.keys === undefined) {
      if (['None','none',undefined].includes(corrAns2)) {
         resp_2.corr = 1;  // correct non-response
      } else {
         resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_2.corr, level);
    }
    psychoJS.experiment.addData('resp_2.keys', resp_2.keys);
    psychoJS.experiment.addData('resp_2.corr', resp_2.corr);
    if (typeof resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_2.rt', resp_2.rt);
        routineTimer.reset();
        }
    
    resp_2.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fdb2_text;
var fdb2_col;
var feed2Components;
function feed2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feed2' ---
    t = 0;
    feed2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.200000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from fb_code_2
    if (resp_2.corr) {
        fdb2_text = "Correcto!";
        fdb2_col = "green";
    } else {
        fdb2_text = "Incorrecto";
        fdb2_col = "red";
    }
    
    fb.setColor(new util.Color(fdb2_col));
    fb.setText(fdb2_text);
    // keep track of which components have finished
    feed2Components = [];
    feed2Components.push(fb);
    
    for (const thisComponent of feed2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feed2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feed2' ---
    // get current time
    t = feed2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fb* updates
    if (t >= 0.2 && fb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fb.tStart = t;  // (not accounting for frame time here)
      fb.frameNStart = frameN;  // exact frame index
      
      fb.setAutoDraw(true);
    }

    frameRemains = 0.2 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fb.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feed2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feed2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feed2' ---
    for (const thisComponent of feed2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FinComponents;
function FinRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Fin' ---
    t = 0;
    FinClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    FinComponents = [];
    FinComponents.push(text_7);
    
    for (const thisComponent of FinComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FinRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Fin' ---
    // get current time
    t = FinClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_7.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FinComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FinRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Fin' ---
    for (const thisComponent of FinComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
