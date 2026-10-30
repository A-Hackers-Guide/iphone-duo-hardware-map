# `SRSourceDevice`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 7 properties, 18 instance methods, 2 class methods

## Instance variables

```
@"NSString" _manufacturer;
@"NSString" _model;
@"NSString" _hardwareVersion;
@"NSString" _firmwareVersion;
@"NSString" _ephemeralIdentifier;
@"NSData" _encryptedIdentifier;
```

## Properties

```
@property (T@"NSString",&,N,V_ephemeralIdentifier) ephemeralIdentifier;
@property (T@"NSData",&,N,V_encryptedIdentifier) encryptedIdentifier;
@property (T@"NSString",R,C,N) localIdentifier;
@property (T@"NSString",R,C,N,V_manufacturer) manufacturer;
@property (T@"NSString",R,C,N,V_model) model;
@property (T@"NSString",R,C,N,V_hardwareVersion) hardwareVersion;
@property (T@"NSString",R,C,N,V_firmwareVersion) firmwareVersion;
```

## Class methods

```
+[SRSourceDevice supportsSecureCoding];
+[SRSourceDevice initialize];
```

## Instance methods

```
-[SRSourceDevice hardwareVersion];
-[SRSourceDevice model];
-[SRSourceDevice firmwareVersion];
-[SRSourceDevice dealloc];
-[SRSourceDevice manufacturer];
-[SRSourceDevice encodeWithCoder:];
-[SRSourceDevice hash];
-[SRSourceDevice description];
-[SRSourceDevice initWithCoder:];
-[SRSourceDevice copyWithZone:];
-[SRSourceDevice isEqual:];
-[SRSourceDevice localIdentifier];
-[SRSourceDevice sr_dictionaryRepresentation];
-[SRSourceDevice encryptedIdentifier];
-[SRSourceDevice ephemeralIdentifier];
-[SRSourceDevice initWithIdentifier:manufacturer:model:hardwareVersion:firmwareVersion:];
-[SRSourceDevice setEncryptedIdentifier:];
-[SRSourceDevice setEphemeralIdentifier:];
```
