# `AVCaptureSecureVideoDataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- Protocols: `AVCaptureDataOutputDelegateOverride`
- 6 instance variables, 9 properties, 25 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureDataOutputDelegateCallbackHelper" _delegateCallbackHelper;
@"AVWeakReference" _weakReference;
B _alwaysDiscardsLateSecureVideoFrames;
@"FigCaptureFrameRateMonitor" _frameRateMonitor;
@"<AVCaptureSecureVideoDataOutputSampleBufferDelegate>" _sampleBufferDelegate;
@"NSObject<OS_dispatch_queue>" _sampleBufferCallbackQueue;
```

## Properties

```
@property (T@"<AVCaptureSecureVideoDataOutputSampleBufferDelegate>",R,N,V_sampleBufferDelegate) sampleBufferDelegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_sampleBufferCallbackQueue) sampleBufferCallbackQueue;
@property (TB,N,V_alwaysDiscardsLateSecureVideoFrames) alwaysDiscardsLateSecureVideoFrames;
@property (T@,R,N) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateOverrideCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureSecureVideoDataOutput initialize];
+[AVCaptureSecureVideoDataOutput new];
```

## Instance methods

```
-[AVCaptureSecureVideoDataOutput canAddConnection:failureReason:];
-[AVCaptureSecureVideoDataOutput _handleNotification:payload:];
-[AVCaptureSecureVideoDataOutput _processSampleBuffer:];
-[AVCaptureSecureVideoDataOutput setSampleBufferDelegate:queue:];
-[AVCaptureSecureVideoDataOutput init];
-[AVCaptureSecureVideoDataOutput _handleLocalQueueMessage:];
-[AVCaptureSecureVideoDataOutput sampleBufferDelegate];
-[AVCaptureSecureVideoDataOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureSecureVideoDataOutput dealloc];
-[AVCaptureSecureVideoDataOutput _updateRemoteQueue:];
-[AVCaptureSecureVideoDataOutput delegate];
-[AVCaptureSecureVideoDataOutput sampleBufferCallbackQueue];
-[AVCaptureSecureVideoDataOutput delegateCallbackQueue];
-[AVCaptureSecureVideoDataOutput _handleRemoteQueueOperation:];
-[AVCaptureSecureVideoDataOutput connectionMediaTypes];
-[AVCaptureSecureVideoDataOutput removeConnection:];
-[AVCaptureSecureVideoDataOutput _updateLocalQueue:];
-[AVCaptureSecureVideoDataOutput delegateOverrideCallbackQueue];
-[AVCaptureSecureVideoDataOutput attachSafelyToFigCaptureSession:];
-[AVCaptureSecureVideoDataOutput setDelegateOverride:delegateOverrideCallbackQueue:];
-[AVCaptureSecureVideoDataOutput addConnection:error:];
-[AVCaptureSecureVideoDataOutput delegateOverride];
-[AVCaptureSecureVideoDataOutput alwaysDiscardsLateSecureVideoFrames];
-[AVCaptureSecureVideoDataOutput alwaysDiscardsLateSecureVideoFrames:];
-[AVCaptureSecureVideoDataOutput setAlwaysDiscardsLateSecureVideoFrames:];
```
