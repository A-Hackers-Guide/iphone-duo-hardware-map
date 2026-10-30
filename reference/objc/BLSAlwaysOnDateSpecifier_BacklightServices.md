# `BLSAlwaysOnDateSpecifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `BSXPCCoding`
- 4 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _date;
q _fidelity;
@ _userObject;
Q _lowPowerRenderingPresentationTime;
```

## Properties

```
@property (T@"NSDate",R,N,V_date) date;
@property (Tq,R,N,V_fidelity) fidelity;
@property (T@,R,N,V_userObject) userObject;
@property (TQ,R,N,V_lowPowerRenderingPresentationTime) lowPowerRenderingPresentationTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSAlwaysOnDateSpecifier supportsSecureCoding];
```

## Instance methods

```
-[BLSAlwaysOnDateSpecifier bls_loggingString];
-[BLSAlwaysOnDateSpecifier bls_shortLoggingString];
-[BLSAlwaysOnDateSpecifier compare:];
-[BLSAlwaysOnDateSpecifier initWithXPCDictionary:];
-[BLSAlwaysOnDateSpecifier date];
-[BLSAlwaysOnDateSpecifier encodeWithXPCDictionary:];
-[BLSAlwaysOnDateSpecifier encodeWithCoder:];
-[BLSAlwaysOnDateSpecifier hash];
-[BLSAlwaysOnDateSpecifier description];
-[BLSAlwaysOnDateSpecifier initWithCoder:];
-[BLSAlwaysOnDateSpecifier copyWithZone:];
-[BLSAlwaysOnDateSpecifier isEqual:];
-[BLSAlwaysOnDateSpecifier lowPowerRenderingPresentationTime];
-[BLSAlwaysOnDateSpecifier fidelity];
-[BLSAlwaysOnDateSpecifier initWithDate:fidelity:];
-[BLSAlwaysOnDateSpecifier userObject];
-[BLSAlwaysOnDateSpecifier initWithDate:fidelity:userObject:lowPowerRenderingPresentationTime:];
-[BLSAlwaysOnDateSpecifier newSpecifierWithMaxFidelity:];
-[BLSAlwaysOnDateSpecifier initWithDate:fidelity:userObject:];
```
