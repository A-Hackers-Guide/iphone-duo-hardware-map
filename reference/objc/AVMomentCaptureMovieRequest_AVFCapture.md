# `AVMomentCaptureMovieRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 8 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReferencingDelegateStorage" _delegateStorage;
@"AVMomentCaptureSettings" _momentCaptureSettings;
@"AVMomentCaptureMovieRecordingSettings" _unresolvedSettings;
@"AVMomentCaptureMovieRecordingResolvedSettings" _resolvedSettings;
I _firedCallbackFlags;
@"AVMomentCaptureMovie" movie;
@"AVMomentCaptureMovie" spatialOverCaptureMovie;
Q _expectedMovieCount;
@"AVMomentCaptureMovie" _movie;
@"AVMomentCaptureMovie" _spatialOverCaptureMovie;
```

## Properties

```
@property (T@"AVWeakReferencingDelegateStorage",R,V_delegateStorage) delegateStorage;
@property (T@"AVMomentCaptureSettings",R,V_momentCaptureSettings) momentCaptureSettings;
@property (T@"AVMomentCaptureMovieRecordingSettings",R,V_unresolvedSettings) unresolvedSettings;
@property (T@"AVMomentCaptureMovieRecordingResolvedSettings",&,N) resolvedSettings;
@property (TQ,R,N,V_expectedMovieCount) expectedMovieCount;
@property (TI,N,V_firedCallbackFlags) firedCallbackFlags;
@property (T@"AVMomentCaptureMovie",&,N,V_movie) movie;
@property (T@"AVMomentCaptureMovie",&,N,V_spatialOverCaptureMovie) spatialOverCaptureMovie;
```

## Class methods

```
+[AVMomentCaptureMovieRequest requestWithDelegate:movieRecordingSettings:momentSettings:];
```

## Instance methods

```
-[AVMomentCaptureMovieRequest setFiredCallbackFlags:];
-[AVMomentCaptureMovieRequest dealloc];
-[AVMomentCaptureMovieRequest delegateStorage];
-[AVMomentCaptureMovieRequest unresolvedSettings];
-[AVMomentCaptureMovieRequest resolvedSettings];
-[AVMomentCaptureMovieRequest setResolvedSettings:];
-[AVMomentCaptureMovieRequest movie];
-[AVMomentCaptureMovieRequest firedCallbackFlags];
-[AVMomentCaptureMovieRequest setMovie:];
-[AVMomentCaptureMovieRequest _initWithDelegate:movieRecordingSettings:momentSettings:];
-[AVMomentCaptureMovieRequest expectedMovieCount];
-[AVMomentCaptureMovieRequest momentCaptureSettings];
-[AVMomentCaptureMovieRequest setSpatialOverCaptureMovie:];
-[AVMomentCaptureMovieRequest spatialOverCaptureMovie];
```
