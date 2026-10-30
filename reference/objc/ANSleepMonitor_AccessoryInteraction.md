# `ANSleepMonitor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
I _powerManagementConnection;
^{IONotificationPort=} _powerManagementPort;
I _powerManagementNotifier;
@? _onSystemWillSleep;
@? _onSystemWillPowerOn;
@? _onSystemWillNotSleep;
```

## Properties

```
@property (T@?,C,N,V_onSystemWillSleep) onSystemWillSleep;
@property (T@?,C,N,V_onSystemWillPowerOn) onSystemWillPowerOn;
@property (T@?,C,N,V_onSystemWillNotSleep) onSystemWillNotSleep;
```

## Instance methods

```
-[ANSleepMonitor initWithQueue:];
-[ANSleepMonitor dealloc];
-[ANSleepMonitor _onPowerManagementNotificationForService:messageType:messageArgument:];
-[ANSleepMonitor onSystemWillNotSleep];
-[ANSleepMonitor onSystemWillPowerOn];
-[ANSleepMonitor onSystemWillSleep];
-[ANSleepMonitor setOnSystemWillNotSleep:];
-[ANSleepMonitor setOnSystemWillPowerOn:];
-[ANSleepMonitor setOnSystemWillSleep:];
```
