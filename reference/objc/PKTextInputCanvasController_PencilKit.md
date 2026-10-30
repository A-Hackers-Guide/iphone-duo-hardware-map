# `PKTextInputCanvasController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTiledCanvasViewDelegate`, `PKTextInputDebugStateReporting`
- 13 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _recentlyRemovedStrokeIDs;
B _useSlidingCanvas;
{vector<CGPoint, std::allocator<CGPoint>>="__begin_"^{CGPoint}"__end_"^{CGPoint}""{?="__cap_"^{CGPoint}}} _currentStrokePoints;
@"NSMutableDictionary" _strokeColorForStrokeUUID;
@"PKStroke" _currentStroke;
B _wantsCanvasVisible;
B _wantsCanvasViewLoaded;
@"<PKTextInputCanvasControllerDelegate>" _delegate;
@"<PKTextInputCanvasControllerChangeObserver>" _changeObserver;
@"UIColor" _strokeColor;
@"PKTiledCanvasView" __canvasView;
@"PKTextInputFloatingBackgroundView" __floatingBackgroundView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _floatingBackgroundRect;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputCanvasController init];
-[PKTextInputCanvasController dealloc];
-[PKTextInputCanvasController canvasView:beganStroke:];
-[PKTextInputCanvasController canvasView:cancelledStroke:];
-[PKTextInputCanvasController canvasView:didPresentWithCanvasOffset:];
-[PKTextInputCanvasController canvasView:drawingDidChange:];
-[PKTextInputCanvasController canvasView:endedStroke:];
-[PKTextInputCanvasController canvasView:inkForStroke:];
-[PKTextInputCanvasController canvasViewAllowSnapToShape:];
-[PKTextInputCanvasController canvasViewDidBeginDrawing:];
-[PKTextInputCanvasController canvasViewDidEndDrawing:];
-[PKTextInputCanvasController canvasViewDidFinishAnimatingStrokes:];
-[PKTextInputCanvasController canvasViewDrawingMoved:withTouch:];
-[PKTextInputCanvasController canvasViewHasVisibleStrokesChanged:];
-[PKTextInputCanvasController canvasViewTouchView:];
-[PKTextInputCanvasController canvasViewWillBeginNewStroke:withTouch:location:];
-[PKTextInputCanvasController reportDebugStateDescription:];
```
