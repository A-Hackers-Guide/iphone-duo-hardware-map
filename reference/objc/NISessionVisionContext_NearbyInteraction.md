# `NISessionVisionContext`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _cameraAssistanceEnabled;
B _arSessionInternal;
B _arSessionInClientProcess;
@"ARSession" _arSession;
Q _arSessionState;
@"ARFrame" _latestARFrame;
```

## Properties

```
@property (T@"ARSession",&,N,V_arSession) arSession;
@property (TQ,N,V_arSessionState) arSessionState;
@property (TB,N,GisCameraAssistanceEnabled,V_cameraAssistanceEnabled) cameraAssistanceEnabled;
@property (TB,N,GisARSessionInternal,V_arSessionInternal) arSessionInternal;
@property (TB,N,GisARSessionInClientProcess,V_arSessionInClientProcess) arSessionInClientProcess;
@property (T@"ARFrame",C,N,V_latestARFrame) latestARFrame;
```

## Instance methods

```
-[NISessionVisionContext setCameraAssistanceEnabled:];
-[NISessionVisionContext init];
-[NISessionVisionContext isCameraAssistanceEnabled];
-[NISessionVisionContext arSession];
-[NISessionVisionContext arSessionState];
-[NISessionVisionContext isARSessionInClientProcess];
-[NISessionVisionContext isARSessionInternal];
-[NISessionVisionContext latestARFrame];
-[NISessionVisionContext setArSession:];
-[NISessionVisionContext setArSessionInClientProcess:];
-[NISessionVisionContext setArSessionInternal:];
-[NISessionVisionContext setArSessionState:];
-[NISessionVisionContext setLatestARFrame:];
```
