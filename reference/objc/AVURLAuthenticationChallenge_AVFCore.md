# `AVURLAuthenticationChallenge`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLAuthenticationChallenge`
- Protocols: `AVAssetResourceLoaderRequest`
- 3 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _weakReference;
Q _requestID;
^{__CFDictionary=} _requestInfo;
```

## Properties

```
@property (TQ,R,N) _requestID;
@property (T^{__CFDictionary=},R,N,V_requestInfo) _requestInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVURLAuthenticationChallenge _selectorForInformingDelegateOfCancellationByFig];
```

## Instance methods

```
-[AVURLAuthenticationChallenge _requestID];
-[AVURLAuthenticationChallenge initWithProtectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:];
-[AVURLAuthenticationChallenge init];
-[AVURLAuthenticationChallenge dealloc];
-[AVURLAuthenticationChallenge initWithAuthenticationChallenge:sender:];
-[AVURLAuthenticationChallenge _weakReference];
-[AVURLAuthenticationChallenge _requestInfo];
-[AVURLAuthenticationChallenge initWithAuthenticationChallenge:sender:requestInfo:requestID:];
-[AVURLAuthenticationChallenge _shouldInformDelegateOfFigCancellation];
-[AVURLAuthenticationChallenge _performCancellationByClient];
```
