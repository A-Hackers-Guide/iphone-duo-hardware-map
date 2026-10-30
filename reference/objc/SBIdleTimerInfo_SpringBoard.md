# `SBIdleTimerInfo`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<SBIdleTimerProviding>" _provider;
@"<SBFIdleTimerBehaviorProviding>" _behavior;
@"NSString" _reason;
@"SBIdleTimerProxy" _idleTimerProxy;
```

## Properties

```
@property (T@"<SBIdleTimerProviding>",R,W,N,V_provider) provider;
@property (T@"<SBFIdleTimerBehaviorProviding>",&,N,V_behavior) behavior;
@property (T@"NSString",C,N,V_reason) reason;
@property (T@"SBIdleTimerProxy",&,N,V_idleTimerProxy) idleTimerProxy;
```

## Instance methods

```
-[SBIdleTimerInfo provider];
-[SBIdleTimerInfo setReason:];
-[SBIdleTimerInfo setBehavior:];
-[SBIdleTimerInfo behavior];
-[SBIdleTimerInfo reason];
-[SBIdleTimerInfo idleTimerProxy];
-[SBIdleTimerInfo initWithProvider:behavior:reason:idleTimerProxy:];
-[SBIdleTimerInfo setIdleTimerProxy:];
```
