# `ANDeviceDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 31 instance methods, 0 class methods

## Instance methods

```
-[ANDeviceDelegate requestDisconnectionForDevice:];
-[ANDeviceDelegate cancelConnectionTimeoutForPeripheral:];
-[ANDeviceDelegate device:checkForEchoOfOpcode:fromAck:];
-[ANDeviceDelegate device:didAcknowledgeCommandForTask:];
-[ANDeviceDelegate device:didCompleteTask:withCompletionCommand:];
-[ANDeviceDelegate device:didFailToCompleteTask:withError:andDisconnect:];
-[ANDeviceDelegate device:didPrepareForRangingWithError:withConnectionInterval:];
-[ANDeviceDelegate device:didReceiveGroupRelationStatus:andMainteanceStatus:];
-[ANDeviceDelegate device:didReceiveHawkeyeDataFragment:duringActiveTask:];
-[ANDeviceDelegate device:didReceiveInvalidDataWithError:];
-[ANDeviceDelegate device:didReceiveKeyRollIndex:];
-[ANDeviceDelegate device:didReceiveRangingResponse:withOpcode:];
-[ANDeviceDelegate device:didUpdateActivePeripheral:withError:];
-[ANDeviceDelegate didFailToConnectDevice:withError:];
-[ANDeviceDelegate didReceiveUarpMessage:fromDevice:];
-[ANDeviceDelegate didReceiveUarpMessageFromAccessory:fromDevice:];
-[ANDeviceDelegate didRetrievePersonalizationInfo:forDevice:error:];
-[ANDeviceDelegate didUpdateFirmwareForDevice:error:];
-[ANDeviceDelegate getLastCarScanTime];
-[ANDeviceDelegate notifyMaintenanceStateForAccessory:isMaintained:];
-[ANDeviceDelegate onConnectionStateChangeForDeviceWithUUID:fromState:toState:];
-[ANDeviceDelegate requestDiscoveryScan];
-[ANDeviceDelegate retryBeaconRecordFWVersionUpdateIfNeeded:];
-[ANDeviceDelegate sendConnectionMetrics:forDevice:];
-[ANDeviceDelegate sendConnectionMetricsForDevice:withDuration:];
-[ANDeviceDelegate sendFirmwareUpdateMetrics:forDevice:];
-[ANDeviceDelegate startMonitoringAirTagForFirmwareUpdate:];
-[ANDeviceDelegate startMonitoringDeviceForFirmwareUpdate:];
-[ANDeviceDelegate stopMonitoringAirTagForFirmwareUpdate:];
-[ANDeviceDelegate stopMonitoringDeviceForFirmwareUpdate:];
-[ANDeviceDelegate onObservationForDeviceWithUUID:type:];
```
