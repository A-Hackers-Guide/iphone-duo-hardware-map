# `AVCaptureCameraCalibrationDataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- Protocols: `AVCaptureDataOutputDelegateOverride`
- 3 instance variables, 9 properties, 20 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureDataOutputDelegateCallbackHelper" _delegateCallbackHelper;
@"AVWeakReference" _weakReference;
B _alwaysDiscardsLateCameraCalibrationData;
```

## Properties

```
@property (T@"<AVCaptureCameraCalibrationDataOutputDelegate>",R,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateCallbackQueue;
@property (TB,N) alwaysDiscardsLateCameraCalibrationData;
@property (T@,R,N) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateOverrideCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureCameraCalibrationDataOutput initialize];
+[AVCaptureCameraCalibrationDataOutput new];
```

## Instance methods

```
-[AVCaptureCameraCalibrationDataOutput canAddConnection:failureReason:];
-[AVCaptureCameraCalibrationDataOutput _handleNotification:payload:];
-[AVCaptureCameraCalibrationDataOutput _processSampleBuffer:];
-[AVCaptureCameraCalibrationDataOutput init];
-[AVCaptureCameraCalibrationDataOutput _handleLocalQueueMessage:];
-[AVCaptureCameraCalibrationDataOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureCameraCalibrationDataOutput dealloc];
-[AVCaptureCameraCalibrationDataOutput _updateRemoteQueue:];
-[AVCaptureCameraCalibrationDataOutput delegate];
-[AVCaptureCameraCalibrationDataOutput delegateCallbackQueue];
-[AVCaptureCameraCalibrationDataOutput _handleRemoteQueueOperation:];
-[AVCaptureCameraCalibrationDataOutput connectionMediaTypes];
-[AVCaptureCameraCalibrationDataOutput _updateLocalQueue:];
-[AVCaptureCameraCalibrationDataOutput delegateOverrideCallbackQueue];
-[AVCaptureCameraCalibrationDataOutput attachSafelyToFigCaptureSession:];
-[AVCaptureCameraCalibrationDataOutput setDelegateOverride:delegateOverrideCallbackQueue:];
-[AVCaptureCameraCalibrationDataOutput delegateOverride];
-[AVCaptureCameraCalibrationDataOutput alwaysDiscardsLateCameraCalibrationData];
-[AVCaptureCameraCalibrationDataOutput setAlwaysDiscardsLateCameraCalibrationData:];
-[AVCaptureCameraCalibrationDataOutput setDelegate:callbackQueue:];
```
