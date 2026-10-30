# `AVMomentCaptureMovieRecordingResolvedSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _uniqueID;
B _torchEnabled;
@"NSURL" _movieURL;
@"NSURL" _spatialOverCaptureURL;
{?="width"i"height"i} _movieDimensions;
```

## Properties

```
@property (Tq,R,V_uniqueID) uniqueID;
@property (TB,R,GisTorchEnabled,V_torchEnabled) torchEnabled;
@property (T@"NSURL",R,V_movieURL) movieURL;
@property (T@"NSURL",R,V_spatialOverCaptureURL) spatialOverCaptureURL;
@property (T{?=ii},R,V_movieDimensions) movieDimensions;
```

## Class methods

```
+[AVMomentCaptureMovieRecordingResolvedSettings movieRecordingResolvedSettingsWithUniqueID:torchEnabled:movieURL:spatialOverCaptureURL:movieDimensions:];
```

## Instance methods

```
-[AVMomentCaptureMovieRecordingResolvedSettings debugDescription];
-[AVMomentCaptureMovieRecordingResolvedSettings dealloc];
-[AVMomentCaptureMovieRecordingResolvedSettings uniqueID];
-[AVMomentCaptureMovieRecordingResolvedSettings description];
-[AVMomentCaptureMovieRecordingResolvedSettings movieDimensions];
-[AVMomentCaptureMovieRecordingResolvedSettings _initWithUniqueID:torchEnabled:movieURL:spatialOverCaptureURL:movieDimensions:];
-[AVMomentCaptureMovieRecordingResolvedSettings isTorchEnabled];
-[AVMomentCaptureMovieRecordingResolvedSettings movieURL];
-[AVMomentCaptureMovieRecordingResolvedSettings spatialOverCaptureURL];
```
