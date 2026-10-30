# `JFXAVMediaVideoTrackReader`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXAVMediaDataReader`
- Protocols: `JFXMediaVideoTrackReader`
- 2 instance variables, 12 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"JFXAVMediaVideoTrackReaderSample" _currentSample;
@"JFXAVMediaVideoTrackReaderSample" _nextSample;
```

## Properties

```
@property (T@"JFXAVMediaVideoTrackReaderSample",&,N,V_currentSample) currentSample;
@property (T@"JFXAVMediaVideoTrackReaderSample",&,N,V_nextSample) nextSample;
@property (T{?={?=qiIq}{?=qiIq}},R,N) readableTimeRange;
@property (TB,N) isScrubbing;
@property (Tq,R,N) status;
@property (T@"NSError",R,N) error;
@property (TQ,R,N) signPostID;
@property (T@"NSString",R,N) name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JFXAVMediaVideoTrackReader currentSample];
-[JFXAVMediaVideoTrackReader setCurrentSample:];
-[JFXAVMediaVideoTrackReader nextSample];
-[JFXAVMediaVideoTrackReader JFX_preloadData];
-[JFXAVMediaVideoTrackReader JFX_updateCurrentSampleDurationIfNeeded];
-[JFXAVMediaVideoTrackReader createAssetReaderTrackOutput];
-[JFXAVMediaVideoTrackReader didUpdateReadingRange];
-[JFXAVMediaVideoTrackReader hasRemainingAvailableData];
-[JFXAVMediaVideoTrackReader readAheadToTime:];
-[JFXAVMediaVideoTrackReader readAndDiscardRemainingAvailableData];
-[JFXAVMediaVideoTrackReader setNextSample:];
-[JFXAVMediaVideoTrackReader startTimeOfCurrentData];
-[JFXAVMediaVideoTrackReader videoSampleForTime:];
```
