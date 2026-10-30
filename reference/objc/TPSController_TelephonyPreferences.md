# `TPSController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _delegateLock;
@"NSMapTable" _delegateToQueue;
```

## Properties

```
@property (T{os_unfair_lock_s=I},N,V_delegateLock) delegateLock;
@property (T@"NSMapTable",R,N,V_delegateToQueue) delegateToQueue;
```

## Instance methods

```
-[TPSController removeDelegate:];
-[TPSController addDelegate:queue:];
-[TPSController delegateToQueue];
-[TPSController init];
-[TPSController delegateLock];
-[TPSController setDelegateLock:];
-[TPSController performAtomicDelegateBlock:];
```
