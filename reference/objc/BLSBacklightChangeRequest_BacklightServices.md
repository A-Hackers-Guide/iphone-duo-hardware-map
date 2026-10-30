# `BLSBacklightChangeRequest`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSSecureCoding`
- 5 instance variables, 9 properties, 14 instance methods, 1 class methods

## Instance variables

```
q _requestedActivityState;
@"NSString" _explanation;
Q _timestamp;
q _sourceEvent;
@"BLSBacklightChangeSourceEventMetadata" _sourceEventMetadata;
```

## Properties

```
@property (Tq,R,N,V_requestedActivityState) requestedActivityState;
@property (T@"NSString",R,C,N,V_explanation) explanation;
@property (TQ,R,N,V_timestamp) timestamp;
@property (Tq,R,N,V_sourceEvent) sourceEvent;
@property (T@"BLSBacklightChangeSourceEventMetadata",R,N,V_sourceEventMetadata) sourceEventMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSBacklightChangeRequest supportsSecureCoding];
```

## Instance methods

```
-[BLSBacklightChangeRequest explanation];
-[BLSBacklightChangeRequest initWithXPCDictionary:];
-[BLSBacklightChangeRequest timestamp];
-[BLSBacklightChangeRequest requestedActivityState];
-[BLSBacklightChangeRequest encodeWithXPCDictionary:];
-[BLSBacklightChangeRequest sourceEvent];
-[BLSBacklightChangeRequest encodeWithCoder:];
-[BLSBacklightChangeRequest hash];
-[BLSBacklightChangeRequest description];
-[BLSBacklightChangeRequest initWithCoder:];
-[BLSBacklightChangeRequest sourceEventMetadata];
-[BLSBacklightChangeRequest copyWithZone:];
-[BLSBacklightChangeRequest isEqual:];
-[BLSBacklightChangeRequest initWithRequestedActivityState:explanation:timestamp:sourceEvent:sourceEventMetadata:];
```
