# `SBCAAnimationBlockDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`
- 2 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
@? _animationDidStartHandler;
@? _animationDidStopHandler;
```

## Properties

```
@property (T@?,C,N,V_animationDidStartHandler) animationDidStartHandler;
@property (T@?,C,N,V_animationDidStopHandler) animationDidStopHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCAAnimationBlockDelegate animationDidStart:];
-[SBCAAnimationBlockDelegate animationDidStop:finished:];
-[SBCAAnimationBlockDelegate animationDidStartHandler];
-[SBCAAnimationBlockDelegate animationDidStopHandler];
-[SBCAAnimationBlockDelegate setAnimationDidStartHandler:];
-[SBCAAnimationBlockDelegate setAnimationDidStopHandler:];
```
