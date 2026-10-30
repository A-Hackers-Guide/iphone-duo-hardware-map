# `AVCaptureFileOutputDelegateWrapper`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _recording;
B _paused;
B _trueVideoCaptureEnabled;
q _settingsID;
@"NSURL" _outputFileURL;
@"NSString" _outputFileType;
@"NSArray" _metadata;
@"AVWeakReferencingDelegateStorage" _delegateStorage;
@"NSArray" _connections;
^{OpaqueFigCaptureSession=} _pendingDidStopRecordingUnregistrationCaptureSession;
{?="value"q"timescale"i"flags"I"epoch"q} _timewarpDestinationFrameRate;
```

## Properties

```
@property (Tq,R,V_settingsID) settingsID;
@property (T@"NSURL",R,V_outputFileURL) outputFileURL;
@property (T@"NSString",&,V_outputFileType) outputFileType;
@property (T@"NSArray",&,V_metadata) metadata;
@property (T@"AVWeakReferencingDelegateStorage",R,V_delegateStorage) delegateStorage;
@property (T@"NSArray",R,V_connections) connections;
@property (TB,N,GisRecording,V_recording) recording;
@property (TB,N,GisPaused,V_paused) paused;
@property (T^{OpaqueFigCaptureSession=},&,N,V_pendingDidStopRecordingUnregistrationCaptureSession) pendingDidStopRecordingUnregistrationCaptureSession;
@property (TB,N,GisTrueVideoCaptureEnabled,V_trueVideoCaptureEnabled) trueVideoCaptureEnabled;
@property (T{?=qiIq},N,V_timewarpDestinationFrameRate) timewarpDestinationFrameRate;
```

## Class methods

```
+[AVCaptureFileOutputDelegateWrapper wrapperWithURL:delegate:settingsID:connections:];
```

## Instance methods

```
-[AVCaptureFileOutputDelegateWrapper setTrueVideoCaptureEnabled:];
-[AVCaptureFileOutputDelegateWrapper isPaused];
-[AVCaptureFileOutputDelegateWrapper isRecording];
-[AVCaptureFileOutputDelegateWrapper setOutputFileType:];
-[AVCaptureFileOutputDelegateWrapper connections];
-[AVCaptureFileOutputDelegateWrapper timewarpDestinationFrameRate];
-[AVCaptureFileOutputDelegateWrapper dealloc];
-[AVCaptureFileOutputDelegateWrapper settingsID];
-[AVCaptureFileOutputDelegateWrapper setRecording:];
-[AVCaptureFileOutputDelegateWrapper metadata];
-[AVCaptureFileOutputDelegateWrapper setPaused:];
-[AVCaptureFileOutputDelegateWrapper delegateStorage];
-[AVCaptureFileOutputDelegateWrapper outputFileType];
-[AVCaptureFileOutputDelegateWrapper setMetadata:];
-[AVCaptureFileOutputDelegateWrapper setTimewarpDestinationFrameRate:];
-[AVCaptureFileOutputDelegateWrapper outputFileURL];
-[AVCaptureFileOutputDelegateWrapper initWithURL:delegate:settingsID:connections:];
-[AVCaptureFileOutputDelegateWrapper isTrueVideoCaptureEnabled];
-[AVCaptureFileOutputDelegateWrapper pendingDidStopRecordingUnregistrationCaptureSession];
-[AVCaptureFileOutputDelegateWrapper setPendingDidStopRecordingUnregistrationCaptureSession:];
```
