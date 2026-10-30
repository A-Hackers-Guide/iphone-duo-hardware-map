# `AVCaptureDepthDataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- Protocols: `AVCaptureDataOutputDelegateOverride`
- 1 instance variables, 10 properties, 29 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureDepthDataOutputInternal" _internal;
```

## Properties

```
@property (T@"<AVCaptureDepthDataOutputDelegate>",R,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateCallbackQueue;
@property (TB,N) alwaysDiscardsLateDepthData;
@property (TB,N,GisFilteringEnabled) filteringEnabled;
@property (T@,R,N) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateOverrideCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureDepthDataOutput initialize];
+[AVCaptureDepthDataOutput new];
```

## Instance methods

```
-[AVCaptureDepthDataOutput canAddConnection:failureReason:];
-[AVCaptureDepthDataOutput _handleNotification:payload:];
-[AVCaptureDepthDataOutput observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureDepthDataOutput _processSampleBuffer:];
-[AVCaptureDepthDataOutput appliesOrientationWithPhysicalRotationForConnection:];
-[AVCaptureDepthDataOutput init];
-[AVCaptureDepthDataOutput _handleLocalQueueMessage:];
-[AVCaptureDepthDataOutput appliesMirroringWithPhysicalFlipForConnection:];
-[AVCaptureDepthDataOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureDepthDataOutput dealloc];
-[AVCaptureDepthDataOutput _updateRemoteQueue:];
-[AVCaptureDepthDataOutput delegate];
-[AVCaptureDepthDataOutput delegateCallbackQueue];
-[AVCaptureDepthDataOutput _handleRemoteQueueOperation:];
-[AVCaptureDepthDataOutput connectionMediaTypes];
-[AVCaptureDepthDataOutput removeConnection:];
-[AVCaptureDepthDataOutput _updateLocalQueue:];
-[AVCaptureDepthDataOutput delegateOverrideCallbackQueue];
-[AVCaptureDepthDataOutput attachSafelyToFigCaptureSession:];
-[AVCaptureDepthDataOutput setDelegateOverride:delegateOverrideCallbackQueue:];
-[AVCaptureDepthDataOutput addConnection:error:];
-[AVCaptureDepthDataOutput delegateOverride];
-[AVCaptureDepthDataOutput setAlwaysDiscardsLateDepthData:];
-[AVCaptureDepthDataOutput alwaysDiscardsLateDepthData];
-[AVCaptureDepthDataOutput companionSettingsVideoDataOutput];
-[AVCaptureDepthDataOutput isFilteringEnabled];
-[AVCaptureDepthDataOutput setCompanionSettingsVideoDataOutput:];
-[AVCaptureDepthDataOutput setDelegate:callbackQueue:];
-[AVCaptureDepthDataOutput setFilteringEnabled:];
```
