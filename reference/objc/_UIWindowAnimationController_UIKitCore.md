# `_UIWindowAnimationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _shouldCrossfade;
@"UIWindow" _window;
```

## Properties

```
@property (T@"UIWindow",N,V_window) window;
@property (TB,N,V_shouldCrossfade) shouldCrossfade;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIWindowAnimationController animationControllerWithWindow:];
```

## Instance methods

```
-[_UIWindowAnimationController shouldCrossfade];
-[_UIWindowAnimationController setShouldCrossfade:];
-[_UIWindowAnimationController _performLayoutAnimationWithContext:windowGeometryUpdatingBlock:];
-[_UIWindowAnimationController animateTransition:];
-[_UIWindowAnimationController transitionDuration:];
-[_UIWindowAnimationController initWithWindow:];
-[_UIWindowAnimationController _performCrossfadeAnimationWithContext:windowGeometryUpdatingBlock:];
-[_UIWindowAnimationController window];
-[_UIWindowAnimationController setWindow:];
```
