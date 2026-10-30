# `SRReaderRequest`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRRequestReading`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _sensor;
@"NSString" _bundleIdentifier;
@"NSString" _deviceIdentifier;
```

## Properties

```
@property (T@"NSString",&,N,V_sensor) sensor;
@property (T@"NSString",&,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",&,N,V_deviceIdentifier) deviceIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRReaderRequest supportsSecureCoding];
```

## Instance methods

```
-[SRReaderRequest setDeviceIdentifier:];
-[SRReaderRequest dealloc];
-[SRReaderRequest bundleIdentifier];
-[SRReaderRequest deviceIdentifier];
-[SRReaderRequest sensor];
-[SRReaderRequest encodeWithCoder:];
-[SRReaderRequest description];
-[SRReaderRequest initWithCoder:];
-[SRReaderRequest setBundleIdentifier:];
-[SRReaderRequest setSensor:];
```
