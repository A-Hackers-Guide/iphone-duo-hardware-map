# `_UIViewWeakCAAnimationDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`
- 2 instance variables, 5 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"<CAAnimationDelegate>" _animationDelegate;
{?="delegateAnimationDidStart"b1"delegateAnimationDidStopFinished"b1} _flags;
```

## Properties

```
@property (T@"<CAAnimationDelegate>",R,W,N,V_animationDelegate) animationDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIViewWeakCAAnimationDelegate weakAnimationDelegate:];
```

## Instance methods

```
-[_UIViewWeakCAAnimationDelegate animationDidStart:];
-[_UIViewWeakCAAnimationDelegate animationDidStop:finished:];
-[_UIViewWeakCAAnimationDelegate animationDelegate];
-[_UIViewWeakCAAnimationDelegate initWithAnimationDelegate:];
```
