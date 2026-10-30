# `PLAWDNetworkUsage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAWDAuxMetrics`
- 4 instance variables, 4 properties, 14 instance methods, 3 class methods

## Instance variables

```
I _netState;
@"PLEntryNotificationOperatorComposition" _netEventCallback;
@"PLEntryNotificationOperatorComposition" _nameConnectionCallback;
@"NSTimer" _snapshotTimer;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_netEventCallback) netEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_nameConnectionCallback) nameConnectionCallback;
@property (TI,V_netState) netState;
@property (T@"NSTimer",&,V_snapshotTimer) snapshotTimer;
```

## Class methods

```
+[PLAWDNetworkUsage entryAggregateDefinitions];
+[PLAWDNetworkUsage entryAggregateDefinitionNetUsage];
+[PLAWDNetworkUsage getSharedObjWithOperator:];
```

## Instance methods

```
-[PLAWDNetworkUsage handleNameConnectionCallback:];
-[PLAWDNetworkUsage handleNetCallback:];
-[PLAWDNetworkUsage nameConnectionCallback];
-[PLAWDNetworkUsage netEventCallback];
-[PLAWDNetworkUsage netState];
-[PLAWDNetworkUsage resetNetUsageTable];
-[PLAWDNetworkUsage setNameConnectionCallback:];
-[PLAWDNetworkUsage setNetEventCallback:];
-[PLAWDNetworkUsage setNetState:];
-[PLAWDNetworkUsage setSnapshotTimer:];
-[PLAWDNetworkUsage snapshotTimer];
-[PLAWDNetworkUsage startMetricCollection:];
-[PLAWDNetworkUsage stopMetricCollection:];
-[PLAWDNetworkUsage submitDataToAWDServer:withAwdConn:];
```
