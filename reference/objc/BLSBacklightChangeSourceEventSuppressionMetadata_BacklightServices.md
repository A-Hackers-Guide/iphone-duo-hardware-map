# `BLSBacklightChangeSourceEventSuppressionMetadata`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSBacklightChangeSourceEventMetadata`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
Q _type;
Q _reason;
```

## Properties

```
@property (TQ,R,N,V_type) type;
@property (TQ,R,N,V_reason) reason;
```

## Class methods

```
+[BLSBacklightChangeSourceEventSuppressionMetadata supportsSecureCoding];
```

## Instance methods

```
-[BLSBacklightChangeSourceEventSuppressionMetadata initWithXPCDictionary:];
-[BLSBacklightChangeSourceEventSuppressionMetadata type];
-[BLSBacklightChangeSourceEventSuppressionMetadata encodeWithXPCDictionary:];
-[BLSBacklightChangeSourceEventSuppressionMetadata encodeWithCoder:];
-[BLSBacklightChangeSourceEventSuppressionMetadata hash];
-[BLSBacklightChangeSourceEventSuppressionMetadata description];
-[BLSBacklightChangeSourceEventSuppressionMetadata initWithCoder:];
-[BLSBacklightChangeSourceEventSuppressionMetadata reason];
-[BLSBacklightChangeSourceEventSuppressionMetadata copyWithZone:];
-[BLSBacklightChangeSourceEventSuppressionMetadata isEqual:];
-[BLSBacklightChangeSourceEventSuppressionMetadata initWithType:reason:];
```
