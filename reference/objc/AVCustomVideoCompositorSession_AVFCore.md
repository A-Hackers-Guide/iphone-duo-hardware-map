# `AVCustomVideoCompositorSession`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 2 properties, 24 instance methods, 2 class methods

## Instance variables

```
^{OpaqueFigVideoCompositor=} _figCustomCompositor;
B _hasRegisteredFigCustomCompositorCallbacks;
@"NSDictionary" _clientRequiredPixelBufferAttributes;
@"AVWeakReference" _weakSelf;
^v _callbackContextToken;
@"NSObject<OS_dispatch_queue>" _videoCompositionQ;
@"AVVideoComposition" _videoComposition;
B _videoCompositionDidChange;
@"NSObject<OS_dispatch_queue>" _clientCustomCompositorQ;
@"<AVVideoCompositing>" _clientCustomCompositor;
@"NSObject<OS_dispatch_queue>" _clientErrorQ;
@"NSError" _clientError;
@"NSObject<OS_dispatch_queue>" _renderContextQ;
@"AVVideoCompositionRenderContext" _renderContext;
@"NSObject<OS_dispatch_queue>" _finishedRequestQ;
```

## Properties

```
@property (TB,R,N) supportsWideColorSourceFrames;
@property (TB,R,N) supportsHDRSourceFrames;
```

## Class methods

```
+[AVCustomVideoCompositorSession _colorPropertiesAreSetInVideoComposition:];
+[AVCustomVideoCompositorSession sessionWithVideoComposition:recyclingSession:];
```

## Instance methods

```
-[AVCustomVideoCompositorSession setVideoComposition:];
-[AVCustomVideoCompositorSession dealloc];
-[AVCustomVideoCompositorSession _willDeallocOrFinalize];
-[AVCustomVideoCompositorSession _cleanupFigCallbacks];
-[AVCustomVideoCompositorSession _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:];
-[AVCustomVideoCompositorSession _copyFigVideoCompositor];
-[AVCustomVideoCompositorSession _customCompositorFigPropertyDidChange];
-[AVCustomVideoCompositorSession _customCompositorShouldAnticipateRenderingFromTime:toTime:andThenFromTime:toTime:];
-[AVCustomVideoCompositorSession _customCompositorShouldCancelPendingFrames];
-[AVCustomVideoCompositorSession _customCompositorShouldPrerollForRenderingFromTime:toTime:andThenFromTime:toTime:requestID:];
-[AVCustomVideoCompositorSession _setupFigCallbacks];
-[AVCustomVideoCompositorSession _validateRequiredPixelBufferAttributesForRenderContext:andReturnException:];
-[AVCustomVideoCompositorSession _validateSourcePixelBufferAttributes:andReturnException:];
-[AVCustomVideoCompositorSession commitCustomVideoCompositorPropertiesAndReturnError:];
-[AVCustomVideoCompositorSession compositionFrame:didFinishWithComposedPixelBuffer:];
-[AVCustomVideoCompositorSession compositionFrame:didFinishWithComposedTaggedBufferGroup:];
-[AVCustomVideoCompositorSession compositionFrame:didFinishWithError:];
-[AVCustomVideoCompositorSession compositionFrameDidCancel:];
-[AVCustomVideoCompositorSession customVideoCompositor];
-[AVCustomVideoCompositorSession detachVideoComposition];
-[AVCustomVideoCompositorSession getAndClearClientError];
-[AVCustomVideoCompositorSession initWithVideoComposition:];
-[AVCustomVideoCompositorSession supportsHDRSourceFrames];
-[AVCustomVideoCompositorSession supportsWideColorSourceFrames];
```
