# `CAFIndicators`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 6 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFTurnSignals",R,N) turnSignalsService;
@property (T@"CAFProximityAlerts",R,N) proximityAlertsService;
@property (T@"CAFLaneKeepAlerts",R,N) laneKeepAlertsService;
@property (T@"CAFTurnSignals",R,N) turnSignals;
@property (T@"CAFProximityAlerts",R,N) proximityAlerts;
@property (T@"CAFLaneKeepAlerts",R,N) laneKeepAlerts;
```

## Class methods

```
+[CAFIndicators accessoryIdentifier];
+[CAFIndicators observerProtocol];
```

## Instance methods

```
-[CAFIndicators removeObserver:];
-[CAFIndicators addObserver:];
-[CAFIndicators registerObserver:];
-[CAFIndicators unregisterObserver:];
-[CAFIndicators proximityAlerts];
-[CAFIndicators laneKeepAlerts];
-[CAFIndicators laneKeepAlertsService];
-[CAFIndicators proximityAlertsService];
-[CAFIndicators turnSignals];
-[CAFIndicators turnSignalsService];
```
