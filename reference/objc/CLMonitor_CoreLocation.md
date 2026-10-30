# `CLMonitor`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLIdentifiableClientProtocol`
- 11 instance variables, 11 properties, 36 instance methods, 7 class methods

## Instance variables

```
^v _locationdConnection;
@? _connectionFactory;
@"CLDispatchSilo" _silo;
@"CLConditionLedger" _conditionLedger;
@? _eventHandler;
@"NSString" identityToken;
@"NSData" storageToken;
@"CLLocationManager" manager;
@? weakClient;
@"NSString" _name;
@"NSString" _monitorName;
```

## Properties

```
@property (T@"NSString",R,N,V_monitorName) monitorName;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSArray",R,N) monitoredIdentifiers;
@property (T@"NSString",&,N,VidentityToken) identityToken;
@property (T@"NSData",&,N,VstorageToken) storageToken;
@property (T@"CLLocationManager",&,N,Vmanager) manager;
@property (T@?,W,N,VweakClient) weakClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CLMonitor requestMonitorWithConfiguration:completion:];
+[CLMonitor addMonitorName:];
+[CLMonitor _requestMonitorWithConfiguration:locationManager:completion:];
+[CLMonitor isMonitorNameInUse:];
+[CLMonitor removeMonitorName:];
+[CLMonitor requestWithConfiguration:locationManager:completion:];
+[CLMonitor sharedMonitorSet];
```

## Instance methods

```
-[CLMonitor createConnection];
-[CLMonitor storageToken];
-[CLMonitor setManager:];
-[CLMonitor dealloc];
-[CLMonitor setStorageToken:];
-[CLMonitor setWeakClient:];
-[CLMonitor manageConnection];
-[CLMonitor destroyConnection];
-[CLMonitor manager];
-[CLMonitor identityToken];
-[CLMonitor setIdentityToken:];
-[CLMonitor hash];
-[CLMonitor weakClient];
-[CLMonitor _setConnectionFactory:];
-[CLMonitor updateIdentityToken:withStorageToken:];
-[CLMonitor name];
-[CLMonitor _addConditionForMonitoring:identifier:options:assumedState:];
-[CLMonitor _getMonitoredIdentifiers];
-[CLMonitor _getMonitoringRecords];
-[CLMonitor _removeConditionFromMonitoringWithIdentifier:];
-[CLMonitor addConditionForMonitoring:identifier:];
-[CLMonitor addConditionForMonitoring:identifier:assumedState:];
-[CLMonitor addConditionForMonitoring:identifier:options:assumedState:];
-[CLMonitor addConstraintForMonitoring:identifier:];
-[CLMonitor addConstraintForMonitoring:identifier:assumedState:];
-[CLMonitor getMonitorConfiguration];
-[CLMonitor handleMessageMonitor:];
-[CLMonitor initWithLedgerName:path:onSilo:authIdentity:locationManager:handler:];
-[CLMonitor monitorName];
-[CLMonitor monitoredIdentifiers];
-[CLMonitor monitoringRecordForIdentifier:];
-[CLMonitor removeConditionFromMonitoringWithIdentifier:];
-[CLMonitor removeConstraintFromMonitoringWithIdentifier:];
-[CLMonitor setMonitoringEventHandler:];
-[CLMonitor updateEvent:forIdentifier:];
-[CLMonitor updateEventReceivedFromDaemon:];
```
