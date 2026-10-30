# `UIWebTiledView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 0 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"WAKWindow" _wakWindow;
i _inGestureType;
i _tilingArea;
B _didFirstTileLayout;
B _layoutTilesInMainThread;
B _tilingModeIsLocked;
B _allowsPaintingAndScriptsWhilePanning;
B _editingTilingModeEnabled;
```

## Instance methods

```
-[UIWebTiledView setNeedsLayout];
-[UIWebTiledView tileSize];
-[UIWebTiledView setNeedsDisplay];
-[UIWebTiledView visibleRect];
-[UIWebTiledView dealloc];
-[UIWebTiledView layoutSubviews];
-[UIWebTiledView setTransform:];
-[UIWebTiledView _screenChanged:];
-[UIWebTiledView willMoveToWindow:];
-[UIWebTiledView setNeedsDisplayInRect:];
-[UIWebTiledView initWithFrame:];
-[UIWebTiledView setTileSize:];
-[UIWebTiledView isTilingEnabled];
-[UIWebTiledView setTilesOpaque:];
-[UIWebTiledView _didScroll];
-[UIWebTiledView _updateForScreen:];
-[UIWebTiledView adjustedMaxTileCount];
-[UIWebTiledView allowsPaintingAndScriptsWhilePanning];
-[UIWebTiledView drawImageIntoTiles:];
-[UIWebTiledView drawsGrid];
-[UIWebTiledView dumpTiles];
-[UIWebTiledView editingTilingModeEnabled];
-[UIWebTiledView keepsZoomedOutTiles];
-[UIWebTiledView layoutTilesInMainThread];
-[UIWebTiledView layoutTilesNow];
-[UIWebTiledView layoutTilesNowForRect:];
-[UIWebTiledView layoutTilesNowOnWebThread];
-[UIWebTiledView lockTilingMode];
-[UIWebTiledView logsTilingChanges];
-[UIWebTiledView maxTileCount];
-[UIWebTiledView removeAllNonVisibleTiles];
-[UIWebTiledView removeAllTiles];
-[UIWebTiledView removeForegroundTiles];
-[UIWebTiledView setAllowsPaintingAndScriptsWhilePanning:];
-[UIWebTiledView setDrawsGrid:];
-[UIWebTiledView setEditingTilingModeEnabled:];
-[UIWebTiledView setInGesture:];
-[UIWebTiledView setKeepsZoomedOutTiles:];
-[UIWebTiledView setLayoutTilesInMainThread:];
-[UIWebTiledView setLogsTilingChanges:];
-[UIWebTiledView setMaxTileCount:];
-[UIWebTiledView setTileDrawingEnabled:];
-[UIWebTiledView setTilingArea:];
-[UIWebTiledView setTilingEnabled:];
-[UIWebTiledView setWAKWindow:];
-[UIWebTiledView tileDrawingEnabled];
-[UIWebTiledView tilesOpaque];
-[UIWebTiledView tilingArea];
-[UIWebTiledView unlockTilingMode];
-[UIWebTiledView updateTilingMode];
-[UIWebTiledView wakWindow];
```
