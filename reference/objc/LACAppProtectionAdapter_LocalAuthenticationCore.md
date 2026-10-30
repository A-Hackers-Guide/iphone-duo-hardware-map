# `LACAppProtectionAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAppProtectionProviding`
- 2 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"LACBackgroundTaskQueued" _backgroundTask;
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
-[LACAppProtectionAdapter initWithWorkQueue:];
-[LACAppProtectionAdapter _lockedBundleIDsFromResult:];
-[LACAppProtectionAdapter lockedAppBundleIdentifiersWithCompletion:];
```
