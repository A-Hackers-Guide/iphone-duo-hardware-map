# `JFXMovieCompositionItem`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXCompositionItem`
- 3 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
i _audioAssetOverwriteStartOffset;
@"AVAsset" _asset;
@"AVAsset" _audioAssetOverwrite;
```

## Properties

```
@property (T@"AVAsset",&,N,V_asset) asset;
@property (T@"AVAsset",&,N,V_audioAssetOverwrite) audioAssetOverwrite;
@property (Ti,N,V_audioAssetOverwriteStartOffset) audioAssetOverwriteStartOffset;
```

## Instance methods

```
-[JFXMovieCompositionItem asset];
-[JFXMovieCompositionItem setAsset:];
-[JFXMovieCompositionItem hasVideoContent];
-[JFXMovieCompositionItem applySpeed:];
-[JFXMovieCompositionItem audioAssetOverwrite];
-[JFXMovieCompositionItem audioAssetOverwriteStartOffset];
-[JFXMovieCompositionItem audioTrackSegmentsLoopedForDestinationTimeRange:];
-[JFXMovieCompositionItem audioTrackSegmentsLoopedWithDestinationTime:];
-[JFXMovieCompositionItem audioTrackSegmentsWithDestinationTime:];
-[JFXMovieCompositionItem audioTrackSegmentsWithDestinationTime:paddedFromTime:];
-[JFXMovieCompositionItem initWithClip:timeScale:];
-[JFXMovieCompositionItem needAudioLoop];
-[JFXMovieCompositionItem segmentWithCharacteristic:sourceRange:destinationRange:];
-[JFXMovieCompositionItem setAudioAssetOverwrite:];
-[JFXMovieCompositionItem setAudioAssetOverwriteStartOffset:];
-[JFXMovieCompositionItem speedRangesForSourceRange:destinationRange:];
-[JFXMovieCompositionItem videoTrackSegmentsWithDestinationRange:];
```
