# `SharedCredentialController`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ASAuthorizationControllerDelegate`, `ASAuthorizationControllerPresentationContextProviding`
- 6 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"ASAuthorizationPasswordProvider" _provider;
@"ASAuthorizationController" _controller;
@"ASPasswordCredential" _passwordCredential;
@"NSObject<OS_dispatch_semaphore>" _semaphore;
@"NSError" _error;
i _result;
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
-[SharedCredentialController dealloc];
-[SharedCredentialController error];
-[SharedCredentialController result];
-[SharedCredentialController _requestCredential];
-[SharedCredentialController authorizationController:didCompleteWithAuthorization:];
-[SharedCredentialController authorizationController:didCompleteWithError:];
-[SharedCredentialController passwordCredential];
-[SharedCredentialController presentationAnchorForAuthorizationController:];
```
