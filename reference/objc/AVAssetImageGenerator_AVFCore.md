# `AVAssetImageGenerator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 9 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"AVAssetImageGeneratorInternal" _priv;
```

## Properties

```
@property (T@"AVAsset",R,N) asset;
@property (TB,N) appliesPreferredTrackTransform;
@property (T{CGSize=dd},N) maximumSize;
@property (T@"NSString",C,N) apertureMode;
@property (T@"NSString",C,N) dynamicRangePolicy;
@property (T@"AVVideoComposition",C,N) videoComposition;
@property (T@"<AVVideoCompositing>",R,N) customVideoCompositor;
@property (T{?=qiIq},N) requestedTimeToleranceBefore;
@property (T{?=qiIq},N) requestedTimeToleranceAfter;
```

## Class methods

```
+[AVAssetImageGenerator assetImageGeneratorWithAsset:];
```

## Instance methods

```
-[AVAssetImageGenerator setMaximumSize:];
-[AVAssetImageGenerator _serverDied];
-[AVAssetImageGenerator setAppliesPreferredTrackTransform:];
-[AVAssetImageGenerator asset];
-[AVAssetImageGenerator maximumSize];
-[AVAssetImageGenerator setVideoComposition:];
-[AVAssetImageGenerator init];
-[AVAssetImageGenerator dealloc];
-[AVAssetImageGenerator status];
-[AVAssetImageGenerator isDefunct];
-[AVAssetImageGenerator appliesPreferredTrackTransform];
-[AVAssetImageGenerator initWithAsset:];
-[AVAssetImageGenerator _invalidated];
-[AVAssetImageGenerator videoComposition];
-[AVAssetImageGenerator copyCGImageAtTime:actualTime:error:];
-[AVAssetImageGenerator _videoSettingWithSize:bitDepth:];
-[AVAssetImageGenerator setRequestedTimeToleranceAfter:];
-[AVAssetImageGenerator setPrefersStandardDynamicRange:];
-[AVAssetImageGenerator _NSErrorForError:];
-[AVAssetImageGenerator _copyCGImageAtTime:usingAssetReader:error:];
-[AVAssetImageGenerator _didGenerateCGImage:];
-[AVAssetImageGenerator _ensureFigAssetImageGeneratorAllowingSynchronousPropertyLoad:error:];
-[AVAssetImageGenerator _failedToGenerateCGImage:];
-[AVAssetImageGenerator _makeAutoreleasedAssetReader];
-[AVAssetImageGenerator _optionsDictionary];
-[AVAssetImageGenerator _requestWithRequestID:];
-[AVAssetImageGenerator _scaledSizeForRenderSize:];
-[AVAssetImageGenerator apertureMode];
-[AVAssetImageGenerator cancelAllCGImageGeneration];
-[AVAssetImageGenerator customVideoCompositor];
-[AVAssetImageGenerator dynamicRangePolicy];
-[AVAssetImageGenerator generateCGImageAsynchronouslyForTime:completionHandler:];
-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:];
-[AVAssetImageGenerator prefersStandardDynamicRange];
-[AVAssetImageGenerator requestedTimeToleranceAfter];
-[AVAssetImageGenerator requestedTimeToleranceBefore];
-[AVAssetImageGenerator setApertureMode:];
-[AVAssetImageGenerator setDynamicRangePolicy:];
-[AVAssetImageGenerator setRequestedTimeToleranceBefore:];
-[AVAssetImageGenerator setUseSWDecoderForAV1:];
-[AVAssetImageGenerator useSWDecoderForAV1];
```
