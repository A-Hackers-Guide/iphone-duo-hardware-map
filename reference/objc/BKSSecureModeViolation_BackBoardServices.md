# `BKSSecureModeViolation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSSecureCoding`
- 4 instance variables, 8 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _processId;
@"NSArray" _contextIds;
@"NSDictionary" _layerNamesByContext;
@"NSString" _displayUUID;
```

## Properties

```
@property (T@"NSNumber",&,N,V_processId) processId;
@property (T@"NSArray",C,N,V_contextIds) contextIds;
@property (T@"NSDictionary",C,N,V_layerNamesByContext) layerNamesByContext;
@property (T@"NSString",C,N,V_displayUUID) displayUUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSSecureModeViolation supportsSecureCoding];
```

## Instance methods

```
-[BKSSecureModeViolation setProcessId:];
-[BKSSecureModeViolation succinctDescriptionBuilder];
-[BKSSecureModeViolation processId];
-[BKSSecureModeViolation displayUUID];
-[BKSSecureModeViolation descriptionWithMultilinePrefix:];
-[BKSSecureModeViolation succinctDescription];
-[BKSSecureModeViolation setDisplayUUID:];
-[BKSSecureModeViolation encodeWithCoder:];
-[BKSSecureModeViolation hash];
-[BKSSecureModeViolation description];
-[BKSSecureModeViolation initWithCoder:];
-[BKSSecureModeViolation isEqual:];
-[BKSSecureModeViolation descriptionBuilderWithMultilinePrefix:];
-[BKSSecureModeViolation contextIds];
-[BKSSecureModeViolation initWithProcessId:contextIds:];
-[BKSSecureModeViolation layerNamesByContext];
-[BKSSecureModeViolation setContextIds:];
-[BKSSecureModeViolation setLayerNamesByContext:];
```
