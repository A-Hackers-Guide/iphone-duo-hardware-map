# `_SBFContinuityUnlockAuthenticationStatusProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFAuthenticationStatusProvider`
- 2 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBFMobileKeyBag" _keybag;
@"<SBFAuthenticationStatusProvider>" _underlyingProvider;
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
-[_SBFContinuityUnlockAuthenticationStatusProvider isAuthenticated];
-[_SBFContinuityUnlockAuthenticationStatusProvider revokeAuthenticationIfNecessaryForPublicReason:];
-[_SBFContinuityUnlockAuthenticationStatusProvider revokeAuthenticationImmediatelyIfNecessaryForPublicReason:];
-[_SBFContinuityUnlockAuthenticationStatusProvider hasAuthenticatedAtLeastOnceSinceBoot];
-[_SBFContinuityUnlockAuthenticationStatusProvider hasPasscodeSet];
-[_SBFContinuityUnlockAuthenticationStatusProvider revokeAuthenticationImmediatelyForPublicReason:];
-[_SBFContinuityUnlockAuthenticationStatusProvider isAuthenticatedCached];
-[_SBFContinuityUnlockAuthenticationStatusProvider initWithMobileKeyBag:underlyingProvider:];
```
