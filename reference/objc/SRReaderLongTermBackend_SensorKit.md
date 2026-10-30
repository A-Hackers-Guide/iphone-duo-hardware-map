# `SRReaderLongTermBackend`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRReaderStorageBackend`
- 3 instance variables, 5 properties, 12 instance methods, 5 class methods

## Instance variables

```
B _connectionDidInvalidate;
@"NSString" _sensor;
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
+[SRReaderLongTermBackend remoteInterface];
+[SRReaderLongTermBackend initialize];
+[SRReaderLongTermBackend new];
+[SRReaderLongTermBackend clientInterface];
+[SRReaderLongTermBackend connectionToEndpoint];
```

## Instance methods

```
-[SRReaderLongTermBackend setupConnection];
-[SRReaderLongTermBackend init];
-[SRReaderLongTermBackend dealloc];
-[SRReaderLongTermBackend connection];
-[SRReaderLongTermBackend setConnection:];
-[SRReaderLongTermBackend continueFetchRequest:samples:timestamp:cursor:fetchState:error:withCallback:];
-[SRReaderLongTermBackend fetch:withCallback:];
-[SRReaderLongTermBackend fetchDevices:reply:];
-[SRReaderLongTermBackend fetchReaderMetadata:reply:];
-[SRReaderLongTermBackend initWithSensor:xpcConnection:];
-[SRReaderLongTermBackend startRecording:reply:];
-[SRReaderLongTermBackend stopRecording:reply:];
```
