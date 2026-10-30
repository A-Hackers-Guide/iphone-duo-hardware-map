# `_UISceneEventResponder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _sendLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _dataLock;
@"_UISceneEventResponse" _dataLock_first;
@"_UISceneEventResponse" _dataLock_last;
```

## Instance methods

```
-[_UISceneEventResponder init];
-[_UISceneEventResponder enqueuePostSynchronizeResponse:];
-[_UISceneEventResponder enqueuePostCommitResponse:];
```
