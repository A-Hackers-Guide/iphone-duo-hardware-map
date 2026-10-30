# `AVVCSessionFactory`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSMutableDictionary" _sessionManagerMap;
@"AVVCSessionManager" _primarySessionManager;
@? _sessionWasCreatedBlock;
@? _sessionWillBeDestroyedBlock;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"NSMutableDictionary",&,N,V_sessionManagerMap) sessionManagerMap;
@property (T@"AVVCSessionManager",&,N,V_primarySessionManager) primarySessionManager;
@property (T@?,C,N,V_sessionWasCreatedBlock) sessionWasCreatedBlock;
@property (T@?,C,N,V_sessionWillBeDestroyedBlock) sessionWillBeDestroyedBlock;
```

## Class methods

```
+[AVVCSessionFactory sharedInstance];
```

## Instance methods

```
-[AVVCSessionFactory setWorkQueue:];
-[AVVCSessionFactory init];
-[AVVCSessionFactory workQueue];
-[AVVCSessionFactory cleanupContext:];
-[AVVCSessionFactory setSessionWillBeDestroyedBlock:];
-[AVVCSessionFactory _wqCreateAuxSessionAndManagerForDeviceUID:clientType:session:manager:error:];
-[AVVCSessionFactory _wqCreatePrimarySessionManagerIfNeeded:clientType:error:];
-[AVVCSessionFactory _wqSessionAndManagerForContext:clientType:session:manager:error:];
-[AVVCSessionFactory auxSessionManagers];
-[AVVCSessionFactory primarySessionManager];
-[AVVCSessionFactory releasePrimarySessionManager];
-[AVVCSessionFactory sessionForContext:clientType:completion:];
-[AVVCSessionFactory sessionForContext:clientType:error:];
-[AVVCSessionFactory sessionForContext:completion:];
-[AVVCSessionFactory sessionForContext:error:];
-[AVVCSessionFactory sessionManagerForContext:clientType:completion:];
-[AVVCSessionFactory sessionManagerForContext:clientType:error:];
-[AVVCSessionFactory sessionManagerMap];
-[AVVCSessionFactory sessionWasCreatedBlock];
-[AVVCSessionFactory sessionWillBeDestroyedBlock];
-[AVVCSessionFactory setPrimarySessionManager:];
-[AVVCSessionFactory setSessionManagerMap:];
-[AVVCSessionFactory setSessionWasCreatedBlock:];
```
