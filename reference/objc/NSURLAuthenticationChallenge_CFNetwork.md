# `NSURLAuthenticationChallenge`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 6 properties, 15 instance methods, 3 class methods

## Instance variables

```
@"NSURLAuthenticationChallengeInternal" _internal;
```

## Properties

```
@property (T@"NSURLProtectionSpace",R,C) protectionSpace;
@property (T@"NSURLCredential",R,C) proposedCredential;
@property (Tq,R) previousFailureCount;
@property (T@"NSURLResponse",R,C) failureResponse;
@property (T@"NSError",R,C) error;
@property (T@"<NSURLAuthenticationChallengeSender>",R,&) sender;
```

## Class methods

```
+[NSURLAuthenticationChallenge supportsSecureCoding];
+[NSURLAuthenticationChallenge _createAuthenticationChallengeForCFAuthChallenge:sender:];
+[NSURLAuthenticationChallenge _authenticationChallengeForCFAuthChallenge:sender:];
```

## Instance methods

```
-[NSURLAuthenticationChallenge proposedCredential];
-[NSURLAuthenticationChallenge failureResponse];
-[NSURLAuthenticationChallenge initWithProtectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:];
-[NSURLAuthenticationChallenge init];
-[NSURLAuthenticationChallenge dealloc];
-[NSURLAuthenticationChallenge previousFailureCount];
-[NSURLAuthenticationChallenge error];
-[NSURLAuthenticationChallenge initWithAuthenticationChallenge:sender:];
-[NSURLAuthenticationChallenge protectionSpace];
-[NSURLAuthenticationChallenge sender];
-[NSURLAuthenticationChallenge encodeWithCoder:];
-[NSURLAuthenticationChallenge initWithCoder:];
-[NSURLAuthenticationChallenge setSender:];
-[NSURLAuthenticationChallenge _initWithListOfProtectionSpaces:CurrentProtectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:];
-[NSURLAuthenticationChallenge _createCFAuthChallenge];
```
