# `_UIGestureRecognizerTransformAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _lowPassTranslationMagnitudeDelta;
d _lowPassScaleDelta;
d _lowPassRotationDelta;
d _translationWeight;
d _pinchingWeight;
d _rotationWeight;
q _dominantComponent;
```

## Properties

```
@property (Tq,R,N,V_dominantComponent) dominantComponent;
@property (Td,N,V_translationWeight) translationWeight;
@property (Td,N,V_pinchingWeight) pinchingWeight;
@property (Td,N,V_rotationWeight) rotationWeight;
```

## Instance methods

```
-[_UIGestureRecognizerTransformAnalyzer init];
-[_UIGestureRecognizerTransformAnalyzer setTranslationWeight:];
-[_UIGestureRecognizerTransformAnalyzer reset];
-[_UIGestureRecognizerTransformAnalyzer analyzeTouches:];
-[_UIGestureRecognizerTransformAnalyzer dominantComponent];
-[_UIGestureRecognizerTransformAnalyzer setRotationWeight:];
-[_UIGestureRecognizerTransformAnalyzer setPinchingWeight:];
-[_UIGestureRecognizerTransformAnalyzer translationWeight];
-[_UIGestureRecognizerTransformAnalyzer pinchingWeight];
-[_UIGestureRecognizerTransformAnalyzer rotationWeight];
```
