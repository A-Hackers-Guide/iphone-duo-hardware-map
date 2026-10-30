# `CTPNRSupportStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _supportType;
```

## Properties

```
@property (Tq,N,V_supportType) supportType;
@property (TB,R,N,GisSupported) supported;
@property (TB,R,N,GisDisallowedByMDM) disallowedByMDM;
```

## Class methods

```
+[CTPNRSupportStatus supportsSecureCoding];
```

## Instance methods

```
-[CTPNRSupportStatus init];
-[CTPNRSupportStatus isSupported];
-[CTPNRSupportStatus encodeWithCoder:];
-[CTPNRSupportStatus description];
-[CTPNRSupportStatus initWithCoder:];
-[CTPNRSupportStatus copyWithZone:];
-[CTPNRSupportStatus isEqual:];
-[CTPNRSupportStatus isDisallowedByMDM];
-[CTPNRSupportStatus setSupportType:];
-[CTPNRSupportStatus initWithSupportType:];
-[CTPNRSupportStatus isEqualToCTPNRSupportStatus:];
-[CTPNRSupportStatus supportType];
```
