# `SRReaderStorageBackend` (protocol)

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 7 instance methods, 3 class methods

## Properties

```
@property (T@"NSXPCConnection",R,N) connection;
```

## Class methods

```
+[SRReaderStorageBackend remoteInterface];
+[SRReaderStorageBackend clientInterface];
+[SRReaderStorageBackend connectionToEndpoint];
```

## Instance methods

```
-[SRReaderStorageBackend setupConnection];
-[SRReaderStorageBackend connection];
-[SRReaderStorageBackend fetch:withCallback:];
-[SRReaderStorageBackend fetchDevices:reply:];
-[SRReaderStorageBackend fetchReaderMetadata:reply:];
-[SRReaderStorageBackend startRecording:reply:];
-[SRReaderStorageBackend stopRecording:reply:];
```
