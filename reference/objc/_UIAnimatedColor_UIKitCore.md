# `_UIAnimatedColor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIColor`
- Protocols: `_UIGeometryChangeObserver`
- 8 instance variables, 3 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"UIColor" _wrappedColor;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
@"CADisplayLink" _displayLink;
@"UIViewFloatAnimatableProperty" _progressAnimatableProperty;
@? _invalidationHandler;
B _animating;
@"UIView" _parentView;
d _progress;
```

## Properties

```
@property (T@"UIView",R,W,N,V_parentView) parentView;
@property (TB,N,GisAnimating,V_animating) animating;
@property (Td,N,V_progress) progress;
```

## Class methods

```
+[_UIAnimatedColor _patternCallbacks];
+[_UIAnimatedColor animatedColorForParentView:];
```

## Instance methods

```
-[_UIAnimatedColor setStroke];
-[_UIAnimatedColor getRed:green:blue:alpha:];
-[_UIAnimatedColor isPatternColor];
-[_UIAnimatedColor colorWithAlphaComponent:];
-[_UIAnimatedColor CGColor];
-[_UIAnimatedColor setFill];
-[_UIAnimatedColor getWhite:alpha:];
-[_UIAnimatedColor getHue:saturation:brightness:alpha:];
-[_UIAnimatedColor colorSpaceName];
-[_UIAnimatedColor parentView];
-[_UIAnimatedColor alphaComponent];
-[_UIAnimatedColor setProgress:];
-[_UIAnimatedColor dealloc];
-[_UIAnimatedColor set];
-[_UIAnimatedColor _geometryChanged:forAncestor:];
-[_UIAnimatedColor progress];
-[_UIAnimatedColor hash];
-[_UIAnimatedColor isAnimating];
-[_UIAnimatedColor isEqual:];
-[_UIAnimatedColor setAnimating:];
-[_UIAnimatedColor _recreatePatternColorForBounds:];
-[_UIAnimatedColor drawRect:usingContext:progress:];
-[_UIAnimatedColor _didFireDisplayLink:];
-[_UIAnimatedColor _drawPatternWithContext:];
-[_UIAnimatedColor _patternColorForSize:];
-[_UIAnimatedColor _presentationValueChanged];
-[_UIAnimatedColor initWithBounds:view:invalidationHandler:];
-[_UIAnimatedColor initWithParentView:];
```
