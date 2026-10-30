# `FigCameraViewfinder`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"FigDelegateStorage" _delegateStorage;
@"FigCameraViewfinderSession" _delegateActiveViewfinderSession;
```

## Properties

```
@property (T@"FigCameraViewfinderSession",&,V_delegateActiveViewfinderSession) delegateActiveViewfinderSession;
@property (T@"<FigCameraViewfinderDelegate><FigCameraViewfinderSessionDelegate>",R) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R) queue;
```

## Class methods

```
+[FigCameraViewfinder cameraViewfinder];
+[FigCameraViewfinder clientIsAllowedToUseCameraViewfinder:];
```

## Instance methods

```
-[FigCameraViewfinder setDelegate:queue:];
-[FigCameraViewfinder init];
-[FigCameraViewfinder stop];
-[FigCameraViewfinder startWithOptions:];
-[FigCameraViewfinder dealloc];
-[FigCameraViewfinder queue];
-[FigCameraViewfinder delegate];
-[FigCameraViewfinder delegateActiveViewfinderSession];
-[FigCameraViewfinder setDelegateActiveViewfinderSession:];
```
