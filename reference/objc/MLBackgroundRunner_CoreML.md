# `MLBackgroundRunner`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_DASExtensionRunner`
- 6 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _shouldStop;
@"_DASActivity" _activity;
@"MLBackgroundTask" _task;
@"<NSObject>" _dataSource;
@"NSObject<OS_dispatch_queue>" _watchdogQueue;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
```

## Properties

```
@property (TB,V_shouldStop) shouldStop;
@property (T@"_DASActivity",&,N,V_activity) activity;
@property (T@"MLBackgroundTask",&,N,V_task) task;
@property (T@"<NSObject>",&,N,V_dataSource) dataSource;
@property (T@"NSObject<OS_dispatch_queue>",&,V_watchdogQueue) watchdogQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,V_delegateQueue) delegateQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLBackgroundRunner setActivity:];
-[MLBackgroundRunner init];
-[MLBackgroundRunner stop];
-[MLBackgroundRunner start];
-[MLBackgroundRunner setDataSource:];
-[MLBackgroundRunner watchdogQueue];
-[MLBackgroundRunner activity];
-[MLBackgroundRunner setTask:];
-[MLBackgroundRunner dataSource];
-[MLBackgroundRunner setDelegateQueue:];
-[MLBackgroundRunner setWatchdogQueue:];
-[MLBackgroundRunner task];
-[MLBackgroundRunner delegateQueue];
-[MLBackgroundRunner createExtensionDataSourceWithInfoKey:conformingToProtocol:];
-[MLBackgroundRunner prepareForActivity:];
-[MLBackgroundRunner setShouldStop:];
-[MLBackgroundRunner shouldStop];
```
