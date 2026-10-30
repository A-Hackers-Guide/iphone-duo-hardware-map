# `_UIViewServiceReplyControlProxy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewServiceProxy_ReplyControl`
- 4 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@ _target;
@"_UIViewServiceReplyControlTrampoline" _controlTrampoline;
@"_UIViewServiceReplyAwaitingTrampoline" _awaitingTrampoline;
@"NSLock" _lock;
```

## Class methods

```
+[_UIViewServiceReplyControlProxy proxyWithTarget:];
```

## Instance methods

```
-[_UIViewServiceReplyControlProxy forwardingTargetForSelector:];
-[_UIViewServiceReplyControlProxy methodSignatureForSelector:];
-[_UIViewServiceReplyControlProxy respondsToSelector:];
-[_UIViewServiceReplyControlProxy _awaitingReply];
-[_UIViewServiceReplyControlProxy _deliveringRepliesAsynchronously];
```
