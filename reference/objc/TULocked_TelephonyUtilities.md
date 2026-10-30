# `TULocked`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _lock;
@ _object;
```

## Instance methods

```
-[TULocked initWithObject:];
-[TULocked debugDescription];
-[TULocked setObject:];
-[TULocked description];
-[TULocked object];
-[TULocked performWhileLocked:];
-[TULocked unfairLockForTesting];
```
