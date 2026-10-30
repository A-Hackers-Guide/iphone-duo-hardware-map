# `MTLTargetDeviceArchitecture`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
I _cpuType;
I _subType;
{MTLTargetDeviceArchVersion="major"S"minor"C"update"C} _version;
Q _driverVersion;
```

## Properties

```
@property (TI,N,V_cpuType) cpuType;
@property (TI,N,V_subType) subType;
@property (T{MTLTargetDeviceArchVersion=SCC},N,V_version) version;
@property (TI,R) versionCombined;
@property (TQ,N,V_driverVersion) driverVersion;
```

## Instance methods

```
-[MTLTargetDeviceArchitecture setDriverVersion:];
-[MTLTargetDeviceArchitecture init];
-[MTLTargetDeviceArchitecture versionCombined];
-[MTLTargetDeviceArchitecture version];
-[MTLTargetDeviceArchitecture driverVersion];
-[MTLTargetDeviceArchitecture setSubType:];
-[MTLTargetDeviceArchitecture setCpuType:];
-[MTLTargetDeviceArchitecture subType];
-[MTLTargetDeviceArchitecture cpuType];
-[MTLTargetDeviceArchitecture setVersion:];
```
