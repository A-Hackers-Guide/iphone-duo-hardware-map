# `BWImageControlModeTransitionMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _expectedSphereModesByPortType;
@"NSDictionary" _expectedMinimumFrameRatesByPortType;
@"NSDictionary" _expectedMaximumFrameRatesByPortType;
@"NSDictionary" _expectedLTMCurvesByPortType;
i _ltmCurvesTransitionFrameCount;
d _coarseFocusCheckTimeout;
B _waitForTorchToRampUp;
@"NSMutableDictionary" _currentSphereModesByPortType;
@"NSMutableDictionary" _currentFrameRatesByPortType;
@"NSMutableDictionary" _currentLTMCurvesByPortType;
i _ltmCurvesTransitionFrameWaitCount;
{?="value"q"timescale"i"flags"I"epoch"q} _firstFramePTS;
i _frameWaitCount;
B _coarseFocusHasSettled;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_expectedSphereModesByPortType) expectedSphereModesByPortType;
@property (T@"NSDictionary",C,N,V_expectedMinimumFrameRatesByPortType) expectedMinimumFrameRatesByPortType;
@property (T@"NSDictionary",C,N,V_expectedMaximumFrameRatesByPortType) expectedMaximumFrameRatesByPortType;
@property (T@"NSDictionary",C,N,V_expectedLTMCurvesByPortType) expectedLTMCurvesByPortType;
@property (Ti,N,V_ltmCurvesTransitionFrameCount) ltmCurvesTransitionFrameCount;
@property (Td,N,V_coarseFocusCheckTimeout) coarseFocusCheckTimeout;
@property (TB,N,V_waitForTorchToRampUp) waitForTorchToRampUp;
```

## Class methods

```
+[BWImageControlModeTransitionMonitor initialize];
```

## Instance methods

```
-[BWImageControlModeTransitionMonitor init];
-[BWImageControlModeTransitionMonitor dealloc];
-[BWImageControlModeTransitionMonitor description];
-[BWImageControlModeTransitionMonitor setExpectedLTMCurvesByPortType:];
-[BWImageControlModeTransitionMonitor coarseFocusCheckTimeout];
-[BWImageControlModeTransitionMonitor expectedLTMCurvesByPortType];
-[BWImageControlModeTransitionMonitor expectedMaximumFrameRatesByPortType];
-[BWImageControlModeTransitionMonitor expectedMinimumFrameRatesByPortType];
-[BWImageControlModeTransitionMonitor expectedSphereModesByPortType];
-[BWImageControlModeTransitionMonitor isTransitionCompleteWithSampleBuffer:masterCaptureStreamPortType:activeSlaveStreamPortType:];
-[BWImageControlModeTransitionMonitor ltmCurvesTransitionFrameCount];
-[BWImageControlModeTransitionMonitor setCoarseFocusCheckTimeout:];
-[BWImageControlModeTransitionMonitor setExpectedMaximumFrameRatesByPortType:];
-[BWImageControlModeTransitionMonitor setExpectedMinimumFrameRatesByPortType:];
-[BWImageControlModeTransitionMonitor setExpectedSphereModesByPortType:];
-[BWImageControlModeTransitionMonitor setLtmCurvesTransitionFrameCount:];
-[BWImageControlModeTransitionMonitor setWaitForTorchToRampUp:];
-[BWImageControlModeTransitionMonitor waitForTorchToRampUp];
```
