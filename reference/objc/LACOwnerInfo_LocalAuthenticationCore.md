# `LACOwnerInfo`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 0 class methods

## Instance variables

```
i _pid;
@? _invalidationBlock;
@ _proxy;
```

## Properties

```
@property (Ti,R,N,V_pid) pid;
@property (T@?,R,N,V_invalidationBlock) invalidationBlock;
@property (T@,R,W,N,V_proxy) proxy;
```

## Instance methods

```
-[LACOwnerInfo proxy];
-[LACOwnerInfo pid];
-[LACOwnerInfo invalidationBlock];
-[LACOwnerInfo initWithProcessId:proxy:invalidationBlock:];
```
