# `_UISceneOpenItemProvidersDataTransferSessionManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneOpenItemProvidersDataTransferSessionDelegate`
- 2 instance variables, 6 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _sessions;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_sessions) sessions;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISceneOpenItemProvidersDataTransferSessionManager sharedInstance];
```

## Instance methods

```
-[_UISceneOpenItemProvidersDataTransferSessionManager setWorkQueue:];
-[_UISceneOpenItemProvidersDataTransferSessionManager init];
-[_UISceneOpenItemProvidersDataTransferSessionManager sessions];
-[_UISceneOpenItemProvidersDataTransferSessionManager workQueue];
-[_UISceneOpenItemProvidersDataTransferSessionManager setSessions:];
-[_UISceneOpenItemProvidersDataTransferSessionManager addSession:];
-[_UISceneOpenItemProvidersDataTransferSessionManager dataTransferSessionBeganTransfers:];
-[_UISceneOpenItemProvidersDataTransferSessionManager dataTransferSessionFinishedTransfers:];
```
