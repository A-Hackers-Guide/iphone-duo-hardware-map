# `CTPriVersion`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _majorVersion;
@"NSNumber" _minorVersion;
@"NSNumber" _releaseVersion;
```

## Properties

```
@property (T@"NSNumber",&,N,V_majorVersion) majorVersion;
@property (T@"NSNumber",&,N,V_minorVersion) minorVersion;
@property (T@"NSNumber",&,N,V_releaseVersion) releaseVersion;
```

## Class methods

```
+[CTPriVersion supportsSecureCoding];
```

## Instance methods

```
-[CTPriVersion majorVersion];
-[CTPriVersion releaseVersion];
-[CTPriVersion encodeWithCoder:];
-[CTPriVersion description];
-[CTPriVersion initWithCoder:];
-[CTPriVersion copyWithZone:];
-[CTPriVersion minorVersion];
-[CTPriVersion setReleaseVersion:];
-[CTPriVersion setMajorVersion:];
-[CTPriVersion setMinorVersion:];
```
