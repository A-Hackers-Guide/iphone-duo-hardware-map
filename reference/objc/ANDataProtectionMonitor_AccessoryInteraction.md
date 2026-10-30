# `ANDataProtectionMonitor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
i _lockStatusNotificationToken;
i _firstUnlockNotificationToken;
B _deviceUnlockedSinceBoot;
B _dataAvailable;
@? _onDataAvailabilityUpdate;
@? _onFirstUnlockSinceBoot;
```

## Properties

```
@property (TB,R,N,V_deviceUnlockedSinceBoot) deviceUnlockedSinceBoot;
@property (TB,R,N,V_dataAvailable) dataAvailable;
@property (T@?,C,N,V_onDataAvailabilityUpdate) onDataAvailabilityUpdate;
@property (T@?,C,N,V_onFirstUnlockSinceBoot) onFirstUnlockSinceBoot;
```

## Instance methods

```
-[ANDataProtectionMonitor initWithQueue:];
-[ANDataProtectionMonitor dealloc];
-[ANDataProtectionMonitor deviceUnlockedSinceBoot];
-[ANDataProtectionMonitor _updateIfNeeded];
-[ANDataProtectionMonitor _cancelFirstUnlockNotificationIfNeeded];
-[ANDataProtectionMonitor _cancelLockStatusNotificationIfNeeded];
-[ANDataProtectionMonitor dataAvailable];
-[ANDataProtectionMonitor onDataAvailabilityUpdate];
-[ANDataProtectionMonitor onFirstUnlockSinceBoot];
-[ANDataProtectionMonitor setOnDataAvailabilityUpdate:];
-[ANDataProtectionMonitor setOnFirstUnlockSinceBoot:];
```
