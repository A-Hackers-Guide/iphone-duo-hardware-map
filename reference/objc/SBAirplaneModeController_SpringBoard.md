# `SBAirplaneModeController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `RadiosPreferencesDelegate`
- 4 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"RadiosPreferences" _radioPrefs;
B _cachedInAirplaneMode;
@"NSObject<OS_dispatch_queue>" _radioQueue;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (TB,N,GisInAirplaneMode) inAirplaneMode;
```

## Instance methods

```
-[SBAirplaneModeController isInAirplaneMode];
-[SBAirplaneModeController airplaneModeChanged];
-[SBAirplaneModeController init];
-[SBAirplaneModeController initWithApplicationController:];
-[SBAirplaneModeController setInAirplaneMode:];
```
