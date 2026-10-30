# `UWBSessionServerProtocol` (protocol)

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 44 instance methods, 0 class methods

## Instance methods

```
-[UWBSessionServerProtocol pause:];
-[UWBSessionServerProtocol activate:];
-[UWBSessionServerProtocol runWithConfiguration:reply:];
-[UWBSessionServerProtocol generateDiscoveryToken];
-[UWBSessionServerProtocol queryDeviceCapabilities:];
-[UWBSessionServerProtocol getInteractableDiscoveryTokens:];
-[UWBSessionServerProtocol _addObject:reply:];
-[UWBSessionServerProtocol _debugInjectFakeUUID:degrees:];
-[UWBSessionServerProtocol _processBluetoothSample:];
-[UWBSessionServerProtocol _processCarKeyEvent:reply:];
-[UWBSessionServerProtocol _processCombinedIQSamples:];
-[UWBSessionServerProtocol _processFindingEvent:reply:];
-[UWBSessionServerProtocol _processSystemEvent:reply:];
-[UWBSessionServerProtocol _provideTruthTag:];
-[UWBSessionServerProtocol _removeObject:reply:];
-[UWBSessionServerProtocol _setDebugURSK:transactionIdentifier:reply:];
-[UWBSessionServerProtocol _setURSKTTL:reply:];
-[UWBSessionServerProtocol _updateInterfaceAngle:forBodyWithUUID:];
-[UWBSessionServerProtocol _updateMotionState:forObjectWithToken:];
-[UWBSessionServerProtocol arSessionDidFailWithError:];
-[UWBSessionServerProtocol arSessionInterruptionEnded];
-[UWBSessionServerProtocol arSessionWasInterrupted];
-[UWBSessionServerProtocol arSessionWillRunWithInvalidConfiguration];
-[UWBSessionServerProtocol deleteURSKs:];
-[UWBSessionServerProtocol generateSOSBeaconDataForSubject:peerData:reply:];
-[UWBSessionServerProtocol getActivelyInteractingDiscoveryTokens:];
-[UWBSessionServerProtocol getLocalDevicePrintableState:];
-[UWBSessionServerProtocol getRangingAuthUWBInfo:];
-[UWBSessionServerProtocol isExtendedDistanceMeasurementAllowed:];
-[UWBSessionServerProtocol isPreciseRangingAllowed:];
-[UWBSessionServerProtocol isRangingLimitExceeded:];
-[UWBSessionServerProtocol notifySystemShutdownWithReason:reply:];
-[UWBSessionServerProtocol prefetchAcwgUrsk:];
-[UWBSessionServerProtocol processAcwgM1Msg:withSessionTriggerReason:];
-[UWBSessionServerProtocol processAcwgM3Msg:];
-[UWBSessionServerProtocol processAcwgRangingSessionResumeRequestMsg:withResumeTriggerReason:];
-[UWBSessionServerProtocol processBluetoothHostTimeSyncWithType:btcClockTicks:eventCounter:reply:];
-[UWBSessionServerProtocol processDCKMessage:reply:];
-[UWBSessionServerProtocol processUpdatedLockState:];
-[UWBSessionServerProtocol processVisionInput:];
-[UWBSessionServerProtocol setLocalDeviceCanInteract:withDiscoveryTokens:reply:];
-[UWBSessionServerProtocol setLocalDeviceDebugParameters:reply:];
-[UWBSessionServerProtocol setLocalDeviceInteractableDiscoveryTokens:reply:];
-[UWBSessionServerProtocol suspendAcwgRanging:withSuspendTriggerReason:];
```
