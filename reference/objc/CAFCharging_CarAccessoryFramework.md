# `CAFCharging`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 12 properties, 16 instance methods, 2 class methods

## Properties

```
@property (T@"CAFChargingStatus",R,N) chargingStatusService;
@property (T@"CAFTargetChargingLevel",R,N) targetChargingLevelService;
@property (T@"CAFMinimumChargingLevel",R,N) minimumChargingLevelService;
@property (T@"CAFChargingTime",R,N) chargingTimeService;
@property (T@"CAFChargingSchedule",R,N) chargingScheduleService;
@property (T@"CAFChargingRate",R,N) chargingRateService;
@property (T@"CAFChargingStatus",R,N) chargingStatus;
@property (T@"CAFTargetChargingLevel",R,N) targetChargingLevel;
@property (T@"CAFMinimumChargingLevel",R,N) minimumChargingLevel;
@property (T@"CAFChargingTime",R,N) chargingTime;
@property (T@"CAFChargingSchedule",R,N) chargingSchedule;
@property (T@"CAFChargingRate",R,N) chargingRate;
```

## Class methods

```
+[CAFCharging accessoryIdentifier];
+[CAFCharging observerProtocol];
```

## Instance methods

```
-[CAFCharging removeObserver:];
-[CAFCharging addObserver:];
-[CAFCharging registerObserver:];
-[CAFCharging unregisterObserver:];
-[CAFCharging chargingTime];
-[CAFCharging chargingRate];
-[CAFCharging chargingRateService];
-[CAFCharging chargingSchedule];
-[CAFCharging chargingScheduleService];
-[CAFCharging chargingStatus];
-[CAFCharging chargingStatusService];
-[CAFCharging chargingTimeService];
-[CAFCharging minimumChargingLevel];
-[CAFCharging minimumChargingLevelService];
-[CAFCharging targetChargingLevel];
-[CAFCharging targetChargingLevelService];
```
