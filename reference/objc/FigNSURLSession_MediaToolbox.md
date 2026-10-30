# `FigNSURLSession`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 11 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSURLSessionConfiguration" _configuration;
@"NSURLSession" _session;
@"<NSURLSessionDataDelegate>" _dataDelegate;
@"NSOperationQueue" _opQueue;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"NSString" _clientBundleIdentifier;
@"NSString" _clientPersonaIdentifier;
^{OpaqueFigCFWeakReferenceHolder=} _weakAssertion;
q _doomTime;
i _deferReleaseSeconds;
B _doomCheckScheduled;
i _assertionCount;
@"NSObject<OS_os_transaction>" _transaction;
B _usesNWLoader;
```

## Properties

```
@property (T@"NSURLSession",R,N,V_session) session;
@property (T@"<NSURLSessionDataDelegate>",R,N,V_dataDelegate) dataDelegate;
@property (T@"NSOperationQueue",R,N,V_opQueue) opQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_dispatchQueue) dispatchQueue;
@property (T@"NSString",R,N,V_clientBundleIdentifier) clientBundleIdentifier;
@property (T@"NSString",R,N,V_clientPersonaIdentifier) clientPersonaIdentifier;
@property (TB,R,N,V_usesNWLoader) usesNWLoader;
@property (Tq,N,V_doomTime) doomTime;
@property (Ti,N,V_deferReleaseSeconds) deferReleaseSeconds;
@property (TB,N,V_doomCheckScheduled) doomCheckScheduled;
@property (Ti,N,V_assertionCount) assertionCount;
```

## Instance methods

```
-[FigNSURLSession debug];
-[FigNSURLSession dispatchQueue];
-[FigNSURLSession initWithClientBundleIdentifier:clientPersonaIdentifier:dispatchQueue:useNWLoader:createOptions:];
-[FigNSURLSession dealloc];
-[FigNSURLSession clientPersonaIdentifier];
-[FigNSURLSession releaseOSTransaction];
-[FigNSURLSession setDoomTime:];
-[FigNSURLSession usesNWLoader];
-[FigNSURLSession acquireAssertion];
-[FigNSURLSession doomTime];
-[FigNSURLSession clientBundleIdentifier];
-[FigNSURLSession setDeferReleaseSeconds:];
-[FigNSURLSession setDoomCheckScheduled:];
-[FigNSURLSession dataDelegate];
-[FigNSURLSession opQueue];
-[FigNSURLSession acquireOSTransaction];
-[FigNSURLSession deferReleaseSeconds];
-[FigNSURLSession session];
-[FigNSURLSession assertionCount];
-[FigNSURLSession doomCheckScheduled];
-[FigNSURLSession setAssertionCount:];
```
