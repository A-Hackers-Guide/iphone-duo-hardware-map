# `ULLifeCycleManager`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 20 instance methods, 1 class methods

## Instance variables

```
{unique_ptr<ULDatabase, std::default_delete<ULDatabase>>=""{?="__ptr_"^{ULDatabase}}} db;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableSet" _signals;
@"ULEnvironment" _environment;
@"ULLogicAdapter" _logicAdapter;
@"ULServer" _server;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableSet",&,N,V_signals) signals;
@property (T@"ULEnvironment",&,N,V_environment) environment;
@property (T@"ULLogicAdapter",&,N,V_logicAdapter) logicAdapter;
@property (T@"ULServer",&,N,V_server) server;
```

## Class methods

```
+[ULLifeCycleManager _createIfCondition:block:];
```

## Instance methods

```
-[ULLifeCycleManager setEnvironment:];
-[ULLifeCycleManager setServer:];
-[ULLifeCycleManager server];
-[ULLifeCycleManager _start];
-[ULLifeCycleManager init];
-[ULLifeCycleManager setSignals:];
-[ULLifeCycleManager dealloc];
-[ULLifeCycleManager start];
-[ULLifeCycleManager queue];
-[ULLifeCycleManager signals];
-[ULLifeCycleManager environment];
-[ULLifeCycleManager setQueue:];
-[ULLifeCycleManager _createSourceForSignal:withBlock:];
-[ULLifeCycleManager _exitWithDate:];
-[ULLifeCycleManager _spinUpListeners];
-[ULLifeCycleManager _spinUpModulesConstructorsAndDependencies];
-[ULLifeCycleManager _spinUpSignals];
-[ULLifeCycleManager _spinUpWakeUpNotifications];
-[ULLifeCycleManager logicAdapter];
-[ULLifeCycleManager setLogicAdapter:];
```
