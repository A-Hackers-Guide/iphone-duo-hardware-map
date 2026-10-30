# `AVMomentCaptureMovieFileOutputDelegateWrapper`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureFileOutputDelegateWrapper`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _videoCodecType;
@"NSURL" _spatialOverCaptureMovieFileURL;
@"NSArray" _spatialOverCaptureMovieMetadata;
@"AVMomentCaptureMovieRecordingResolvedSettings" _resolvedSettings;
B _didFinishWritingMovieCallbackFired;
B _didFinishWritingSpatialOverCaptureMovieCallbackFired;
```

## Properties

```
@property (T@"NSString",R,V_videoCodecType) videoCodecType;
@property (T@"NSURL",R,V_spatialOverCaptureMovieFileURL) spatialOverCaptureMovieFileURL;
@property (T@"NSArray",R,V_spatialOverCaptureMovieMetadata) spatialOverCaptureMovieMetadata;
@property (T@"AVMomentCaptureMovieRecordingResolvedSettings",&,N,V_resolvedSettings) resolvedSettings;
@property (TB,N,V_didFinishWritingMovieCallbackFired) didFinishWritingMovieCallbackFired;
@property (TB,N,V_didFinishWritingSpatialOverCaptureMovieCallbackFired) didFinishWritingSpatialOverCaptureMovieCallbackFired;
```

## Class methods

```
+[AVMomentCaptureMovieFileOutputDelegateWrapper wrapperWithSettings:delegate:connections:];
```

## Instance methods

```
-[AVMomentCaptureMovieFileOutputDelegateWrapper dealloc];
-[AVMomentCaptureMovieFileOutputDelegateWrapper resolvedSettings];
-[AVMomentCaptureMovieFileOutputDelegateWrapper setResolvedSettings:];
-[AVMomentCaptureMovieFileOutputDelegateWrapper videoCodecType];
-[AVMomentCaptureMovieFileOutputDelegateWrapper spatialOverCaptureMovieMetadata];
-[AVMomentCaptureMovieFileOutputDelegateWrapper didFinishWritingMovieCallbackFired];
-[AVMomentCaptureMovieFileOutputDelegateWrapper didFinishWritingSpatialOverCaptureMovieCallbackFired];
-[AVMomentCaptureMovieFileOutputDelegateWrapper initWithSettings:delegate:connections:];
-[AVMomentCaptureMovieFileOutputDelegateWrapper setDidFinishWritingMovieCallbackFired:];
-[AVMomentCaptureMovieFileOutputDelegateWrapper setDidFinishWritingSpatialOverCaptureMovieCallbackFired:];
-[AVMomentCaptureMovieFileOutputDelegateWrapper spatialOverCaptureMovieFileURL];
```
