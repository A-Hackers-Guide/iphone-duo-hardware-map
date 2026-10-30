# `/System/Library/PrivateFrameworks/AccessoryFirmwareUpdate.framework/AccessoryFirmwareUpdate`

iOS 27.2 dyld shared cache image. Version `33.0.0.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags`
- `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 4 classes, 4 protocols, 34 methods, 4 properties

### Class pages

Every class and protocol, with its methods: [`NSObject`](../objc/NSObject_AccessoryFirmwareUpdate.protocol.md), [`OS_dispatch_source`](../objc/OS_dispatch_source_AccessoryFirmwareUpdate.protocol.md), [`OS_dispatch_source_timer`](../objc/OS_dispatch_source_timer_AccessoryFirmwareUpdate.protocol.md), [`UARPDeviceDelegateProtocol`](../objc/UARPDeviceDelegateProtocol_AccessoryFirmwareUpdate.protocol.md), [`_TtC23AccessoryFirmwareUpdate25AccessoryUarpDeviceBridge`](../objc/_TtC23AccessoryFirmwareUpdate25AccessoryUarpDeviceBridge_AccessoryFirmwareUpdate.md), [`_TtC23AccessoryFirmwareUpdate30AccessoryFirmwareUpdateManager`](../objc/_TtC23AccessoryFirmwareUpdate30AccessoryFirmwareUpdateManager_AccessoryFirmwareUpdate.md), [`_TtC23AccessoryFirmwareUpdate33AccessoryFirmwareUpdateSerializer`](../objc/_TtC23AccessoryFirmwareUpdate33AccessoryFirmwareUpdateSerializer_AccessoryFirmwareUpdate.md), [`_TtC23AccessoryFirmwareUpdate41AccessoryFirmwareUpdateDeviceStateMachine`](../objc/_TtC23AccessoryFirmwareUpdate41AccessoryFirmwareUpdateDeviceStateMachine_AccessoryFirmwareUpdate.md)

### Classes

`_TtC23AccessoryFirmwareUpdate25AccessoryUarpDeviceBridge`, `_TtC23AccessoryFirmwareUpdate30AccessoryFirmwareUpdateManager`, `_TtC23AccessoryFirmwareUpdate33AccessoryFirmwareUpdateSerializer`, `_TtC23AccessoryFirmwareUpdate41AccessoryFirmwareUpdateDeviceStateMachine`

### Protocols

`NSObject`, `OS_dispatch_source`, `OS_dispatch_source_timer`, `UARPDeviceDelegateProtocol`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Swift types (21)

`AccessoryFirmwareUpdate.AccessorFirmwareUpdateDelegateError`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateAccessory`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateDeviceState`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateDeviceStateMachine`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateDeviceStateMachineMonitorProtocol`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateDeviceType`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateEvent`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateEventData`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateManager:`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateManagerDelegateProtocol`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateManagerProtocol`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateSerializer:`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateSerializerClientProtocol`, `AccessoryFirmwareUpdate.AccessoryFirmwareUpdateStatusEvent`, `AccessoryFirmwareUpdate.AccessoryPairingStatus`, `AccessoryFirmwareUpdate.AccessoryUarpDeviceBridge`, `AccessoryFirmwareUpdate.AccessoryUarpDeviceBridgeProtocol`, `AccessoryFirmwareUpdate.AccessoryUarpDeviceDelegateProtocol`, `AccessoryFirmwareUpdate.AirTag`, `AccessoryFirmwareUpdate.StateTransition`, `conformance`

## Strings (108)

```
sendUarpMessageToAccessory
transportDisconnected
teardownTransport
maintenanceCompleted
FirmwareUpdateCompletionEvent
deviceBecameUnresponsive
deviceActiveFirmwareVersionRetrieved(activeFirmwareVersion:)
notifyOnConnectionStateChangeForDevice(isConnected:deviceUuid:error:)
notifyMaintenanceStateForAccessory(deviceUuid:isMaintained:)
receivedUarpMessageFromAccessory(deviceUuid:uarpMessage:)
deviceTransportNotNeeded(_:)
activeFirmwareVersion()
deviceReceivedUarpMessageFromTransport(uarpMessage:)
deviceAvailable()
disconnectedDueToInactivity
processMaintenanceEventForDevice(deviceUuid:)
createStateMachineForDevice(deviceUuid:deviceType:currentFirmwareVersion:)
updateStateMachineUponPairingStateChange(isPaired:deviceUuid:deviceType:currentFirmwareVersion:)
transportSetupSucceeded
completionReason
startMonitoringAccessoryForFirmwareUpdate(device:)
init(uarpDeviceBridge:accessoryFirmwareUpdateDelegate:queue:deviceUuid:deviceType:currentFirmwareVersion:availableFirmwareVersion:currentState:)
readFirmwareVersionsAndDecideNextSteps(completionReason:)
deviceTransportTeardown(_:)
updateFirmwareUpdateStartTime()
firmwareUpdateStatusEvent reported 
deviceFirmwareUpdateComplete(toVersion:completionReason:)
AccessoryFirmwareUpdate
processNexTopOfQueue()
completedProcessing(deviceUuid:)
deviceTransportSetupRequested(_:)
deviceTransportAvailable()
setupDevice(uuid:delegate:delegateQueue:)
pairingStateChanged to 
com.apple.AccessoryInteraction
failedWithError(deviceUuid:error:)
init()
Distribution
stateMachineTransitionedStates(deviceUuid:from:to:)
stopSerializing(deviceUuid:)
backstopTimerFired
transportSetupFailed
stopMonitoringAccessoryForFirmwareUpdate(deviceUuid:)
AccessoryFirmwareUpdate.AccessoryFirmwareUpdateManager
AccessoryFirmwareUpdate.AccessoryFirmwareUpdateSerializer
deviceUnresponsive(_:)
deviceUnavailable()
handleEvent(event:eventData:)
newFirmwareVersion: 
interruptedOrNotNeeded
serialize(deviceUuid:)
deviceSendUarpMessage(toTransport:uarpMessage:)
definestateTransitionTables()
firmwareVersionUpdated
receivedUarpMessageFromAccessory
AccessoryFirmwareUpdateManager: %s - isConnected %{bool}d, deviceUUID %s with error %s
AccessoryFirmwareUpdateManager: %s - received error for accessory that is not monitored with deviceUUID %s
AccessoryFirmwareUpdateManager: %s - received error for accessory that doesn't have an active statemachine with deviceUUID %s
AccessoryFirmwareUpdateManager: %s - failed with error: error %@ for device %s
AccessoryFirmwareUpdateSerializer %s No-op, device %s not currently being processed
AccessoryFirmwareUpdateSerializer %s queue after removing device %s
#AccessoryUarpDeviceBridge -%s - activeFirmwareVersion: %s, stagedFirmwareVersion: %s with completionReason: %s
#AccessoryUarpDeviceBridge -%s for %@
AccessoryFirmwareUpdateManager: %s - feature flag is not enabled
AccessoryFirmwareUpdateManager: %s - deviceUUID %s, relax the policy of needing a successful maintenance and instead use maintenance as a timer and kick off firmware update on every maintenance event
AccessoryFirmwareUpdateManager: %s - deviceUUID %s - transitioned from %s to %s - completed processing maintenance event
AccessoryFirmwareUpdateManager: %s - creating a state machine for an existing device %s
AccessoryFirmwareUpdateSerializer %s Device %s already in queue
#AccessoryUarpDeviceBridge -%s - only activeFirmwareVersion: %s retrieved -- reporting to delegate with completionReason: %s
#AccessoryUarpDeviceBridge -%s activeFirmwareVersionStr is invalid - %s
#AccessoryUarpDeviceBridge -%s for %s
AccessoryFirmwareUpdateManager: %s - deviceUUID %s
AccessoryFirmwareUpdateManager: %s - unable to find device to remove, deviceUUID %s
AccessoryFirmwareUpdateSerializer %s queue before removing device %s
AccessoryFirmwareUpdateSerializer %s Adding device %s to queue
#AccessoryInteraction: %s - activeFirmwareVersion: %s & currentFirmwareVersion: %s
AccessoryFirmwareUpdateManager: %s - deviceUUID %s, isMaintained %{bool}d
AccessoryFirmwareUpdateManager: %s - deviceUUID %s, uarpMessage length %ld
AccessoryFirmwareUpdateSerializer %s No more devices to serialize
AccessoryFirmwareUpdateSerializer %s Device %s currently not in queue
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s firmware update is ongoing, overriding previous firmware update start time
AccessoryFirmwareUpdateDeviceStateMachine: device %s - Starting backstop timer
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s - no state change, staying in: %s
AccessoryFirmwareUpdateSerializer %s Already in the middle of processing a device %s; ignoring current call 
#AccessoryUarpDeviceBridge -%s for %@ with %s
#AccessoryUarpDeviceBridge -%s
AccessoryFirmwareUpdateManager: %s - failed to update state machine of %s since no record found
AccessoryFirmwareUpdateDeviceStateMachine: %s
AccessoryFirmwareUpdateManager: %s - removing state machine of %s due to an unpairing event
#AccessoryUarpDeviceBridge -%s activeFirmwareVersionStr is nil
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s - no state change because no event handler found, staying in: %s
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s - handled event: %s new state: %s
#AccessoryInteraction: %s - invalid firmware update duration calculated
#AccessoryInteraction: %s - firmware version has not been updated
AccessoryFirmwareUpdateManager: %s - this device is not eligible for firmware update, deviceUUID %s
AccessoryFirmwareUpdateSerializer %s Stop serializing device %s to queue
AccessoryFirmwareUpdateManager: %s - failed to remove state machine of %s since no record found
AccessoryFirmwareUpdateDeviceStateMachine: device %s -  Stopping backstop timer
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s - defining state transition table for device %s
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s - No state transition found for state %s
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s: state changed from %s to %s
AccessoryFirmwareUpdateManager: %s - no state machine found for device %s upon connection state change
AccessoryFirmwareUpdateManager: %s - failed to process %s because we don't have a record of it
AccessoryFirmwareUpdateSerializer %s Processing next device %s
#AccessoryUarpDeviceBridge -%s - No active firmware version found - exiting with completionReason: %s
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s - No state transition found for event %s with state %s
AccessoryFirmwareUpdateDeviceStateMachine: device %s - %s - currentState: %s - event: %s with eventData: %s
#AccessoryInteraction: %s - firmware update start time has not been set
```
