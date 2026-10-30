# `AVAssetWriterInputInterPassAnalysisHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetWriterInputHelper`
- 2 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"AVAssetWriterInputWritingHelper" _writingHelper;
@"AVAssetWriterInputPassDescription" _initialPassDescription;
```

## Instance methods

```
-[AVAssetWriterInputInterPassAnalysisHelper pixelBufferPool];
-[AVAssetWriterInputInterPassAnalysisHelper isReadyForMoreMediaData];
-[AVAssetWriterInputInterPassAnalysisHelper stopRequestingMediaData];
-[AVAssetWriterInputInterPassAnalysisHelper dealloc];
-[AVAssetWriterInputInterPassAnalysisHelper requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVAssetWriterInputInterPassAnalysisHelper status];
-[AVAssetWriterInputInterPassAnalysisHelper appendPixelBuffer:withPresentationTime:];
-[AVAssetWriterInputInterPassAnalysisHelper markAsFinished];
-[AVAssetWriterInputInterPassAnalysisHelper appendCaption:error:];
-[AVAssetWriterInputInterPassAnalysisHelper appendCaptionGroup:error:];
-[AVAssetWriterInputInterPassAnalysisHelper appendSampleBuffer:error:];
-[AVAssetWriterInputInterPassAnalysisHelper appendTaggedPixelBufferGroup:withPresentationTime:];
-[AVAssetWriterInputInterPassAnalysisHelper canBecomeReadyForMoreMediaDataAndReturnError:];
-[AVAssetWriterInputInterPassAnalysisHelper canPerformMultiplePasses];
-[AVAssetWriterInputInterPassAnalysisHelper currentPassDescription];
-[AVAssetWriterInputInterPassAnalysisHelper initWithConfigurationState:];
-[AVAssetWriterInputInterPassAnalysisHelper initWithWritingHelper:];
-[AVAssetWriterInputInterPassAnalysisHelper markCurrentPassAsFinished];
-[AVAssetWriterInputInterPassAnalysisHelper shouldRespondToInitialPassDescription];
-[AVAssetWriterInputInterPassAnalysisHelper startPassAnalysis];
```
