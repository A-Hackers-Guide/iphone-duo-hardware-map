# `CAMTimelapseState`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 19 instance variables, 20 properties, 53 instance methods, 3 class methods

## Instance variables

```
B _captureMirrored;
B _allFramesWritten;
B _preferHEVC;
S _sessionIdentifier;
i _captureOrientation;
f _focusLensPosition;
@"NSString" _timelapseUUID;
q _captureDevice;
q _deviceDirection;
@"NSDate" _startTime;
@"CLLocation" _startLocation;
@"NSDate" _lastFrameResponseTime;
@"NSDate" _stopTime;
q _stopReasons;
d _captureTimeInterval;
q _frameIndexStride;
q _nextFrameIndex;
@"NSURL" _localPrivateMetadataFileURL;
{CGSize="width"d"height"d} _nominalIntermediateFrameSize;
```

## Properties

```
@property (T@"NSString",&,N,V_timelapseUUID) timelapseUUID;
@property (TS,N,V_sessionIdentifier) sessionIdentifier;
@property (Tq,N,V_captureDevice) captureDevice;
@property (Tq,N,V_deviceDirection) deviceDirection;
@property (Ti,N,V_captureOrientation) captureOrientation;
@property (TB,N,GisCaptureMirrored,V_captureMirrored) captureMirrored;
@property (T@"NSDate",&,N,V_startTime) startTime;
@property (T@"CLLocation",&,N,V_startLocation) startLocation;
@property (T@"NSDate",&,N,V_lastFrameResponseTime) lastFrameResponseTime;
@property (T@"NSDate",&,N,V_stopTime) stopTime;
@property (Tq,N,V_stopReasons) stopReasons;
@property (TB,N,V_allFramesWritten) allFramesWritten;
@property (Td,R,N,V_captureTimeInterval) captureTimeInterval;
@property (Tq,R,N,V_frameIndexStride) frameIndexStride;
@property (Tq,R,N,V_nextFrameIndex) nextFrameIndex;
@property (Tf,N,V_focusLensPosition) focusLensPosition;
@property (Tq,R,N) connectionMode;
@property (T{CGSize=dd},N,V_nominalIntermediateFrameSize) nominalIntermediateFrameSize;
@property (TB,N,V_preferHEVC) preferHEVC;
@property (T@"NSURL",&,N,V_localPrivateMetadataFileURL) localPrivateMetadataFileURL;
```

## Class methods

```
+[CAMTimelapseState supportsSecureCoding];
+[CAMTimelapseState maxTimeToWaitForWrittenFrameAfterStop];
+[CAMTimelapseState stateWithContentsOfFile:];
```

## Instance methods

```
-[CAMTimelapseState sessionIdentifier];
-[CAMTimelapseState setCaptureDevice:];
-[CAMTimelapseState isCaptureMirrored];
-[CAMTimelapseState setCaptureOrientation:];
-[CAMTimelapseState isEqualToState:];
-[CAMTimelapseState init];
-[CAMTimelapseState startTime];
-[CAMTimelapseState captureDevice];
-[CAMTimelapseState stopTime];
-[CAMTimelapseState setCaptureMirrored:];
-[CAMTimelapseState fullDescription];
-[CAMTimelapseState setSessionIdentifier:];
-[CAMTimelapseState localPrivateMetadataFileURL];
-[CAMTimelapseState setStartTime:];
-[CAMTimelapseState encodeWithCoder:];
-[CAMTimelapseState description];
-[CAMTimelapseState initWithCoder:];
-[CAMTimelapseState setStopTime:];
-[CAMTimelapseState copyWithZone:];
-[CAMTimelapseState isEqual:];
-[CAMTimelapseState connectionMode];
-[CAMTimelapseState captureOrientation];
-[CAMTimelapseState setStartLocation:];
-[CAMTimelapseState startLocation];
-[CAMTimelapseState deviceDirection];
-[CAMTimelapseState setStopReasons:];
-[CAMTimelapseState setLocalPrivateMetadataFileURL:];
-[CAMTimelapseState _commonCAMTimelapseStateInitWithCoder:];
-[CAMTimelapseState addStopReasons:stopTime:];
-[CAMTimelapseState allFramesWritten];
-[CAMTimelapseState canContinueCapture];
-[CAMTimelapseState captureTimeInterval];
-[CAMTimelapseState filePathForNextFrameIndex];
-[CAMTimelapseState focusLensPosition];
-[CAMTimelapseState forceCompleted];
-[CAMTimelapseState frameIndexStride];
-[CAMTimelapseState incrementFrameIndex];
-[CAMTimelapseState isReadyForWritingMovie];
-[CAMTimelapseState lastFrameResponseTime];
-[CAMTimelapseState mergeSecondaryState:];
-[CAMTimelapseState nextFrameIndex];
-[CAMTimelapseState nominalIntermediateFrameSize];
-[CAMTimelapseState preferHEVC];
-[CAMTimelapseState setAllFramesWritten:];
-[CAMTimelapseState setDeviceDirection:];
-[CAMTimelapseState setFocusLensPosition:];
-[CAMTimelapseState setLastFrameResponseTime:];
-[CAMTimelapseState setNominalIntermediateFrameSize:];
-[CAMTimelapseState setPreferHEVC:];
-[CAMTimelapseState setTimelapseUUID:];
-[CAMTimelapseState stopReasons];
-[CAMTimelapseState timelapseUUID];
-[CAMTimelapseState writeToFile:createDirectoryIfNeeded:];
```
