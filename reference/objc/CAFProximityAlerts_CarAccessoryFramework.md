# `CAFProximityAlerts`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"CAFProximityAlertCharacteristic",R,N) proximityAlertRearLeftCharacteristic;
@property (T@"CAFProximityAlertCharacteristic",R,N) proximityAlertRearRightCharacteristic;
@property (TC,R,N) proximityAlertRearLeft;
@property (TB,R,N) hasProximityAlertRearLeft;
@property (TC,R,N) proximityAlertRearRight;
@property (TB,R,N) hasProximityAlertRearRight;
```

## Class methods

```
+[CAFProximityAlerts serviceIdentifier];
+[CAFProximityAlerts observerProtocol];
```

## Instance methods

```
-[CAFProximityAlerts removeObserver:];
-[CAFProximityAlerts addObserver:];
-[CAFProximityAlerts registerObserver:];
-[CAFProximityAlerts name];
-[CAFProximityAlerts unregisterObserver:];
-[CAFProximityAlerts hasProximityAlertRearLeft];
-[CAFProximityAlerts hasProximityAlertRearRight];
-[CAFProximityAlerts proximityAlertRearLeft];
-[CAFProximityAlerts proximityAlertRearRight];
-[CAFProximityAlerts registeredForProximityAlertRearLeft];
-[CAFProximityAlerts registeredForProximityAlertRearRight];
-[CAFProximityAlerts _characteristicDidUpdate:fromGroupUpdate:];
-[CAFProximityAlerts proximityAlertRearLeftCharacteristic];
-[CAFProximityAlerts proximityAlertRearRightCharacteristic];
```
