# `FigVideoLayer`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigThreadSafeCALayer`
- 2 instance variables, 1 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"FigVideoLayerInternal" _videoLayer;
I _contentsSlotID;
```

## Properties

```
@property (TI,N) contentsSlotID;
```

## Class methods

```
+[FigVideoLayer defaultActionForKey:];
```

## Instance methods

```
-[FigVideoLayer actionForKey:];
-[FigVideoLayer layerDisplayName];
-[FigVideoLayer contentsSlotID];
-[FigVideoLayer initWithDeferredTransaction:];
-[FigVideoLayer isVideoLayerBeingServiced];
-[FigVideoLayer dealloc];
-[FigVideoLayer _setupInternalFigVideoLayer];
-[FigVideoLayer initWithLayer:];
-[FigVideoLayer layerDidBecomeVisible:];
-[FigVideoLayer initWithoutDeferredTransaction];
-[FigVideoLayer setContentsSlotID:];
-[FigVideoLayer notificationBarrier];
-[FigVideoLayer _sendVideoLayerIsBeingServicedNotification];
-[FigVideoLayer _setupTraceLevel];
```
