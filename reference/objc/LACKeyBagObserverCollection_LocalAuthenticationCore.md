# `LACKeyBagObserverCollection`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"LACThreadSafeCollection" _observers;
q _lastPublishedState;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[LACKeyBagObserverCollection initWithState:];
-[LACKeyBagObserverCollection removeObserver:];
-[LACKeyBagObserverCollection addObserver:];
-[LACKeyBagObserverCollection publishKeybagStateUpdate:state:];
```
