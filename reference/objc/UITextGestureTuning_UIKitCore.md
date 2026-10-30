# `UITextGestureTuning`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _didBreakLineThreshold;
{CGPoint="x"d"y"d} _caretDistance;
d _initialOffsetFromTopOfCaret;
@"UITextMagnifierTimeWeightedPoint" _weightedPoint;
q _lastTouchType;
B _shouldUseLineThreshold;
B _shouldIncludeConstantOffset;
B _includeTipProjection;
B _strongerBiasAgainstUp;
@"NSObject<UICoordinateSpace>" _containerCoordinateSpace;
@"NSObject<UICoordinateSpace>" _gestureCoordinateSpace;
d _initialPosition;
d _lineBreakProgress;
```

## Properties

```
@property (T@"NSObject<UICoordinateSpace>",W,N,V_containerCoordinateSpace) containerCoordinateSpace;
@property (T@"NSObject<UICoordinateSpace>",W,N,V_gestureCoordinateSpace) gestureCoordinateSpace;
@property (TB,N,V_shouldUseLineThreshold) shouldUseLineThreshold;
@property (TB,N,V_shouldIncludeConstantOffset) shouldIncludeConstantOffset;
@property (TB,N,V_includeTipProjection) includeTipProjection;
@property (TB,N,V_strongerBiasAgainstUp) strongerBiasAgainstUp;
@property (TB,R,N,V_didBreakLineThreshold) didBreakLineThreshold;
@property (Td,R,N,V_initialPosition) initialPosition;
@property (Td,R,N,V_lineBreakProgress) lineBreakProgress;
```

## Instance methods

```
-[UITextGestureTuning _reset];
-[UITextGestureTuning touchAlignedPointForPoint:translation:];
-[UITextGestureTuning init];
-[UITextGestureTuning setStrongerBiasAgainstUp:];
-[UITextGestureTuning pointIfPlacedCarefully:];
-[UITextGestureTuning strongerBiasAgainstUp];
-[UITextGestureTuning shouldUseLineThreshold];
-[UITextGestureTuning setShouldUseLineThreshold:];
-[UITextGestureTuning updateWithTouches:gestureState:];
-[UITextGestureTuning initialPosition];
-[UITextGestureTuning setShouldIncludeConstantOffset:];
-[UITextGestureTuning assertInitialPositionFromTopOfCaret:distanceFromCaret:];
-[UITextGestureTuning containerCoordinateSpace];
-[UITextGestureTuning didBreakLineThreshold];
-[UITextGestureTuning gestureCoordinateSpace];
-[UITextGestureTuning includeTipProjection];
-[UITextGestureTuning lineBreakProgress];
-[UITextGestureTuning pointForGestureState:point:translation:];
-[UITextGestureTuning setContainerCoordinateSpace:];
-[UITextGestureTuning setGestureCoordinateSpace:];
-[UITextGestureTuning setIncludeTipProjection:];
-[UITextGestureTuning shouldIncludeConstantOffset];
-[UITextGestureTuning updateVisibilityOffsetForGestureState:touchType:locationInSceneReferenceSpace:majorRadius:];
-[UITextGestureTuning updateWeightedPointWithGestureState:location:];
```
