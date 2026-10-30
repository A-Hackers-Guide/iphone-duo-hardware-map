# `SBCameraViewfinderMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCameraViewfinderDelegate`, `FigCameraViewfinderSessionDelegate`
- 4 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"BSAuditToken" _activeSessionAuditToken;
B _hasActiveMovieRecordingSession;
@"FigCameraViewfinder" _cameraViewFinder;
```

## Properties

```
@property (T@"FigCameraViewfinder",&,N,V_cameraViewFinder) cameraViewFinder;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCameraViewfinderMonitor sharedInstance];
```

## Instance methods

```
-[SBCameraViewfinderMonitor _start];
-[SBCameraViewfinderMonitor dealloc];
-[SBCameraViewfinderMonitor _cancel];
-[SBCameraViewfinderMonitor cameraViewfinder:viewfinderSessionWillBegin:];
-[SBCameraViewfinderMonitor addObserver:];
-[SBCameraViewfinderMonitor cameraViewfinder:viewfinderSessionDidEnd:];
-[SBCameraViewfinderMonitor cameraViewfinder:viewfinderSessionDidBegin:];
-[SBCameraViewfinderMonitor _removeObserver:];
-[SBCameraViewfinderMonitor cameraViewfinderSessionDidFinishMovieRecording:];
-[SBCameraViewfinderMonitor cameraViewfinderSessionDidStartMovieRecording:];
-[SBCameraViewfinderMonitor auditTokenForProcessWithActiveOrImminentViewfinderSession];
-[SBCameraViewfinderMonitor cameraViewFinder];
-[SBCameraViewfinderMonitor setCameraViewFinder:];
```
