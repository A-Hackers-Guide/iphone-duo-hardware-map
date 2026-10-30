# `SBHomeScreenConfigurationServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSHomeScreenConfigurationClientToServerInterface`, `BSServiceConnectionListenerDelegate`
- 6 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"<SBSHomeScreenConfigurationServerDelegate>" _delegate;
@"BSServiceConnectionListener" _listener;
@"FBServiceClientAuthenticator" _authenticator;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _connections;
@"BSServiceConnection" _configurationSessionConnection;
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
-[SBHomeScreenConfigurationServer listener:didReceiveConnection:withContext:];
-[SBHomeScreenConfigurationServer init];
-[SBHomeScreenConfigurationServer applyConfiguration:completion:];
-[SBHomeScreenConfigurationServer beginConfigurationSessionWithCompletion:];
-[SBHomeScreenConfigurationServer endConfigurationSessionWithCompletion:];
```
