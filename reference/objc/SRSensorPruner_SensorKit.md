# `SRSensorPruner`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRDaemonNotificationDelegate`
- 9 instance variables, 12 properties, 26 instance methods, 6 class methods

## Instance variables

```
@"SRDatastore" _datastore;
@"SRDaemonNotification" _daemonNotification;
B _connectionDidInterrupt;
B _connectionDidInvalidate;
@"<SRSensorPrunerDelegate>" _delegate;
@"NSString" _sensor;
@"NSDictionary" _nextDatastoreFiles;
@"SRDevice" _device;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSString",C,V_sensor) sensor;
@property (T@"SRDatastore",R,&) datastore;
@property (T@"NSDictionary",&,V_nextDatastoreFiles) nextDatastoreFiles;
@property (TB,V_connectionDidInterrupt) connectionDidInterrupt;
@property (TB,V_connectionDidInvalidate) connectionDidInvalidate;
@property (T@"SRDevice",&,V_device) device;
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (T@"<SRSensorPrunerDelegate>",W,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRSensorPruner remoteInterface];
+[SRSensorPruner initialize];
+[SRSensorPruner clientInterface];
+[SRSensorPruner connectionToDaemon];
+[SRSensorPruner removeAllSamplesForAllSensorsWithCompletionHandler:];
+[SRSensorPruner removeAllSamplesForAllSensorsWithConnection:completionHandler:];
```

## Instance methods

```
-[SRSensorPruner setupConnection];
-[SRSensorPruner setDevice:];
-[SRSensorPruner device];
-[SRSensorPruner dealloc];
-[SRSensorPruner setDelegate:];
-[SRSensorPruner sensor];
-[SRSensorPruner connection];
-[SRSensorPruner delegate];
-[SRSensorPruner setConnection:];
-[SRSensorPruner datastore];
-[SRSensorPruner removeAllSamples];
-[SRSensorPruner setSensor:];
-[SRSensorPruner connectionDidInterrupt];
-[SRSensorPruner connectionDidInvalidate];
-[SRSensorPruner removeSamplesFrom:to:inSegment:];
-[SRSensorPruner continuePruneFrom:to:withDatastoreFiles:];
-[SRSensorPruner daemonNotificationDaemonDidStart:];
-[SRSensorPruner initWithSensor:device:];
-[SRSensorPruner initWithSensor:xpcConnection:daemonNotification:device:];
-[SRSensorPruner nextDatastoreFiles];
-[SRSensorPruner registerWithDaemonIfNeededWithReply:];
-[SRSensorPruner removeSamplesFrom:to:];
-[SRSensorPruner resetDatastoreFiles:];
-[SRSensorPruner setConnectionDidInterrupt:];
-[SRSensorPruner setConnectionDidInvalidate:];
-[SRSensorPruner setNextDatastoreFiles:];
```
