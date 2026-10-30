# `LACTimer`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACTimer`
- 2 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _timer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _timerLock;
```

## Properties

```
@property (TB,R,N) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACTimer isRunning];
-[LACTimer init];
-[LACTimer dealloc];
-[LACTimer cancel];
-[LACTimer _dispatchAfter:inQueue:repeat:block:];
-[LACTimer dispatchAfter:inQueue:block:];
-[LACTimer dispatchAfter:inQueue:repeat:block:];
```
