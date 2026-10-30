# `WFControlCenterStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFWiFiStateMonitor`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _chinaDevice;
@"UIViewController" _presenter;
@? _satelliteAlertCompletion;
```

## Properties

```
@property (TB,N,V_chinaDevice) chinaDevice;
@property (T@"UIViewController",&,N,V_presenter) presenter;
@property (T@?,C,N,V_satelliteAlertCompletion) satelliteAlertCompletion;
@property (T@"StateMonitor",&,D,N) stateMonitor;
```

## Instance methods

```
-[WFControlCenterStateMonitor performAction:];
-[WFControlCenterStateMonitor performActionFrom:withCSLSConnectionState:completion:];
-[WFControlCenterStateMonitor presenter];
-[WFControlCenterStateMonitor setPresenter:];
-[WFControlCenterStateMonitor performAction];
-[WFControlCenterStateMonitor _getSatelliteAlert:];
-[WFControlCenterStateMonitor _performAction:];
-[WFControlCenterStateMonitor chinaDevice];
-[WFControlCenterStateMonitor _promptMISDisable];
-[WFControlCenterStateMonitor _promptCellularOutankDisable];
-[WFControlCenterStateMonitor _isCellularOutrankingWiFi];
-[WFControlCenterStateMonitor _airplaneModeEnabled];
-[WFControlCenterStateMonitor _promptCarPlayDisable];
-[WFControlCenterStateMonitor satelliteAlertCompletion];
-[WFControlCenterStateMonitor setSatelliteAlertCompletion:];
-[WFControlCenterStateMonitor setChinaDevice:];
-[WFControlCenterStateMonitor _performActionWithStateMonitor:];
```
