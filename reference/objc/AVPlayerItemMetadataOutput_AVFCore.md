# `AVPlayerItemMetadataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayerItemOutput`
- 1 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"AVPlayerItemMetadataOutputInternal" _metadataOutputInternal;
```

## Properties

```
@property (T@"NSDictionary",R,N,G_figMetadataOutputsDictionaryOptions) figMetadataOutputsDictionaryOptions;
@property (T@"<AVPlayerItemMetadataOutputPushDelegate>",R,W,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
@property (Td,N) advanceIntervalForDelegateInvocation;
```

## Class methods

```
+[AVPlayerItemMetadataOutput initialize];
```

## Instance methods

```
-[AVPlayerItemMetadataOutput setDelegate:queue:];
-[AVPlayerItemMetadataOutput init];
-[AVPlayerItemMetadataOutput dealloc];
-[AVPlayerItemMetadataOutput isDefunct];
-[AVPlayerItemMetadataOutput delegate];
-[AVPlayerItemMetadataOutput delegateQueue];
-[AVPlayerItemMetadataOutput initWithIdentifiers:];
-[AVPlayerItemMetadataOutput _attachToPlayerItem:];
-[AVPlayerItemMetadataOutput _collectUncollectables];
-[AVPlayerItemMetadataOutput _detachFromPlayerItem];
-[AVPlayerItemMetadataOutput _figMetadataOutputsDictionaryOptions];
-[AVPlayerItemMetadataOutput _pushTimedMetadataGroups:fromPlayerItemTrack:];
-[AVPlayerItemMetadataOutput _signalFlush];
-[AVPlayerItemMetadataOutput advanceIntervalForDelegateInvocation];
-[AVPlayerItemMetadataOutput setAdvanceIntervalForDelegateInvocation:];
```
