# `AVCaptureFileOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- 2 instance variables, 9 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureFileOutputInternal" _fileOutputInternal;
@"<AVCaptureFileOutputDelegate>" _delegate;
```

## Properties

```
@property (T@"<AVCaptureFileOutputDelegate>",N,V_delegate) delegate;
@property (T@"NSURL",R,N) outputFileURL;
@property (TB,R,N,GisRecording) recording;
@property (TB,R,N,GisRecordingPaused) recordingPaused;
@property (T{?=qiIq},R,N) recordedDuration;
@property (Tq,R,N) recordedFileSize;
@property (T{?=qiIq},N) maxRecordedDuration;
@property (Tq,N) maxRecordedFileSize;
@property (Tq,N) minFreeDiskSpaceLimit;
```

## Class methods

```
+[AVCaptureFileOutput initialize];
```

## Instance methods

```
-[AVCaptureFileOutput stopRecording];
-[AVCaptureFileOutput isRecording];
-[AVCaptureFileOutput dealloc];
-[AVCaptureFileOutput resumeRecording];
-[AVCaptureFileOutput setDelegate:];
-[AVCaptureFileOutput delegate];
-[AVCaptureFileOutput startRecordingToOutputFileURL:recordingDelegate:];
-[AVCaptureFileOutput pauseRecording];
-[AVCaptureFileOutput outputFileURL];
-[AVCaptureFileOutput initSubclass];
-[AVCaptureFileOutput isRecordingPaused];
-[AVCaptureFileOutput maxRecordedDuration];
-[AVCaptureFileOutput maxRecordedFileSize];
-[AVCaptureFileOutput minFreeDiskSpaceLimit];
-[AVCaptureFileOutput pausesRecordingOnInterruption];
-[AVCaptureFileOutput recordedDuration];
-[AVCaptureFileOutput recordedFileSize];
-[AVCaptureFileOutput setMaxRecordedDuration:];
-[AVCaptureFileOutput setMaxRecordedFileSize:];
-[AVCaptureFileOutput setMinFreeDiskSpaceLimit:];
-[AVCaptureFileOutput setPausesRecordingOnInterruption:];
```
