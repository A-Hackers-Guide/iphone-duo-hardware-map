# `BLSDiagnosticEnvironmentDateSpecifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSEnvironmentDateSpecifying`, `NSSecureCoding`, `BSXPCCoding`
- 2 instance variables, 6 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"BLSAlwaysOnDateSpecifier" _dateSpecifier;
@"NSString" _environmentIdentifier;
```

## Properties

```
@property (T@"BLSAlwaysOnDateSpecifier",R,N,V_dateSpecifier) dateSpecifier;
@property (T@"NSString",R,C,N,V_environmentIdentifier) environmentIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSDiagnosticEnvironmentDateSpecifier supportsSecureCoding];
+[BLSDiagnosticEnvironmentDateSpecifier createWithSpecifier:];
```

## Instance methods

```
-[BLSDiagnosticEnvironmentDateSpecifier bls_loggingString];
-[BLSDiagnosticEnvironmentDateSpecifier bls_shortLoggingString];
-[BLSDiagnosticEnvironmentDateSpecifier initWithXPCDictionary:];
-[BLSDiagnosticEnvironmentDateSpecifier environmentIdentifier];
-[BLSDiagnosticEnvironmentDateSpecifier encodeWithXPCDictionary:];
-[BLSDiagnosticEnvironmentDateSpecifier encodeWithCoder:];
-[BLSDiagnosticEnvironmentDateSpecifier hash];
-[BLSDiagnosticEnvironmentDateSpecifier description];
-[BLSDiagnosticEnvironmentDateSpecifier initWithCoder:];
-[BLSDiagnosticEnvironmentDateSpecifier copyWithZone:];
-[BLSDiagnosticEnvironmentDateSpecifier isEqual:];
-[BLSDiagnosticEnvironmentDateSpecifier dateSpecifier];
-[BLSDiagnosticEnvironmentDateSpecifier initWithDateSpecifier:environmentIdentifier:];
```
