# `BKSTouchDeliveryPolicy`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 0 instance variables, 1 properties, 14 instance methods, 5 class methods

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,N) assertionEndpoint;
```

## Class methods

```
+[BKSTouchDeliveryPolicy allocWithZone:];
+[BKSTouchDeliveryPolicy supportsSecureCoding];
+[BKSTouchDeliveryPolicy policyByCombiningPolicies:];
+[BKSTouchDeliveryPolicy policyCancelingTouchesDeliveredToContextId:withInitialTouchTimestamp:];
+[BKSTouchDeliveryPolicy policyRequiringSharingOfTouchesDeliveredToChildContextId:withHostContextId:];
```

## Instance methods

```
-[BKSTouchDeliveryPolicy matchSharingTouchesPolicy:orCancelTouchesPolicy:orCombinedPolicy:];
-[BKSTouchDeliveryPolicy setAssertionEndpoint:];
-[BKSTouchDeliveryPolicy appendDescriptionToFormatter:];
-[BKSTouchDeliveryPolicy assertionEndpoint];
-[BKSTouchDeliveryPolicy encodeWithCoder:];
-[BKSTouchDeliveryPolicy hash];
-[BKSTouchDeliveryPolicy description];
-[BKSTouchDeliveryPolicy initWithCoder:];
-[BKSTouchDeliveryPolicy isEqual:];
-[BKSTouchDeliveryPolicy policyByMappingContainedPoliciesWithBlock:];
-[BKSTouchDeliveryPolicy policyExcludingPolicy:];
-[BKSTouchDeliveryPolicy policyExcludingPolicyIdenticalTo:];
-[BKSTouchDeliveryPolicy policyIncludingPolicy:];
-[BKSTouchDeliveryPolicy reducePolicyToObjectWithBlock:];
```
