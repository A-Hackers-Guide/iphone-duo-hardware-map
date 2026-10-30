# `SBReachabilityGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 6 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _everTranslatedUpwards;
B _movedPastHysteresis;
@"SBTouchHistory" _touchHistory;
@"UITouch" _activeTouch;
@"SBReachabilitySettings" _settings;
{CGPoint="x"d"y"d} _initialTouchLocation;
```

## Properties

```
@property (T@"SBTouchHistory",&,N,V_touchHistory) touchHistory;
@property (T@"UITouch",&,N,V_activeTouch) activeTouch;
@property (T{CGPoint=dd},N,V_initialTouchLocation) initialTouchLocation;
@property (TB,N,V_everTranslatedUpwards) everTranslatedUpwards;
@property (TB,N,V_movedPastHysteresis) movedPastHysteresis;
@property (T@"SBReachabilitySettings",&,N,V_settings) settings;
```

## Instance methods

```
-[SBReachabilityGestureRecognizer setTouchHistory:];
-[SBReachabilityGestureRecognizer touchesEnded:withEvent:];
-[SBReachabilityGestureRecognizer initialTouchLocation];
-[SBReachabilityGestureRecognizer touchHistory];
-[SBReachabilityGestureRecognizer setEverTranslatedUpwards:];
-[SBReachabilityGestureRecognizer touchesCancelled:withEvent:];
-[SBReachabilityGestureRecognizer setInitialTouchLocation:];
-[SBReachabilityGestureRecognizer activeTouch];
-[SBReachabilityGestureRecognizer setSettings:];
-[SBReachabilityGestureRecognizer settings];
-[SBReachabilityGestureRecognizer reset];
-[SBReachabilityGestureRecognizer setMovedPastHysteresis:];
-[SBReachabilityGestureRecognizer touchesBegan:withEvent:];
-[SBReachabilityGestureRecognizer touchesMoved:withEvent:];
-[SBReachabilityGestureRecognizer initWithTarget:action:];
-[SBReachabilityGestureRecognizer setActiveTouch:];
-[SBReachabilityGestureRecognizer movedPastHysteresis];
-[SBReachabilityGestureRecognizer everTranslatedUpwards];
```
