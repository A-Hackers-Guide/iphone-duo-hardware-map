# `SBPresentationObservationToken`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 6 instance variables, 10 properties, 16 instance methods, 0 class methods

## Instance variables

```
q _state;
@? _willPresentHandler;
@? _didPresentHandler;
@? _willDismissHandler;
@? _didDismissHandler;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (Tq,R,N,V_state) state;
@property (T@?,C,N,V_willPresentHandler) willPresentHandler;
@property (T@?,C,N,V_didPresentHandler) didPresentHandler;
@property (T@?,C,N,V_willDismissHandler) willDismissHandler;
@property (T@?,C,N,V_didDismissHandler) didDismissHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPresentationObservationToken willPresent];
-[SBPresentationObservationToken didPresent];
-[SBPresentationObservationToken initWithScene:];
-[SBPresentationObservationToken willDismiss];
-[SBPresentationObservationToken invalidate];
-[SBPresentationObservationToken didDismiss];
-[SBPresentationObservationToken windowScene];
-[SBPresentationObservationToken state];
-[SBPresentationObservationToken setDidDismissHandler:];
-[SBPresentationObservationToken didDismissHandler];
-[SBPresentationObservationToken didPresentHandler];
-[SBPresentationObservationToken setDidPresentHandler:];
-[SBPresentationObservationToken setWillDismissHandler:];
-[SBPresentationObservationToken setWillPresentHandler:];
-[SBPresentationObservationToken willDismissHandler];
-[SBPresentationObservationToken willPresentHandler];
```
