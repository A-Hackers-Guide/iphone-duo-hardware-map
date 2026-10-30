# `CTEOSFirmwareInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSData" _currentVersion;
@"NSNumber" _userProfiles;
@"NSData" _updateCsn;
```

## Properties

```
@property (T@"NSData",&,N,V_currentVersion) currentVersion;
@property (T@"NSNumber",&,N,V_userProfiles) userProfiles;
@property (T@"NSData",&,N,V_updateCsn) updateCsn;
```

## Class methods

```
+[CTEOSFirmwareInfo supportsSecureCoding];
```

## Instance methods

```
-[CTEOSFirmwareInfo encodeWithCoder:];
-[CTEOSFirmwareInfo description];
-[CTEOSFirmwareInfo initWithCoder:];
-[CTEOSFirmwareInfo copyWithZone:];
-[CTEOSFirmwareInfo currentVersion];
-[CTEOSFirmwareInfo setCurrentVersion:];
-[CTEOSFirmwareInfo setUpdateCsn:];
-[CTEOSFirmwareInfo setUserProfiles:];
-[CTEOSFirmwareInfo updateCsn];
-[CTEOSFirmwareInfo userProfiles];
```
