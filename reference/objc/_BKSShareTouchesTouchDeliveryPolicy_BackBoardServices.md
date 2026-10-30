# `_BKSShareTouchesTouchDeliveryPolicy`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSTouchDeliveryPolicy`
- 3 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
I _childContextId;
I _hostContextId;
@"NSObject<OS_xpc_object>" _assertionEndpoint;
```

## Properties

```
@property (TI,R,N,V_childContextId) childContextId;
@property (TI,R,N,V_hostContextId) hostContextId;
```

## Class methods

```
+[_BKSShareTouchesTouchDeliveryPolicy supportsSecureCoding];
```

## Instance methods

```
-[_BKSShareTouchesTouchDeliveryPolicy matchSharingTouchesPolicy:orCancelTouchesPolicy:orCombinedPolicy:];
-[_BKSShareTouchesTouchDeliveryPolicy setAssertionEndpoint:];
-[_BKSShareTouchesTouchDeliveryPolicy appendDescriptionToFormatter:];
-[_BKSShareTouchesTouchDeliveryPolicy assertionEndpoint];
-[_BKSShareTouchesTouchDeliveryPolicy initWithChildContextId:hostContextId:];
-[_BKSShareTouchesTouchDeliveryPolicy encodeWithCoder:];
-[_BKSShareTouchesTouchDeliveryPolicy hash];
-[_BKSShareTouchesTouchDeliveryPolicy initWithCoder:];
-[_BKSShareTouchesTouchDeliveryPolicy hostContextId];
-[_BKSShareTouchesTouchDeliveryPolicy isEqual:];
-[_BKSShareTouchesTouchDeliveryPolicy childContextId];
```
