# `AVCaptureBroadcastVideoOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- 7 instance variables, 6 properties, 21 instance methods, 3 class methods

## Instance variables

```
q _maxBufferedFrameCount;
@"AVCaptureDataOutputDelegateCallbackHelper" _delegateCallbackHelper;
q _testPatternToInject;
@"AVWeakReference" _weakReference;
@"NSDictionary" _videoSettings;
q _droppedFrameReplacementPolicy;
@"AVCaptureAncillaryDataEncoder" _ancillaryDataEncoder;
```

## Properties

```
@property (T@"<AVCaptureBroadcastVideoOutputDelegate>",R,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateCallbackQueue;
@property (T@"NSDictionary",R,N,V_videoSettings) videoSettings;
@property (Tq,N,V_maxBufferedFrameCount) maxBufferedFrameCount;
@property (T@"AVCaptureAncillaryDataEncoder",R,N,V_ancillaryDataEncoder) ancillaryDataEncoder;
@property (Tq,N) droppedFrameReplacementPolicy;
```

## Class methods

```
+[AVCaptureBroadcastVideoOutput initialize];
+[AVCaptureBroadcastVideoOutput new];
+[AVCaptureBroadcastVideoOutput maxSupportedBufferedFrameCount];
```

## Instance methods

```
-[AVCaptureBroadcastVideoOutput setDelegate:queue:];
-[AVCaptureBroadcastVideoOutput videoSettings];
-[AVCaptureBroadcastVideoOutput canAddConnection:failureReason:];
-[AVCaptureBroadcastVideoOutput init];
-[AVCaptureBroadcastVideoOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureBroadcastVideoOutput dealloc];
-[AVCaptureBroadcastVideoOutput delegate];
-[AVCaptureBroadcastVideoOutput delegateCallbackQueue];
-[AVCaptureBroadcastVideoOutput connectionMediaTypes];
-[AVCaptureBroadcastVideoOutput attachSafelyToFigCaptureSession:];
-[AVCaptureBroadcastVideoOutput ancillaryDataEncoder];
-[AVCaptureBroadcastVideoOutput droppedFrameReplacementPolicy];
-[AVCaptureBroadcastVideoOutput handleDidDropSampleBufferWithPayload:];
-[AVCaptureBroadcastVideoOutput handleVideoSettingsDidChangeWithPayload:];
-[AVCaptureBroadcastVideoOutput maxBufferedFrameCount];
-[AVCaptureBroadcastVideoOutput resetFrameBuffer];
-[AVCaptureBroadcastVideoOutput sendAncillaryUserDataToCCD:];
-[AVCaptureBroadcastVideoOutput setDroppedFrameReplacementPolicy:];
-[AVCaptureBroadcastVideoOutput setMaxBufferedFrameCount:];
-[AVCaptureBroadcastVideoOutput setTestPatternToInject:];
-[AVCaptureBroadcastVideoOutput testPatternToInject];
```
