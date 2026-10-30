# `SBReachabilitySettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 10 instance variables, 10 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _allowOnAllDevices;
d _reachabilityDefaultKeepAlive;
d _reachabilityInteractiveKeepAlive;
d _yOffsetFactor;
d _homeGestureSwipeDownHysteresis;
d _homeGestureSwipeDownHeight;
d _systemWideSwipeDownHeight;
@"SBFFluidBehaviorSettings" _animationSettings;
@"SBFCAColorMatrixSettings" _jindoTintColorMatrixSettings;
d _jindoInertDisableOffset;
```

## Properties

```
@property (TB,N,V_allowOnAllDevices) allowOnAllDevices;
@property (Td,N,V_reachabilityDefaultKeepAlive) reachabilityDefaultKeepAlive;
@property (Td,N,V_reachabilityInteractiveKeepAlive) reachabilityInteractiveKeepAlive;
@property (Td,N,V_yOffsetFactor) yOffsetFactor;
@property (Td,N,V_homeGestureSwipeDownHysteresis) homeGestureSwipeDownHysteresis;
@property (Td,N,V_homeGestureSwipeDownHeight) homeGestureSwipeDownHeight;
@property (Td,N,V_systemWideSwipeDownHeight) systemWideSwipeDownHeight;
@property (T@"SBFFluidBehaviorSettings",&,N,V_animationSettings) animationSettings;
@property (T@"SBFCAColorMatrixSettings",&,N,V_jindoTintColorMatrixSettings) jindoTintColorMatrixSettings;
@property (Td,N,V_jindoInertDisableOffset) jindoInertDisableOffset;
```

## Class methods

```
+[SBReachabilitySettings settingsControllerModule];
```

## Instance methods

```
-[SBReachabilitySettings setAnimationSettings:];
-[SBReachabilitySettings animationSettings];
-[SBReachabilitySettings setJindoTintColorMatrixSettings:];
-[SBReachabilitySettings setYOffsetFactor:];
-[SBReachabilitySettings homeGestureSwipeDownHysteresis];
-[SBReachabilitySettings jindoTintColorMatrixSettings];
-[SBReachabilitySettings yOffset];
-[SBReachabilitySettings jindoInertDisableOffset];
-[SBReachabilitySettings systemWideSwipeDownHeight];
-[SBReachabilitySettings setDefaultValues];
-[SBReachabilitySettings allowOnAllDevices];
-[SBReachabilitySettings yOffsetFactor];
-[SBReachabilitySettings homeGestureSwipeDownHeight];
-[SBReachabilitySettings setJindoInertDisableOffset:];
-[SBReachabilitySettings setSystemWideSwipeDownHeight:];
-[SBReachabilitySettings reachabilityInteractiveKeepAlive];
-[SBReachabilitySettings setReachabilityInteractiveKeepAlive:];
-[SBReachabilitySettings setHomeGestureSwipeDownHeight:];
-[SBReachabilitySettings setReachabilityDefaultKeepAlive:];
-[SBReachabilitySettings reachabilityDefaultKeepAlive];
-[SBReachabilitySettings setHomeGestureSwipeDownHysteresis:];
-[SBReachabilitySettings setAllowOnAllDevices:];
```
