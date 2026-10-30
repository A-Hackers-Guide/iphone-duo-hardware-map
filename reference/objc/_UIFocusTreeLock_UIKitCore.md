# `_UIFocusTreeLock`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _lockedEnvironments;
@"NSTimer" _validationTimer;
```

## Properties

```
@property (T@"NSMapTable",R,N,V_lockedEnvironments) lockedEnvironments;
@property (T@"NSTimer",R,N,V_validationTimer) validationTimer;
```

## Instance methods

```
-[_UIFocusTreeLock init];
-[_UIFocusTreeLock description];
-[_UIFocusTreeLock validationTimer];
-[_UIFocusTreeLock _validateLockedEnvironments];
-[_UIFocusTreeLock isEnvironmentLocked:];
-[_UIFocusTreeLock lockEnvironmentTree:];
-[_UIFocusTreeLock lockedEnvironments];
-[_UIFocusTreeLock unlockEnvironmentTree:];
```
