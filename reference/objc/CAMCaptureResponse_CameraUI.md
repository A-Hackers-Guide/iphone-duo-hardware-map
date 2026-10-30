# `CAMCaptureResponse`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
S _sessionIdentifier;
q _type;
@"CAMCaptureCoordinationInfo" _coordinationInfo;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (TS,R,N,V_sessionIdentifier) sessionIdentifier;
@property (T@"CAMCaptureCoordinationInfo",R,N,V_coordinationInfo) coordinationInfo;
```

## Instance methods

```
-[CAMCaptureResponse sessionIdentifier];
-[CAMCaptureResponse init];
-[CAMCaptureResponse type];
-[CAMCaptureResponse coordinationInfo];
-[CAMCaptureResponse initWithType:captureSession:coordinationInfo:];
-[CAMCaptureResponse releaseCachedImages];
```
