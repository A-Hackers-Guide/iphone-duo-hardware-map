# `_BKSCancelTouchesTouchDeliveryPolicy`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSTouchDeliveryPolicy`
- 3 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
I _contextId;
@"NSObject<OS_xpc_object>" _assertionEndpoint;
d _initialTouchTimestamp;
```

## Properties

```
@property (TI,R,N,V_contextId) contextId;
@property (Td,R,N,V_initialTouchTimestamp) initialTouchTimestamp;
```

## Class methods

```
+[_BKSCancelTouchesTouchDeliveryPolicy supportsSecureCoding];
```

## Instance methods

```
-[_BKSCancelTouchesTouchDeliveryPolicy matchSharingTouchesPolicy:orCancelTouchesPolicy:orCombinedPolicy:];
-[_BKSCancelTouchesTouchDeliveryPolicy setAssertionEndpoint:];
-[_BKSCancelTouchesTouchDeliveryPolicy contextId];
-[_BKSCancelTouchesTouchDeliveryPolicy appendDescriptionToFormatter:];
-[_BKSCancelTouchesTouchDeliveryPolicy assertionEndpoint];
-[_BKSCancelTouchesTouchDeliveryPolicy initialTouchTimestamp];
-[_BKSCancelTouchesTouchDeliveryPolicy encodeWithCoder:];
-[_BKSCancelTouchesTouchDeliveryPolicy hash];
-[_BKSCancelTouchesTouchDeliveryPolicy initWithCoder:];
-[_BKSCancelTouchesTouchDeliveryPolicy isEqual:];
-[_BKSCancelTouchesTouchDeliveryPolicy initWithContextId:initialTouchTimestamp:];
```
