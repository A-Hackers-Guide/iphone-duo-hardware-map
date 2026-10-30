# `CTSimHardwareInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSSecureCoding`
- 2 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _hardwareType;
q _simLocation;
```

## Properties

```
@property (Tq,N,V_hardwareType) hardwareType;
@property (Tq,N,V_simLocation) simLocation;
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
```

## Class methods

```
+[CTSimHardwareInfo supportsSecureCoding];
```

## Instance methods

```
-[CTSimHardwareInfo ct_shortDescription];
-[CTSimHardwareInfo hardwareType];
-[CTSimHardwareInfo setHardwareType:];
-[CTSimHardwareInfo ct_shortName];
-[CTSimHardwareInfo simLocation];
-[CTSimHardwareInfo encodeWithCoder:];
-[CTSimHardwareInfo description];
-[CTSimHardwareInfo initWithCoder:];
-[CTSimHardwareInfo setSimLocation:];
-[CTSimHardwareInfo initWithHardwareInfo:simLocation:];
```
