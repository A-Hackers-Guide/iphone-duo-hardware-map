# `PowerMonitor`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`](../userland/System__Library__CoreAccessories__PlugIns__Platform__IOKit.platform__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 22 properties, 60 instance methods, 1 class methods

## Instance variables

```
B _sleepNotificationsEnabled;
B _systemIsAsleep;
B _isExtChargerConnected;
B _isBatteryCharging;
C _batteryChargeLevelPercent;
I _systemPowerPort;
I _systemPowerIterator;
i _batteryCapacity;
i _batteryCapacityOverride;
i _batteryCapacityMax;
I _battery_iter;
i _batteryChargingType;
i _batteryChargingTypeExternal;
@"NSObject<OS_dispatch_queue>" _systemPowerQueue;
^{IONotificationPort=} _systemPowerNotifyPortRef;
@"NSMutableArray" _sleepNotificationClients;
@"NSMutableArray" _clientsPreventingSleep;
@"NSObject<OS_dispatch_semaphore>" _sleepSemaphore;
@"NSObject<OS_dispatch_queue>" _clientsPreventingSleepLock;
^{IONotificationPort=} _batteryNotifyPortRef;
@"NSMutableArray" _batteryNotificationClients;
@"NSLock" _batteryNotificationClientsLock;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_systemPowerQueue) systemPowerQueue;
@property (TI,N,V_systemPowerPort) systemPowerPort;
@property (T^{IONotificationPort=},N,V_systemPowerNotifyPortRef) systemPowerNotifyPortRef;
@property (TI,N,V_systemPowerIterator) systemPowerIterator;
@property (TB,N,V_sleepNotificationsEnabled) sleepNotificationsEnabled;
@property (T@"NSMutableArray",&,N,V_sleepNotificationClients) sleepNotificationClients;
@property (T@"NSMutableArray",&,N,V_clientsPreventingSleep) clientsPreventingSleep;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_sleepSemaphore) sleepSemaphore;
@property (TB,N,V_systemIsAsleep) systemIsAsleep;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_clientsPreventingSleepLock) clientsPreventingSleepLock;
@property (TB,N,V_isExtChargerConnected) isExtChargerConnected;
@property (Ti,N,V_batteryCapacity) batteryCapacity;
@property (Ti,N,V_batteryCapacityOverride) batteryCapacityOverride;
@property (Ti,N,V_batteryCapacityMax) batteryCapacityMax;
@property (TB,N,V_isBatteryCharging) isBatteryCharging;
@property (TC,N,V_batteryChargeLevelPercent) batteryChargeLevelPercent;
@property (T^{IONotificationPort=},N,V_batteryNotifyPortRef) batteryNotifyPortRef;
@property (TI,N,V_battery_iter) battery_iter;
@property (T@"NSMutableArray",&,N,V_batteryNotificationClients) batteryNotificationClients;
@property (T@"NSLock",&,N,V_batteryNotificationClientsLock) batteryNotificationClientsLock;
@property (Ti,N,V_batteryChargingType) batteryChargingType;
@property (Ti,N,V_batteryChargingTypeExternal) batteryChargingTypeExternal;
```

## Class methods

```
+[PowerMonitor sharedMonitor];
```

## Instance methods

```
-[PowerMonitor setBatteryNotifyPortRef:];
-[PowerMonitor batteryNotifyPortRef];
-[PowerMonitor battery_iter];
-[PowerMonitor init];
-[PowerMonitor dealloc];
-[PowerMonitor batteryChargeLevelPercent];
-[PowerMonitor isBatteryCharging];
-[PowerMonitor batteryCapacity];
-[PowerMonitor setBattery_iter:];
-[PowerMonitor setBatteryChargeLevelPercent:];
-[PowerMonitor setBatteryCapacity:];
-[PowerMonitor systemPowerPort];
-[PowerMonitor createBatteryNotificationClient];
-[PowerMonitor setBatteryChargingTypeExternal:];
-[PowerMonitor clientHandledSleepNotification:];
-[PowerMonitor _checkAndSendNotificationForOldConnected:oldIsBatteryCharging:oldBatteryChargeLevelPercent:oldBatteryChargingType:oldBatteryChargingTypeExt:overrideChanged:];
-[PowerMonitor _getBatteryChargingTypeIsInductive:];
-[PowerMonitor batteryCapacityMax];
-[PowerMonitor batteryCapacityOverride];
-[PowerMonitor batteryChargingType];
-[PowerMonitor batteryChargingTypeExternal];
-[PowerMonitor batteryNotificationClients];
-[PowerMonitor batteryNotificationClientsLock];
-[PowerMonitor clientsPreventingSleep];
-[PowerMonitor clientsPreventingSleepLock];
-[PowerMonitor createSleepNotificationClient];
-[PowerMonitor destroyBatteryNotificationsForClient:];
-[PowerMonitor destroySleepNotificationsForClient:];
-[PowerMonitor getBatteryChargeLevel];
-[PowerMonitor getBatteryChargingState];
-[PowerMonitor getBatteryChargingType];
-[PowerMonitor getBatteryChargingTypeIsInductive];
-[PowerMonitor getExternalBatteryChargingType];
-[PowerMonitor getExternalBatteryChargingTypeIsInductive];
-[PowerMonitor isExtChargerConnected];
-[PowerMonitor isExternalChargerConnected];
-[PowerMonitor setBatteryCapacityMax:];
-[PowerMonitor setBatteryCapacityOverride:];
-[PowerMonitor setBatteryChargingType:];
-[PowerMonitor setBatteryNotificationClients:];
-[PowerMonitor setBatteryNotificationClientsLock:];
-[PowerMonitor setClientsPreventingSleep:];
-[PowerMonitor setClientsPreventingSleepLock:];
-[PowerMonitor setIsBatteryCharging:];
-[PowerMonitor setIsExtChargerConnected:];
-[PowerMonitor setSleepNotificationClients:];
-[PowerMonitor setSleepNotificationsEnabled:];
-[PowerMonitor setSleepSemaphore:];
-[PowerMonitor setSystemIsAsleep:];
-[PowerMonitor setSystemPowerIterator:];
-[PowerMonitor setSystemPowerNotifyPortRef:];
-[PowerMonitor setSystemPowerPort:];
-[PowerMonitor setSystemPowerQueue:];
-[PowerMonitor sleepNotificationClients];
-[PowerMonitor sleepNotificationsEnabled];
-[PowerMonitor sleepSemaphore];
-[PowerMonitor systemIsAsleep];
-[PowerMonitor systemPowerIterator];
-[PowerMonitor systemPowerNotifyPortRef];
-[PowerMonitor systemPowerQueue];
```
