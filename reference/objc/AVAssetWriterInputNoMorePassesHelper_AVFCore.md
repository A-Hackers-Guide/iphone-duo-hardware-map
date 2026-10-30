# `AVAssetWriterInputNoMorePassesHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetWriterInputHelper`
- 1 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"AVAssetWriterInputWritingHelper" _writingHelper;
```

## Instance methods

```
-[AVAssetWriterInputNoMorePassesHelper pixelBufferPool];
-[AVAssetWriterInputNoMorePassesHelper isReadyForMoreMediaData];
-[AVAssetWriterInputNoMorePassesHelper stopRequestingMediaData];
-[AVAssetWriterInputNoMorePassesHelper dealloc];
-[AVAssetWriterInputNoMorePassesHelper requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVAssetWriterInputNoMorePassesHelper status];
-[AVAssetWriterInputNoMorePassesHelper appendPixelBuffer:withPresentationTime:];
-[AVAssetWriterInputNoMorePassesHelper markAsFinished];
-[AVAssetWriterInputNoMorePassesHelper appendCaption:error:];
-[AVAssetWriterInputNoMorePassesHelper appendCaptionGroup:error:];
-[AVAssetWriterInputNoMorePassesHelper appendSampleBuffer:error:];
-[AVAssetWriterInputNoMorePassesHelper appendTaggedPixelBufferGroup:withPresentationTime:];
-[AVAssetWriterInputNoMorePassesHelper canBecomeReadyForMoreMediaDataAndReturnError:];
-[AVAssetWriterInputNoMorePassesHelper canPerformMultiplePasses];
-[AVAssetWriterInputNoMorePassesHelper currentPassDescription];
-[AVAssetWriterInputNoMorePassesHelper initWithConfigurationState:];
-[AVAssetWriterInputNoMorePassesHelper initWithWritingHelper:];
-[AVAssetWriterInputNoMorePassesHelper markCurrentPassAsFinished];
```
