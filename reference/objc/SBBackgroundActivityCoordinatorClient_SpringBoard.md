# `SBBackgroundActivityCoordinatorClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
@"NSSet" _registeredBackgroundActivityIdentifiers;
@"NSObject<OS_dispatch_queue>" _registeredOverridesQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_registeredOverridesQueue) registeredOverridesQueue;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"NSSet",C,N,V_registeredBackgroundActivityIdentifiers) registeredBackgroundActivityIdentifiers;
```

## Instance methods

```
-[SBBackgroundActivityCoordinatorClient connection];
-[SBBackgroundActivityCoordinatorClient setConnection:];
-[SBBackgroundActivityCoordinatorClient acquireAssertionAndDeliverTapContextToClient:];
-[SBBackgroundActivityCoordinatorClient initWithConnection:andBackgroundActivityIdentifiers:];
-[SBBackgroundActivityCoordinatorClient registeredBackgroundActivityIdentifiers];
-[SBBackgroundActivityCoordinatorClient registeredOverridesQueue];
-[SBBackgroundActivityCoordinatorClient setRegisteredBackgroundActivityIdentifiers:];
-[SBBackgroundActivityCoordinatorClient setRegisteredOverridesQueue:];
```
