# `PLCFNotificationOperatorComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _listeningForNotifications;
B _isStateRequired;
i _stateToken;
@"NSString" _notificationName;
@? _operatorBlock;
@"PLOperator" _operator;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"PLOperator",W,V_operator) operator;
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
@property (TB,V_isStateRequired) isStateRequired;
@property (Ti,V_stateToken) stateToken;
@property (TB,V_listeningForNotifications) listeningForNotifications;
@property (T@"NSString",&,V_notificationName) notificationName;
@property (T@?,C,N,V_operatorBlock) operatorBlock;
```

## Instance methods

```
-[PLCFNotificationOperatorComposition setWorkQueue:];
-[PLCFNotificationOperatorComposition workQueue];
-[PLCFNotificationOperatorComposition dealloc];
-[PLCFNotificationOperatorComposition setNotificationName:];
-[PLCFNotificationOperatorComposition operator];
-[PLCFNotificationOperatorComposition notificationName];
-[PLCFNotificationOperatorComposition setOperator:];
-[PLCFNotificationOperatorComposition isStateRequired];
-[PLCFNotificationOperatorComposition initWithOperator:forNotification:requireState:withBlock:];
-[PLCFNotificationOperatorComposition initWithWorkQueue:forNotification:requireState:withBlock:];
-[PLCFNotificationOperatorComposition listenForNotifications:];
-[PLCFNotificationOperatorComposition listeningForNotifications];
-[PLCFNotificationOperatorComposition operatorBlock];
-[PLCFNotificationOperatorComposition setIsStateRequired:];
-[PLCFNotificationOperatorComposition setListeningForNotifications:];
-[PLCFNotificationOperatorComposition setOperatorBlock:];
-[PLCFNotificationOperatorComposition setStateToken:];
-[PLCFNotificationOperatorComposition stateToken];
```
