# `SBTouchSuppressionShieldWindow`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRootWindow`
- 1 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _touchSuppressionActive;
```

## Properties

```
@property (TB,N,GisTouchSuppressionActive,V_touchSuppressionActive) touchSuppressionActive;
```

## Class methods

```
+[SBTouchSuppressionShieldWindow _isSecure];
```

## Instance methods

```
-[SBTouchSuppressionShieldWindow _canBecomeKeyWindow];
-[SBTouchSuppressionShieldWindow _shouldPrepareScreenForWindow];
-[SBTouchSuppressionShieldWindow _appearsInLoupe];
-[SBTouchSuppressionShieldWindow _usesWindowServerHitTesting];
-[SBTouchSuppressionShieldWindow pointInside:withEvent:];
-[SBTouchSuppressionShieldWindow isTouchSuppressionActive];
-[SBTouchSuppressionShieldWindow setTouchSuppressionActive:];
```
