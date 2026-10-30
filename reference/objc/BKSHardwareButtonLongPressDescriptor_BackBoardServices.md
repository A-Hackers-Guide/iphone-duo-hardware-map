# `BKSHardwareButtonLongPressDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
S _page;
S _usage;
d _timeout;
```

## Properties

```
@property (TS,R,N,V_page) page;
@property (TS,R,N,V_usage) usage;
@property (Td,R,N,V_timeout) timeout;
```

## Class methods

```
+[BKSHardwareButtonLongPressDescriptor supportsSecureCoding];
```

## Instance methods

```
-[BKSHardwareButtonLongPressDescriptor usage];
-[BKSHardwareButtonLongPressDescriptor copy];
-[BKSHardwareButtonLongPressDescriptor timeout];
-[BKSHardwareButtonLongPressDescriptor encodeWithCoder:];
-[BKSHardwareButtonLongPressDescriptor page];
-[BKSHardwareButtonLongPressDescriptor hash];
-[BKSHardwareButtonLongPressDescriptor description];
-[BKSHardwareButtonLongPressDescriptor initWithCoder:];
-[BKSHardwareButtonLongPressDescriptor copyWithZone:];
-[BKSHardwareButtonLongPressDescriptor isEqual:];
-[BKSHardwareButtonLongPressDescriptor initWithPage:usage:timeout:];
```
