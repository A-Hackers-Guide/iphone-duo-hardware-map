# `AVPlayerConnection`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" _playerReference;
@"AVWeakReference" _playerItemReference;
q _status;
@"NSError" _error;
```

## Properties

```
@property (Tq,R,N) status;
```

## Instance methods

```
-[AVPlayerConnection player];
-[AVPlayerConnection playerItem];
-[AVPlayerConnection dealloc];
-[AVPlayerConnection removeItemFromPlayQueueWithoutFigRemoval];
-[AVPlayerConnection addItemToPlayQueueAfterPlaybackItemOfItem:];
-[AVPlayerConnection status];
-[AVPlayerConnection initWithWeakReferenceToPlayer:weakReferenceToPlayerItem:];
-[AVPlayerConnection error];
-[AVPlayerConnection _removeItemFromPlayQueueWithFigRemovalHandler:];
-[AVPlayerConnection removeItemFromPlayQueue];
-[AVPlayerConnection description];
```
