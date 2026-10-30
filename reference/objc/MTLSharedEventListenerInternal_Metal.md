# `MTLSharedEventListenerInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLSharedEventListener`
- 2 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
^{IONotificationPort=} _notificationPort;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Instance methods

```
-[MTLSharedEventListenerInternal dispatchQueue];
-[MTLSharedEventListenerInternal init];
-[MTLSharedEventListenerInternal dealloc];
-[MTLSharedEventListenerInternal _notifyEventPort:event:atValue:block:];
-[MTLSharedEventListenerInternal initWithDispatchQueue:];
```
