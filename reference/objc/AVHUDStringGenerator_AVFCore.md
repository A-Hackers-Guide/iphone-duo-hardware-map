# `AVHUDStringGenerator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 40 instance variables, 10 properties, 20 instance methods, 4 class methods

## Instance variables

```
@"AVPlayer" _player;
@"NSNumber" _audioSpatializationMode;
@"NSString" _playerItemURL;
@"NSString" _assetType;
@"NSString" _sessionID;
@"NSString" _configurationGroup;
@"NSString" _trackFormatDescriptions;
@"NSNumber" _displayResolutionHeight;
@"NSNumber" _displayResolutionWidth;
@"NSNumber" _refreshRate;
@"NSString" _videoRange;
@"NSNumber" _videoApproximateDisplaySizeHeight;
@"NSNumber" _videoApproximateDisplaySizeWidth;
@"NSNumber" _presentationSizeHeight;
@"NSNumber" _presentationSizeWidth;
@"NSNumber" _currentFrameRate;
@"NSNumber" _nominalFrameRate;
@"NSNumber" _networkBandiwdth;
@"NSNumber" _averageVideoBitrate;
@"NSNumber" _averageAudioBitrate;
@"NSString" _assetTrackInfo;
@"NSNumber" _peakIndicatedBitrate;
@"NSNumber" _averageIndicatedBitrate;
@"NSNumber" _variantIndex;
@"NSNumber" _totalFrameDrops;
@"NSNumber" _decoderFrameDrops;
@"NSNumber" _imageQueueFrameDrops;
@"NSNumber" _bufferedVideoPlayed;
@"NSNumber" _bufferedVideoRemaining;
@"NSString" _customPerfInfo;
@"NSString" _playbackCreationOffset;
@"NSNumber" _totalStalls;
@"NSString" _currentDate;
q _prevVariantIdx;
q _prevStallCount;
q _totalStallCount;
d _startupTime;
B _spatialDiagnostics;
B _captureCompleteURI;
@"NSString" _formattedDisplayString;
```

## Properties

```
@property (T@"AVPlayer",W,V_player) player;
@property (TB,N,V_spatialDiagnostics) spatialDiagnostics;
@property (TB,N,V_captureCompleteURI) captureCompleteURI;
@property (Tq,N,V_prevVariantIdx) prevVariantIdx;
@property (Tq,N,V_prevStallCount) prevStallCount;
@property (Tq,N,V_totalStallCount) totalStallCount;
@property (T@"NSString",R,N,V_formattedDisplayString) formattedDisplayString;
@property (T@"NSNumber",R,N,V_displayResolutionHeight) displayResolutionHeight;
@property (T@"NSNumber",R,N,V_displayResolutionWidth) displayResolutionWidth;
@property (T@"NSNumber",R,N,V_audioSpatializationMode) audioSpatializationMode;
```

## Class methods

```
+[AVHUDStringGenerator descriptionStringForBitRate:];
+[AVHUDStringGenerator descriptionStringForFormatOfTrack:];
+[AVHUDStringGenerator descriptionStringForTracksOfPlayerItem:];
+[AVHUDStringGenerator descriptionStringForVideoRangeOfFormatDescription:];
```

## Instance methods

```
-[AVHUDStringGenerator player];
-[AVHUDStringGenerator update];
-[AVHUDStringGenerator dealloc];
-[AVHUDStringGenerator setPlayer:];
-[AVHUDStringGenerator totalStallCount];
-[AVHUDStringGenerator audioSpatializationMode];
-[AVHUDStringGenerator captureCompleteURI];
-[AVHUDStringGenerator displayResolutionHeight];
-[AVHUDStringGenerator displayResolutionWidth];
-[AVHUDStringGenerator formattedDisplayString];
-[AVHUDStringGenerator prevStallCount];
-[AVHUDStringGenerator prevVariantIdx];
-[AVHUDStringGenerator setCaptureCompleteURI:];
-[AVHUDStringGenerator setPrevStallCount:];
-[AVHUDStringGenerator setPrevVariantIdx:];
-[AVHUDStringGenerator setSpatialDiagnostics:];
-[AVHUDStringGenerator setTotalStallCount:];
-[AVHUDStringGenerator spatialDiagnostics];
-[AVHUDStringGenerator updateFromPlayer];
-[AVHUDStringGenerator updateFromPlayerItem];
```
