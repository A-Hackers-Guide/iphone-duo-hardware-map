# `MGNotificationRegistration`

- Image: [`/usr/lib/libMobileGestaltExtensions.dylib`](../userland/usr__lib__libMobileGestaltExtensions.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _observers;
@"NSObject<OS_dispatch_queue>" _queue;
@? _block;
B _deliverNotifications;
@"NSMutableDictionary" _requestedRegistrations;
```

## Instance methods

```
-[MGNotificationRegistration dealloc];
-[MGNotificationRegistration start];
-[MGNotificationRegistration initWithQueue:block:];
-[MGNotificationRegistration cancel];
-[MGNotificationRegistration registerForNotification:argument:question:];
```
