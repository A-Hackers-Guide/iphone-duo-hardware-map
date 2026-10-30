# `AVMutableComposition`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVComposition`
- 1 instance variables, 2 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"AVMutableCompositionInternal" _mutablePriv;
```

## Properties

```
@property (T@"NSArray",R,N) tracks;
@property (T{CGSize=dd},N) naturalSize;
```

## Class methods

```
+[AVMutableComposition composition];
+[AVMutableComposition compositionWithURLAssetInitializationOptions:];
```

## Instance methods

```
-[AVMutableComposition setNaturalSize:];
-[AVMutableComposition _removeTrack:fireKVO:];
-[AVMutableComposition tracksWithMediaCharacteristic:];
-[AVMutableComposition tracksWithMediaType:];
-[AVMutableComposition _addMutableTrackWithMediaType:preferredTrackID:fireKVO:];
-[AVMutableComposition naturalSize];
-[AVMutableComposition _initWithComposition:];
-[AVMutableComposition insertTimeRange:ofAsset:atTime:completionHandler:];
-[AVMutableComposition removeTimeRange:];
-[AVMutableComposition mutableTrackCompatibleWithTrack:];
-[AVMutableComposition removeTrack:];
-[AVMutableComposition _notifyTracksThatSegmentsDidChange:successfully:];
-[AVMutableComposition trackWithTrackID:];
-[AVMutableComposition insertEmptyTimeRange:];
-[AVMutableComposition scaleTimeRange:toDuration:];
-[AVMutableComposition setMetadata:];
-[AVMutableComposition _notifyTracksThatSegmentsWillChange:];
-[AVMutableComposition addMutableTrackWithMediaType:preferredTrackID:];
-[AVMutableComposition copyWithZone:];
-[AVMutableComposition tracks];
-[AVMutableComposition insertTimeRange:ofAsset:atTime:error:];
-[AVMutableComposition _newTrackForIndex:];
```
