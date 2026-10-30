# `CEKAnimationGenerator`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" __animations;
@"CADisplayLink" __displayLink;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V__animations) _animations;
@property (T@"CADisplayLink",&,N,V__displayLink) _displayLink;
@property (TB,R,N,GisAnimating) animating;
```

## Instance methods

```
-[CEKAnimationGenerator _animations];
-[CEKAnimationGenerator init];
-[CEKAnimationGenerator dealloc];
-[CEKAnimationGenerator _displayLink];
-[CEKAnimationGenerator isAnimating];
-[CEKAnimationGenerator stopAllAnimations];
-[CEKAnimationGenerator set_animations:];
-[CEKAnimationGenerator _handleDisplayLinkFired:];
-[CEKAnimationGenerator _stopAnimationForIdentifier:didComplete:];
-[CEKAnimationGenerator _updateAnimationForIdentifer:timestamp:];
-[CEKAnimationGenerator isAnimatingForIdentifier:];
-[CEKAnimationGenerator set_displayLink:];
-[CEKAnimationGenerator startAnimationForIdentifier:duration:updateHandler:completionHandler:];
-[CEKAnimationGenerator stopAnimationForIdentifier:];
```
