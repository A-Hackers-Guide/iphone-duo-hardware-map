# `SRDevice`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 8 instance variables, 8 properties, 21 instance methods, 2 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _model;
@"NSString" _systemName;
@"NSString" _systemVersion;
@"NSString" _internalProductType;
@"NSString" _deviceIdentifier;
q _deviceEnclosureMaterial;
@"NSString" _buildVersion;
```

## Properties

```
@property (T@"NSString",C,V_deviceIdentifier) deviceIdentifier;
@property (Tq,V_deviceEnclosureMaterial) deviceEnclosureMaterial;
@property (T@"NSString",C,V_buildVersion) buildVersion;
@property (T@"NSString",R,C,V_name) name;
@property (T@"NSString",R,C,V_model) model;
@property (T@"NSString",R,C,V_systemName) systemName;
@property (T@"NSString",R,C,V_systemVersion) systemVersion;
@property (T@"NSString",R,C) productType;
```

## Class methods

```
+[SRDevice supportsSecureCoding];
+[SRDevice currentDevice];
```

## Instance methods

```
-[SRDevice model];
-[SRDevice setDeviceIdentifier:];
-[SRDevice buildVersion];
-[SRDevice systemVersion];
-[SRDevice dealloc];
-[SRDevice productType];
-[SRDevice deviceIdentifier];
-[SRDevice encodeWithCoder:];
-[SRDevice hash];
-[SRDevice description];
-[SRDevice initWithCoder:];
-[SRDevice systemName];
-[SRDevice copyWithZone:];
-[SRDevice isEqual:];
-[SRDevice name];
-[SRDevice setBuildVersion:];
-[SRDevice _productType];
-[SRDevice sr_dictionaryRepresentation];
-[SRDevice deviceEnclosureMaterial];
-[SRDevice initWithDeviceDetails:];
-[SRDevice setDeviceEnclosureMaterial:];
```
