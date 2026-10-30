# `BWPocketDetectionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `SBSAccidentalActivationMitigationSessionObserver`
- 27 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"BWCoreMotionSuppressionStateMonitor" _coreMotionSuppressionStateMonitor;
i _coreMotionSuppressionState;
d _coreMotionSuppressionStateChangeTime;
i _coreMotionFacedownState;
B _suppressFacedownSetdownAccidentals;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _coreMotionSuppressionStateLock;
B _resourcesAllocated;
@"NSObject<OS_dispatch_queue>" _detectionQueue;
i _cumulativeEnergyHistoryLength;
@"NSMutableArray" _cumulativeEnergyHistory;
f _cumulativeEnergy;
f _cumulativeEnergyFiltered;
B _inPocketConsolidatedDecision;
{?="value"q"timescale"i"flags"I"epoch"q} _lastDetectionFramePTS;
f _detectionIntervalInSeconds;
B _previousDetectionComplete;
{?="value"q"timescale"i"flags"I"epoch"q} _firstFramePts;
f _detectionEnabledDurationInSeconds;
B _stopDetection;
f _cumulativeEnergyInPocketThreshold;
B _enableSBAccidentalActivationMitigation;
@"SBSAccidentalActivationMitigationClientSession" _sbAccidentalActivationMitigationClientSession;
B _sbAccidentalActivationMitigationObserverAdded;
d _sbMitigationSessionDurationInSeconds;
@"NSArray" _suppressionStateStrings;
@"BWPocketDetectionFFTProcessor" _fftProcessor;
{?="detectionSessionStartTime"d"detectionSessionStopTime"d"inPocket"B} _ppsData;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPocketDetectionNode initialize];
```

## Instance methods

```
-[BWPocketDetectionNode prepareForCurrentConfigurationToBecomeLive];
-[BWPocketDetectionNode renderSampleBuffer:forInput:];
-[BWPocketDetectionNode _allocateResources];
-[BWPocketDetectionNode dealloc];
-[BWPocketDetectionNode hasNonLiveConfigurationChanges];
-[BWPocketDetectionNode didReachEndOfDataForConfigurationID:input:];
-[BWPocketDetectionNode nodeSubType];
-[BWPocketDetectionNode didSelectFormat:forInput:];
-[BWPocketDetectionNode nodeType];
-[BWPocketDetectionNode accidentalActivationMitigationSessionStateDidChange:];
-[BWPocketDetectionNode _cleanupResources];
-[BWPocketDetectionNode _detectPocket:];
-[BWPocketDetectionNode _waitForDetectionToComplete];
-[BWPocketDetectionNode initWithMetalCommandQueue:clientApplicationID:];
```
