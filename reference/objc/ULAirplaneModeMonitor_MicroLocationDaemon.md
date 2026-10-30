# `ULAirplaneModeMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- Protocols: `RadiosPreferencesDelegate`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _airplaneMode;
@"RadiosPreferences" _radiosPref;
```

## Properties

```
@property (T@"RadiosPreferences",&,N,V_radiosPref) radiosPref;
@property (TB,N,V_airplaneMode) airplaneMode;
```

## Instance methods

```
-[ULAirplaneModeMonitor stopMonitoring:];
-[ULAirplaneModeMonitor airplaneModeChanged];
-[ULAirplaneModeMonitor latestEventAfterAddingObserverForEventName:];
-[ULAirplaneModeMonitor airplaneMode];
-[ULAirplaneModeMonitor startMonitoring:];
-[ULAirplaneModeMonitor setAirplaneMode:];
-[ULAirplaneModeMonitor _checkAirplaneMode];
-[ULAirplaneModeMonitor radiosPref];
-[ULAirplaneModeMonitor setRadiosPref:];
```
