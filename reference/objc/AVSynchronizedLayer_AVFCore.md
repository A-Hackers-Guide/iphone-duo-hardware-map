# `AVSynchronizedLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 1 instance variables, 1 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"AVSynchronizedLayerInternal" _syncLayer;
```

## Properties

```
@property (T@"AVPlayerItem",&,N) playerItem;
```

## Class methods

```
+[AVSynchronizedLayer initialize];
+[AVSynchronizedLayer synchronizedLayerWithPlayerItem:];
```

## Instance methods

```
-[AVSynchronizedLayer _isVisible];
-[AVSynchronizedLayer init];
-[AVSynchronizedLayer playerItem];
-[AVSynchronizedLayer dealloc];
-[AVSynchronizedLayer layerDidBecomeVisible:];
-[AVSynchronizedLayer _popAllOldPlayerItems];
-[AVSynchronizedLayer _removeSelfFromPlayerItem:];
-[AVSynchronizedLayer _updatePlayerItemState];
-[AVSynchronizedLayer setPlayerItem:];
```
