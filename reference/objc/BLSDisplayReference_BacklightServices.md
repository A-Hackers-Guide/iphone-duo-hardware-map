# `BLSDisplayReference`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `BLSDisplay`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 6 properties, 15 instance methods, 6 class methods

## Instance variables

```
Q _referenceId;
@"NSString" _loggingName;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) referenceId;
@property (T@"NSString",R,C,N) loggingName;
```

## Class methods

```
+[BLSDisplayReference supportsSecureCoding];
+[BLSDisplayReference referenceForCADisplay:];
+[BLSDisplayReference referenceForAggregateDisplay];
+[BLSDisplayReference referenceIdForCADisplay:];
+[BLSDisplayReference setDisplays:];
+[BLSDisplayReference displays];
```

## Instance methods

```
-[BLSDisplayReference loggingName];
-[BLSDisplayReference init];
-[BLSDisplayReference initWithXPCDictionary:];
-[BLSDisplayReference initWithCADisplay:];
-[BLSDisplayReference encodeWithXPCDictionary:];
-[BLSDisplayReference encodeWithCoder:];
-[BLSDisplayReference initWithBLSDisplay:];
-[BLSDisplayReference doesMatchCADisplay:];
-[BLSDisplayReference hash];
-[BLSDisplayReference description];
-[BLSDisplayReference initWithCoder:];
-[BLSDisplayReference referenceId];
-[BLSDisplayReference copyWithZone:];
-[BLSDisplayReference isEqual:];
-[BLSDisplayReference initWithReferenceId:loggingName:];
```
