# `ULTransactionManager`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _transactions;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableDictionary",&,N,V_transactions) transactions;
```

## Class methods

```
+[ULTransactionManager shared];
```

## Instance methods

```
-[ULTransactionManager transactions];
-[ULTransactionManager init];
-[ULTransactionManager queue];
-[ULTransactionManager setTransactions:];
-[ULTransactionManager setQueue:];
-[ULTransactionManager dumpActiveTransactions];
-[ULTransactionManager configureTransactionIfNeeded:needed:];
-[ULTransactionManager invalidateAllTransactions];
-[ULTransactionManager isTransactionActive:];
-[ULTransactionManager performUnderTransaction:block:];
```
