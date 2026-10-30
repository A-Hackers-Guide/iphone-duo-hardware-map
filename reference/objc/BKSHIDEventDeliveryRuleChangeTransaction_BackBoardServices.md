# `BKSHIDEventDeliveryRuleChangeTransaction`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`
- 10 instance variables, 14 properties, 26 instance methods, 1 class methods

## Instance variables

```
Q _contentsMask;
@"NSArray" _discreteDispatchingRules;
@"NSArray" _deferringRules;
@"NSArray" _keyCommandDispatchingRules;
@"NSArray" _keyCommandsRegistrations;
@"NSArray" _bufferingPredicates;
@"NSArray" _constraintAssertions;
@"NSArray" _modalityAssertions;
@"NSArray" _selectionRequests;
@"NSArray" _grantAssertions;
```

## Properties

```
@property (TQ,N,V_contentsMask) contentsMask;
@property (T@"NSArray",C,N,V_discreteDispatchingRules) discreteDispatchingRules;
@property (T@"NSArray",C,N,V_deferringRules) deferringRules;
@property (T@"NSArray",C,N,V_keyCommandDispatchingRules) keyCommandDispatchingRules;
@property (T@"NSArray",C,N,V_keyCommandsRegistrations) keyCommandsRegistrations;
@property (T@"NSArray",C,N,V_bufferingPredicates) bufferingPredicates;
@property (T@"NSArray",C,N,V_constraintAssertions) constraintAssertions;
@property (T@"NSArray",C,N,V_modalityAssertions) modalityAssertions;
@property (T@"NSArray",C,N,V_selectionRequests) selectionRequests;
@property (T@"NSArray",C,N,V_grantAssertions) grantAssertions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeliveryRuleChangeTransaction supportsSecureCoding];
```

## Instance methods

```
-[BKSHIDEventDeliveryRuleChangeTransaction setSelectionRequests:];
-[BKSHIDEventDeliveryRuleChangeTransaction contentsMask];
-[BKSHIDEventDeliveryRuleChangeTransaction discreteDispatchingRules];
-[BKSHIDEventDeliveryRuleChangeTransaction modalityAssertions];
-[BKSHIDEventDeliveryRuleChangeTransaction setDeferringRules:];
-[BKSHIDEventDeliveryRuleChangeTransaction setKeyCommandDispatchingRules:];
-[BKSHIDEventDeliveryRuleChangeTransaction deferringRules];
-[BKSHIDEventDeliveryRuleChangeTransaction setKeyCommandsRegistrations:];
-[BKSHIDEventDeliveryRuleChangeTransaction keyCommandDispatchingRules];
-[BKSHIDEventDeliveryRuleChangeTransaction bufferingPredicates];
-[BKSHIDEventDeliveryRuleChangeTransaction keyCommandsRegistrations];
-[BKSHIDEventDeliveryRuleChangeTransaction setDiscreteDispatchingRules:];
-[BKSHIDEventDeliveryRuleChangeTransaction encodeWithCoder:];
-[BKSHIDEventDeliveryRuleChangeTransaction grantAssertions];
-[BKSHIDEventDeliveryRuleChangeTransaction setBufferingPredicates:];
-[BKSHIDEventDeliveryRuleChangeTransaction hash];
-[BKSHIDEventDeliveryRuleChangeTransaction setConstraintAssertions:];
-[BKSHIDEventDeliveryRuleChangeTransaction selectionRequests];
-[BKSHIDEventDeliveryRuleChangeTransaction description];
-[BKSHIDEventDeliveryRuleChangeTransaction setModalityAssertions:];
-[BKSHIDEventDeliveryRuleChangeTransaction initWithCoder:];
-[BKSHIDEventDeliveryRuleChangeTransaction appendDescriptionToStream:];
-[BKSHIDEventDeliveryRuleChangeTransaction constraintAssertions];
-[BKSHIDEventDeliveryRuleChangeTransaction isEqual:];
-[BKSHIDEventDeliveryRuleChangeTransaction setGrantAssertions:];
-[BKSHIDEventDeliveryRuleChangeTransaction setContentsMask:];
```
