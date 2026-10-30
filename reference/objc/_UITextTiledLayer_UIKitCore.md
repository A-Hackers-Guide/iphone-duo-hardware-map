# `_UITextTiledLayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `CALayerDelegate`
- 9 instance variables, 9 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _visibleTiles;
{CGSize="width"d"height"d} _tileSize;
@"CALayer" _viewportLayer;
d _viewportLayerExtraWidthFactor;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleViewportBounds;
@"UIBezierPath" _clip;
{?="disableTiling"b1"ditchAllTiles"b1"suspendLayout"b4"delegateSupportsMaskedRects"b1"delegateImplementsWillDraw"b1} _tcTiledLayerFlags;
d _maxTileHeight;
d _maxPrefetchedTiles;
```

## Properties

```
@property (T@"<_UITextTiledLayerDelegate>",W,D) delegate;
@property (TB,N) usesTiledLayers;
@property (Td,N,V_maxTileHeight) maxTileHeight;
@property (Td,N,V_maxPrefetchedTiles) maxPrefetchedTiles;
@property (T@"NSArray",R,C,N) tiles;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextTiledLayer drawInContext:];
-[_UITextTiledLayer setMaxTileHeight:];
-[_UITextTiledLayer _prepareNonTiledGhostLayersForVisibleBounds:inBounds:];
-[_UITextTiledLayer init];
-[_UITextTiledLayer setContentsMultiplyColor:];
-[_UITextTiledLayer tiles];
-[_UITextTiledLayer _drawInContext:offset:clip:];
-[_UITextTiledLayer setRasterizationScale:];
-[_UITextTiledLayer setUsesTiledLayers:];
-[_UITextTiledLayer maxPrefetchedTiles];
-[_UITextTiledLayer setDelegate:];
-[_UITextTiledLayer resumeTiling];
-[_UITextTiledLayer setContentsScale:];
-[_UITextTiledLayer layoutSublayers];
-[_UITextTiledLayer suspendTiling];
-[_UITextTiledLayer setNeedsDisplayInRect:];
-[_UITextTiledLayer setContentsFormat:];
-[_UITextTiledLayer _prepareTilesForVisibleBounds:inBounds:];
-[_UITextTiledLayer _updateTilingViewportWindow:];
-[_UITextTiledLayer setUnsafeUnretainedDelegate:];
-[_UITextTiledLayer setMaxPrefetchedTiles:];
-[_UITextTiledLayer layerWillDraw:];
-[_UITextTiledLayer _didSetDelegate];
-[_UITextTiledLayer usesTiledLayers];
-[_UITextTiledLayer setDrawsAsynchronously:];
-[_UITextTiledLayer maxTileHeight];
-[_UITextTiledLayer _preparedTileForFrame:mask:opacity:deferred:];
```
