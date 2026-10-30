# `LACAnalyticsServiceXPCHost`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAnalyticsServiceXPC`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSPointerArray" _sessions;
```

## Instance methods

```
-[LACAnalyticsServiceXPCHost initWithWorkQueue:];
-[LACAnalyticsServiceXPCHost connectSessionForContext:reply:];
-[LACAnalyticsServiceXPCHost sessionForContextUUID:];
-[LACAnalyticsServiceXPCHost startSessionForContext:dialogID:bundleID:reply:];
```
