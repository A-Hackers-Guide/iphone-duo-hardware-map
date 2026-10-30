# `CAFLaneKeepAlerts`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"CAFLaneKeepAlertCharacteristic",R,N) laneKeepAlertLeftCharacteristic;
@property (T@"CAFLaneKeepAlertCharacteristic",R,N) laneKeepAlertRightCharacteristic;
@property (TC,R,N) laneKeepAlertLeft;
@property (TB,R,N) hasLaneKeepAlertLeft;
@property (TC,R,N) laneKeepAlertRight;
@property (TB,R,N) hasLaneKeepAlertRight;
```

## Class methods

```
+[CAFLaneKeepAlerts serviceIdentifier];
+[CAFLaneKeepAlerts observerProtocol];
```

## Instance methods

```
-[CAFLaneKeepAlerts removeObserver:];
-[CAFLaneKeepAlerts addObserver:];
-[CAFLaneKeepAlerts registerObserver:];
-[CAFLaneKeepAlerts name];
-[CAFLaneKeepAlerts unregisterObserver:];
-[CAFLaneKeepAlerts registeredForLaneKeepAlertRight];
-[CAFLaneKeepAlerts hasLaneKeepAlertLeft];
-[CAFLaneKeepAlerts hasLaneKeepAlertRight];
-[CAFLaneKeepAlerts laneKeepAlertLeft];
-[CAFLaneKeepAlerts laneKeepAlertRight];
-[CAFLaneKeepAlerts registeredForLaneKeepAlertLeft];
-[CAFLaneKeepAlerts laneKeepAlertLeftCharacteristic];
-[CAFLaneKeepAlerts _characteristicDidUpdate:fromGroupUpdate:];
-[CAFLaneKeepAlerts laneKeepAlertRightCharacteristic];
```
