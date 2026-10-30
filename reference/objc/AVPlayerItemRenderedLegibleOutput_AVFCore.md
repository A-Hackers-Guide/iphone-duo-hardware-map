# `AVPlayerItemRenderedLegibleOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayerItemOutput`
- 7 instance variables, 4 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<AVPlayerItemRenderedLegibleOutputDependencyFactory>" _dependencyFactory;
@"AVWeakReferencingDelegateStorage" _delegateStorage;
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
@"AVWeakReference" _weakReferenceToHost;
B _suppressesPlayerRendering;
d _advanceInterval;
{CGSize="width"d"height"d} _videoDisplaySize;
```

## Properties

```
@property (T@"<AVPlayerItemRenderedLegibleOutputPushDelegate>",R,W,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
@property (Td,N) advanceIntervalForDelegateInvocation;
@property (T{CGSize=dd},N) videoDisplaySize;
```

## Class methods

```
+[AVPlayerItemRenderedLegibleOutput initialize];
```

## Instance methods

```
-[AVPlayerItemRenderedLegibleOutput setDelegate:queue:];
-[AVPlayerItemRenderedLegibleOutput dealloc];
-[AVPlayerItemRenderedLegibleOutput isDefunct];
-[AVPlayerItemRenderedLegibleOutput delegate];
-[AVPlayerItemRenderedLegibleOutput delegateQueue];
-[AVPlayerItemRenderedLegibleOutput _attachToPlayerItem:];
-[AVPlayerItemRenderedLegibleOutput _collectUncollectables];
-[AVPlayerItemRenderedLegibleOutput _detachFromPlayerItem];
-[AVPlayerItemRenderedLegibleOutput _figRenderedLegibleOutputsDictionaryOptions];
-[AVPlayerItemRenderedLegibleOutput _pushRenderedCaptionImages:atItemTime:];
-[AVPlayerItemRenderedLegibleOutput _signalFlush];
-[AVPlayerItemRenderedLegibleOutput advanceIntervalForDelegateInvocation];
-[AVPlayerItemRenderedLegibleOutput initWithDependencyFactory:videoDisplaySize:];
-[AVPlayerItemRenderedLegibleOutput initWithVideoDisplaySize:];
-[AVPlayerItemRenderedLegibleOutput setAdvanceIntervalForDelegateInvocation:];
-[AVPlayerItemRenderedLegibleOutput setSuppressesPlayerRendering:];
-[AVPlayerItemRenderedLegibleOutput setVideoDisplaySize:];
-[AVPlayerItemRenderedLegibleOutput suppressesPlayerRendering];
-[AVPlayerItemRenderedLegibleOutput videoDisplaySize];
```
