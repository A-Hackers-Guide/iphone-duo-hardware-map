# `BKSHIDEventDeliveryRuleWrapper`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
I _seed;
@"NSString" _reason;
@ _payload;
```

## Properties

```
@property (T@"NSString",R,C,N,V_reason) reason;
@property (T@,R,C,N,V_payload) payload;
@property (TI,R,N,V_seed) seed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeliveryRuleWrapper supportsSecureCoding];
```

## Instance methods

```
-[BKSHIDEventDeliveryRuleWrapper seed];
-[BKSHIDEventDeliveryRuleWrapper payload];
-[BKSHIDEventDeliveryRuleWrapper encodeWithCoder:];
-[BKSHIDEventDeliveryRuleWrapper hash];
-[BKSHIDEventDeliveryRuleWrapper initWithCoder:];
-[BKSHIDEventDeliveryRuleWrapper appendDescriptionToStream:];
-[BKSHIDEventDeliveryRuleWrapper reason];
-[BKSHIDEventDeliveryRuleWrapper isEqual:];
-[BKSHIDEventDeliveryRuleWrapper decodePayload:];
-[BKSHIDEventDeliveryRuleWrapper initWithReason:seed:payload:];
```
