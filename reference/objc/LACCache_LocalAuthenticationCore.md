# `LACCache`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"LACThreadSafeDictionary" _cachedValues;
@"NSObject<OS_dispatch_queue>" _workQueue;
d _timeout;
```

## Properties

```
@property (Td,N,V_timeout) timeout;
```

## Instance methods

```
-[LACCache initWithTimeout:];
-[LACCache timeout];
-[LACCache invalidate];
-[LACCache setTimeout:];
-[LACCache _identifierForParameter:];
-[LACCache _invalidateCachedValue:identifier:];
-[LACCache cachedValueWithParameter:];
-[LACCache setCachedValue:withParameter:];
```
