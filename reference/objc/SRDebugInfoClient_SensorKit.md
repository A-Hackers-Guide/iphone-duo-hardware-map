# `SRDebugInfoClient`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 17 instance methods, 4 class methods

## Instance variables

```
B _connectionDidInterrupt;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (TB,V_connectionDidInterrupt) connectionDidInterrupt;
```

## Class methods

```
+[SRDebugInfoClient remoteInterface];
+[SRDebugInfoClient initialize];
+[SRDebugInfoClient clientInterface];
+[SRDebugInfoClient connectionToDaemon];
```

## Instance methods

```
-[SRDebugInfoClient setupConnection];
-[SRDebugInfoClient init];
-[SRDebugInfoClient dealloc];
-[SRDebugInfoClient initWithConnection:];
-[SRDebugInfoClient invalidate];
-[SRDebugInfoClient connection];
-[SRDebugInfoClient setConnection:];
-[SRDebugInfoClient connectionDidInterrupt];
-[SRDebugInfoClient datastoreListingWithReply:];
-[SRDebugInfoClient dumpClientsWithReply:];
-[SRDebugInfoClient dumpConfigurationsWithReply:];
-[SRDebugInfoClient dumpDefaultsWithReply:];
-[SRDebugInfoClient dumpStateCacheWithReply:];
-[SRDebugInfoClient fetchDeviceInformationForDeviceIdentifiers:reply:];
-[SRDebugInfoClient fetchEligibilityStatusForBundleIdentifier:sensor:reply:];
-[SRDebugInfoClient listClientsWithReply:];
-[SRDebugInfoClient setConnectionDidInterrupt:];
```
