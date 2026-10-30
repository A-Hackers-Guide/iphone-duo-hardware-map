# `JFXAVMediaDataReader`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXMediaDataReader`
- 12 instance variables, 16 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _isScrubbing;
@"NSString" _name;
q _status;
@"NSError" _error;
@"AVAssetTrack" _assetTrack;
@"AVAsset" _asset;
@"AVAssetReader" _assetReader;
@"AVAssetReaderTrackOutput" _assetReaderTrackOutput;
Q _signPostID;
{?="value"q"timescale"i"flags"I"epoch"q} _minimumFrameDuration;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _readableTimeRange;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _currentReadingRange;
```

## Properties

```
@property (Tq,N,V_status) status;
@property (T@"NSError",&,N,V_error) error;
@property (T@"AVAssetTrack",&,N,V_assetTrack) assetTrack;
@property (T@"AVAsset",&,N,V_asset) asset;
@property (T@"AVAssetReader",&,N,V_assetReader) assetReader;
@property (T@"AVAssetReaderTrackOutput",&,N,V_assetReaderTrackOutput) assetReaderTrackOutput;
@property (T{?=qiIq},R,N,V_minimumFrameDuration) minimumFrameDuration;
@property (TQ,N,V_signPostID) signPostID;
@property (T{?={?=qiIq}{?=qiIq}},N,V_readableTimeRange) readableTimeRange;
@property (T{?={?=qiIq}{?=qiIq}},N,V_currentReadingRange) currentReadingRange;
@property (TB,N,V_isScrubbing) isScrubbing;
@property (T@"NSString",R,N,V_name) name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JFXAVMediaDataReader didFailWithError:];
-[JFXAVMediaDataReader setError:];
-[JFXAVMediaDataReader asset];
-[JFXAVMediaDataReader setIsScrubbing:];
-[JFXAVMediaDataReader setAsset:];
-[JFXAVMediaDataReader minimumFrameDuration];
-[JFXAVMediaDataReader isScrubbing];
-[JFXAVMediaDataReader status];
-[JFXAVMediaDataReader assetTrack];
-[JFXAVMediaDataReader seekToTime:];
-[JFXAVMediaDataReader error];
-[JFXAVMediaDataReader setStatus:];
-[JFXAVMediaDataReader name];
-[JFXAVMediaDataReader assetReaderTrackOutput];
-[JFXAVMediaDataReader setAssetReader:];
-[JFXAVMediaDataReader assetReader];
-[JFXAVMediaDataReader JFX_allMediaTimeRange];
-[JFXAVMediaDataReader JFX_configureAssetReaderToReadFromTime:];
-[JFXAVMediaDataReader JFX_resetReaderFromTime:];
-[JFXAVMediaDataReader JFX_resetReadingRangeWhenScrubbingToTime:];
-[JFXAVMediaDataReader JFX_configureAssetReaderTrackOutput];
-[JFXAVMediaDataReader JFX_releaseReadersForReset];
-[JFXAVMediaDataReader JFX_resetReaderIfNecessaryToSeekFromStartTimeOfCurrentData:toTime:];
-[JFXAVMediaDataReader JFX_shouldResetReaderWhenSeekingFromStartTimeOfCurrentData:toTime:];
-[JFXAVMediaDataReader beginReading];
-[JFXAVMediaDataReader beginReadingAtTime:];
-[JFXAVMediaDataReader beginReadingAtTimeRange:];
-[JFXAVMediaDataReader cancelReadingForReaderReset];
-[JFXAVMediaDataReader createAssetReader];
-[JFXAVMediaDataReader createAssetReaderTrackOutput];
-[JFXAVMediaDataReader currentReadingRange];
-[JFXAVMediaDataReader didUpdateReadingRange];
-[JFXAVMediaDataReader hasRemainingAvailableData];
-[JFXAVMediaDataReader initWithAVAssetTrack:withName:];
-[JFXAVMediaDataReader prepareAssetReaderForReading];
-[JFXAVMediaDataReader readAheadToTime:];
-[JFXAVMediaDataReader readAndDiscardRemainingAvailableData];
-[JFXAVMediaDataReader readableTimeRange];
-[JFXAVMediaDataReader seekingAheadIsExpensiveFromTime:toTime:];
-[JFXAVMediaDataReader setAssetReaderTrackOutput:];
-[JFXAVMediaDataReader setAssetTrack:];
-[JFXAVMediaDataReader setCurrentReadingRange:];
-[JFXAVMediaDataReader setReadableTimeRange:];
-[JFXAVMediaDataReader setSignPostID:];
-[JFXAVMediaDataReader signPostID];
-[JFXAVMediaDataReader startTimeOfCurrentData];
```
