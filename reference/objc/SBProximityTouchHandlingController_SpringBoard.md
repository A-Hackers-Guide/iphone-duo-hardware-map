# `SBProximityTouchHandlingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `SBWindowSceneAttachmentObserving`
- 8 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _absorbTouchesBelowStatusBar;
@"NSSet" _allowedSystemGestureTypes;
d _statusBarHeight;
@"UIWindowScene" _windowScene;
@"UIWindow" _proxTouchHandlingWindow;
@"_SBProximityTouchHandlingViewController" _proxTouchHandlingViewController;
@"<BSInvalidatable>" _suppressBackBoardTouchCancellation;
@"<BSInvalidatable>" _suppressSystemGestures;
```

## Properties

```
@property (TB,N,V_absorbTouchesBelowStatusBar) absorbTouchesBelowStatusBar;
@property (T@"NSSet",&,N,V_allowedSystemGestureTypes) allowedSystemGestureTypes;
@property (Td,N,V_statusBarHeight) statusBarHeight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProximityTouchHandlingController statusBarHeight];
-[SBProximityTouchHandlingController setStatusBarHeight:];
-[SBProximityTouchHandlingController windowSceneDidDisconnect:];
-[SBProximityTouchHandlingController invalidate];
-[SBProximityTouchHandlingController windowSceneDidConnect:];
-[SBProximityTouchHandlingController setAbsorbTouchesBelowStatusBar:];
-[SBProximityTouchHandlingController absorbTouchesBelowStatusBar];
-[SBProximityTouchHandlingController allowedSystemGestureTypes];
-[SBProximityTouchHandlingController initWithSettings:touchHandlingDelegate:];
-[SBProximityTouchHandlingController setAllowedSystemGestureTypes:];
```
