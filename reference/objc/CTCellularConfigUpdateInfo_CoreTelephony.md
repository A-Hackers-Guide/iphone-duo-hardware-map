# `CTCellularConfigUpdateInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _configType;
@"NSString" _updatedTime;
@"NSString" _updatedDetails;
```

## Properties

```
@property (T@"NSString",&,N,V_configType) configType;
@property (T@"NSString",&,N,V_updatedTime) updatedTime;
@property (T@"NSString",&,N,V_updatedDetails) updatedDetails;
```

## Class methods

```
+[CTCellularConfigUpdateInfo supportsSecureCoding];
```

## Instance methods

```
-[CTCellularConfigUpdateInfo init];
-[CTCellularConfigUpdateInfo encodeWithCoder:];
-[CTCellularConfigUpdateInfo description];
-[CTCellularConfigUpdateInfo initWithCoder:];
-[CTCellularConfigUpdateInfo copyWithZone:];
-[CTCellularConfigUpdateInfo setUpdatedTime:];
-[CTCellularConfigUpdateInfo configType];
-[CTCellularConfigUpdateInfo setConfigType:];
-[CTCellularConfigUpdateInfo setUpdatedDetails:];
-[CTCellularConfigUpdateInfo updatedDetails];
-[CTCellularConfigUpdateInfo updatedTime];
```
