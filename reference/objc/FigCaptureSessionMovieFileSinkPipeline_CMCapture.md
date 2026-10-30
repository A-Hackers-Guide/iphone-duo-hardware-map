# `FigCaptureSessionMovieFileSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureMovieFileSinkPipeline`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _momentCaptureMovieRecordingEnabled;
B _recording;
B _recordedWhileMultitasking;
@"NSMutableArray" _pendingIrisRecordings;
B _checkIfFileAlreadyExistForMFO;
```

## Properties

```
@property (TB,N,V_momentCaptureMovieRecordingEnabled) momentCaptureMovieRecordingEnabled;
@property (TB,N,V_recording) recording;
@property (TB,N,V_recordedWhileMultitasking) recordedWhileMultitasking;
@property (T@"NSMutableArray",&,N,V_pendingIrisRecordings) pendingIrisRecordings;
@property (TB,N,V_checkIfFileAlreadyExistForMFO) checkIfFileAlreadyExistForMFO;
```

## Instance methods

```
-[FigCaptureSessionMovieFileSinkPipeline checkIfFileAlreadyExistForMFO];
-[FigCaptureSessionMovieFileSinkPipeline setRecordedWhileMultitasking:];
-[FigCaptureSessionMovieFileSinkPipeline recordedWhileMultitasking];
-[FigCaptureSessionMovieFileSinkPipeline dealloc];
-[FigCaptureSessionMovieFileSinkPipeline setCheckIfFileAlreadyExistForMFO:];
-[FigCaptureSessionMovieFileSinkPipeline setMomentCaptureMovieRecordingEnabled:];
-[FigCaptureSessionMovieFileSinkPipeline setRecording:];
-[FigCaptureSessionMovieFileSinkPipeline pendingIrisRecordings];
-[FigCaptureSessionMovieFileSinkPipeline recording];
-[FigCaptureSessionMovieFileSinkPipeline momentCaptureMovieRecordingEnabled];
-[FigCaptureSessionMovieFileSinkPipeline setPendingIrisRecordings:];
```
