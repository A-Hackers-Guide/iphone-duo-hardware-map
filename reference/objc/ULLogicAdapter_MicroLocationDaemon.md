# `ULLogicAdapter`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULDiagnosticsProvider`, `ULLogicAdapterServiceHandlingInterface`, `ULLogicAdapterDiagnosticsHandlingInterface`, `ULLogicAdapterLegacyServiceHandlingInterface`, `ULLogicAdapterTemporaryMapHandlingInterface`, `ULRapportMonitorHandlingInterface`, `ULDataProtectionMonitorHandlingInterface`
- 4 instance variables, 11 properties, 72 instance methods, 1 class methods

## Instance variables

```
{unique_ptr<ULLogicAdapterImpl, std::default_delete<ULLogicAdapterImpl>>=""{?="__ptr_"^{ULLogicAdapterImpl}}} logicAdapterImpl;
@"ULEnvironment" _environment;
@"_TtC19MicroLocationDaemon19ULPeripheralControl" _peripheralControl;
@"<_TtP19MicroLocationDaemon31ReconstructionDataStoreManaging_>" _reconstructionDataStoreManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_TtC19MicroLocationDaemon19ULPeripheralControl",&,N,V_peripheralControl) peripheralControl;
@property (T@"<_TtP19MicroLocationDaemon31ReconstructionDataStoreManaging_>",&,N,V_reconstructionDataStoreManager) reconstructionDataStoreManager;
@property (T@"ULEnvironment",&,N,V_environment) environment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULLogicAdapter _newULServiceDescriptorFromInternalDescriptor:];
```

## Instance methods

```
-[ULLogicAdapter peripheralControl];
-[ULLogicAdapter _stop];
-[ULLogicAdapter removePendingConnectionRequestsByConnectionToken:];
-[ULLogicAdapter setEnvironment:];
-[ULLogicAdapter _routineStateAnalyzerExecute:];
-[ULLogicAdapter purgeMicroLocationData];
-[ULLogicAdapter diagnosticInfo];
-[ULLogicAdapter _exportiCloudBackupExecute:];
-[ULLogicAdapter _handleULBuddyMonitorEventBuddyComplete:];
-[ULLogicAdapter _start];
-[ULLogicAdapter removeAllModelsOfType:reply:];
-[ULLogicAdapter init];
-[ULLogicAdapter _handleULPrivacyMonitorEventLocationServices:];
-[ULLogicAdapter _handleULInternalNotifyMonitorEventLocalize:];
-[ULLogicAdapter requestPredictionForConnectionToken:clientIdentifier:requestIdentifier:];
-[ULLogicAdapter requestMapReconstructionForConnectionToken:requestIdentifier:];
-[ULLogicAdapter _maintenanceExecute:];
-[ULLogicAdapter requestObservationForConnectionToken:clientIdentifier:requestIdentifier:];
-[ULLogicAdapter _stopMonitoringEvents];
-[ULLogicAdapter requestMicroLocationRecordingScanWithAdditionalInformation:clientId:];
-[ULLogicAdapter _handleULBatteryModeMonitorEventLowPowerMode:];
-[ULLogicAdapter dealloc];
-[ULLogicAdapter exportDatabase];
-[ULLogicAdapter start];
-[ULLogicAdapter startRapportSession];
-[ULLogicAdapter _registerOnDatabaseValidNotification];
-[ULLogicAdapter requestCurrentMicroLocationWithAdditionalInformation:clientId:];
-[ULLogicAdapter _handleULDataProtectionMonitorEventDataAvailable:];
-[ULLogicAdapter _wifiAnalyticsExecute:];
-[ULLogicAdapter _registerOrUnregisterForActivities:];
-[ULLogicAdapter exportVisualLoggerDataWithCompletion:];
-[ULLogicAdapter purgeDatabase];
-[ULLogicAdapter visualLoggerAddDestinationWithHost:];
-[ULLogicAdapter addAnchorForConnectionToken:anchor:];
-[ULLogicAdapter peripheralDebugTask:reply:];
-[ULLogicAdapter _handleULInternalNotifyMonitorEventSettingsRefrsh:];
-[ULLogicAdapter imageFeaturesDebugWithTask:additionalInformation:reply:];
-[ULLogicAdapter _handleULDisplayMonitorEventDisplayState_OSX:];
-[ULLogicAdapter queryServicesForClient:];
-[ULLogicAdapter runWithConfiguration:serviceIdentifier:legacyServiceIdentifier:clientIdentifier:connectionToken:requestIdentifier:];
-[ULLogicAdapter reconstructionDataStoreManager];
-[ULLogicAdapter requestModelLearningForConnectionToken:requestIdentifier:];
-[ULLogicAdapter disconnectWithConnectionToken:clientIdentifier:requestIdentifier:];
-[ULLogicAdapter updateHomeKitUserInteractionAnchorForConnectionToken:anchor:];
-[ULLogicAdapter getMicroLocationInternalVersion];
-[ULLogicAdapter _handleULDisplayMonitorEventDisplayState:];
-[ULLogicAdapter setPeripheralControl:];
-[ULLogicAdapter _registerOrUnregisterForBackgroundTaskWithRequest:withSelector:launchCondition:isRegister:];
-[ULLogicAdapter deleteServiceWithIdentifier:clientIdentifier:];
-[ULLogicAdapter removeCustomLoiWithIdentifier:forConnectionToken:];
-[ULLogicAdapter _learnExecute:];
-[ULLogicAdapter _handleULInternalNotifyMonitorEventPurge:];
-[ULLogicAdapter _handleULBluetoothMonitorEventPowerOn:];
-[ULLogicAdapter setDependencies:peripheralControl:reconstructionDataStoreManager:environment:];
-[ULLogicAdapter _handleULRapportMonitorEventDeviceFound:];
-[ULLogicAdapter _startMonitoringEvents];
-[ULLogicAdapter isDataAvailable];
-[ULLogicAdapter stopRapportSession];
-[ULLogicAdapter setReconstructionDataStoreManager:];
-[ULLogicAdapter clearAllLabelsForContextLayer:reply:];
-[ULLogicAdapter createCustomLoiAtCurrentLocationForConnectionToken:withConfiguration:];
-[ULLogicAdapter configureVisualLoggerStreamWithIdentifier:networkHost:networkPort:];
-[ULLogicAdapter _handleULInternalNotifyMonitorEventRecord:];
-[ULLogicAdapter _handleULSleepWakeMonitorEvent:];
-[ULLogicAdapter _mapReconstructionExecute:];
-[ULLogicAdapter createServiceWithServiceType:locationTypes:clientId:];
-[ULLogicAdapter _handleULAirplaneModeMonitorEventAirplaneMode:];
-[ULLogicAdapter addAnchorForConnectionToken:anchor:betweenStartDate:andEndDate:];
-[ULLogicAdapter environment];
-[ULLogicAdapter _analyticsExecute:];
-[ULLogicAdapter injectNPDROdometryStateWithDeltaX:deltaY:deltaZ:quaternionX:quaternionY:quaternionZ:quaternionW:northAlignmentAngle:reply:];
-[ULLogicAdapter _handleULBatteryModeMonitorEventUnlimitedPower:];
```
