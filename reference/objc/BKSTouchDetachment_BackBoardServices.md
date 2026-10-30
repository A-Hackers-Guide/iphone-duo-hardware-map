# `BKSTouchDetachment`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`
- 5 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
I _userIdentifier;
@"BKSHIDTouchRoutingPolicy" _routingPolicy;
@"BKSTouchEventService" _service;
@"NSMutableArray" _mutableTouchIdentifiers;
{CGPoint="x"d"y"d} _touchOffset;
```

## Properties

```
@property (TI,R,N,V_userIdentifier) userIdentifier;
@property (T@"NSArray",R,N) touchIdentifiers;
@property (T{CGPoint=dd},N,V_touchOffset) touchOffset;
@property (T@"BKSHIDTouchRoutingPolicy",C,N,V_routingPolicy) routingPolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKSTouchDetachment userIdentifier];
-[BKSTouchDetachment appendDescriptionToFormatter:];
-[BKSTouchDetachment description];
-[BKSTouchDetachment routingPolicy];
-[BKSTouchDetachment setRoutingPolicy:];
-[BKSTouchDetachment touchIdentifiers];
-[BKSTouchDetachment touchOffset];
-[BKSTouchDetachment setTouchOffset:];
-[BKSTouchDetachment addTouchIdentifiers:];
```
