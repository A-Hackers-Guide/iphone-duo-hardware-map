# `PLXPCService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 11 instance variables, 11 properties, 39 instance methods, 10 class methods

## Instance variables

```
I _responderWaitTime;
@"NSObject<OS_xpc_object>" _xpcConnection;
@"NSMutableDictionary" _registeredListeners;
@"NSMutableDictionary" _registeredResponders;
@"NSDictionary" _permissionCache;
@"PLNSNotificationOperatorComposition" _registrationNotification;
@"NSArray" _clientIDs;
@"NSDictionary" _clientNames;
@"PLTimer" _resetPermissionsForClientsTimer;
@"PLNSNotificationOperatorComposition" _dailyTaskNotification;
@"PLSemaphore" _satelliteProcessSemaphore;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,V_xpcConnection) xpcConnection;
@property (T@"NSMutableDictionary",&,V_registeredListeners) registeredListeners;
@property (T@"NSMutableDictionary",&,V_registeredResponders) registeredResponders;
@property (T@"NSDictionary",&,V_permissionCache) permissionCache;
@property (T@"PLNSNotificationOperatorComposition",&,V_registrationNotification) registrationNotification;
@property (T@"NSArray",&,V_clientIDs) clientIDs;
@property (T@"NSDictionary",&,V_clientNames) clientNames;
@property (T@"PLTimer",&,V_resetPermissionsForClientsTimer) resetPermissionsForClientsTimer;
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (T@"PLSemaphore",&,V_satelliteProcessSemaphore) satelliteProcessSemaphore;
@property (TI,V_responderWaitTime) responderWaitTime;
```

## Class methods

```
+[PLXPCService entryEventIntervalDefinitions];
+[PLXPCService entryEventPointDefinitions];
+[PLXPCService load];
+[PLXPCService defaults];
+[PLXPCService entryAggregateDefinitions];
+[PLXPCService clientPermissions];
+[PLXPCService entryAggregateDefinitionXPCEvent];
+[PLXPCService entryEventIntervalDefinitionResponderEvent];
+[PLXPCService entryEventPointDefinitionClientLogging];
+[PLXPCService entryEventPointDefinitionClientLoggingDrops];
```

## Instance methods

```
-[PLXPCService dailyTasks];
-[PLXPCService init];
-[PLXPCService setXpcConnection:];
-[PLXPCService permissionCache];
-[PLXPCService initOperatorDependancies];
-[PLXPCService xpcConnection];
-[PLXPCService setDailyTaskNotification:];
-[PLXPCService setPermissionCache:];
-[PLXPCService dailyTaskNotification];
-[PLXPCService handlePeer:forEvent:];
-[PLXPCService setClientNames:];
-[PLXPCService resetPermissionsForClientsTimer];
-[PLXPCService clientIDs];
-[PLXPCService clientNames];
-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:];
-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:];
-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:];
-[PLXPCService handleSingleMessage:fromPeer:forEvent:];
-[PLXPCService initSatelliteProcessSemaphore];
-[PLXPCService logMessage:withPayload:];
-[PLXPCService permissionForClientID:withKey:withType:withProcessName:];
-[PLXPCService registeredListeners];
-[PLXPCService registeredOperatorFromDictionary:forMessage:];
-[PLXPCService registeredResponders];
-[PLXPCService registrationNotification];
-[PLXPCService resetPermissionsForClients];
-[PLXPCService respondToEvent:withResponse:];
-[PLXPCService responderWaitTime];
-[PLXPCService satelliteProcessSemaphore];
-[PLXPCService setClientIDs:];
-[PLXPCService setRegisteredListeners:];
-[PLXPCService setRegisteredResponders:];
-[PLXPCService setRegistrationNotification:];
-[PLXPCService setResetPermissionsForClientsTimer:];
-[PLXPCService setResponderWaitTime:];
-[PLXPCService setSatelliteProcessExit];
-[PLXPCService setSatelliteProcessExitWithTime:];
-[PLXPCService setSatelliteProcessSemaphore:];
-[PLXPCService stopPowerlogHelperd:];
```
