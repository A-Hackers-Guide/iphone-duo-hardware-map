# `LACSharedModeProcessor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACEvaluationRequestProcessor`
- 4 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"<LACSharedModeDataSource>" _dataSource;
@"<LACSharedModePolicyCoordinator>" _policyCoordinator;
@"<LACSharedModePolicyTraitsManager>" _policyTraitsManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACSharedModeProcessor processRequest:configuration:completion:];
-[LACSharedModeProcessor _processRequest:completion:];
-[LACSharedModeProcessor initWithReplyQueue:dataSource:policyTraitsManager:policyCoordinator:];
-[LACSharedModeProcessor canProcessRequest:];
```
