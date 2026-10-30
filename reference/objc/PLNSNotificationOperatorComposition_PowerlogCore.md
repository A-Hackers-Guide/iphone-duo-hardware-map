# `PLNSNotificationOperatorComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableArray" _notificationObservers;
@"NSArray" _notificationNames;
@? _operatorBlock;
@"PLOperator" _operator;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"PLOperator",W,V_operator) operator;
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
@property (T@"NSArray",R,C,V_notificationNames) notificationNames;
@property (T@"NSString",R,C) notificationName;
@property (T@?,C,V_operatorBlock) operatorBlock;
```

## Instance methods

```
-[PLNSNotificationOperatorComposition setWorkQueue:];
-[PLNSNotificationOperatorComposition workQueue];
-[PLNSNotificationOperatorComposition dealloc];
-[PLNSNotificationOperatorComposition operator];
-[PLNSNotificationOperatorComposition notificationName];
-[PLNSNotificationOperatorComposition setOperator:];
-[PLNSNotificationOperatorComposition notificationNames];
-[PLNSNotificationOperatorComposition initWithOperator:forNotification:withBlock:];
-[PLNSNotificationOperatorComposition initWithOperator:forNotifications:withBlock:];
-[PLNSNotificationOperatorComposition initWithWorkQueue:forNotification:withBlock:];
-[PLNSNotificationOperatorComposition initWithWorkQueue:forNotifications:withBlock:];
-[PLNSNotificationOperatorComposition listenForNotifications:];
-[PLNSNotificationOperatorComposition notification:];
-[PLNSNotificationOperatorComposition operatorBlock];
-[PLNSNotificationOperatorComposition setOperatorBlock:];
```
