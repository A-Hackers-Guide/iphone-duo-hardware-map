# `BWPendingIrisRecordingRequest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"FigCaptureMovieFileRecordingSettings" _settings;
q _enqueuedHostTime;
{?="value"q"timescale"i"flags"I"epoch"q} _momentCaptureMovieRecordingMasterEndTime;
B _pairedRequestCreated;
@"BWIrisMovieInfo" _irisMovieInfo;
```

## Properties

```
@property (T@"FigCaptureMovieFileRecordingSettings",R,N,V_settings) settings;
@property (Tq,N,V_enqueuedHostTime) enqueuedHostTime;
@property (T@"BWIrisMovieInfo",&,N,V_irisMovieInfo) irisMovieInfo;
@property (T{?=qiIq},N,V_momentCaptureMovieRecordingMasterEndTime) momentCaptureMovieRecordingMasterEndTime;
@property (TB,N,GisPairedRequestCreated,V_pairedRequestCreated) pairedRequestCreated;
@property (TB,R,N) isEmpty;
```

## Class methods

```
+[BWPendingIrisRecordingRequest irisRecordingRequestWithFigCaptureMovieFileRecordingSettings:];
```

## Instance methods

```
-[BWPendingIrisRecordingRequest momentCaptureMovieRecordingMasterEndTime];
-[BWPendingIrisRecordingRequest enqueuedHostTime];
-[BWPendingIrisRecordingRequest setPairedRequestCreated:];
-[BWPendingIrisRecordingRequest settings];
-[BWPendingIrisRecordingRequest dealloc];
-[BWPendingIrisRecordingRequest irisMovieInfo];
-[BWPendingIrisRecordingRequest isPairedRequestCreated];
-[BWPendingIrisRecordingRequest setEnqueuedHostTime:];
-[BWPendingIrisRecordingRequest setIrisMovieInfo:];
-[BWPendingIrisRecordingRequest isEmpty];
-[BWPendingIrisRecordingRequest setMomentCaptureMovieRecordingMasterEndTime:];
-[BWPendingIrisRecordingRequest description];
-[BWPendingIrisRecordingRequest copyWithZone:];
```
