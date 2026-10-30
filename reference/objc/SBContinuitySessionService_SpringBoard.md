# `SBContinuitySessionService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBContinuitySessionServiceConnectionListenerDelegate`
- 3 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<_SBContinuitySessionServiceConnectionListening>" _serviceConnectionListener;
@"NSMapTable" _sessions;
@"<SBContinuitySessionFactory>" _sessionFactory;
```

## Properties

```
@property (T@"<SBContinuitySessionFactory>",W,N,V_sessionFactory) sessionFactory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuitySessionService init];
-[SBContinuitySessionService activate];
-[SBContinuitySessionService sessionFactory];
-[SBContinuitySessionService clientDidConnect:];
-[SBContinuitySessionService initWithServiceListenerFactory:];
-[SBContinuitySessionService clientDidDisconnect:];
-[SBContinuitySessionService setSessionFactory:];
```
