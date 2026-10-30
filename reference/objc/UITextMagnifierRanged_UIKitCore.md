# `UITextMagnifierRanged`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextMagnifier`
- 6 instance variables, 1 properties, 17 instance methods, 3 class methods

## Instance variables

```
d _touchOffsetFromMagnificationPoint;
d _magnifierOffsetFromTouch;
B _isHorizontal;
B _isAnimating;
q _delayedAnimationType;
{CGPoint="x"d"y"d} _delayedAnimationPoint;
```

## Properties

```
@property (TB,N,V_isHorizontal) isHorizontal;
```

## Class methods

```
+[UITextMagnifierRanged activeRangedMagnifier];
+[UITextMagnifierRanged renderClass];
+[UITextMagnifierRanged sharedRangedMagnifier];
```

## Instance methods

```
-[UITextMagnifierRanged clipPoint:inRect:];
-[UITextMagnifierRanged isHorizontal];
-[UITextMagnifierRanged stopMagnifying:];
-[UITextMagnifierRanged zoomUpAnimation];
-[UITextMagnifierRanged adjustMagnificationPoint:];
-[UITextMagnifierRanged beginMagnifyingTarget:text:magnificationPoint:offset:animated:];
-[UITextMagnifierRanged caretRectClosestToPoint:];
-[UITextMagnifierRanged horizontalMovement];
-[UITextMagnifierRanged horizontalMovementAtTime:];
-[UITextMagnifierRanged initWithFrame];
-[UITextMagnifierRanged offsetFromMagnificationPoint];
-[UITextMagnifierRanged setIsHorizontal:];
-[UITextMagnifierRanged setMagnificationPoint:];
-[UITextMagnifierRanged terminalPointPlacedCarefully];
-[UITextMagnifierRanged updateFrameAndOffset];
-[UITextMagnifierRanged wasPlacedCarefullyAtTime:];
-[UITextMagnifierRanged zoomDownAnimation];
```
