# `_UIViewAdditiveAnimationAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAction`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"CAAnimation" _pendingAnimation;
@"UIViewPropertyAnimator" _animationObject;
@"UIView" _view;
```

## Properties

```
@property (T@"CAAnimation",R,&,N,V_pendingAnimation) pendingAnimation;
@property (T@"UIViewPropertyAnimator",R,&,N,V_animationObject) animationObject;
@property (T@"UIView",R,&,N,V_view) view;
```

## Instance methods

```
-[_UIViewAdditiveAnimationAction pendingAnimation];
-[_UIViewAdditiveAnimationAction view];
-[_UIViewAdditiveAnimationAction initWithPendingAnimation:withAnimationObject:forView:];
-[_UIViewAdditiveAnimationAction animationObject];
-[_UIViewAdditiveAnimationAction runActionForKey:object:arguments:];
```
