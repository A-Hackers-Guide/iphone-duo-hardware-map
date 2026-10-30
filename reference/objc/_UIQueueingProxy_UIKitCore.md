# `_UIQueueingProxy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITargetedProxy`
- 5 instance variables, 1 properties, 9 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _suspensionCount;
@"NSMutableArray" _queuedInvocations;
@? _shouldSuspendInvocationBlock;
B _bypassSuspension;
```

## Properties

```
@property (TB,N) bypassSuspensionForSynchronousReply;
```

## Class methods

```
+[_UIQueueingProxy proxyWithTarget:];
+[_UIQueueingProxy proxyWithTarget:shouldSuspendInvocationBlock:];
```

## Instance methods

```
-[_UIQueueingProxy suspend];
-[_UIQueueingProxy description];
-[_UIQueueingProxy respondsToSelector:];
-[_UIQueueingProxy forwardInvocation:];
-[_UIQueueingProxy resume];
-[_UIQueueingProxy _dispatchSuspendedMessages];
-[_UIQueueingProxy bypassSuspensionForSynchronousReply];
-[_UIQueueingProxy removeAllEnqueuedInvocations];
-[_UIQueueingProxy setBypassSuspensionForSynchronousReply:];
```
