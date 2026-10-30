# `PKTiledGestureView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 2 instance variables, 2 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"PKTiledView" _tiledView;
@"<PKDrawingPaletteStatistics>" _drawingPaletteStatistics;
```

## Properties

```
@property (T@"<PKDrawingPaletteStatistics>",&,N,V_drawingPaletteStatistics) drawingPaletteStatistics;
@property (T@"PKTiledView",W,N,V_tiledView) tiledView;
```

## Instance methods

```
-[PKTiledGestureView rulerController];
-[PKTiledGestureView init];
-[PKTiledGestureView scrollView];
-[PKTiledGestureView hitTest:withEvent:];
-[PKTiledGestureView selectionController];
-[PKTiledGestureView ink];
-[PKTiledGestureView hoverController];
-[PKTiledGestureView _hitTestAttachmentMiniMenu:];
-[PKTiledGestureView _recordDrawingStatisticsForHitPoint:withEvent:];
-[PKTiledGestureView _setupPencilShadowViewIfNecessary];
-[PKTiledGestureView _shouldForwardSelectionAtPoint:withEvent:];
-[PKTiledGestureView _shouldSelectionBeginAtPoint:withEvent:];
-[PKTiledGestureView drawingPaletteStatistics];
-[PKTiledGestureView hitTestAttachmentChrome_point:isStylus:withEvent:hit:];
-[PKTiledGestureView hitTestClearSelectionIfItExists_point:isHover:withEvent:hit:];
-[PKTiledGestureView hitTestDataDetector_point:isStylus:withEvent:hit:];
-[PKTiledGestureView hitTestDelegateSelection_point:isHover:withEvent:hit:];
-[PKTiledGestureView hitTestDragEvent_point:withEvent:hit:];
-[PKTiledGestureView hitTestHandleScrolling_point:isStylus:isHover:];
-[PKTiledGestureView hitTestHandwritingInk_point:isStylus:isHover:];
-[PKTiledGestureView hitTestInsertNewAttachments_point:isStylus:isHover:withEvent:hit:];
-[PKTiledGestureView hitTestPencilStickiness_point:isStylus:isHover:withEvent:hit:];
-[PKTiledGestureView hitTestSelectionGestures_point:isStylus:isHover:withEvent:hit:];
-[PKTiledGestureView hitTestSelectionView_point:withEvent:hit:];
-[PKTiledGestureView hitTestUpdateEffects_point:isStylus:isHover:];
-[PKTiledGestureView setDrawingPaletteStatistics:];
-[PKTiledGestureView setTiledView:];
-[PKTiledGestureView tiledView];
```
