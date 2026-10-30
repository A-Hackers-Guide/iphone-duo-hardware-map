# `CSPowerStatusProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisOnAC) onAC;
@property (TB,R,N,GisConnectedToExternalChargingSource) connectedToExternalChargingSource;
@property (TB,R,N,GisConnectedToWirelessInternalCharger) connectedToWirelessInternalCharger;
@property (TB,R,N,GisConnectedToWirelessInternalChargingAccessory) connectedToWirelessInternalChargingAccessory;
@property (TB,R,N,GisConnectedToQiPower) connectedToQiPower;
```

## Instance methods

```
-[CSPowerStatusProviding isConnectedToQiPower];
-[CSPowerStatusProviding localizedBatteryDetailTextForBatteryLevel:];
-[CSPowerStatusProviding isConnectedToWirelessInternalChargingAccessory];
-[CSPowerStatusProviding internalBatteryDevice];
-[CSPowerStatusProviding isConnectedToWirelessInternalCharger];
-[CSPowerStatusProviding supportsDetailedBatteryMetrics];
-[CSPowerStatusProviding isOnAC];
-[CSPowerStatusProviding fetchFormattedChargeTimeEstimateWithCompletion:];
-[CSPowerStatusProviding isConnectedToExternalChargingSource];
```
