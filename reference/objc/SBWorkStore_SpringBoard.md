# `SBWorkStore`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _workItemsPerKey;
@"NSMutableArray" _keysWithWork;
@"NSMutableDictionary" _workExpirationPeriods;
@"NSObject<OS_dispatch_queue>" _workQueue;
Q _maxWorkPerKey;
@"NSMutableArray" _observers;
@"NSObject<OS_dispatch_queue>" _observerQueue;
d _defaultWorkExpirationPeriod;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_workItemsPerKey) workItemsPerKey;
@property (T@"NSMutableArray",R,N,V_observers) observers;
@property (TQ,R,N,V_maxWorkPerKey) maxWorkPerKey;
@property (T@"NSArray",R,N) keysWithWork;
@property (Td,N,V_defaultWorkExpirationPeriod) defaultWorkExpirationPeriod;
```

## Instance methods

```
-[SBWorkStore debugDescription];
-[SBWorkStore removeObserver:];
-[SBWorkStore addObserver:];
-[SBWorkStore description];
-[SBWorkStore observers];
-[SBWorkStore setDefaultWorkExpirationPeriod:];
-[SBWorkStore setWorkExpirationPeriod:forKey:];
-[SBWorkStore workItemsPerKey];
-[SBWorkStore _notifyObserversWorkDidChange];
-[SBWorkStore _workQueue_expireWorkForKey:];
-[SBWorkStore addWorkItem:forKey:];
-[SBWorkStore defaultWorkExpirationPeriod];
-[SBWorkStore dequeueWorkForKey:];
-[SBWorkStore initWithMaximumNumberOfWorkItemsPerKey:];
-[SBWorkStore keysWithWork];
-[SBWorkStore maxWorkPerKey];
-[SBWorkStore purgeWorkForKey:];
```
