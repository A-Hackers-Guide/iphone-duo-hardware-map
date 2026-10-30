# `CtrClient`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 57 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<CtrXPC::Client>="__ptr_"^{Client}"__cntrl_"^{__shared_weak_count}} CtrXPCClientPtr;
```

## Instance methods

```
-[CtrClient setChannel:];
-[CtrClient reset:];
-[CtrClient join:];
-[CtrClient removeService:];
-[CtrClient init:];
-[CtrClient resume];
-[CtrClient leave];
-[CtrClient addService:];
-[CtrClient scan:];
-[CtrClient createClient:];
-[CtrClient captureTriggerData:triggerId:accessoryInfoList:completionHandler:];
-[CtrClient getProperty:output:];
-[CtrClient provideExtendedMACAddress:completion:];
-[CtrClient setClientEventsOff];
-[CtrClient setClientEventsOn];
-[CtrClient setEventHandler:EventBlock:dqueue:];
-[CtrClient startFWUpdate:isWedDevice:completion:];
-[CtrClient startPairingForExtendedMACAddress:isWedDevice:completion:];
-[CtrClient stopFWUpdate:];
-[CtrClient stopPairing:];
-[CtrClient threadStart:geoAvailable:isPrimaryUser:waitForSync:completion:];
-[CtrClient threadStopWithCompletion:];
-[CtrClient updatePrimaryResident:isPrimaryResidentThreadCapable:primaryResidentInfo:];
-[CtrClient commissionOrFormNetwork:output:];
-[CtrClient joiner:];
-[CtrClient addPrefix:];
-[CtrClient attachToNetwork:];
-[CtrClient attachToNetwork:output:];
-[CtrClient form:];
-[CtrClient generatePSKc:output:];
-[CtrClient generateThreadDiagnosticsMonitorLogs];
-[CtrClient getThreadMeshWirelessInsights:completionHandler:];
-[CtrClient parseAsymmetricLinksResult:];
-[CtrClient parseBottleneckNodesResult:];
-[CtrClient parseCriticalNodesResult:];
-[CtrClient parseDataArray:key:];
-[CtrClient parseExtendedAddress:key:];
-[CtrClient parseResilienceResult:];
-[CtrClient parseString:key:];
-[CtrClient parseStringArray:key:];
-[CtrClient parseUnreachableNodesResult:];
-[CtrClient parseUnreliableNodesResult:];
-[CtrClient parseUnsupportedEnhancedDiagnosticsResult:];
-[CtrClient removePrefix:];
-[CtrClient sendData:data:data_length:];
-[CtrClient sendNwDiagReqGet:];
-[CtrClient setProperty:prperty_val:];
-[CtrClient threadLeave];
-[CtrClient threadLeaveWithCompletion:];
-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:];
-[CtrClient threadStart:activeOperationalDataSet:geoAvailable:routerMode:eMAC:waitForSync:completion:];
-[CtrClient threadStart:activeOperationalDataSet:geoAvailable:waitForSync:completion:];
-[CtrClient threadStart:outUniqueId:];
-[CtrClient threadStart:outUniqueId:waitForSync:];
-[CtrClient threadStart:outputUniqueId:];
-[CtrClient updateAccData:];
-[CtrClient updateHomeThreadInfo:];
```
