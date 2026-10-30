# `CAMCaptureRequestInfo`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"CAMStillImageCaptureRequest" _request;
@"NSMutableArray" __receivedCallbacks;
Q __userInitiationTime;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V__receivedCallbacks) _receivedCallbacks;
@property (TQ,R,N,V__userInitiationTime) _userInitiationTime;
@property (T@"CAMStillImageCaptureRequest",R,N,V_request) request;
@property (T@"NSArray",R,N) callbackReceipts;
```

## Instance methods

```
-[CAMCaptureRequestInfo initWithRequest:];
-[CAMCaptureRequestInfo request];
-[CAMCaptureRequestInfo _receivedCallbacks];
-[CAMCaptureRequestInfo _userInitiationTime];
-[CAMCaptureRequestInfo callbackReceipts];
-[CAMCaptureRequestInfo didReceiveCallback:atAbsoluteTime:error:];
```
