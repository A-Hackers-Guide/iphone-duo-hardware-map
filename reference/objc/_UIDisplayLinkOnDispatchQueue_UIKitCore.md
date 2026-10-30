# `_UIDisplayLinkOnDispatchQueue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _targetLock;
@ _target;
: _selector;
@"NSObject<OS_dispatch_queue>" _queue;
^{_opaque_pthread_t=q^{__darwin_pthread_handler_rec}[8176c]} _thread;
(?="startedSemaphore"@"NSObject<OS_dispatch_semaphore>""ref"^{__CFRunLoop}) _runLoop;
```

## Instance methods

```
-[_UIDisplayLinkOnDispatchQueue _displayLinkFired:];
-[_UIDisplayLinkOnDispatchQueue dealloc];
```
