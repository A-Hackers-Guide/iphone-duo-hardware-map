# `AVCaptureAudioDataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- Protocols: `AVCaptureDataOutputDelegateOverride`
- 1 instance variables, 10 properties, 25 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureAudioDataOutputInternal" _internal;
```

## Properties

```
@property (T@"<AVCaptureAudioDataOutputSampleBufferDelegate>",R,N) sampleBufferDelegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) sampleBufferCallbackQueue;
@property (T@"NSDictionary",C,N) audioSettings;
@property (TI,N) spatialAudioChannelLayoutTag;
@property (T@,R,N) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateOverrideCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureAudioDataOutput initialize];
+[AVCaptureAudioDataOutput new];
```

## Instance methods

```
-[AVCaptureAudioDataOutput canAddConnection:failureReason:];
-[AVCaptureAudioDataOutput _handleNotification:payload:];
-[AVCaptureAudioDataOutput spatialAudioChannelLayoutTag];
-[AVCaptureAudioDataOutput setSampleBufferDelegate:queue:];
-[AVCaptureAudioDataOutput init];
-[AVCaptureAudioDataOutput _handleLocalQueueMessage:];
-[AVCaptureAudioDataOutput sampleBufferDelegate];
-[AVCaptureAudioDataOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureAudioDataOutput dealloc];
-[AVCaptureAudioDataOutput _updateRemoteQueue:];
-[AVCaptureAudioDataOutput sampleBufferCallbackQueue];
-[AVCaptureAudioDataOutput setAudioSettings:];
-[AVCaptureAudioDataOutput supportedAssetWriterOutputFileTypes];
-[AVCaptureAudioDataOutput _handleRemoteQueueOperation:];
-[AVCaptureAudioDataOutput connectionMediaTypes];
-[AVCaptureAudioDataOutput audioSettings];
-[AVCaptureAudioDataOutput _updateLocalQueue:];
-[AVCaptureAudioDataOutput delegateOverrideCallbackQueue];
-[AVCaptureAudioDataOutput attachSafelyToFigCaptureSession:];
-[AVCaptureAudioDataOutput setDelegateOverride:delegateOverrideCallbackQueue:];
-[AVCaptureAudioDataOutput delegateOverride];
-[AVCaptureAudioDataOutput setSpatialAudioChannelLayoutTag:];
-[AVCaptureAudioDataOutput _handleConfigurationLiveEventForID:updatedFormatDescription:];
-[AVCaptureAudioDataOutput _handleSampleBufferEventForSampleBuffer:];
-[AVCaptureAudioDataOutput recommendedAudioSettingsForAssetWriterWithOutputFileType:];
```
