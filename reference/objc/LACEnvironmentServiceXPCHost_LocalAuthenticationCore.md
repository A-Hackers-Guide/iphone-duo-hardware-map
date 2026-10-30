# `LACEnvironmentServiceXPCHost`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACEnvironmentServiceXPC`
- 3 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"LACEnvironmentDependencies" _dependencies;
@"NSMutableDictionary" _stateForUser;
@"NSObject<OS_dispatch_queue>" _workQueue;
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
-[LACEnvironmentServiceXPCHost environmentStateForUser:completion:];
-[LACEnvironmentServiceXPCHost initWithDependencies:workQueue:];
```
