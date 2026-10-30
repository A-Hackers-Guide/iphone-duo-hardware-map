# `BWIrisMovieGenerator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _sourceIsFrontFacingCamera;
B _sourceIsExternalCamera;
B _clientExpectsCameraMountedInLandscapeOrientation;
B _sampleReferenceMoviesEnabled;
{?="value"q"timescale"i"flags"I"epoch"q} _masterMovieDuration;
^{OpaqueCMByteStream=} _byteStream;
^{OpaqueFigFormatReader=} _masterMovieReader;
B _masterMovieParsingComplete;
B _vitalInputStreamHasBeenForcedOff;
i _streamForcedOffErrorCode;
q _masterMovieAudioExtractionID;
{?="value"q"timescale"i"flags"I"epoch"q} _actualMovieStartTime;
^{OpaqueFigSimpleMutex=} _movieInfoAndCallbacksMutex;
@"NSMutableArray" _movieInfoAndCallbacks;
i _numberOfPendingReferenceMovies;
@"NSObject<OS_dispatch_queue>" _movieGenerationQueue;
B _suspended;
@"BWIrisStillImageMovieMetadataCache" _irisStillImageMovieMetadataCache;
@"BWVideoOrientationTimeMachine" _videoOrientationTimeMachine;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
I _smartStyleEditInfosBitmask;
```

## Properties

```
@property (TB) suspended;
@property (Ti,R) numberOfPendingReferenceMovies;
@property (T{?=qiIq},N,V_actualMovieStartTime) actualMovieStartTime;
@property (TB,V_vitalInputStreamHasBeenForcedOff) vitalInputStreamHasBeenForcedOff;
@property (Ti,V_streamForcedOffErrorCode) streamForcedOffErrorCode;
@property (TI,V_smartStyleEditInfosBitmask) smartStyleEditInfosBitmask;
```

## Class methods

```
+[BWIrisMovieGenerator initialize];
```

## Instance methods

```
-[BWIrisMovieGenerator suspended];
-[BWIrisMovieGenerator setSuspended:];
-[BWIrisMovieGenerator disableVitalityForSettingsID:];
-[BWIrisMovieGenerator flush];
-[BWIrisMovieGenerator dealloc];
-[BWIrisMovieGenerator actualMovieStartTime];
-[BWIrisMovieGenerator flushAsync];
-[BWIrisMovieGenerator initWithReadableByteStream:forFrontFacingCamera:forExternalCamera:clientExpectsCameraMountedInLandscapeOrientation:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:];
-[BWIrisMovieGenerator numberOfPendingReferenceMovies];
-[BWIrisMovieGenerator parseAdditionalFragments];
-[BWIrisMovieGenerator setActualMovieStartTime:];
-[BWIrisMovieGenerator setSmartStyleEditInfosBitmask:];
-[BWIrisMovieGenerator setStreamForcedOffErrorCode:];
-[BWIrisMovieGenerator setVitalInputStreamHasBeenForcedOff:];
-[BWIrisMovieGenerator smartStyleEditInfosBitmask];
-[BWIrisMovieGenerator streamForcedOffErrorCode];
-[BWIrisMovieGenerator updateOverCaptureQualityScoresForMoviesEndingBefore:fromMetadataRingBuffer:];
-[BWIrisMovieGenerator vitalInputStreamHasBeenForcedOff];
-[BWIrisMovieGenerator writeMovieWithInfo:completionHandler:];
```
