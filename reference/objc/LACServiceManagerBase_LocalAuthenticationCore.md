# `LACServiceManagerBase`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LACServiceBase`
- Protocols: `LACServiceManager`
- 1 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _sessions;
```

## Properties

```
@property (TQ,R,N) sessionsCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACServiceManagerBase init];
-[LACServiceManagerBase exportedInterface];
-[LACServiceManagerBase shutdownSessionsWithMatchingID:];
-[LACServiceManagerBase _shutdownSessionsWithServiceType:];
-[LACServiceManagerBase allowsMultipleClientsForServiceType:];
-[LACServiceManagerBase bootstrapServiceWithType:clientConnection:completionHandler:];
-[LACServiceManagerBase bootstrapSessionServiceType:clientID:clientConnection:completionHandler:];
-[LACServiceManagerBase bootstrapSessionServiceType:clientID:completionHandler:];
-[LACServiceManagerBase sessionsCount];
```
