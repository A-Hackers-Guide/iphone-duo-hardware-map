# `AirplaneModeObserver`

- Image: [`/usr/lib/libBasebandManager.dylib`](../userland/usr__lib__libBasebandManager.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `RadiosPreferencesDelegate`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"RadiosPreferences" _radioPrefs;
^{dispatch_queue_s=} _queue;
{CFSharedRef<__CFUserNotification>="fRef"^{__CFUserNotification}} _notification;
```

## Properties

```
@property (T@"RadiosPreferences",&,N,V_radioPrefs) radioPrefs;
@property (T^{dispatch_queue_s=},N,V_queue) queue;
@property (T{CFSharedRef<__CFUserNotification>=^{__CFUserNotification}},N,V_notification) notification;
```

## Instance methods

```
-[AirplaneModeObserver startMonitoring];
-[AirplaneModeObserver notification];
-[AirplaneModeObserver airplaneModeChanged];
-[AirplaneModeObserver setNotification:];
-[AirplaneModeObserver dealloc];
-[AirplaneModeObserver setRadioPrefs:];
-[AirplaneModeObserver queue];
-[AirplaneModeObserver stopMonitoring];
-[AirplaneModeObserver radioPrefs];
-[AirplaneModeObserver setQueue:];
-[AirplaneModeObserver initWithNotification:];
```
