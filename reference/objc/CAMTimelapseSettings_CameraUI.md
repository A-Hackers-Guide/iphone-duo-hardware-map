# `CAMTimelapseSettings`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
d _initialCaptureTimeInterval;
d _maxOutputFPS;
d _maxOutputLength;
```

## Properties

```
@property (Td,R,N,V_initialCaptureTimeInterval) initialCaptureTimeInterval;
@property (Td,R,N,V_maxOutputFPS) maxOutputFPS;
@property (Td,R,N,V_maxOutputLength) maxOutputLength;
@property (Tq,R,N) maxOutputFrames;
@property (Tq,R,N) maxMovieWriteAttempts;
@property (Tq,R,N) maxFailedStateReadAttempts;
```

## Class methods

```
+[CAMTimelapseSettings sharedInstance];
```

## Instance methods

```
-[CAMTimelapseSettings init];
-[CAMTimelapseSettings maxOutputLength];
-[CAMTimelapseSettings maxOutputFrames];
-[CAMTimelapseSettings _averageMovieBitrateForWidth:height:useHEVC:];
-[CAMTimelapseSettings _outputSettingsPresetForWidth:height:];
-[CAMTimelapseSettings initialCaptureTimeInterval];
-[CAMTimelapseSettings maxFailedStateReadAttempts];
-[CAMTimelapseSettings maxMovieFileLengthForWidth:height:useHEVC:];
-[CAMTimelapseSettings maxMovieWriteAttempts];
-[CAMTimelapseSettings maxOutputFPS];
-[CAMTimelapseSettings minAvailableBytesNeededForCaptureForWidth:height:useHEVC:];
-[CAMTimelapseSettings outputFPSForFrameCount:];
-[CAMTimelapseSettings outputSettingsForWidth:height:videoFormatDescription:framesPerSecond:frameCount:useHEVC:];
-[CAMTimelapseSettings waitTimeBeforeNextWriteForNumberOfPreviousAttempts:];
```
