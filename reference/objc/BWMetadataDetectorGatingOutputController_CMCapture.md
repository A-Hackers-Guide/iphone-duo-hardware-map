# `BWMetadataDetectorGatingOutputController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWMetadataDetectedResultsObserver`
- 26 instance variables, 20 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"BWNodeOutput" _nodeOutput;
B _usesSceneClassifierToGateDetection;
B _shouldEmitFirstBufferAfterSceneChange;
B _sceneMotionEstimatesSupported;
B _lowPowerModeEnabled;
B _synchronizeWithOtherControllers;
{?="value"q"timescale"i"flags"I"epoch"q} _currentPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastDetectionPTS;
@"NSArray" _detectionFrameRateRamp;
c _detectionFrameRateRampStartIndex;
@"BWSceneStabilityMonitor" _sceneStabilityMonitor;
B _shouldRunDetection;
B _shouldApplySceneMotion;
B _isHandlingFirstBufferAfterSceneChange;
B _firstBufferAfterSceneChangeHasCodes;
@"FigCaptureLogSmartCameraGating" _logger;
@"NSObject<OS_dispatch_group>" _detectorAvailableGroup;
B _sceneLikelyToHaveCodes;
B _emittedFirstBufferAfterSceneChange;
B _isSmartCameraSceneConfident;
q _lastDetectedCodesCount;
{?="value"q"timescale"i"flags"I"epoch"q} _detectedCodesLastSeenPTS;
c _detectionFrameRateRampIndex;
B _forceSynchronizedControllersToRunDetectionImmediately;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_nodeOutput) nodeOutput;
@property (TB,N,V_usesSceneClassifierToGateDetection) usesSceneClassifierToGateDetection;
@property (TB,N,V_shouldEmitFirstBufferAfterSceneChange) shouldEmitFirstBufferAfterSceneChange;
@property (TB,N,V_sceneMotionEstimatesSupported) sceneMotionEstimatesSupported;
@property (TB,N,V_lowPowerModeEnabled) lowPowerModeEnabled;
@property (TB,N,V_synchronizeWithOtherControllers) synchronizeWithOtherControllers;
@property (TB,R,N,V_shouldRunDetection) shouldRunDetection;
@property (TB,R,N,V_shouldApplySceneMotion) shouldApplySceneMotion;
@property (TB,R,N,GisHandlingFirstBufferAfterSceneChange,V_isHandlingFirstBufferAfterSceneChange) handlingFirstBufferAfterSceneChange;
@property (TB,R,N) shouldEmitBuffer;
@property (TB,R,N,V_sceneLikelyToHaveCodes) sceneLikelyToHaveCodes;
@property (TB,N,GisSmartCameraSceneConfident) smartCameraSceneConfident;
@property (Tq,N,V_lastDetectedCodesCount) lastDetectedCodesCount;
@property (T@"FigCaptureLogSmartCameraGating",&,N,V_logger) logger;
@property (TB,N) forceSynchronizedControllersToRunDetectionImmediately;
@property (T{?=qiIq},N,V_lastDetectionPTS) lastDetectionPTS;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWMetadataDetectorGatingOutputController logger];
-[BWMetadataDetectorGatingOutputController setLogger:];
-[BWMetadataDetectorGatingOutputController dealloc];
-[BWMetadataDetectorGatingOutputController setLowPowerModeEnabled:];
-[BWMetadataDetectorGatingOutputController lowPowerModeEnabled];
-[BWMetadataDetectorGatingOutputController synchronizeWithOtherControllers];
-[BWMetadataDetectorGatingOutputController emitPixelBuffer:inputSampleBuffer:appliedPrimaryCaptureRect:];
-[BWMetadataDetectorGatingOutputController enableDetectionFrameRateControllingWithRamp:startIndex:];
-[BWMetadataDetectorGatingOutputController forceSynchronizedControllersToRunDetectionImmediately];
-[BWMetadataDetectorGatingOutputController initWithOutput:name:sceneStabilityMonitor:detectorAvailableGroup:];
-[BWMetadataDetectorGatingOutputController isHandlingFirstBufferAfterSceneChange];
-[BWMetadataDetectorGatingOutputController isSmartCameraSceneConfident];
-[BWMetadataDetectorGatingOutputController lastDetectedCodesCount];
-[BWMetadataDetectorGatingOutputController lastDetectionPTS];
-[BWMetadataDetectorGatingOutputController node:didEmitCodesCount:emittedIdentifiers:originalPTS:];
-[BWMetadataDetectorGatingOutputController nodeOutput];
-[BWMetadataDetectorGatingOutputController prepareToEmitBuffer:];
-[BWMetadataDetectorGatingOutputController sceneLikelyToHaveCodes];
-[BWMetadataDetectorGatingOutputController sceneMotionEstimatesSupported];
-[BWMetadataDetectorGatingOutputController setForceSynchronizedControllersToRunDetectionImmediately:];
-[BWMetadataDetectorGatingOutputController setLastDetectedCodesCount:];
-[BWMetadataDetectorGatingOutputController setLastDetectedCodesCount:originalPTS:];
-[BWMetadataDetectorGatingOutputController setLastDetectionPTS:];
-[BWMetadataDetectorGatingOutputController setSceneMotionEstimatesSupported:];
-[BWMetadataDetectorGatingOutputController setShouldEmitFirstBufferAfterSceneChange:];
-[BWMetadataDetectorGatingOutputController setSmartCameraSceneConfident:];
-[BWMetadataDetectorGatingOutputController setSynchronizeWithOtherControllers:];
-[BWMetadataDetectorGatingOutputController setUsesSceneClassifierToGateDetection:];
-[BWMetadataDetectorGatingOutputController shouldApplySceneMotion];
-[BWMetadataDetectorGatingOutputController shouldEmitBuffer];
-[BWMetadataDetectorGatingOutputController shouldEmitFirstBufferAfterSceneChange];
-[BWMetadataDetectorGatingOutputController shouldRunDetection];
-[BWMetadataDetectorGatingOutputController usesSceneClassifierToGateDetection];
```
