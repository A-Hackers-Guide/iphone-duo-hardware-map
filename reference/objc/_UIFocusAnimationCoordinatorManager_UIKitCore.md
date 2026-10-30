# `_UIFocusAnimationCoordinatorManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"UIFocusAnimationCoordinator" _activeFocusAnimationCoordinator;
@"NSHashTable" _unfocusingItems;
d _lastFocusUpdateTime;
@"UIFocusAnimationCoordinator" _lastFocusingItemAnimationCoordinator;
@"NSMutableArray" _inheritedAnimationCoordinatorActiveAnimationStack;
```

## Properties

```
@property (T@"NSHashTable",R,N,V_unfocusingItems) unfocusingItems;
@property (Td,N,V_lastFocusUpdateTime) lastFocusUpdateTime;
@property (T@"UIFocusAnimationCoordinator",&,N,V_activeFocusAnimationCoordinator) activeFocusAnimationCoordinator;
@property (T@"UIFocusAnimationCoordinator",&,N,V_lastFocusingItemAnimationCoordinator) lastFocusingItemAnimationCoordinator;
@property (T@"NSMutableArray",&,N,V_inheritedAnimationCoordinatorActiveAnimationStack) inheritedAnimationCoordinatorActiveAnimationStack;
```

## Class methods

```
+[_UIFocusAnimationCoordinatorManager animationCoordinatorForContext:];
+[_UIFocusAnimationCoordinatorManager activeCoordinatorMap];
```

## Instance methods

```
-[_UIFocusAnimationCoordinatorManager init];
-[_UIFocusAnimationCoordinatorManager activeFocusAnimationCoordinator];
-[_UIFocusAnimationCoordinatorManager unfocusingItems];
-[_UIFocusAnimationCoordinatorManager _performDelayedFocusingAnimationIfNecessary];
-[_UIFocusAnimationCoordinatorManager _scheduleDelayedFocusingAnimationWithDelay:];
-[_UIFocusAnimationCoordinatorManager didUpdateFocusInContext:fromItem:];
-[_UIFocusAnimationCoordinatorManager inheritedAnimationCoordinatorActiveAnimationStack];
-[_UIFocusAnimationCoordinatorManager lastFocusUpdateTime];
-[_UIFocusAnimationCoordinatorManager lastFocusingItemAnimationCoordinator];
-[_UIFocusAnimationCoordinatorManager setActiveFocusAnimationCoordinator:];
-[_UIFocusAnimationCoordinatorManager setInheritedAnimationCoordinatorActiveAnimationStack:];
-[_UIFocusAnimationCoordinatorManager setLastFocusUpdateTime:];
-[_UIFocusAnimationCoordinatorManager setLastFocusingItemAnimationCoordinator:];
-[_UIFocusAnimationCoordinatorManager willUpdateFocusInContext:];
```
