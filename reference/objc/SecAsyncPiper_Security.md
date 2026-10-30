# `SecAsyncPiper`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"NSFileHandle" _readHandle;
@"NSObject<OS_xpc_object>" _writeXpcFd;
@"NSMutableData" _bigData;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_semaphore>" _semaForTestingOnly;
```

## Properties

```
@property (T@"NSFileHandle",&,V_readHandle) readHandle;
@property (T@"NSObject<OS_xpc_object>",&,V_writeXpcFd) writeXpcFd;
@property (T@"NSMutableData",&,V_bigData) bigData;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_semaForTestingOnly) semaForTestingOnly;
```

## Class methods

```
+[SecAsyncPiper forTestingOnlySetFailPipe:];
+[SecAsyncPiper forTestingOnlySetFailXpcFdWrapping:];
```

## Instance methods

```
-[SecAsyncPiper initWithError:];
-[SecAsyncPiper queue];
-[SecAsyncPiper setQueue:];
-[SecAsyncPiper waitAndReleaseFd_ForTestingOnly];
-[SecAsyncPiper bigData];
-[SecAsyncPiper dictWithError:];
-[SecAsyncPiper moreData];
-[SecAsyncPiper readHandle];
-[SecAsyncPiper semaForTestingOnly];
-[SecAsyncPiper setBigData:];
-[SecAsyncPiper setReadHandle:];
-[SecAsyncPiper setSemaForTestingOnly:];
-[SecAsyncPiper setWriteXpcFd:];
-[SecAsyncPiper writeXpcFd];
-[SecAsyncPiper xpcFd];
```
