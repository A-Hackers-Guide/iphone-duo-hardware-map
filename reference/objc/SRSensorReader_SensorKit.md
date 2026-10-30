# `SRSensorReader`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRAuthorizationClientDelegate`
- 13 instance variables, 18 properties, 56 instance methods, 9 class methods

## Instance variables

```
d _serviceStartTime;
d _earliestEligibleTime;
Ai _authState;
B _bypassHoldingPeriod;
@"<SRSensorReaderDelegate>" _delegate;
@"NSString" _canonicalSensor;
@"SRAuthorizationClient" _authorizationClient;
@"NSString" _bundleId;
@"NSDate" __lastModifiedAuthorizationTime;
@"NSString" _requestedSensor;
@"<SRReaderStorageBackend>" _datastoreBackend;
# _sampleClass;
# _exportingSampleClass;
```

## Properties

```
@property (T@"NSString",C,V_canonicalSensor) canonicalSensor;
@property (T@"SRAuthorizationClient",&,V_authorizationClient) authorizationClient;
@property (T@"NSString",C,V_bundleId) bundleId;
@property (T@"NSDate",&,V__lastModifiedAuthorizationTime) _lastModifiedAuthorizationTime;
@property (T@"NSString",&,V_requestedSensor) requestedSensor;
@property (T@"<SRReaderStorageBackend>",&,N,V_datastoreBackend) datastoreBackend;
@property (T#,R,N,V_sampleClass) sampleClass;
@property (T#,R,N,V_exportingSampleClass) exportingSampleClass;
@property (TB,N,V_bypassHoldingPeriod) bypassHoldingPeriod;
@property (Td,R,N) earliestEligibleTime;
@property (Td,R,N) serviceStartTime;
@property (Tq,R) authorizationStatus;
@property (T@"NSString",R,C) sensor;
@property (T@"<SRSensorReaderDelegate>",W,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRSensorReader initialize];
+[SRSensorReader new];
+[SRSensorReader _requestAuthorizationMigrationForSensors:completion:];
+[SRSensorReader authorizationRequestStatusForBundle:sensors:completionHandler:];
+[SRSensorReader createExportDataForServices:withCompletionHandler:];
+[SRSensorReader createExportDataWithCompletionHandler:];
+[SRSensorReader requestAuthorizationForBundle:sensors:legacyPromptErrorBehavior:withCompletionHandler:];
+[SRSensorReader requestAuthorizationForBundle:sensors:withCompletionHandler:];
+[SRSensorReader requestAuthorizationForSensors:completion:];
```

## Instance methods

```
-[SRSensorReader authorizationStatus];
-[SRSensorReader startRecording];
-[SRSensorReader stopRecording];
-[SRSensorReader init];
-[SRSensorReader dealloc];
-[SRSensorReader setBundleId:];
-[SRSensorReader setAuthorizationStatus:];
-[SRSensorReader setDelegate:];
-[SRSensorReader sensor];
-[SRSensorReader bundleId];
-[SRSensorReader delegate];
-[SRSensorReader fetch:];
-[SRSensorReader isAuthorized];
-[SRSensorReader initWithSensor:];
-[SRSensorReader requestedSensor];
-[SRSensorReader canonicalSensor];
-[SRSensorReader fetchingRequest:didFetchResult:];
-[SRSensorReader _lastModifiedAuthorizationTime];
-[SRSensorReader _startRecordingWithSensorConfiguration:completionHandler:];
-[SRSensorReader _updateAuthorizationStatusWithAuthorizedServices:deniedServices:dataCollectionEnabled:onboardingCompleted:lastModifiedTimes:forBundleIdentifier:];
-[SRSensorReader _updateAuthorizationStatusWithAuthorizedServices:deniedServices:dataCollectionEnabled:onboardingCompleted:lastModifiedTimes:forBundleIdentifier:previousAuthorizationStatus:];
-[SRSensorReader authorizationClient];
-[SRSensorReader authorizedServicesDidChange:deniedServices:dataCollectionEnabled:onboardingCompleted:lastModifiedTimes:forBundleIdentifier:];
-[SRSensorReader bypassHoldingPeriod];
-[SRSensorReader createExportDataWithCompletionHandler:];
-[SRSensorReader datastoreBackend];
-[SRSensorReader didChangeAuthorizationStatus:];
-[SRSensorReader didCompleteFetch:];
-[SRSensorReader didFetchDevices:];
-[SRSensorReader earliestEligibleTime];
-[SRSensorReader exportingSampleClass];
-[SRSensorReader fetch:fetchResultHandler:fetchDidCompleteHandler:fetchFailedWithErrorHandler:];
-[SRSensorReader fetchDevices];
-[SRSensorReader fetchDevices:];
-[SRSensorReader fetchDevicesDidFailWithError:];
-[SRSensorReader fetchDevicesWithRetryAttempt:];
-[SRSensorReader fetchReaderMetadata];
-[SRSensorReader fetchingRequest:failedWithError:];
-[SRSensorReader initWithSensor:bundle:];
-[SRSensorReader initWithSensor:sensorDescription:datastoreBackend:authorizationClient:bundleId:];
-[SRSensorReader sampleClass];
-[SRSensorReader sensorReaderDidStopRecording];
-[SRSensorReader sensorReaderWillStartRecording];
-[SRSensorReader serviceStartTime];
-[SRSensorReader setAuthorizationClient:];
-[SRSensorReader setBypassHoldingPeriod:];
-[SRSensorReader setCanonicalSensor:];
-[SRSensorReader setDatastoreBackend:];
-[SRSensorReader setExportingSampleFromDescription:];
-[SRSensorReader setRequestedSensor:];
-[SRSensorReader setSampleClassFromDescription:];
-[SRSensorReader set_lastModifiedAuthorizationTime:];
-[SRSensorReader startRecordingFailedWithError:];
-[SRSensorReader startRecordingWithCompletionHandler:];
-[SRSensorReader stopRecordingFailedWithError:];
-[SRSensorReader stopRecordingWithCompletionHandler:];
```
