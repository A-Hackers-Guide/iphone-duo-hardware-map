# `UIGestureRecognizerTransformAnalyzerInfo`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
d _translationMagnitude;
d _scale;
d _rotation;
{CGPoint="x"d"y"d} _translation;
{CGPoint="x"d"y"d} _absoluteTranslation;
```

## Properties

```
@property (T{CGPoint=dd},N,S_setTranslation:,V_translation) translation;
@property (Td,N,S_setTranslationMagnitude:,V_translationMagnitude) translationMagnitude;
@property (T{CGPoint=dd},N,S_setAbsoluteTranslation:,V_absoluteTranslation) absoluteTranslation;
@property (Td,N,S_setScale:,V_scale) scale;
@property (Td,N,S_setRotation:,V_rotation) rotation;
```

## Instance methods

```
-[UIGestureRecognizerTransformAnalyzerInfo _reset];
-[UIGestureRecognizerTransformAnalyzerInfo rotation];
-[UIGestureRecognizerTransformAnalyzerInfo scale];
-[UIGestureRecognizerTransformAnalyzerInfo description];
-[UIGestureRecognizerTransformAnalyzerInfo absoluteTranslation];
-[UIGestureRecognizerTransformAnalyzerInfo translation];
-[UIGestureRecognizerTransformAnalyzerInfo _setScale:];
-[UIGestureRecognizerTransformAnalyzerInfo _setRotation:];
-[UIGestureRecognizerTransformAnalyzerInfo translationMagnitude];
-[UIGestureRecognizerTransformAnalyzerInfo _setAbsoluteTranslation:];
-[UIGestureRecognizerTransformAnalyzerInfo _setTranslation:];
-[UIGestureRecognizerTransformAnalyzerInfo _setTranslationMagnitude:];
```
