# `_BKSCombinedTouchDeliveryPolicy`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSTouchDeliveryPolicy`
- 1 instance variables, 1 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _policies;
```

## Properties

```
@property (T@"NSArray",R,N,V_policies) policies;
```

## Class methods

```
+[_BKSCombinedTouchDeliveryPolicy supportsSecureCoding];
```

## Instance methods

```
-[_BKSCombinedTouchDeliveryPolicy policies];
-[_BKSCombinedTouchDeliveryPolicy matchSharingTouchesPolicy:orCancelTouchesPolicy:orCombinedPolicy:];
-[_BKSCombinedTouchDeliveryPolicy setAssertionEndpoint:];
-[_BKSCombinedTouchDeliveryPolicy appendDescriptionToFormatter:];
-[_BKSCombinedTouchDeliveryPolicy assertionEndpoint];
-[_BKSCombinedTouchDeliveryPolicy encodeWithCoder:];
-[_BKSCombinedTouchDeliveryPolicy hash];
-[_BKSCombinedTouchDeliveryPolicy initWithPolicies:];
-[_BKSCombinedTouchDeliveryPolicy initWithCoder:];
-[_BKSCombinedTouchDeliveryPolicy isEqual:];
```
