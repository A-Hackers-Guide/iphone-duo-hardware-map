# `SRReaderSensorKitBackend`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRReaderStorageBackend`
- 6 instance variables, 5 properties, 13 instance methods, 5 class methods

## Instance variables

```
@"SRDatastore" _datastore;
@"NSDictionary" _deviceDetails;
B _connectionDidInvalidate;
@"NSString" _sensor;
@"NSDictionary" _nextDatastoreFiles;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRReaderSensorKitBackend remoteInterface];
+[SRReaderSensorKitBackend initialize];
+[SRReaderSensorKitBackend new];
+[SRReaderSensorKitBackend clientInterface];
+[SRReaderSensorKitBackend connectionToEndpoint];
```

## Instance methods

```
-[SRReaderSensorKitBackend setupConnection];
-[SRReaderSensorKitBackend init];
-[SRReaderSensorKitBackend dealloc];
-[SRReaderSensorKitBackend connection];
-[SRReaderSensorKitBackend setConnection:];
-[SRReaderSensorKitBackend datastore];
-[SRReaderSensorKitBackend fetch:withCallback:];
-[SRReaderSensorKitBackend fetchDevices:reply:];
-[SRReaderSensorKitBackend fetchReaderMetadata:reply:];
-[SRReaderSensorKitBackend initWithSensor:xpcConnection:];
-[SRReaderSensorKitBackend resetDatastoreFiles:];
-[SRReaderSensorKitBackend startRecording:reply:];
-[SRReaderSensorKitBackend stopRecording:reply:];
```
