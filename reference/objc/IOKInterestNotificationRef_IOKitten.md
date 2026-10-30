# `IOKInterestNotificationRef`

- Image: [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](../userland/System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _lock;
@"IOKInterestNotification" _notification;
```

## Properties

```
@property (T@"IOKInterestNotification",N,V_notification) notification;
```

## Instance methods

```
-[IOKInterestNotificationRef notification];
-[IOKInterestNotificationRef init];
-[IOKInterestNotificationRef setNotification:];
-[IOKInterestNotificationRef lock];
-[IOKInterestNotificationRef unlock];
```
