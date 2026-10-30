# `PKDrawingGestureRecognizer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `PKDrawingGestureRecognizerProtocol`
- 11 instance variables, 12 properties, 29 instance methods, 1 class methods

## Instance variables

```
d _thresholdDistance;
d _squaredThreshold;
{CGPoint="x"d"y"d} _drawTouchStartPoint;
B _drawingTargetIsDrawing;
B _gestureDetected;
B _ignoreFingerTouchesUntilReset;
@"<PKDrawingGestureTarget>" drawingTarget;
Q _activeInputProperties;
d _startTimeInterval;
@"UITouch" _drawingTouch;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentBoundingBoxInWindow;
```

## Properties

```
@property (T@"UITouch",&,N,V_drawingTouch) drawingTouch;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_currentBoundingBoxInWindow) currentBoundingBoxInWindow;
@property (Td,R,N,V_startTimeInterval) startTimeInterval;
@property (Td,N,V_thresholdDistance) thresholdDistance;
@property (TB,R,N) isReplaying;
@property (T@"<PKDrawingGestureRecognizerDelegate>",W,D,N) delegate;
@property (T@"<PKDrawingGestureTarget>",W,N,VdrawingTarget) drawingTarget;
@property (TQ,R,N,V_activeInputProperties) activeInputProperties;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKDrawingGestureRecognizer activeInputPropertiesForTouch:event:];
```

## Instance methods

```
-[PKDrawingGestureRecognizer touchesEnded:withEvent:];
-[PKDrawingGestureRecognizer touchesCancelled:withEvent:];
-[PKDrawingGestureRecognizer thresholdDistance];
-[PKDrawingGestureRecognizer setDrawingTarget:];
-[PKDrawingGestureRecognizer currentBoundingBoxInWindow];
-[PKDrawingGestureRecognizer isReplaying];
-[PKDrawingGestureRecognizer _cancelDrawing];
-[PKDrawingGestureRecognizer reset];
-[PKDrawingGestureRecognizer end];
-[PKDrawingGestureRecognizer setThresholdDistance:];
-[PKDrawingGestureRecognizer touchesBegan:withEvent:];
-[PKDrawingGestureRecognizer touchesMoved:withEvent:];
-[PKDrawingGestureRecognizer initWithTarget:action:];
-[PKDrawingGestureRecognizer setDrawingTouch:];
-[PKDrawingGestureRecognizer _drawingCancelled];
-[PKDrawingGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:];
-[PKDrawingGestureRecognizer drawingTarget];
-[PKDrawingGestureRecognizer _drawingEnded];
-[PKDrawingGestureRecognizer activeInputProperties];
-[PKDrawingGestureRecognizer _shouldBeginDrawing:withEvent:];
-[PKDrawingGestureRecognizer startTimeInterval];
-[PKDrawingGestureRecognizer cancel];
-[PKDrawingGestureRecognizer _endDrawing];
-[PKDrawingGestureRecognizer _beginDrawingWithTouch:];
-[PKDrawingGestureRecognizer drawingTouch];
-[PKDrawingGestureRecognizer _drawingBegan];
-[PKDrawingGestureRecognizer _drawingMoved:];
-[PKDrawingGestureRecognizer _updateDrawingWithEvent:];
-[PKDrawingGestureRecognizer touchesEstimatedPropertiesUpdated:];
```
