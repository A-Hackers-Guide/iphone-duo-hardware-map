# `AVMutableCompositionTrack`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCompositionTrack`
- 1 instance variables, 7 properties, 35 instance methods, 1 class methods

## Instance variables

```
@"AVMutableCompositionTrackInternal" _mutablePriv;
```

## Properties

```
@property (TB,N,GisEnabled) enabled;
@property (Ti,N) naturalTimeScale;
@property (T@"NSString",C,N) languageCode;
@property (T@"NSString",C,N) extendedLanguageTag;
@property (T{CGAffineTransform=dddddd},N) preferredTransform;
@property (Tf,N) preferredVolume;
@property (T@"NSArray",C,N) segments;
```

## Class methods

```
+[AVMutableCompositionTrack expectsPropertyRevisedNotifications];
```

## Instance methods

```
-[AVMutableCompositionTrack segments];
-[AVMutableCompositionTrack setExtendedLanguageTag:];
-[AVMutableCompositionTrack setPreferredVolume:];
-[AVMutableCompositionTrack replaceFormatDescription:withFormatDescription:];
-[AVMutableCompositionTrack _notifySelfThatSegmentsDidChangeWithSuccess:];
-[AVMutableCompositionTrack preferredTransform];
-[AVMutableCompositionTrack _insertTimeRange:ofTrack:atTime:fireKVO:error:];
-[AVMutableCompositionTrack _updateTrackAssociationToTrack:type:operation:];
-[AVMutableCompositionTrack removeTimeRange:];
-[AVMutableCompositionTrack setPreferredTransform:];
-[AVMutableCompositionTrack _removeTimeRange:fireKVO:];
-[AVMutableCompositionTrack isEnabled];
-[AVMutableCompositionTrack preferredVolume];
-[AVMutableCompositionTrack languageCode];
-[AVMutableCompositionTrack _notifyAssetThatDurationDidChangeWithSuccess:];
-[AVMutableCompositionTrack insertEmptyTimeRange:];
-[AVMutableCompositionTrack setNaturalTimeScale:];
-[AVMutableCompositionTrack alternateGroupID];
-[AVMutableCompositionTrack setEnabled:];
-[AVMutableCompositionTrack scaleTimeRange:toDuration:];
-[AVMutableCompositionTrack removeTrackAssociationToTrack:type:];
-[AVMutableCompositionTrack setMetadata:];
-[AVMutableCompositionTrack insertTimeRange:ofTrack:atTime:error:];
-[AVMutableCompositionTrack naturalTimeScale];
-[AVMutableCompositionTrack _notifySelfThatSegmentsWillChange];
-[AVMutableCompositionTrack setAlternateGroupID:];
-[AVMutableCompositionTrack insertTimeRanges:ofTracks:atTime:error:];
-[AVMutableCompositionTrack addTrackAssociationToTrack:type:];
-[AVMutableCompositionTrack validateTrackSegments:error:];
-[AVMutableCompositionTrack extendedLanguageTag];
-[AVMutableCompositionTrack _notifyAssetThatDurationWillChange];
-[AVMutableCompositionTrack _setTrackReaderPropertyValue:forKey:];
-[AVMutableCompositionTrack setSegments:];
-[AVMutableCompositionTrack _insertEmptyTimeRange:fireKVO:];
-[AVMutableCompositionTrack setLanguageCode:];
```
