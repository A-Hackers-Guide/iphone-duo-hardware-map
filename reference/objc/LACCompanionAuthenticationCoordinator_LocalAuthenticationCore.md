# `LACCompanionAuthenticationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACCompanionAuthenticationProviderDelegate`, `LACDarwinNotificationCenterObserver`, `LACCompanionAuthenticationCoordinating`, `LACDomainStateProviding`
- 5 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<LACCompanionAuthenticationProviding>" authProvider;
q companion;
@"OS_dispatch_queue" replyQueue;
$__lazy_storage_$_mockedAuthProvider;
pendingSessions;
```

## Properties

```
@property (T@"<LACCompanionAuthenticationProviding>",N,&,VauthProvider) authProvider;
@property (Tq,N,R,Vcompanion) companion;
@property (T@"OS_dispatch_queue",N,R,VreplyQueue) replyQueue;
@property (T@"<LACCompanionAuthenticationProviding>",N,&) mockedAuthProvider;
@property (T@"<LACCompanionAuthenticationProviding>",N,R) authenticationProvider;
@property (T@"NSString",N,R) description;
@property (TB,N,R) isAvailable;
```

## Instance methods

```
-[LACCompanionAuthenticationCoordinator isAvailable];
-[LACCompanionAuthenticationCoordinator companion];
-[LACCompanionAuthenticationCoordinator init];
-[LACCompanionAuthenticationCoordinator dealloc];
-[LACCompanionAuthenticationCoordinator description];
-[LACCompanionAuthenticationCoordinator replyQueue];
-[LACCompanionAuthenticationCoordinator setAuthProvider:];
-[LACCompanionAuthenticationCoordinator authenticationProvider];
-[LACCompanionAuthenticationCoordinator authenticateRequest:completion:];
-[LACCompanionAuthenticationCoordinator authProvider];
-[LACCompanionAuthenticationCoordinator authenticationProvider:didCompleteAuthenticationWithID:];
-[LACCompanionAuthenticationCoordinator authenticationProvider:didFailAuthenticationWithID:error:];
-[LACCompanionAuthenticationCoordinator authenticationProvider:didStartAuthenticationWithID:];
-[LACCompanionAuthenticationCoordinator cancelAuthenticationForRequestIdentifier:];
-[LACCompanionAuthenticationCoordinator domainStateForRequest:completion:];
-[LACCompanionAuthenticationCoordinator initWithCompanion:replyQueue:];
-[LACCompanionAuthenticationCoordinator mockedAuthProvider];
-[LACCompanionAuthenticationCoordinator notificationCenter:didReceiveNotification:];
-[LACCompanionAuthenticationCoordinator setMockedAuthProvider:];
```
