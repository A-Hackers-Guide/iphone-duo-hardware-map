# `AVPlayerItemMetadataCollector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayerItemMediaDataCollector`
- 1 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"AVPlayerItemMetadataCollectorInternal" _metadataCollectorInternal;
```

## Properties

```
@property (T@"<AVPlayerItemMetadataCollectorPushDelegate>",R,W,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
```

## Instance methods

```
-[AVPlayerItemMetadataCollector setDelegate:queue:];
-[AVPlayerItemMetadataCollector init];
-[AVPlayerItemMetadataCollector dealloc];
-[AVPlayerItemMetadataCollector delegate];
-[AVPlayerItemMetadataCollector delegateQueue];
-[AVPlayerItemMetadataCollector _attachToPlayerItem:];
-[AVPlayerItemMetadataCollector _detatchFromPlayerItem];
-[AVPlayerItemMetadataCollector _getFilteredMetadataGroups:fromIdentifiers:andClassifyingLabels:modifiedIndexesOut:newIndexesOut:];
-[AVPlayerItemMetadataCollector _isAttachedToPlayerItem];
-[AVPlayerItemMetadataCollector _updateTaggedRangeMetadataArray:];
-[AVPlayerItemMetadataCollector initWithIdentifiers:classifyingLabels:];
```
