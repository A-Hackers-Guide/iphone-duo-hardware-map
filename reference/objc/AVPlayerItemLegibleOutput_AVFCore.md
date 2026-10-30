# `AVPlayerItemLegibleOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayerItemOutput`
- 1 instance variables, 3 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"AVPlayerItemLegibleOutputInternal" _legibleOutputInternal;
```

## Properties

```
@property (T@"<AVPlayerItemLegibleOutputPushDelegate>",R,W,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
@property (Td,N) advanceIntervalForDelegateInvocation;
```

## Class methods

```
+[AVPlayerItemLegibleOutput initialize];
```

## Instance methods

```
-[AVPlayerItemLegibleOutput setDelegate:queue:];
-[AVPlayerItemLegibleOutput init];
-[AVPlayerItemLegibleOutput dealloc];
-[AVPlayerItemLegibleOutput isDefunct];
-[AVPlayerItemLegibleOutput delegate];
-[AVPlayerItemLegibleOutput delegateQueue];
-[AVPlayerItemLegibleOutput initWithDependencyFactory:mediaSubtypesForNativeRepresentation:];
-[AVPlayerItemLegibleOutput _attachToPlayerItem:];
-[AVPlayerItemLegibleOutput _collectUncollectables];
-[AVPlayerItemLegibleOutput _detachFromPlayerItem];
-[AVPlayerItemLegibleOutput _figLegibleOutputsDictionaryOptions];
-[AVPlayerItemLegibleOutput _pushAttributedStrings:andSampleBuffers:atItemTime:];
-[AVPlayerItemLegibleOutput _signalFlush];
-[AVPlayerItemLegibleOutput advanceIntervalForDelegateInvocation];
-[AVPlayerItemLegibleOutput initWithMediaSubtypesForNativeRepresentation:];
-[AVPlayerItemLegibleOutput setAdvanceIntervalForDelegateInvocation:];
-[AVPlayerItemLegibleOutput setSuppressesPlayerRendering:];
-[AVPlayerItemLegibleOutput setTextStylingResolution:];
-[AVPlayerItemLegibleOutput suppressesPlayerRendering];
-[AVPlayerItemLegibleOutput textStylingResolution];
```
