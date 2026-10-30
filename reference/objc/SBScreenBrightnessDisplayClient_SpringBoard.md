# `SBScreenBrightnessDisplayClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDisplayBrightnessClientObserver`, `SBBacklightControllerObserver`, `BSInvalidatable`
- 10 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" _displayHardwareIdentifier;
@"NSObject<OS_dispatch_queue>" _notifyQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"CBDisplayClient" _lock_displayClient;
@"NSHashTable" _lock_observers;
B _lock_registeredForBrightnessUpdates;
B _lock_displayIsOff;
@"NSNumber" _lock_lastNotifiedBrightness;
@"SBScreenBrightnessRequest" _lock_request;
@"SBBacklightController" _backlightController;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R) notifyQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBScreenBrightnessDisplayClient backlightController:didTransitionToBacklightState:source:];
-[SBScreenBrightnessDisplayClient backlightController:willTransitionToBacklightState:source:];
-[SBScreenBrightnessDisplayClient removeObserver:];
-[SBScreenBrightnessDisplayClient notifyQueue];
-[SBScreenBrightnessDisplayClient addObserver:];
-[SBScreenBrightnessDisplayClient invalidate];
-[SBScreenBrightnessDisplayClient _displayDidTurnOn];
-[SBScreenBrightnessDisplayClient _displayWillTurnOff];
-[SBScreenBrightnessDisplayClient _isBrightnessUnchangedFrom:to:];
-[SBScreenBrightnessDisplayClient _newRequestWithBrightness:pendingDisplayOn:];
-[SBScreenBrightnessDisplayClient _notifyQueue_readBrightnessFromDisplayForced:];
-[SBScreenBrightnessDisplayClient _sanitizedBrightnessLevel:];
-[SBScreenBrightnessDisplayClient _updateBrightnessTracking];
-[SBScreenBrightnessDisplayClient _updateDisplayWithBrightness:displayClient:];
-[SBScreenBrightnessDisplayClient brightnessControlAvailableUpdate:];
-[SBScreenBrightnessDisplayClient brightnessUpdate:];
-[SBScreenBrightnessDisplayClient initWithClient:windowScene:];
-[SBScreenBrightnessDisplayClient relinquishRequest:];
-[SBScreenBrightnessDisplayClient requestPreferredBrightness:];
```
