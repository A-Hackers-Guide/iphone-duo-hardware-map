# `PKDrawingReplayController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 17 properties, 51 instance methods, 1 class methods

## Instance variables

```
B _isAnimating;
B _setupComplete;
B _cancelled;
d _speedRatio;
@"PKTiledCanvasView" _canvasView;
@"PKDrawing" _drawing;
@"UITextField" _textField;
@? _completionHandler;
@"PKTextInputInteraction" _textInputInteraction;
@"PKTextInputDrawingGestureRecognizer" _drawingGestureRecognizer;
Q _currentPointIndex;
@"NSMutableArray" _pointArray;
{CGPoint="x"d"y"d} _startingTextFieldOrigin;
{CGPoint="x"d"y"d} _originOffset;
{CGPoint="x"d"y"d} _currentOffset;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
```

## Properties

```
@property (TB,N,V_setupComplete) setupComplete;
@property (T@"PKTiledCanvasView",&,N,V_canvasView) canvasView;
@property (T@"PKDrawing",&,N,V_drawing) drawing;
@property (T@"UITextField",W,N,V_textField) textField;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"PKTextInputInteraction",W,N,V_textInputInteraction) textInputInteraction;
@property (T@"PKTextInputDrawingGestureRecognizer",W,N,V_drawingGestureRecognizer) drawingGestureRecognizer;
@property (TQ,N,V_currentPointIndex) currentPointIndex;
@property (T{CGPoint=dd},N,V_startingTextFieldOrigin) startingTextFieldOrigin;
@property (T{CGPoint=dd},N,V_originOffset) originOffset;
@property (T{CGPoint=dd},N,V_currentOffset) currentOffset;
@property (T{CGAffineTransform=dddddd},N,V_transform) transform;
@property (T@"NSMutableArray",&,N,V_pointArray) pointArray;
@property (TB,N,V_cancelled) cancelled;
@property (TB,N,V_isAnimating) isAnimating;
@property (Td,N,V_speedRatio) speedRatio;
@property (TB,N) disablePencilInput;
```

## Class methods

```
+[PKDrawingReplayController isDrawingInProgressForWindow:];
```

## Instance methods

```
-[PKDrawingReplayController drawing];
-[PKDrawingReplayController cancelled];
-[PKDrawingReplayController setCompletionHandler:];
-[PKDrawingReplayController setSetupComplete:];
-[PKDrawingReplayController completionHandler];
-[PKDrawingReplayController setCancelled:];
-[PKDrawingReplayController dealloc];
-[PKDrawingReplayController textField];
-[PKDrawingReplayController setTransform:];
-[PKDrawingReplayController setIsAnimating:];
-[PKDrawingReplayController currentOffset];
-[PKDrawingReplayController transform];
-[PKDrawingReplayController setDrawing:];
-[PKDrawingReplayController setDrawingGestureRecognizer:];
-[PKDrawingReplayController setCanvasView:];
-[PKDrawingReplayController setupComplete];
-[PKDrawingReplayController canvasView];
-[PKDrawingReplayController cancel];
-[PKDrawingReplayController _endDrawing];
-[PKDrawingReplayController isAnimating];
-[PKDrawingReplayController drawingGestureRecognizer];
-[PKDrawingReplayController setCurrentOffset:];
-[PKDrawingReplayController setTextField:];
-[PKDrawingReplayController _loadPointArray];
-[PKDrawingReplayController _beginDrawing];
-[PKDrawingReplayController _beginStrokeWithPoint:];
-[PKDrawingReplayController _processNextPoint];
-[PKDrawingReplayController _setUpIfNecessary];
-[PKDrawingReplayController _strokeEndedWithReplayPoint:];
-[PKDrawingReplayController _strokeMovedWithReplayPoint:];
-[PKDrawingReplayController beginDrawingAnimationAtPoint:completion:];
-[PKDrawingReplayController beginDrawingAnimationAtRange:offset:completion:];
-[PKDrawingReplayController beginInsertTextAnimationAtIndex:offset:completion:];
-[PKDrawingReplayController currentPointIndex];
-[PKDrawingReplayController disablePencilInput];
-[PKDrawingReplayController initWithDrawing:transform:sourceTextField:];
-[PKDrawingReplayController initWithSourceTextField:];
-[PKDrawingReplayController originOffset];
-[PKDrawingReplayController pencilTextInputInteractionFromWindowScene:];
-[PKDrawingReplayController pointArray];
-[PKDrawingReplayController setCurrentPointIndex:];
-[PKDrawingReplayController setDisablePencilInput:];
-[PKDrawingReplayController setOriginOffset:];
-[PKDrawingReplayController setPointArray:];
-[PKDrawingReplayController setSpeedRatio:];
-[PKDrawingReplayController setStartingTextFieldOrigin:];
-[PKDrawingReplayController setTextInputInteraction:];
-[PKDrawingReplayController shouldEndDrawing];
-[PKDrawingReplayController speedRatio];
-[PKDrawingReplayController startingTextFieldOrigin];
-[PKDrawingReplayController textInputInteraction];
```
