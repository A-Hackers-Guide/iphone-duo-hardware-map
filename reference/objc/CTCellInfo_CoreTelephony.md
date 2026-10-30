# `CTCellInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSCopying`, `NSSecureCoding`
- 1 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _legacyInfo;
```

## Properties

```
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
@property (T@"NSArray",&,N,V_legacyInfo) legacyInfo;
```

## Class methods

```
+[CTCellInfo supportsSecureCoding];
```

## Instance methods

```
-[CTCellInfo ct_shortDescription];
-[CTCellInfo ct_shortName];
-[CTCellInfo encodeWithCoder:];
-[CTCellInfo description];
-[CTCellInfo initWithCoder:];
-[CTCellInfo copyWithZone:];
-[CTCellInfo legacyInfo];
-[CTCellInfo setLegacyInfo:];
```
