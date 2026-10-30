# `AVAsynchronousVideoCompositionRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"AVAsynchronousVideoCompositionRequestInternal" _internal;
```

## Properties

```
@property (T@"AVVideoCompositionRenderContext",R,N) renderContext;
@property (T{?=qiIq},R,N) compositionTime;
@property (T@"NSArray",R,N) sourceTrackIDs;
@property (T@"NSArray",R,N) sourceSampleDataTrackIDs;
@property (T@"<AVVideoCompositionInstruction>",R,N) videoCompositionInstruction;
```

## Instance methods

```
-[AVAsynchronousVideoCompositionRequest finishWithError:];
-[AVAsynchronousVideoCompositionRequest dealloc];
-[AVAsynchronousVideoCompositionRequest copyWithZone:];
-[AVAsynchronousVideoCompositionRequest _willDeallocOrFinalize];
-[AVAsynchronousVideoCompositionRequest renderContext];
-[AVAsynchronousVideoCompositionRequest compositionTime];
-[AVAsynchronousVideoCompositionRequest _validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:reportingObject:reportingSelector:];
-[AVAsynchronousVideoCompositionRequest attachSpatialVideoConfiguration:toPixelBuffer:];
-[AVAsynchronousVideoCompositionRequest compositionFrame];
-[AVAsynchronousVideoCompositionRequest finishCancelledRequest];
-[AVAsynchronousVideoCompositionRequest finishWithComposedTaggedBufferGroup:];
-[AVAsynchronousVideoCompositionRequest finishWithComposedVideoFrame:];
-[AVAsynchronousVideoCompositionRequest initUsingSession:withRenderContext:compositionFrame:atTime:usingSources:instruction:withSampleBuffers:lookupableSpatialVideoConfigurations:];
-[AVAsynchronousVideoCompositionRequest numberOfSourceFramesInWindowForTrackID:];
-[AVAsynchronousVideoCompositionRequest numberOfSourceSampleBuffersInWindowForTrackID:];
-[AVAsynchronousVideoCompositionRequest sourceFrameByTrackID:];
-[AVAsynchronousVideoCompositionRequest sourceFrameByTrackID:atIndexInWindow:presentationTimeStamp:];
-[AVAsynchronousVideoCompositionRequest sourceSampleBufferByTrackID:];
-[AVAsynchronousVideoCompositionRequest sourceSampleBufferByTrackID:atIndexInWindow:presentationTimeStamp:];
-[AVAsynchronousVideoCompositionRequest sourceSampleDataTrackIDs];
-[AVAsynchronousVideoCompositionRequest sourceTaggedBufferGroupByTrackID:];
-[AVAsynchronousVideoCompositionRequest sourceTimedMetadataByTrackID:];
-[AVAsynchronousVideoCompositionRequest sourceTimedMetadataByTrackID:atIndexInWindow:presentationTimeStamp:];
-[AVAsynchronousVideoCompositionRequest sourceTrackIDs];
-[AVAsynchronousVideoCompositionRequest videoCompositionInstruction];
```
