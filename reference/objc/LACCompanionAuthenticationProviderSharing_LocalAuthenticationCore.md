# `LACCompanionAuthenticationProviderSharing`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACSharingManagerDelegate`, `LACCompanionAuthenticationProviding`
- 3 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
q _companion;
@"<LACSharingManaging>" _sharingManager;
@"<LACCompanionAuthenticationProviderDelegate>" delegate;
```

## Properties

```
@property (T@"<LACCompanionAuthenticationProviderDelegate>",W,N,Vdelegate) delegate;
@property (TB,R,N) isAvailable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACCompanionAuthenticationProviderSharing isAvailable];
-[LACCompanionAuthenticationProviderSharing setDelegate:];
-[LACCompanionAuthenticationProviderSharing delegate];
-[LACCompanionAuthenticationProviderSharing _domainStateDictionaryForJoinedIDs:];
-[LACCompanionAuthenticationProviderSharing authenticateWithRequest:];
-[LACCompanionAuthenticationProviderSharing cancelAuthenticationWithID:];
-[LACCompanionAuthenticationProviderSharing domainStateForRequest:completion:];
-[LACCompanionAuthenticationProviderSharing initForCompanion:replyQueue:];
-[LACCompanionAuthenticationProviderSharing manager:didCompleteSessionWithID:];
-[LACCompanionAuthenticationProviderSharing manager:didFailSessionWithID:error:];
-[LACCompanionAuthenticationProviderSharing manager:didStartSessionWithID:];
```
