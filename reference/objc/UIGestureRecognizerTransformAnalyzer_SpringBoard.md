# `UIGestureRecognizerTransformAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIGestureRecognizerTransformAnalyzerInfo" _smoothedInfo;
d _translationWeight;
d _pinchingWeight;
d _rotationWeight;
i _dominantComponent;
```

## Properties

```
@property (Ti,R,N,V_dominantComponent) dominantComponent;
@property (Td,N,V_translationWeight) translationWeight;
@property (Td,N,V_pinchingWeight) pinchingWeight;
@property (Td,N,V_rotationWeight) rotationWeight;
@property (T@"UIGestureRecognizerTransformAnalyzerInfo",R,N,V_smoothedInfo) smoothedInfo;
```

## Instance methods

```
-[UIGestureRecognizerTransformAnalyzer init];
-[UIGestureRecognizerTransformAnalyzer setTranslationWeight:];
-[UIGestureRecognizerTransformAnalyzer reset];
-[UIGestureRecognizerTransformAnalyzer analyzeTouches:];
-[UIGestureRecognizerTransformAnalyzer dominantComponent];
-[UIGestureRecognizerTransformAnalyzer setRotationWeight:];
-[UIGestureRecognizerTransformAnalyzer setPinchingWeight:];
-[UIGestureRecognizerTransformAnalyzer translationWeight];
-[UIGestureRecognizerTransformAnalyzer pinchingWeight];
-[UIGestureRecognizerTransformAnalyzer rotationWeight];
-[UIGestureRecognizerTransformAnalyzer smoothedInfo];
```
