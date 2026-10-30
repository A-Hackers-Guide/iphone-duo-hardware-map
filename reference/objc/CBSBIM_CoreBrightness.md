# `CBSBIM`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _timerQueue;
@"NSObject<OS_os_log>" _log;
@"CBDisplayModule" _displayModule;
B _sbimEnabled;
B _isMonitoring;
@"CBEDR" _edr;
B _edrOn;
^{__IOMobileFramebuffer=} _iomfb;
I _iomfbService;
@"NSObject<OS_dispatch_source>" _dataTimer;
@"NSObject<OS_dispatch_source>" _mitigationTimer;
r^[3f] _limits;
I _limitsSize;
{MitigationState="stage"i"violation"B"sbim_reset_frequency"I"sbim_timer_interval"I"mitigation_timer_interval"I"sbim_size"I"delta_factor"f"minutes_per_stop_mitigate"f"minutes_per_stop_recovery"f"sbim_above_max"i"sbim_sustain_max"i"sbim_above_num"i"sbim_sustain_num"i"lastStateUpdate_"d"sbim_read_stage"I"lastSBIMBlock_"{IOMFBShortTermBIM="version"I""(?="v1"{?="sbim"[3I]"duration_us"Q})}"scalingFactor"f} mitigation;
{valarray<float>="__begin_"^f"__end_"^f} _previousAccumulatedSBIM;
f _sdrBrightness;
f _currentHeadroom;
f _currentHeadroomRequest;
f _cap;
f _edrThreshold;
```

## Properties

```
@property (Tf,V_sdrBrightness) sdrBrightness;
@property (Tf,V_currentHeadroom) currentHeadroom;
@property (Tf,N,SsetCurrentHeadroomRequest:,V_currentHeadroomRequest) currentHeadroomRequest;
@property (Tf,R,V_cap) cap;
@property (Tf,R,V_edrThreshold) edrThreshold;
```

## Instance methods

```
-[CBSBIM enable];
-[CBSBIM startMonitoring];
-[CBSBIM setCurrentHeadroom:];
-[CBSBIM currentHeadroomRequest];
-[CBSBIM edrThreshold];
-[CBSBIM resetMitigationState];
-[CBSBIM mitigationStageToString:];
-[CBSBIM mitigatedHeadroomFromRequestedHeadroom];
-[CBSBIM dealloc];
-[CBSBIM initWithContext:andDisplayModule:andEDRModule:andEDRThreshold:];
-[CBSBIM setSdrBrightness:];
-[CBSBIM stopMonitoring];
-[CBSBIM disable];
-[CBSBIM mitigationTimerHandler];
-[CBSBIM dataTimerHandler];
-[CBSBIM exitEDR];
-[CBSBIM currentHeadroom];
-[CBSBIM updateMitigationStateWithData:andCurrentHeadroom:andRequestedHeadroom:andSDRBrightness:andReset:];
-[CBSBIM enterEDR];
-[CBSBIM enableSBIM:];
-[CBSBIM sendEDRHeadroomRequest:];
-[CBSBIM initialiseLimits:];
-[CBSBIM cap];
-[CBSBIM sdrBrightness];
-[CBSBIM setCurrentHeadroomRequest:];
```
