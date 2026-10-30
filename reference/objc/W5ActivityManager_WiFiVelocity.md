# `W5ActivityManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSTimer" _eagerExitTimeout;
@"NSTimer" _periodicActiveListTimer;
@"NSMutableArray" _active_transactions;
@? _alternateExecutionBlockForCleanExit;
@"NSObject<OS_dispatch_queue>" _queue;
Q _transactionsStarted;
@"NSDate" _dateFirstTransaction;
Q _transactionsCompleted;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,V_transactionsStarted) transactionsStarted;
@property (T@"NSDate",&,V_dateFirstTransaction) dateFirstTransaction;
@property (TQ,V_transactionsCompleted) transactionsCompleted;
@property (T@?,C,N,V_alternateExecutionBlockForCleanExit) alternateExecutionBlockForCleanExit;
```

## Class methods

```
+[W5ActivityManager sharedActivityManager];
```

## Instance methods

```
-[W5ActivityManager init];
-[W5ActivityManager queue];
-[W5ActivityManager setQueue:];
-[W5ActivityManager debugTimer];
-[W5ActivityManager _executeTimerBlock];
-[W5ActivityManager alternateExecutionBlockForCleanExit];
-[W5ActivityManager dateFirstTransaction];
-[W5ActivityManager debugTimerEnabled];
-[W5ActivityManager osTransactionComplete:];
-[W5ActivityManager osTransactionCreate:transaction:];
-[W5ActivityManager osTransactionsActive];
-[W5ActivityManager setAlternateExecutionBlockForCleanExit:];
-[W5ActivityManager setDateFirstTransaction:];
-[W5ActivityManager setTransactionsCompleted:];
-[W5ActivityManager setTransactionsStarted:];
-[W5ActivityManager transactionsCompleted];
-[W5ActivityManager transactionsStarted];
```
