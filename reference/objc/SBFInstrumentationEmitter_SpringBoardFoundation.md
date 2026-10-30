# `SBFInstrumentationEmitter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 8 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"BSCompoundAssertion" _dynamicMarkPersistenceAssertion;
Q _currentPoseEnqueuedMCT;
B _rotationIsInFlight;
B _hingeInFlight;
B _displayContentModeUpdateInFlight;
B _displayContentModeUpdateBacklightStateWasUpdated;
@"NSMutableDictionary" _inFlightPoseUpdates;
Q _displayContentModeStartMCT;
@"_SBFInFlightPoseUpdate" _currentPoseUpdate;
@"NSObject<OS_dispatch_queue>" _signpostingQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_inFlightPoseUpdates) inFlightPoseUpdates;
@property (TB,N,V_rotationIsInFlight) rotationIsInFlight;
@property (TB,N,V_hingeInFlight) hingeInFlight;
@property (TB,N,V_displayContentModeUpdateInFlight) displayContentModeUpdateInFlight;
@property (TB,N,V_displayContentModeUpdateBacklightStateWasUpdated) displayContentModeUpdateBacklightStateWasUpdated;
@property (TQ,N,V_displayContentModeStartMCT) displayContentModeStartMCT;
@property (T@"_SBFInFlightPoseUpdate",&,N,V_currentPoseUpdate) currentPoseUpdate;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_signpostingQueue) signpostingQueue;
```

## Class methods

```
+[SBFInstrumentationEmitter sharedInstance];
```

## Instance methods

```
-[SBFInstrumentationEmitter init];
-[SBFInstrumentationEmitter dealloc];
-[SBFInstrumentationEmitter _poseEnqueuedMCTIfKnown];
-[SBFInstrumentationEmitter acquireDynamicMarkPersistenceAssertionForReason:];
-[SBFInstrumentationEmitter currentPoseUpdate];
-[SBFInstrumentationEmitter displayContentModeStartMCT];
-[SBFInstrumentationEmitter displayContentModeUpdateBacklightStateWasUpdated];
-[SBFInstrumentationEmitter displayContentModeUpdateInFlight];
-[SBFInstrumentationEmitter emitAdHocSpanForIntervalMark:fromMCT:toMCT:minimumDurationMs:file:line:];
-[SBFInstrumentationEmitter hingeInFlight];
-[SBFInstrumentationEmitter inFlightPoseUpdates];
-[SBFInstrumentationEmitter logHandleForCategory:storageTier:];
-[SBFInstrumentationEmitter logHandleForImpulseMark:];
-[SBFInstrumentationEmitter logHandleForIntervalMark:];
-[SBFInstrumentationEmitter markBacklightState:forDisplayId:];
-[SBFInstrumentationEmitter markCorrelationID];
-[SBFInstrumentationEmitter markDeviceOrientationChangeEnd];
-[SBFInstrumentationEmitter markDeviceOrientationChangeStartFromDeviceOrientation:toDeviceOrientation:displayId:surfaceType:];
-[SBFInstrumentationEmitter markHingePoseUpdateDidEnd];
-[SBFInstrumentationEmitter markHingePoseUpdateStartFromDevicePose:toDevicePose:displayId:surfaceType:];
-[SBFInstrumentationEmitter markRotateScenesWorkspaceTransactionEnd];
-[SBFInstrumentationEmitter markRotateScenesWorkspaceTransactionStart];
-[SBFInstrumentationEmitter markSceneContentMoveFinishedWithStart:];
-[SBFInstrumentationEmitter performSignpostEmission:];
-[SBFInstrumentationEmitter rotationIsInFlight];
-[SBFInstrumentationEmitter setCurrentPoseUpdate:];
-[SBFInstrumentationEmitter setDisplayContentModeStartMCT:];
-[SBFInstrumentationEmitter setDisplayContentModeUpdateBacklightStateWasUpdated:];
-[SBFInstrumentationEmitter setDisplayContentModeUpdateInFlight:];
-[SBFInstrumentationEmitter setHingeInFlight:];
-[SBFInstrumentationEmitter setRotationIsInFlight:];
-[SBFInstrumentationEmitter signpostingQueue];
-[SBFInstrumentationEmitter spanFromMCT:toMCT:clearsMinimumDurationMs:];
-[SBFInstrumentationEmitter storageTierForTier:];
```
