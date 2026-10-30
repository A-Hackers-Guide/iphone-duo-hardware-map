# `BWDockKitNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `NSXPCListenerDelegate`
- 9 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"BWDeviceOrientationMonitor" _deviceOrientationMonitor;
@"DKTrackingAgent" _agent;
B _isRunningForContinuityCapture;
B _cinematicVideoEnabled;
@"DKNotificationAgent" _dockingNotificationAgent;
B _customInferenceEnabled;
@"<BWCinematicVideoFocusDetectionProvider>" _cinematicVideoFocusDetectionsProvider;
@"BWFigVideoCaptureDevice" _captureDevice;
@"NSString" _clientApplicationID;
```

## Properties

```
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (TB,N,V_customInferenceEnabled) customInferenceEnabled;
@property (T@"<BWCinematicVideoFocusDetectionProvider>",W,V_cinematicVideoFocusDetectionsProvider) cinematicVideoFocusDetectionsProvider;
@property (T@"BWFigVideoCaptureDevice",&,N,V_captureDevice) captureDevice;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWDockKitNode initialize];
```

## Instance methods

```
-[BWDockKitNode setCaptureDevice:];
-[BWDockKitNode renderSampleBuffer:forInput:];
-[BWDockKitNode setCinematicVideoFocusDetectionsProvider:];
-[BWDockKitNode customInferenceEnabled];
-[BWDockKitNode captureDevice];
-[BWDockKitNode dealloc];
-[BWDockKitNode cinematicVideoFocusDetectionsProvider];
-[BWDockKitNode setClientApplicationID:];
-[BWDockKitNode handleDroppedSample:forInput:];
-[BWDockKitNode nodeSubType];
-[BWDockKitNode setCustomInferenceEnabled:];
-[BWDockKitNode didSelectFormat:forInput:];
-[BWDockKitNode initWithIsRunningForContinuityCapture:cinematicVideoEnabled:captureDevice:];
-[BWDockKitNode nodeType];
-[BWDockKitNode clientApplicationID];
```
