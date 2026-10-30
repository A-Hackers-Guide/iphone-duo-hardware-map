# `_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
os.Logger logger;
_$sSD -> Foundation.UUID Foundation.Date lastAttemptTimestamps;
_$sSD -> Foundation.UUID Foundation.Date lastDisconnectionTimestamps;
(objc_protocol 0x23b0aae00) systemUtils;
```

## Instance methods

```
-[_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator init];
-[_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator initWithSystemUtils:];
-[_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator recordAttemptForDeviceWithUUID:];
-[_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator clearDataIfNeeded];
-[_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator recordDisconnectionForDeviceWithUUID:];
-[_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator shouldAttemptProactiveMaintenanceWithUUID:nearOwnerTimeout:];
```
