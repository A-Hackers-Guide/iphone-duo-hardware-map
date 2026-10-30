# `AVCapturePointCloudDataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- Protocols: `AVCaptureDataOutputDelegateOverride`
- 3 instance variables, 9 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureDataOutputDelegateCallbackHelper" _delegateCallbackHelper;
@"AVWeakReference" _weakReference;
B _alwaysDiscardsLatePointCloudData;
```

## Properties

```
@property (T@"<AVCapturePointCloudDataOutputDelegate>",R,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateCallbackQueue;
@property (TB,N) alwaysDiscardsLatePointCloudData;
@property (T@,R,N) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateOverrideCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCapturePointCloudDataOutput initialize];
+[AVCapturePointCloudDataOutput new];
```

## Instance methods

```
-[AVCapturePointCloudDataOutput canAddConnection:failureReason:];
-[AVCapturePointCloudDataOutput _handleNotification:payload:];
-[AVCapturePointCloudDataOutput _processSampleBuffer:];
-[AVCapturePointCloudDataOutput appliesOrientationWithPhysicalRotationForConnection:];
-[AVCapturePointCloudDataOutput init];
-[AVCapturePointCloudDataOutput _handleLocalQueueMessage:];
-[AVCapturePointCloudDataOutput appliesMirroringWithPhysicalFlipForConnection:];
-[AVCapturePointCloudDataOutput detachSafelyFromFigCaptureSession:];
-[AVCapturePointCloudDataOutput dealloc];
-[AVCapturePointCloudDataOutput _updateRemoteQueue:];
-[AVCapturePointCloudDataOutput delegate];
-[AVCapturePointCloudDataOutput delegateCallbackQueue];
-[AVCapturePointCloudDataOutput _handleRemoteQueueOperation:];
-[AVCapturePointCloudDataOutput connectionMediaTypes];
-[AVCapturePointCloudDataOutput _updateLocalQueue:];
-[AVCapturePointCloudDataOutput delegateOverrideCallbackQueue];
-[AVCapturePointCloudDataOutput attachSafelyToFigCaptureSession:];
-[AVCapturePointCloudDataOutput setDelegateOverride:delegateOverrideCallbackQueue:];
-[AVCapturePointCloudDataOutput delegateOverride];
-[AVCapturePointCloudDataOutput alwaysDiscardsLatePointCloudData];
-[AVCapturePointCloudDataOutput setAlwaysDiscardsLatePointCloudData:];
-[AVCapturePointCloudDataOutput setDelegate:callbackQueue:];
```
