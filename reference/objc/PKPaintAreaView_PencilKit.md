# `PKPaintAreaView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKDrawingGestureRecognizerDelegate`, `PKDrawingGestureTarget`, `PKShapeDrawingControllerDelegate`
- 12 instance variables, 13 properties, 46 instance methods, 0 class methods

## Instance variables

```
@"PKDrawingGestureRecognizer" _drawingGestureRecognizer;
@"PKPaintAreaViewSurface" _currentPaintSurfaceObject;
@"NSMutableArray" _liveSurfaces;
@"<MTLDevice>" _device;
B _switchSurfacesDuringStrokes;
B _fingerDrawingEnabled;
B _drawingDisabled;
@"<PKPaintAreaViewDelegate>" _delegate;
@"PKTool" _tool;
@"PKShapeDrawingController" _shapeDrawingController;
@"PKAlternativeStrokesAnimation" _alternativeStrokesAnimation;
d _liveAnimationStartTime;
```

## Properties

```
@property (T@"PKShapeDrawingController",&,N,V_shapeDrawingController) shapeDrawingController;
@property (T@"PKAlternativeStrokesAnimation",&,N,V_alternativeStrokesAnimation) alternativeStrokesAnimation;
@property (T{CGAffineTransform=dddddd},R,N) strokeTransform;
@property (Td,N,V_liveAnimationStartTime) liveAnimationStartTime;
@property (T@"<PKPaintAreaViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_switchSurfacesDuringStrokes) switchSurfacesDuringStrokes;
@property (TB,N,V_fingerDrawingEnabled) fingerDrawingEnabled;
@property (TB,N,V_drawingDisabled) drawingDisabled;
@property (T@"PKTool",&,N,V_tool) tool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaintAreaView _commonInit];
-[PKPaintAreaView drawingEstimatedPropertiesUpdated:];
-[PKPaintAreaView _isLiveAnimating];
-[PKPaintAreaView drawingMoved:withEvent:];
-[PKPaintAreaView hitTest:withEvent:];
-[PKPaintAreaView liveAnimationStartTime];
-[PKPaintAreaView applyTransformToTouchLocation:];
-[PKPaintAreaView shapeDrawingControllerShapeGestureDetected:isFastGesture:];
-[PKPaintAreaView setDelegate:];
-[PKPaintAreaView drawingGestureRecognizer:shouldBeginDrawingWithTouches:event:];
-[PKPaintAreaView strokeTransform];
-[PKPaintAreaView setShapeDrawingController:];
-[PKPaintAreaView drawingCancelled];
-[PKPaintAreaView _rendererController];
-[PKPaintAreaView shapeDrawingControllerRendererController:];
-[PKPaintAreaView delegate];
-[PKPaintAreaView _endAlternativeStrokeIfNecessaryAccepted:];
-[PKPaintAreaView initWithCoder:];
-[PKPaintAreaView drawingBegan:];
-[PKPaintAreaView setAlternativeStrokesAnimation:];
-[PKPaintAreaView checkAnimationsDidEndAtTime:];
-[PKPaintAreaView _drawingController];
-[PKPaintAreaView drawingEnded:];
-[PKPaintAreaView tool];
-[PKPaintAreaView shapeDrawingController];
-[PKPaintAreaView canBecomeFirstResponder];
-[PKPaintAreaView initWithFrame:];
-[PKPaintAreaView setLiveAnimationStartTime:];
-[PKPaintAreaView alternativeStrokesAnimation];
-[PKPaintAreaView shapeDrawingControllerShapeDetectionCancelled:];
-[PKPaintAreaView setTool:];
-[PKPaintAreaView setSwitchSurfacesDuringStrokes:];
-[PKPaintAreaView drawingDisabled];
-[PKPaintAreaView _drawingBegan:locationInView:inputType:];
-[PKPaintAreaView applyTransformToTouchLocation:previousPoint:newSurface:];
-[PKPaintAreaView beginDrawingAtPoint:surface:locationInView:inputType:];
-[PKPaintAreaView canAddStroke];
-[PKPaintAreaView drawingEnded];
-[PKPaintAreaView drawingMovedToPoint:locationInView:];
-[PKPaintAreaView fingerDrawingEnabled];
-[PKPaintAreaView hitSurface:];
-[PKPaintAreaView setDrawingDisabled:];
-[PKPaintAreaView setFingerDrawingEnabled:];
-[PKPaintAreaView switchSurfacesDuringStrokes];
-[PKPaintAreaView switchToNewPaintSurface:];
-[PKPaintAreaView vsync:];
```
