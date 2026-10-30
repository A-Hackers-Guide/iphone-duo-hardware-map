# `PLClientLogAggregator`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 20 instance methods, 1 class methods

## Instance variables

```
C _numAggregates;
C _numAggregations;
@"NSMutableDictionary" _aggregatesCache;
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _executionQueue;
@"NSObject<OS_dispatch_source>" _flushTimer;
```

## Properties

```
@property (T@"NSMutableDictionary",R,V_aggregatesCache) aggregatesCache;
@property (TC,V_numAggregates) numAggregates;
@property (TC,V_numAggregations) numAggregations;
@property (T@"NSObject<OS_os_log>",&,V_logHandle) logHandle;
@property (T@"NSObject<OS_dispatch_queue>",&,V_executionQueue) executionQueue;
@property (T@"NSObject<OS_dispatch_source>",&,V_flushTimer) flushTimer;
```

## Class methods

```
+[PLClientLogAggregator sharedInstance];
```

## Instance methods

```
-[PLClientLogAggregator init];
-[PLClientLogAggregator logHandle];
-[PLClientLogAggregator flushTimer];
-[PLClientLogAggregator setLogHandle:];
-[PLClientLogAggregator executionQueue];
-[PLClientLogAggregator setExecutionQueue:];
-[PLClientLogAggregator numAggregations];
-[PLClientLogAggregator aggregatesCache];
-[PLClientLogAggregator _aggregateForClientID:eventName:eventDictionary:configuration:];
-[PLClientLogAggregator _eventAggregate:eventName:aggregateKey:valueLabel:];
-[PLClientLogAggregator _flushToPowerLog];
-[PLClientLogAggregator _isEventInputValid:configuration:];
-[PLClientLogAggregator _scheduleFlushTimer];
-[PLClientLogAggregator _setEventAggregate:eventName:aggregateKey:valueLabel:value:];
-[PLClientLogAggregator aggregateForClientID_async:eventName:eventDictionary:configuration:];
-[PLClientLogAggregator cleanCache];
-[PLClientLogAggregator numAggregates];
-[PLClientLogAggregator setFlushTimer:];
-[PLClientLogAggregator setNumAggregates:];
-[PLClientLogAggregator setNumAggregations:];
```
