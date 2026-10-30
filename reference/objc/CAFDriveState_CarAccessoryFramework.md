# `CAFDriveState`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 6 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFTransmissionStatus",R,N) transmissionStatusService;
@property (T@"CAFGearRecommendation",R,N) gearRecommendationService;
@property (T@"CAFDriveMode",R,N) driveModeService;
@property (T@"CAFTransmissionStatus",R,N) transmissionStatus;
@property (T@"CAFGearRecommendation",R,N) gearRecommendation;
@property (T@"CAFDriveMode",R,N) driveMode;
```

## Class methods

```
+[CAFDriveState accessoryIdentifier];
+[CAFDriveState observerProtocol];
```

## Instance methods

```
-[CAFDriveState removeObserver:];
-[CAFDriveState addObserver:];
-[CAFDriveState registerObserver:];
-[CAFDriveState unregisterObserver:];
-[CAFDriveState driveMode];
-[CAFDriveState driveModeService];
-[CAFDriveState gearRecommendation];
-[CAFDriveState gearRecommendationService];
-[CAFDriveState transmissionStatus];
-[CAFDriveState transmissionStatusService];
```
