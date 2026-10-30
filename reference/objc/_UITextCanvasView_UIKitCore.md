# `_UITextCanvasView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UITextTiledLayerDelegate`, `_UIGeometryChangeObserver`, `_UITextKit1Canvas`
- 5 instance variables, 12 properties, 43 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _ghostedRanges;
@"NSMutableSet" _invisibleRanges;
@"NSArray" _maskedRects;
B _layoutFragmentViewsNeedDisplay;
@"<_UITextKit1CanvasContext>" _context;
```

## Properties

```
@property (T@"_UITextTiledLayer",R,D,N) layer;
@property (TB,N,GisTilingEnabled) tilingEnabled;
@property (Td,N) maxTileHeight;
@property (TB,N,S_setDrawsDebugBaselines:) _drawsDebugBaselines;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_UITextKit1CanvasContext>",W,N,V_context) context;
@property (TB,V_layoutFragmentViewsNeedDisplay) layoutFragmentViewsNeedDisplay;
@property (T{CGPoint=dd},?,R) viewportAnchor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R) viewport;
```

## Class methods

```
+[_UITextCanvasView layerClass];
```

## Instance methods

```
-[_UITextCanvasView setNeedsLayout];
-[_UITextCanvasView layoutFragmentViewsNeedDisplay];
-[_UITextCanvasView setMaxTileHeight:];
-[_UITextCanvasView viewportBoundsDidChange];
-[_UITextCanvasView isEditingDidChange];
-[_UITextCanvasView textViewportLayoutControllerDidLayout:];
-[_UITextCanvasView flushElementViews];
-[_UITextCanvasView dealloc];
-[_UITextCanvasView drawRect:];
-[_UITextCanvasView viewportBoundsForTextViewportLayoutController:];
-[_UITextCanvasView textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:];
-[_UITextCanvasView layoutSubviews];
-[_UITextCanvasView textViewportLayoutController:retrieveCachedRenderingSurfaceForKey:];
-[_UITextCanvasView textViewportLayoutControllerReceivedSetNeedsLayout:];
-[_UITextCanvasView setBounds:];
-[_UITextCanvasView addInvisibleRange:];
-[_UITextCanvasView _geometryChanged:forAncestor:];
-[_UITextCanvasView updateContentSizeIfNeeded];
-[_UITextCanvasView resumeTiling];
-[_UITextCanvasView setContext:];
-[_UITextCanvasView addGhostedRange:];
-[_UITextCanvasView removeAllGhostedRanges];
-[_UITextCanvasView setFrame:];
-[_UITextCanvasView removeInvisibleRange:];
-[_UITextCanvasView suspendTiling];
-[_UITextCanvasView textViewportLayoutController:renderingSurfaceForTextLayoutFragment:];
-[_UITextCanvasView textViewportLayoutController:cacheRenderingSurface:forKey:];
-[_UITextCanvasView _registerTextAttachmentViewProviderReusePolicy:forTextAttachmentViewProviderType:];
-[_UITextCanvasView drawTextInRect:];
-[_UITextCanvasView isScrollingChangedTo:];
-[_UITextCanvasView context];
-[_UITextCanvasView initWithFrame:];
-[_UITextCanvasView setLayoutFragmentViewsNeedDisplay:];
-[_UITextCanvasView textViewportLayoutControllerWillLayout:];
-[_UITextCanvasView maxTileHeight];
-[_UITextCanvasView configureCustomTextRenderer];
-[_UITextCanvasView isTilingEnabled];
-[_UITextCanvasView _drawsDebugBaselines];
-[_UITextCanvasView _enableAutoConstraining];
-[_UITextCanvasView _setDrawsDebugBaselines:];
-[_UITextCanvasView _textTiledLayer:maskedRectsInVisibleRect:];
-[_UITextCanvasView _updateTilingViewportLayer];
-[_UITextCanvasView setTilingEnabled:];
```
