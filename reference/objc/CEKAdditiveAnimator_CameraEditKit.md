# `CEKAdditiveAnimator`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
{?="respondsToDidFinishAnimationForAllKeys"B} _delegateFlags;
@"<CEKAdditiveAnimatorDelegate>" _delegate;
@"NSMutableDictionary" __values;
@"NSMutableDictionary" __animations;
@"CADisplayLink" __displayLink;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V__values) _values;
@property (T@"NSMutableDictionary",R,N,V__animations) _animations;
@property (T@"CADisplayLink",&,N,V__displayLink) _displayLink;
@property (T@"<CEKAdditiveAnimatorDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisAnimating) animating;
```

## Instance methods

```
-[CEKAdditiveAnimator _animations];
-[CEKAdditiveAnimator init];
-[CEKAdditiveAnimator dealloc];
-[CEKAdditiveAnimator _updateDisplayLink];
-[CEKAdditiveAnimator setValue:forKey:];
-[CEKAdditiveAnimator setDelegate:];
-[CEKAdditiveAnimator valueForKey:];
-[CEKAdditiveAnimator _values];
-[CEKAdditiveAnimator delegate];
-[CEKAdditiveAnimator _displayLink];
-[CEKAdditiveAnimator isAnimating];
-[CEKAdditiveAnimator removeAnimationsForKey:];
-[CEKAdditiveAnimator isAnimatingForKey:];
-[CEKAdditiveAnimator setValue:forKey:duration:timingCurve:];
-[CEKAdditiveAnimator _handleDisplayLinkFired:];
-[CEKAdditiveAnimator set_displayLink:];
```
