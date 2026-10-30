# `BKSHIDEventPolicyObservation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`, `BSDescriptionStreaming`
- 8 instance variables, 12 properties, 17 instance methods, 3 class methods

## Instance variables

```
i _pid;
@"BKSHIDEventDisplay" _display;
@"BKSHIDEventDeferringEnvironment" _environment;
@"BKSHIDEventDeferringSelectionPathIdentifier" _selectionPath;
@"BKSHIDEventDeferringToken" _token;
q _policyStatus;
B _finalStringToken;
q _generation;
```

## Properties

```
@property (Ti,R,N) pid;
@property (T@"BKSHIDEventDisplay",R,N) display;
@property (T@"BKSHIDEventDeferringEnvironment",R,N) environment;
@property (T@"BKSHIDEventDeferringSelectionPathIdentifier",R,N) selectionPath;
@property (T@"BKSHIDEventDeferringToken",R,N) token;
@property (Tq,R,N) policyStatus;
@property (TB,R,N,GisFinalStringToken,V_finalStringToken) finalStringToken;
@property (Tq,R,N) generation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventPolicyObservation build:];
+[BKSHIDEventPolicyObservation supportsSecureCoding];
+[BKSHIDEventPolicyObservation new];
```

## Instance methods

```
-[BKSHIDEventPolicyObservation selectionPath];
-[BKSHIDEventPolicyObservation policyStatus];
-[BKSHIDEventPolicyObservation display];
-[BKSHIDEventPolicyObservation mutableCopyWithZone:];
-[BKSHIDEventPolicyObservation isFinalStringToken];
-[BKSHIDEventPolicyObservation init];
-[BKSHIDEventPolicyObservation pid];
-[BKSHIDEventPolicyObservation generation];
-[BKSHIDEventPolicyObservation encodeWithCoder:];
-[BKSHIDEventPolicyObservation hash];
-[BKSHIDEventPolicyObservation description];
-[BKSHIDEventPolicyObservation initWithCoder:];
-[BKSHIDEventPolicyObservation appendDescriptionToStream:];
-[BKSHIDEventPolicyObservation token];
-[BKSHIDEventPolicyObservation copyWithZone:];
-[BKSHIDEventPolicyObservation isEqual:];
-[BKSHIDEventPolicyObservation environment];
```
