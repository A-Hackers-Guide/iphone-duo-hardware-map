# `AVAssetWriterInputWritingHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetWriterInputHelper`
- Protocols: `AVAssetWriterInputMediaDataRequesterDelegate`, `AVWeakObservable`, `AVKeyPathDependencyHost`
- 9 instance variables, 6 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"AVFigAssetWriterTrack" _assetWriterTrack;
@"AVAssetWriterInputMediaDataRequester" _mediaDataRequester;
B _observingSelf;
B _didCheckProResRAWRequiredMetadata;
^{__CVPixelBufferPool=} _pixelBufferPool;
@"AVAssetWriterInputPassDescription" _currentPassDescription;
@"AVKeyPathDependencyManager" _keyPathDependencyManager;
@"NSObject<OS_dispatch_queue>" _mediaDataRequesterSerialQueue;
@"NSObject<OS_dispatch_queue>" _readyForMoreMediaDataObserverSerialQueue;
```

## Properties

```
@property (T@"AVFigAssetWriterTrack",R,N,G_assetWriterTrack,V_assetWriterTrack) assetWriterTrack;
@property (T@"AVAssetWriterInputPassDescription",&,N,V_currentPassDescription) currentPassDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAssetWriterInputWritingHelper observeValueForKeyPath:ofObject:change:context:];
-[AVAssetWriterInputWritingHelper pixelBufferPool];
-[AVAssetWriterInputWritingHelper isReadyForMoreMediaData];
-[AVAssetWriterInputWritingHelper stopRequestingMediaData];
-[AVAssetWriterInputWritingHelper dealloc];
-[AVAssetWriterInputWritingHelper requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVAssetWriterInputWritingHelper status];
-[AVAssetWriterInputWritingHelper appendPixelBuffer:withPresentationTime:];
-[AVAssetWriterInputWritingHelper markAsFinished];
-[AVAssetWriterInputWritingHelper _assetWriterTrack];
-[AVAssetWriterInputWritingHelper _checkIfClientSetProResRAWRequiredMetadataReturningError:];
-[AVAssetWriterInputWritingHelper _checkProResRAWRequiredMetadataForPixelBufferReturningError:];
-[AVAssetWriterInputWritingHelper _checkProResRAWRequiredMetadataForSampleBuffer:error:];
-[AVAssetWriterInputWritingHelper _nudgeMediaDataRequesterIfAppropriate:];
-[AVAssetWriterInputWritingHelper _startObservingReadyForMoreMediaDataKeyPath];
-[AVAssetWriterInputWritingHelper _stopObservingReadyForMoreMediaDataKeyPath];
-[AVAssetWriterInputWritingHelper addCallbackToCancelDuringDeallocation:];
-[AVAssetWriterInputWritingHelper appendCaption:error:];
-[AVAssetWriterInputWritingHelper appendCaptionGroup:error:];
-[AVAssetWriterInputWritingHelper appendSampleBuffer:error:];
-[AVAssetWriterInputWritingHelper appendTaggedPixelBufferGroup:withPresentationTime:];
-[AVAssetWriterInputWritingHelper beginPassIfAppropriate];
-[AVAssetWriterInputWritingHelper canBecomeReadyForMoreMediaDataAndReturnError:];
-[AVAssetWriterInputWritingHelper canPerformMultiplePasses];
-[AVAssetWriterInputWritingHelper currentPassDescription];
-[AVAssetWriterInputWritingHelper declareKeyPathDependenciesWithRegistry:];
-[AVAssetWriterInputWritingHelper didStartInitialSession];
-[AVAssetWriterInputWritingHelper initWithConfigurationState:];
-[AVAssetWriterInputWritingHelper initWithConfigurationState:assetWriterTrack:error:];
-[AVAssetWriterInputWritingHelper markAsFinishedAndTransitionCurrentHelper:];
-[AVAssetWriterInputWritingHelper markCurrentPassAsFinished];
-[AVAssetWriterInputWritingHelper mediaDataRequesterShouldRequestMediaData];
-[AVAssetWriterInputWritingHelper prepareToEndSession];
-[AVAssetWriterInputWritingHelper prepareToFinishWritingReturningError:];
-[AVAssetWriterInputWritingHelper setCurrentPassDescription:];
-[AVAssetWriterInputWritingHelper transitionToAndReturnTerminalHelperWithTerminalStatus:];
```
