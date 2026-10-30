# `LACSharedModeDataSourceFTRCAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACSharedModeDataSource`
- 2 instance variables, 4 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"TUUIXPCClientConnection" _inCallService;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACSharedModeDataSourceFTRCAdapter _workQueue];
+[LACSharedModeDataSourceFTRCAdapter _callCenter];
```

## Instance methods

```
-[LACSharedModeDataSourceFTRCAdapter dealloc];
-[LACSharedModeDataSourceFTRCAdapter initWithReplyQueue:];
-[LACSharedModeDataSourceFTRCAdapter _performFetchSharedModeWithCompletion:];
-[LACSharedModeDataSourceFTRCAdapter fetchSharedModeWithOptions:completion:];
```
