# `_UIDropAnimationHandlers`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragAnimating`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _alongsideAnimationHandlers;
@"NSMutableArray" _completionHandlers;
```

## Properties

```
@property (T@"NSArray",R,N) alongsideAnimationHandlers;
@property (T@"NSArray",R,N) completionHandlers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDropAnimationHandlers addAnimations:];
-[_UIDropAnimationHandlers addCompletion:];
-[_UIDropAnimationHandlers completionHandlers];
-[_UIDropAnimationHandlers init];
-[_UIDropAnimationHandlers alongsideAnimationHandlers];
-[_UIDropAnimationHandlers invokeAllCompletionHandlers];
-[_UIDropAnimationHandlers resetAllAnimationHandlers];
```
