# `SRSensorWriterClient`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSensorKitServiceClientWriting`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"SRSensorWriter" _writer;
```

## Properties

```
@property (T@"SRSensorWriter",W,V_writer) writer;
```

## Class methods

```
+[SRSensorWriterClient sensorWriterClientWithWriter:];
```

## Instance methods

```
-[SRSensorWriterClient writer];
-[SRSensorWriterClient setWriter:];
-[SRSensorWriterClient initWithWriter:];
-[SRSensorWriterClient resetDatastoreFiles:];
-[SRSensorWriterClient setMonitoring:withRequestedConfigurations:];
```
