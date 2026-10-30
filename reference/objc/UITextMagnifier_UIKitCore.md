# `UITextMagnifier`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 12 instance variables, 8 properties, 32 instance methods, 1 class methods

## Instance variables

```
@"UIView" _target;
{CGPoint="x"d"y"d} _magnificationPoint;
{CGPoint="x"d"y"d} _animationPoint;
{CGPoint="x"d"y"d} _terminalPoint;
B _terminalPointPlacedCarefully;
@"UIResponder<UITextInput>" _text;
@"UITextMagnifierTimeWeightedPoint" _weightedPoint;
@"UIView" _magnifierRenderer;
@"UIView" _autoscrollRenderer;
i _autoscrollDirections;
B _isAnimating;
q _delayedAnimationType;
```

## Properties

```
@property (T@"UIView",&,N,V_target) target;
@property (T@"UIResponder<UITextInput>",&,N,V_text) text;
@property (T{CGPoint=dd},N,V_magnificationPoint) magnificationPoint;
@property (T{CGPoint=dd},N,V_animationPoint) animationPoint;
@property (T{CGPoint=dd},R,N,V_terminalPoint) terminalPoint;
@property (TB,R,N,V_terminalPointPlacedCarefully) terminalPointPlacedCarefully;
@property (TB,R,N) isHorizontal;
@property (Td,R,N) offsetFromMagnificationPoint;
```

## Class methods

```
+[UITextMagnifier renderClass];
```

## Instance methods

```
-[UITextMagnifier setNeedsDisplay];
-[UITextMagnifier text];
-[UITextMagnifier setTarget:];
-[UITextMagnifier remove];
-[UITextMagnifier setFrame:];
-[UITextMagnifier setText:];
-[UITextMagnifier target];
-[UITextMagnifier initWithFrame:];
-[UITextMagnifier isHorizontal];
-[UITextMagnifier stopMagnifying:];
-[UITextMagnifier zoomUpAnimation];
-[UITextMagnifier adjustMagnificationPoint:];
-[UITextMagnifier animateToAutoscrollRenderer];
-[UITextMagnifier animateToMagnifierRenderer];
-[UITextMagnifier animationPoint];
-[UITextMagnifier autoscrollWillNotStart];
-[UITextMagnifier beginMagnifyingTarget:text:magnificationPoint:offset:animated:];
-[UITextMagnifier beginZoomDownAnimation:withDuration:postponeHandler:];
-[UITextMagnifier beginZoomUpAnimation:withDuration:];
-[UITextMagnifier detectLostTouches:];
-[UITextMagnifier magnificationPoint];
-[UITextMagnifier offsetFromMagnificationPoint];
-[UITextMagnifier postAutoscrollPoint:];
-[UITextMagnifier setAnimationPoint:];
-[UITextMagnifier setAutoscrollDirections:];
-[UITextMagnifier setMagnificationPoint:];
-[UITextMagnifier setToMagnifierRenderer];
-[UITextMagnifier terminalPoint];
-[UITextMagnifier terminalPointPlacedCarefully];
-[UITextMagnifier updateFrameAndOffset];
-[UITextMagnifier windowWillRotate:];
-[UITextMagnifier zoomDownAnimation];
```
