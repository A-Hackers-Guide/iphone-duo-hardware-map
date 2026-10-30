# `BLSDurationAttribute`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSAttribute`
- Protocols: `BSXPCCoding`
- 1 instance variables, 5 properties, 11 instance methods, 4 class methods

## Instance variables

```
d _duration;
```

## Properties

```
@property (Td,R,N,V_duration) duration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSDurationAttribute supportsSecureCoding];
+[BLSDurationAttribute timeoutAfterInterval:];
+[BLSDurationAttribute cancelAfterInterval:];
+[BLSDurationAttribute warnAfterInterval:];
```

## Instance methods

```
-[BLSDurationAttribute initWithDuration:];
-[BLSDurationAttribute initWithXPCDictionary:];
-[BLSDurationAttribute duration];
-[BLSDurationAttribute encodeWithXPCDictionary:];
-[BLSDurationAttribute encodeWithCoder:];
-[BLSDurationAttribute hash];
-[BLSDurationAttribute description];
-[BLSDurationAttribute initWithCoder:];
-[BLSDurationAttribute copyWithZone:];
-[BLSDurationAttribute isEqual:];
-[BLSDurationAttribute canBePaused];
```
