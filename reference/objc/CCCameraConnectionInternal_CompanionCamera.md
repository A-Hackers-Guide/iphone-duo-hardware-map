# `CCCameraConnectionInternal`

- Image: [`/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`](../userland/System__Library__PrivateFrameworks__CompanionCamera.framework__CompanionCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CCCameraConnectionProtocol`
- 1 instance variables, 1 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"CCCameraConnection" _parent;
```

## Properties

```
@property (T@"CCCameraConnection",W,N,V_parent) parent;
```

## Instance methods

```
-[CCCameraConnectionInternal xpc_startCaptureWithMode:reply:];
-[CCCameraConnectionInternal xpc_ensureSwitchedToOneOfSupportedCaptureModes:reply:];
-[CCCameraConnectionInternal xpc_endBurstCaptureWithReply:];
-[CCCameraConnectionInternal xpc_setHDRMode:];
-[CCCameraConnectionInternal xpc_setSharedLibraryMode:];
-[CCCameraConnectionInternal xpc_setIrisMode:];
-[CCCameraConnectionInternal setParent:];
-[CCCameraConnectionInternal xpc_stopPersonalPhotographerSessionWithReply:];
-[CCCameraConnectionInternal xpc_toggleCameraDevice];
-[CCCameraConnectionInternal xpc_cancelCountdown];
-[CCCameraConnectionInternal xpc_setZoom:reply:];
-[CCCameraConnectionInternal xpc_pauseCaptureWithReply:];
-[CCCameraConnectionInternal xpc_stopCaptureWithReply:];
-[CCCameraConnectionInternal xpc_setFocusPoint:];
-[CCCameraConnectionInternal parent];
-[CCCameraConnectionInternal xpc_setPreviewEndpoint:];
-[CCCameraConnectionInternal xpc_setCaptureMode:reply:];
-[CCCameraConnectionInternal xpc_startPersonalPhotographerSessionWithReply:];
-[CCCameraConnectionInternal xpc_setFlashMode:];
-[CCCameraConnectionInternal xpc_beginBurstCaptureWithReply:];
-[CCCameraConnectionInternal xpc_setCaptureDevice:reply:];
-[CCCameraConnectionInternal xpc_suspend];
-[CCCameraConnectionInternal xpc_fetchCurrentStateIncludingSupportedCaptureModes:reply:];
-[CCCameraConnectionInternal xpc_resumeCaptureWithReply:];
-[CCCameraConnectionInternal takePhotoWithCountdown:];
-[CCCameraConnectionInternal xpc_setZoomMagnification:reply:];
```
