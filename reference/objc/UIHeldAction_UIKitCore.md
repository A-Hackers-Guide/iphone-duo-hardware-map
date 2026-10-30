# `UIHeldAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDelayedAction`
- 4 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _holding;
@"NSDate" _holdBegan;
d _baseDelay;
d _timeBalance;
```

## Instance methods

```
-[UIHeldAction hold];
-[UIHeldAction unschedule];
-[UIHeldAction cancel];
-[UIHeldAction resume];
-[UIHeldAction touchWithDelay:];
-[UIHeldAction isHolding];
```
