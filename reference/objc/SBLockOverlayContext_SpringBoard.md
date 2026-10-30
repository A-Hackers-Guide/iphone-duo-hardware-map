# `SBLockOverlayContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"SBLockOverlayViewController" _viewController;
Q _priority;
@? _activationBlock;
@? _deactivationBlock;
```

## Properties

```
@property (T@"SBLockOverlayViewController",R,N,V_viewController) viewController;
@property (TQ,R,N,V_priority) priority;
@property (T@?,C,N,V_activationBlock) activationBlock;
@property (T@?,C,N,V_deactivationBlock) deactivationBlock;
```

## Instance methods

```
-[SBLockOverlayContext priority];
-[SBLockOverlayContext viewController];
-[SBLockOverlayContext activationBlock];
-[SBLockOverlayContext deactivationBlock];
-[SBLockOverlayContext initWithOverlayViewController:priority:];
-[SBLockOverlayContext setActivationBlock:];
-[SBLockOverlayContext setDeactivationBlock:];
```
