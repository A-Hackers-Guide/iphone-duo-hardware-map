# `SRReaderRecordingRequest`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRRequestRecording`
- 5 instance variables, 9 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSString" _sensor;
@"NSString" _bundleIdentifier;
@"NSString" _deviceIdentifier;
@"NSDictionary" _sensorConfiguration;
@"NSError" _configurationDecodeError;
```

## Properties

```
@property (T@"NSString",&,N,V_sensor) sensor;
@property (T@"NSString",&,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",&,N,V_deviceIdentifier) deviceIdentifier;
@property (T@"NSDictionary",&,N,V_sensorConfiguration) sensorConfiguration;
@property (T@"NSError",R,&,N,V_configurationDecodeError) configurationDecodeError;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRReaderRecordingRequest supportsSecureCoding];
```

## Instance methods

```
-[SRReaderRecordingRequest setDeviceIdentifier:];
-[SRReaderRecordingRequest dealloc];
-[SRReaderRecordingRequest bundleIdentifier];
-[SRReaderRecordingRequest deviceIdentifier];
-[SRReaderRecordingRequest sensor];
-[SRReaderRecordingRequest encodeWithCoder:];
-[SRReaderRecordingRequest description];
-[SRReaderRecordingRequest initWithCoder:];
-[SRReaderRecordingRequest setBundleIdentifier:];
-[SRReaderRecordingRequest setSensor:];
-[SRReaderRecordingRequest configurationDecodeError];
-[SRReaderRecordingRequest sensorConfiguration];
-[SRReaderRecordingRequest setSensorConfiguration:];
```
