# `_UITabCrossFadeTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning_Internal`, `UIViewControllerAnimatedTransitioning`, `UIViewControllerPreemptableAnimatedTransitioning`
- 4 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
wasPreempted;
fromView;
firstResponderToRemember;
backgroundColor;
```

## Properties

```
@property (Tq,N,R) _navigationBarTransitionVariant;
@property (TB,N,R) _shouldCrossFadeNavigationBarVisibility;
@property (TB,N,R) _shouldCrossFadeBottomBars;
```

## Class methods

```
+[_UITabCrossFadeTransition isSupportedForTraits:];
```

## Instance methods

```
-[_UITabCrossFadeTransition _shouldCrossFadeNavigationBarVisibility];
-[_UITabCrossFadeTransition animateTransition:];
-[_UITabCrossFadeTransition transitionDuration:];
-[_UITabCrossFadeTransition init];
-[_UITabCrossFadeTransition _navigationBarTransitionVariant];
-[_UITabCrossFadeTransition _shouldCrossFadeBottomBars];
-[_UITabCrossFadeTransition animationEnded:];
-[_UITabCrossFadeTransition preemptWithContext:];
-[_UITabCrossFadeTransition willBeginAfterPreemptionWithContext:data:];
-[_UITabCrossFadeTransition shouldPreemptWithContext:];
-[_UITabCrossFadeTransition _customNavigationBarHidingDuration:];
-[_UITabCrossFadeTransition initWithBackgroundColor:];
```
