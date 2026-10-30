# `BKSHIDEventDeliveryChain`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSSecureCoding`, `BSProtobufSerializable`
- 10 instance variables, 16 properties, 28 instance methods, 3 class methods

## Instance variables

```
@"BKSEventDeferringChainIdentity" _identity;
@"BKSHIDEventDisplay" _compatibilityDisplay;
q _generation;
B _containsSubset;
B _containsEndOfChain;
@"BKSHIDEventDeferringSelectionPathIdentifier" _selectionPath;
@"NSArray" _deferringPath;
@"NSSet" _modalities;
@"NSSet" _constraints;
q _finalStringTargetIndex;
```

## Properties

```
@property (TB,N,V_containsEndOfChain) containsEndOfChain;
@property (T@"BKSEventDeferringChainIdentity",R,N,V_identity) identity;
@property (T@"BKSHIDEventDisplay",R,N,V_compatibilityDisplay) compatibilityDisplay;
@property (T@"BKSHIDEventDisplay",R,N) display;
@property (T@"BKSHIDEventDeferringEnvironment",R,N) environment;
@property (T@"BKSHIDEventDeferringSelectionPathIdentifier",R,N,V_selectionPath) selectionPath;
@property (T@"NSArray",R,C,N,V_deferringPath) deferringPath;
@property (T@"NSSet",R,C,N,V_modalities) modalities;
@property (T@"NSSet",R,C,N,V_constraints) constraints;
@property (TB,R,N,V_containsSubset) containsSubset;
@property (Tq,R,N,V_finalStringTargetIndex) finalStringTargetIndex;
@property (Tq,R,N,V_generation) generation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeliveryChain supportsSecureCoding];
+[BKSHIDEventDeliveryChain protobufSchema];
+[BKSHIDEventDeliveryChain new];
```

## Instance methods

```
-[BKSHIDEventDeliveryChain didFinishProtobufDecodingWithError:];
-[BKSHIDEventDeliveryChain selectionPath];
-[BKSHIDEventDeliveryChain display];
-[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:constraints:generation:];
-[BKSHIDEventDeliveryChain constraints];
-[BKSHIDEventDeliveryChain initForProtobufDecoding];
-[BKSHIDEventDeliveryChain compatibilityDisplay];
-[BKSHIDEventDeliveryChain init];
-[BKSHIDEventDeliveryChain modalities];
-[BKSHIDEventDeliveryChain appendDescriptionToFormatter:];
-[BKSHIDEventDeliveryChain containsEndOfChain];
-[BKSHIDEventDeliveryChain _dataProtobufEncoded];
-[BKSHIDEventDeliveryChain _protobufDecodedFromData:];
-[BKSHIDEventDeliveryChain generation];
-[BKSHIDEventDeliveryChain encodeWithCoder:];
-[BKSHIDEventDeliveryChain hash];
-[BKSHIDEventDeliveryChain identity];
-[BKSHIDEventDeliveryChain description];
-[BKSHIDEventDeliveryChain finalStringTargetIndex];
-[BKSHIDEventDeliveryChain setContainsEndOfChain:];
-[BKSHIDEventDeliveryChain initWithCoder:];
-[BKSHIDEventDeliveryChain deferringPath];
-[BKSHIDEventDeliveryChain containsSubset];
-[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:selectionPath:path:modalities:constraints:containsSubset:containsEndOfChain:finalStringTargetIndex:generation:];
-[BKSHIDEventDeliveryChain subsetForPID:];
-[BKSHIDEventDeliveryChain isEqual:];
-[BKSHIDEventDeliveryChain environment];
-[BKSHIDEventDeliveryChain initWithIdentity:compatibilityDisplay:path:];
```
