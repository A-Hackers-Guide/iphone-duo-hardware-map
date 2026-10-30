# `PKRulerController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 20 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"UIView" _rulerHostingView;
B _wantsSharedRuler;
B _isInteractingWithRuler;
B _rulerIsRotating;
B _rulerWasShownViaGesture;
B _canRulerSnapToAngle;
B _lastTouchWasMaskedByRuler;
B _lastDrawingWasMaskedByRuler;
B _lastDrawingWasSnappedToRuler;
B _rulerSnappedToAngle;
@"PKRulerGestureRecognizer" _rulerGestureRecognizer;
@"<PKRulerDelegate>" _delegate;
@"<PKRulerHostingDelegate>" _rulerHostingDelegate;
@"PKRulerView" _rulerView;
@"PKRulerLayer" _rulerLayer;
@"UIImpactFeedbackGenerator" _snapImpactBehavior;
{?="arcType"i"before"B"snapAngle"d} _rulerState;
{?="arcType"i"before"B"snapAngle"d} _previousRulerState;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _rulerStartTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _defaultRulerTransform;
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
-[PKRulerController gestureRecognizer:shouldReceiveTouch:];
-[PKRulerController dealloc];
-[PKRulerController eatPencilGesture:];
-[PKRulerController rulerMoveGesture:];
```
