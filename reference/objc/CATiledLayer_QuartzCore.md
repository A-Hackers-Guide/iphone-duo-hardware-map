# `CATiledLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 0 instance variables, 7 properties, 27 instance methods, 5 class methods

## Properties

```
@property (T^{CGColor=}) fillColor;
@property (Td) maximumTileScale;
@property (TB,GisDrawingEnabled) drawingEnabled;
@property (T@"<CATiledLayerDelegate><CALayerDelegate>",W) delegate;
@property (TQ) levelsOfDetail;
@property (TQ) levelsOfDetailBias;
@property (T{CGSize=dd}) tileSize;
```

## Class methods

```
+[CATiledLayer defaultValueForKey:];
+[CATiledLayer CA_automaticallyNotifiesObservers:];
+[CATiledLayer prefetchedTiles];
+[CATiledLayer fadeDuration];
+[CATiledLayer shouldDrawOnMainThread];
```

## Instance methods

```
-[CATiledLayer tileSize];
-[CATiledLayer didChangeValueForKey:];
-[CATiledLayer levelsOfDetail];
-[CATiledLayer setContents:];
-[CATiledLayer setFillColor:];
-[CATiledLayer fillColor];
-[CATiledLayer dealloc];
-[CATiledLayer shouldArchiveValueForKey:];
-[CATiledLayer invalidateContents];
-[CATiledLayer setNeedsDisplayInRect:];
-[CATiledLayer setUnsafeUnretainedDelegate:];
-[CATiledLayer _dealloc];
-[CATiledLayer setLevelsOfDetail:];
-[CATiledLayer _canDisplayConcurrently];
-[CATiledLayer _colorSpaceDidChange];
-[CATiledLayer _display];
-[CATiledLayer canDrawRect:levelOfDetail:];
-[CATiledLayer displayInRect:levelOfDetail:options:];
-[CATiledLayer isDrawingEnabled];
-[CATiledLayer levelsOfDetailBias];
-[CATiledLayer maximumTileScale];
-[CATiledLayer setDrawingEnabled:];
-[CATiledLayer setLevelsOfDetailBias:];
-[CATiledLayer setMaximumTileScale:];
-[CATiledLayer setNeedsDisplayInRect:levelOfDetail:];
-[CATiledLayer setNeedsDisplayInRect:levelOfDetail:options:];
-[CATiledLayer setTileSize:];
```
