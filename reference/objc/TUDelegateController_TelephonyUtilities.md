# `TUDelegateController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _delegateLock;
@"NSMapTable" _delegateToQueue;
```

## Properties

```
@property (T{os_unfair_lock_s=I},R,N,V_delegateLock) delegateLock;
@property (T@"NSMapTable",R,N,V_delegateToQueue) delegateToQueue;
```

## Instance methods

```
-[TUDelegateController removeDelegate:];
-[TUDelegateController addDelegate:queue:];
-[TUDelegateController delegateToQueue];
-[TUDelegateController init];
-[TUDelegateController delegateLock];
-[TUDelegateController enumerateDelegatesUsingBlock:];
```
