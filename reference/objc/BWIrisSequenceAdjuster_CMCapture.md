# `BWIrisSequenceAdjuster`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _discontinuities;
{?="value"q"timescale"i"flags"I"epoch"q} _firstIrisAudioOffset;
@"NSMutableArray" _interleavingQueues;
{?="value"q"timescale"i"flags"I"epoch"q} _nextAdjustedVideoTime;
^I _mediaTypes;
@"NSMutableArray" _timeSkews;
{?="value"q"timescale"i"flags"I"epoch"q} _masterMovieOriginalStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _previewFrameDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _lastVideoAdjustedTime;
@"BWMotionDataPreserver" _motionDataPreserver;
B _generateIFrames;
@"NSArray" _attachedMediaKeysToPreserve;
@"NSMutableDictionary" _preservedAttachedMediaSbufByKeys;
i _audioOffsetForOriginalStillImageTimeMaximumFrameLatency;
```

## Properties

```
@property (Ti,N,V_audioOffsetForOriginalStillImageTimeMaximumFrameLatency) audioOffsetForOriginalStillImageTimeMaximumFrameLatency;
@property (T{?=qiIq},N) masterMovieOriginalStartTime;
@property (TB,R) readyToReleaseAudio;
@property (TQ,R) maximumNumberOfPreDiscontinuityFramesNeededToSatisfyAllDropFrameRecipes;
@property (T{?=qiIq},R,N,V_previewFrameDuration) previewFrameDuration;
```

## Class methods

```
+[BWIrisSequenceAdjuster initialize];
```

## Instance methods

```
-[BWIrisSequenceAdjuster audioOffsetForOriginalStillImageTime:];
-[BWIrisSequenceAdjuster adjustMovieInfoTimes:];
-[BWIrisSequenceAdjuster setAudioOffsetForOriginalStillImageTimeMaximumFrameLatency:];
-[BWIrisSequenceAdjuster setMasterMovieOriginalStartTime:];
-[BWIrisSequenceAdjuster enqueueSampleBuffer:forMediaTypeWithIndex:];
-[BWIrisSequenceAdjuster dealloc];
-[BWIrisSequenceAdjuster reset];
-[BWIrisSequenceAdjuster enqueueVideoBufferTime:nativeTime:isBracketFrame:isSISFrame:];
-[BWIrisSequenceAdjuster adjustedTimeForStillImageTime:];
-[BWIrisSequenceAdjuster initWithMediaTypes:visMotionMetadataPreloadingEnabled:generateIFrames:attachedMediaKeysToPreserve:];
-[BWIrisSequenceAdjuster previewFrameDuration];
-[BWIrisSequenceAdjuster dequeueAndRetainAdjustedSampleBufferForMediaTypeWithIndex:];
-[BWIrisSequenceAdjuster maximumNumberOfPreDiscontinuityFramesNeededToSatisfyAllDropFrameRecipes];
-[BWIrisSequenceAdjuster discontinuityExistsBetweenCurrentPTS:previousPTS:];
-[BWIrisSequenceAdjuster masterMovieOriginalStartTime];
-[BWIrisSequenceAdjuster audioOffsetForOriginalStillImageTimeMaximumFrameLatency];
-[BWIrisSequenceAdjuster adjustedTimeForTime:];
-[BWIrisSequenceAdjuster readyToReleaseAudio];
```
