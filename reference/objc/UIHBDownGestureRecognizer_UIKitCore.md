# `UIHBDownGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 4 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIDelayedAction" _delayedAction;
@"NSMutableSet" _currentlyPressedTypes;
@"NSSet" _requiredPressTypes;
d _maximumIntervalBetweenPresses;
```

## Properties

```
@property (Td,N,V_maximumIntervalBetweenPresses) maximumIntervalBetweenPresses;
```

## Instance methods

```
-[UIHBDownGestureRecognizer _resetGestureRecognizer];
-[UIHBDownGestureRecognizer _fail];
-[UIHBDownGestureRecognizer setAllowedPressTypes:];
-[UIHBDownGestureRecognizer pressesCancelled:withEvent:];
-[UIHBDownGestureRecognizer pressesEnded:withEvent:];
-[UIHBDownGestureRecognizer initWithTarget:action:];
-[UIHBDownGestureRecognizer pressesBegan:withEvent:];
-[UIHBDownGestureRecognizer pressesChanged:withEvent:];
-[UIHBDownGestureRecognizer _succeed];
-[UIHBDownGestureRecognizer _allRequiredButtonsDown];
-[UIHBDownGestureRecognizer _processPresses:];
-[UIHBDownGestureRecognizer maximumIntervalBetweenPresses];
-[UIHBDownGestureRecognizer setMaximumIntervalBetweenPresses:];
```
