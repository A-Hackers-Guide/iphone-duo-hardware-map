# `UITextRangeAdjustmentInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInteraction`
- Protocols: `UIGestureRecognizerDelegate`, `_UITextLoupeSessionDelegate`
- 17 instance variables, 18 properties, 54 instance methods, 0 class methods

## Instance variables

```
@"UIView" _gestureHostView;
@"UITextGestureTuning" _gestureTuning;
@"UITextLoupeSession" _loupeSession;
B _baseIsStart;
B _clientFlipsBaseIsStart;
@"<UITextRangeAdjustmentInteractionDelegate>" _adjustmentDelegate;
@"UITextRangeAdjustmentGestureRecognizer" _adjustmentGestureRecognizer;
d _initialDistance;
d _firstMovedTime;
@"UITouch" _activeTouch;
{CGPoint="x"d"y"d} _initialExtentPoint;
{CGPoint="x"d"y"d} _extentPoint;
{CGPoint="x"d"y"d} _initialPoint;
{CGPoint="x"d"y"d} _basePoint;
{CGPoint="x"d"y"d} _initialBasePoint;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialStartCaretRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialEndCaretRect;
```

## Properties

```
@property (T{CGPoint=dd},N,V_initialPoint) initialPoint;
@property (T{CGPoint=dd},N,V_basePoint) basePoint;
@property (T{CGPoint=dd},N,V_extentPoint) extentPoint;
@property (T{CGPoint=dd},N,V_initialBasePoint) initialBasePoint;
@property (Td,N,V_initialDistance) initialDistance;
@property (Td,N,V_firstMovedTime) firstMovedTime;
@property (T@"UITouch",&,N,V_activeTouch) activeTouch;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_initialStartCaretRect) initialStartCaretRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_initialEndCaretRect) initialEndCaretRect;
@property (TB,N,V_baseIsStart) baseIsStart;
@property (TB,N,V_clientFlipsBaseIsStart) clientFlipsBaseIsStart;
@property (T{CGPoint=dd},R,N,V_initialExtentPoint) initialExtentPoint;
@property (T@"<UITextRangeAdjustmentInteractionDelegate>",W,N,V_adjustmentDelegate) adjustmentDelegate;
@property (T@"UITextRangeAdjustmentGestureRecognizer",R,N,V_adjustmentGestureRecognizer) adjustmentGestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextRangeAdjustmentInteraction initialPoint];
-[UITextRangeAdjustmentInteraction _gestureView];
-[UITextRangeAdjustmentInteraction setClientFlipsBaseIsStart:];
-[UITextRangeAdjustmentInteraction setInitialStartCaretRect:];
-[UITextRangeAdjustmentInteraction gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[UITextRangeAdjustmentInteraction gestureRecognizer:shouldReceiveTouch:];
-[UITextRangeAdjustmentInteraction activeTouch];
-[UITextRangeAdjustmentInteraction extentPoint];
-[UITextRangeAdjustmentInteraction setExtentPoint:];
-[UITextRangeAdjustmentInteraction _updateAdjustmentInteractionWithState:location:locationOfFirstTouch:forTouchType:];
-[UITextRangeAdjustmentInteraction initialDistance];
-[UITextRangeAdjustmentInteraction setModelPosition:];
-[UITextRangeAdjustmentInteraction _adjustmentInteractionCancelled];
-[UITextRangeAdjustmentInteraction basePoint];
-[UITextRangeAdjustmentInteraction _gestureTuningEnabledForTouches:];
-[UITextRangeAdjustmentInteraction setInitialEndCaretRect:];
-[UITextRangeAdjustmentInteraction _adjustmentInteractionBeganWithLocation:startPoint:forTouchType:];
-[UITextRangeAdjustmentInteraction setAdjustmentDelegate:];
-[UITextRangeAdjustmentInteraction doesControlDelegate];
-[UITextRangeAdjustmentInteraction _createGestureTuningIfNecessary];
-[UITextRangeAdjustmentInteraction adjustmentGestureRecognizer];
-[UITextRangeAdjustmentInteraction _shouldDisplayLoupeForTouchType:];
-[UITextRangeAdjustmentInteraction setFirstMovedTime:];
-[UITextRangeAdjustmentInteraction setInitialPoint:];
-[UITextRangeAdjustmentInteraction _adjustmentInteractionEndedAtLocation:forTouchType:];
-[UITextRangeAdjustmentInteraction initialStartCaretRect];
-[UITextRangeAdjustmentInteraction gestureRecognizerShouldBegin:];
-[UITextRangeAdjustmentInteraction baseIsStart];
-[UITextRangeAdjustmentInteraction setActiveTouch:];
-[UITextRangeAdjustmentInteraction setInitialBasePoint:];
-[UITextRangeAdjustmentInteraction _didRecognizeAdjustmentGesture:];
-[UITextRangeAdjustmentInteraction initialExtentPoint];
-[UITextRangeAdjustmentInteraction _activeTouchEnded];
-[UITextRangeAdjustmentInteraction _loupeSessionDidInvalidate:];
-[UITextRangeAdjustmentInteraction setInitialDistance:];
-[UITextRangeAdjustmentInteraction gestureRecognizerHostView];
-[UITextRangeAdjustmentInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[UITextRangeAdjustmentInteraction clientFlipsBaseIsStart];
-[UITextRangeAdjustmentInteraction _pointCloserToEnd:];
-[UITextRangeAdjustmentInteraction initialBasePoint];
-[UITextRangeAdjustmentInteraction updateBaseAndExtentPointsFromEdges];
-[UITextRangeAdjustmentInteraction _activeAdjustmentEdgeRect];
-[UITextRangeAdjustmentInteraction hasActiveTouch];
-[UITextRangeAdjustmentInteraction _adjustmentInteractionChangedWithLocation:forTouchType:];
-[UITextRangeAdjustmentInteraction initWithAdjustmentDelegate:gestureHostView:];
-[UITextRangeAdjustmentInteraction manuallyUpdateInteractionWithGestureState:location:locationOfFirstTouch:forTouchType:];
-[UITextRangeAdjustmentInteraction firstMovedTime];
-[UITextRangeAdjustmentInteraction adjustmentDelegate];
-[UITextRangeAdjustmentInteraction _convertPointToViewCoordinateSpace:];
-[UITextRangeAdjustmentInteraction _shouldApplyOffsetForTouchType:];
-[UITextRangeAdjustmentInteraction initialEndCaretRect];
-[UITextRangeAdjustmentInteraction setBasePoint:];
-[UITextRangeAdjustmentInteraction setBaseIsStart:];
-[UITextRangeAdjustmentInteraction selectionWidgetForPoint:];
```
