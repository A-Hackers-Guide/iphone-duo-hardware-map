# `AVCaptureDeviceControlRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
@? _completionBlock;
i _errorCode;
i _requestID;
```

## Properties

```
@property (T@?,R,C,N,V_completionBlock) completionBlock;
@property (Ti,R,N,V_requestID) requestID;
@property (Ti,N,V_errorCode) errorCode;
```

## Class methods

```
+[AVCaptureDeviceControlRequest deviceControlRequestWithCompletionBlock:];
```

## Instance methods

```
-[AVCaptureDeviceControlRequest setErrorCode:];
-[AVCaptureDeviceControlRequest errorCode];
-[AVCaptureDeviceControlRequest completionBlock];
-[AVCaptureDeviceControlRequest requestID];
-[AVCaptureDeviceControlRequest dealloc];
-[AVCaptureDeviceControlRequest _initWithCompletionBlock:];
```
