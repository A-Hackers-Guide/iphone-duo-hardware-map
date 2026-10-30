# `UITransformEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- 13 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _gestureRecognizersByWindow;
{CGPoint="x"d"y"d} _sceneReferenceLocation;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
d _scaleDelta;
d _rotationDelta;
d _translationMagDelta;
Q _scalePhase;
Q _rotationPhase;
Q _translationPhase;
@"BKSHIDEventPointerAttributes" _pointerAttributes;
d _scale;
d _rotation;
{CGPoint="x"d"y"d} _translation;
```

## Properties

```
@property (TQ,R) phase;
@property (Td,R,N,V_scale) scale;
@property (Td,R,N,V_rotation) rotation;
@property (T{CGPoint=dd},R,N,V_translation) translation;
@property (T{CGAffineTransform=dddddd},R,N) transform;
```

## Instance methods

```
-[UITransformEvent _allWindows];
-[UITransformEvent _setHIDEvent:];
-[UITransformEvent _removeGestureRecognizer:fromComponents:];
-[UITransformEvent _gestureRecognizersForWindow:];
-[UITransformEvent subtype];
-[UITransformEvent _reset];
-[UITransformEvent rotation];
-[UITransformEvent _sendEventToGestureRecognizer:];
-[UITransformEvent phase];
-[UITransformEvent transform];
-[UITransformEvent locationInView:];
-[UITransformEvent _init];
-[UITransformEvent scale];
-[UITransformEvent type];
-[UITransformEvent _removeGestureRecognizersFromWindows];
-[UITransformEvent _windowServerHitTestWindow];
-[UITransformEvent _initWithEvent:touches:];
-[UITransformEvent translation];
-[UITransformEvent weightedDominantComponentForScaleWeight:rotationWeight:translationWeight:];
```
