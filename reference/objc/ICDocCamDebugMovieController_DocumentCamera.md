# `ICDocCamDebugMovieController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 50 instance methods, 0 class methods

## Instance variables

```
B _recording;
B _readyToRecordVideo;
B _readyToRecordMetadata;
B _recordingWillBeStarted;
B _recordingWillBeStopped;
B _canRecordFrames;
@"AVCaptureConnection" _videoConnection;
@"<ICDocCamDebugMovieControllerDelegate>" _delegate;
@"NSURL" _movieURL;
@"AVAssetWriter" _assetWriter;
@"AVAssetWriterInput" _assetWriterVideoIn;
@"AVAssetWriterInput" _assetWriterMetadataIn;
@"AVAssetWriterInputMetadataAdaptor" _assetWriterMetadataAdaptor;
@"AVAssetWriterInputPixelBufferAdaptor" _pixelBufferAdaptor;
@"NSObject<OS_dispatch_queue>" _movieWritingQueue;
Q _backgroundRecordingID;
```

## Properties

```
@property (T@"AVCaptureConnection",W,N,V_videoConnection) videoConnection;
@property (T@"<ICDocCamDebugMovieControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSURL",&,N,V_movieURL) movieURL;
@property (T@"AVAssetWriter",&,N,V_assetWriter) assetWriter;
@property (T@"AVAssetWriterInput",&,N,V_assetWriterVideoIn) assetWriterVideoIn;
@property (T@"AVAssetWriterInput",&,N,V_assetWriterMetadataIn) assetWriterMetadataIn;
@property (T@"AVAssetWriterInputMetadataAdaptor",&,N,V_assetWriterMetadataAdaptor) assetWriterMetadataAdaptor;
@property (T@"AVAssetWriterInputPixelBufferAdaptor",&,N,V_pixelBufferAdaptor) pixelBufferAdaptor;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_movieWritingQueue) movieWritingQueue;
@property (TB,N,V_readyToRecordVideo) readyToRecordVideo;
@property (TB,N,V_readyToRecordMetadata) readyToRecordMetadata;
@property (TB,N,V_recordingWillBeStarted) recordingWillBeStarted;
@property (TB,N,V_recordingWillBeStopped) recordingWillBeStopped;
@property (TB,N,V_canRecordFrames) canRecordFrames;
@property (TB,GisRecording,V_recording) recording;
@property (TQ,N,V_backgroundRecordingID) backgroundRecordingID;
```

## Instance methods

```
-[ICDocCamDebugMovieController startRecording];
-[ICDocCamDebugMovieController stopRecording];
-[ICDocCamDebugMovieController isRecording];
-[ICDocCamDebugMovieController setRecording:];
-[ICDocCamDebugMovieController setDelegate:];
-[ICDocCamDebugMovieController delegate];
-[ICDocCamDebugMovieController removeFile:];
-[ICDocCamDebugMovieController video:didFinishSavingWithError:contextInfo:];
-[ICDocCamDebugMovieController movieURL];
-[ICDocCamDebugMovieController setAssetWriter:];
-[ICDocCamDebugMovieController assetWriter];
-[ICDocCamDebugMovieController recordingDidStop];
-[ICDocCamDebugMovieController setMovieURL:];
-[ICDocCamDebugMovieController canRecordFrames];
-[ICDocCamDebugMovieController videoConnection];
-[ICDocCamDebugMovieController assetWriterMetadataAdaptor];
-[ICDocCamDebugMovieController assetWriterMetadataIn];
-[ICDocCamDebugMovieController assetWriterVideoIn];
-[ICDocCamDebugMovieController backgroundRecordingID];
-[ICDocCamDebugMovieController initWithDelegate:videoConnection:];
-[ICDocCamDebugMovieController inputsReadyToRecord];
-[ICDocCamDebugMovieController movieWritingQueue];
-[ICDocCamDebugMovieController pauseCaptureSessionForMovieRecording];
-[ICDocCamDebugMovieController pixelBufferAdaptor];
-[ICDocCamDebugMovieController readyToRecordMetadata];
-[ICDocCamDebugMovieController readyToRecordVideo];
-[ICDocCamDebugMovieController recordFrame:fromConnection:transform:];
-[ICDocCamDebugMovieController recordingDidStart];
-[ICDocCamDebugMovieController recordingWillBeStarted];
-[ICDocCamDebugMovieController recordingWillBeStopped];
-[ICDocCamDebugMovieController recordingWillStart];
-[ICDocCamDebugMovieController recordingWillStop];
-[ICDocCamDebugMovieController resumeCaptureSessionForMovieRecording];
-[ICDocCamDebugMovieController saveMovieToCameraRoll];
-[ICDocCamDebugMovieController setAssetWriterMetadataAdaptor:];
-[ICDocCamDebugMovieController setAssetWriterMetadataIn:];
-[ICDocCamDebugMovieController setAssetWriterVideoIn:];
-[ICDocCamDebugMovieController setBackgroundRecordingID:];
-[ICDocCamDebugMovieController setCanRecordFrames:];
-[ICDocCamDebugMovieController setMovieWritingQueue:];
-[ICDocCamDebugMovieController setPixelBufferAdaptor:];
-[ICDocCamDebugMovieController setReadyToRecordMetadata:];
-[ICDocCamDebugMovieController setReadyToRecordVideo:];
-[ICDocCamDebugMovieController setRecordingWillBeStarted:];
-[ICDocCamDebugMovieController setRecordingWillBeStopped:];
-[ICDocCamDebugMovieController setVideoConnection:];
-[ICDocCamDebugMovieController setupAssetWriterMetadataInputAndMetadataAdaptor];
-[ICDocCamDebugMovieController setupAssetWriterVideoInput:transform:];
-[ICDocCamDebugMovieController writeMetaDataAtFrame:intrinsicMatrix:];
-[ICDocCamDebugMovieController writeSampleBuffer:ofType:atFrame:];
```
