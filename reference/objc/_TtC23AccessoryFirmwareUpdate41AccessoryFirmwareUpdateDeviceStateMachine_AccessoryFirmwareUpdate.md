# `_TtC23AccessoryFirmwareUpdate41AccessoryFirmwareUpdateDeviceStateMachine`

- Image: [`/System/Library/PrivateFrameworks/AccessoryFirmwareUpdate.framework/AccessoryFirmwareUpdate`](../userland/System__Library__PrivateFrameworks__AccessoryFirmwareUpdate.framework__AccessoryFirmwareUpdate.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 15 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
_$sSd nearbyStateBackstopTimeoutSeconds;
DispatchQueue queue;
Foundation.UUID deviceUuid;
AccessoryFirmwareUpdate.AccessoryFirmwareUpdateDeviceType deviceType;
AccessoryFirmwareUpdate.AccessoryFirmwareUpdateDeviceState currentState;
_$sSD -> AccessoryFirmwareUpdate.AccessoryFirmwareUpdateDeviceState _$sSD -> AccessoryFirmwareUpdate.AccessoryFirmwareUpdateEvent AccessoryFirmwareUpdate.StateTransition stateTransitionTables;
_$sSS currentFirmwareVersion;
_$sSSSg availableFirmwareVersion;
Swift.Bool isConnected;
dyld_v1  arm64e ? backstopTimer;
AccessoryFirmwareUpdate.AccessoryUarpDeviceBridgeProtocol ? uarpDeviceBridge;
AccessoryFirmwareUpdate.AccessoryFirmwareUpdateManagerDelegateProtocol ? accessoryFirmwareUpdateDelegate;
AccessoryFirmwareUpdate.AccessoryFirmwareUpdateDeviceStateMachineMonitorProtocol ? stateMachineMonitor;
Swift.Error ? accessoryConnectionStateUpdateError;
_$sSd firmwareUpdateStartTime;
```
