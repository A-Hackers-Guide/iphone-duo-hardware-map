# `DYMTLDeviceProfile`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DYCapturableObject`, `DYGraphicsAPIInfo`, `NSSecureCoding`, `NSCopying`
- 6 instance variables, 13 properties, 16 instance methods, 1 class methods

## Instance variables

```
Q _streamRef;
@"NSArray" _supportedFeatureSets;
@"NSArray" _supportedGPUFamilies;
@"NSDictionary" _defaultSamplePositions;
@"NSString" _name;
@"NSNumber" _registryID;
```

## Properties

```
@property (TQ,R,N,V_streamRef) streamRef;
@property (T@"NSArray",R,N,V_supportedFeatureSets) supportedFeatureSets;
@property (T@"NSArray",R,N,V_supportedGPUFamilies) supportedGPUFamilies;
@property (T@"NSDictionary",R,N,V_defaultSamplePositions) defaultSamplePositions;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSNumber",R,N,V_registryID) registryID;
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N) displayName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",?,R,N) descriptionForBugReport;
```

## Class methods

```
+[DYMTLDeviceProfile supportsSecureCoding];
```

## Instance methods

```
-[DYMTLDeviceProfile initWithDevice:];
-[DYMTLDeviceProfile displayName];
-[DYMTLDeviceProfile encodeWithCoder:];
-[DYMTLDeviceProfile description];
-[DYMTLDeviceProfile initWithCoder:];
-[DYMTLDeviceProfile registryID];
-[DYMTLDeviceProfile copyWithZone:];
-[DYMTLDeviceProfile isEqual:];
-[DYMTLDeviceProfile name];
-[DYMTLDeviceProfile defaultSamplePositions];
-[DYMTLDeviceProfile descriptionForBugReport];
-[DYMTLDeviceProfile supportsCapabilitiesOfGraphicsAPI:];
-[DYMTLDeviceProfile streamRef];
-[DYMTLDeviceProfile supportedFeatureSets];
-[DYMTLDeviceProfile supportedGPUFamilies];
-[DYMTLDeviceProfile capturableObjectType];
```
