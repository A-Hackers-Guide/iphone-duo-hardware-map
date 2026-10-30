# `SRAuthorizationStore`

- Image: [`/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting`](../userland/System__Library__PrivateFrameworks__SensorKitWriting.framework__SensorKitWriting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 8 properties, 33 instance methods, 3 class methods

## Instance variables

```
i _notifyToken;
B _fetchAuthorizationTimes;
B _sensorKitActive;
@"NSHashTable" _readerAuthorizationDelegates;
@"NSHashTable" _writerAuthorizationDelegates;
@"<SRTCCStore>" _tccStore;
@"NSDictionary" _readerAuthorizationValues;
@"NSDictionary" _readerLastModifiedAuthorizationTimes;
@"NSDictionary" _writerAuthorizationValues;
@"NSObject<OS_dispatch_queue>" _updateQueue;
@"NSDictionary" _readerAuthorizationGroups;
@"NSDictionary" _writerAuthorizationGroups;
@"NSSet" _sensors;
```

## Properties

```
@property (T@"NSDictionary",C,V_readerAuthorizationValues) readerAuthorizationValues;
@property (T@"NSDictionary",C,V_readerLastModifiedAuthorizationTimes) readerLastModifiedAuthorizationTimes;
@property (T@"NSDictionary",C,V_writerAuthorizationValues) writerAuthorizationValues;
@property (TB,V_sensorKitActive) sensorKitActive;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_updateQueue) updateQueue;
@property (T@"NSDictionary",C,V_readerAuthorizationGroups) readerAuthorizationGroups;
@property (T@"NSDictionary",C,V_writerAuthorizationGroups) writerAuthorizationGroups;
@property (T@"NSSet",&,V_sensors) sensors;
```

## Class methods

```
+[SRAuthorizationStore initialize];
+[SRAuthorizationStore allSensorsStore];
+[SRAuthorizationStore sharedAuthorizationStoreForSensors:];
```

## Instance methods

```
-[SRAuthorizationStore dealloc];
-[SRAuthorizationStore updateQueue];
-[SRAuthorizationStore setUpdateQueue:];
-[SRAuthorizationStore addReaderAuthorizationDelegate:];
-[SRAuthorizationStore addWriterAuthorizationDelegate:];
-[SRAuthorizationStore sensorKitActive];
-[SRAuthorizationStore sensors];
-[SRAuthorizationStore checkAccessForService:auditToken:];
-[SRAuthorizationStore initWithSensors:];
-[SRAuthorizationStore initWithSensors:withAuthorizationTimes:];
-[SRAuthorizationStore listenForAuthorizationUpdates:];
-[SRAuthorizationStore readerAuthorizationBundleIdValues];
-[SRAuthorizationStore readerAuthorizationGroups];
-[SRAuthorizationStore readerAuthorizationValues];
-[SRAuthorizationStore readerLastModifiedAuthorizationTimes];
-[SRAuthorizationStore removeReaderAuthorizationDelegate:];
-[SRAuthorizationStore removeWriterAuthorizationDelegate:];
-[SRAuthorizationStore resetAllAuthorizations];
-[SRAuthorizationStore resetAllAuthorizationsForBundleId:];
-[SRAuthorizationStore resetAuthorizationForService:bundleId:];
-[SRAuthorizationStore sensorHasReaderAuthorization:];
-[SRAuthorizationStore sensorHasReaderAuthorization:forBundleId:];
-[SRAuthorizationStore setAuthorizationForBundleId:service:value:];
-[SRAuthorizationStore setAuthorizationForBundleId:service:value:setOverride:];
-[SRAuthorizationStore setReaderAuthorizationGroups:];
-[SRAuthorizationStore setReaderAuthorizationValues:];
-[SRAuthorizationStore setReaderLastModifiedAuthorizationTimes:];
-[SRAuthorizationStore setSensorKitActive:];
-[SRAuthorizationStore setSensors:];
-[SRAuthorizationStore setWriterAuthorizationGroups:];
-[SRAuthorizationStore setWriterAuthorizationValues:];
-[SRAuthorizationStore writerAuthorizationGroups];
-[SRAuthorizationStore writerAuthorizationValues];
```
