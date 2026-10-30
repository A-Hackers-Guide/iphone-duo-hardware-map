# `SBAmbientDisplayController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAmbientPresentationObserver`, `SBBacklightControllerObserver`
- 9 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBAmbientPresentationController" _ambientPresentationController;
@"SBBacklightController" _backlightController;
@"CBClient" _cbClient;
@"CBDisplayClient" _cbDisplayClient;
@"NSObject<OS_dispatch_queue>" _brightnessSystemQueue;
B _ambientPresented;
B _isCoreBrightnessAmbientModeEnabled;
q _backlightState;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAmbientDisplayController backlightController:didTransitionToBacklightState:source:];
-[SBAmbientDisplayController _loggingIdentifier];
-[SBAmbientDisplayController init];
-[SBAmbientDisplayController dealloc];
-[SBAmbientDisplayController ambientPresentationController:didUpdatePresented:];
-[SBAmbientDisplayController _shouldEnableCoreBrightnessAmbientMode];
-[SBAmbientDisplayController _updateCoreBrightnessAmbientMode];
-[SBAmbientDisplayController _updateCoreBrightnessAmbientModeForce:];
-[SBAmbientDisplayController initWithWindowScene:ambientPresentationController:backlightController:];
```
