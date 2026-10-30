# `AVCallbackContextRegistry`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _contextsForTokens;
Q _currentToken;
@"NSObject<OS_dispatch_queue>" _readWriteQueue;
```

## Class methods

```
+[AVCallbackContextRegistry initialize];
+[AVCallbackContextRegistry sharedCallbackContextRegistry];
```

## Instance methods

```
-[AVCallbackContextRegistry callbackContextForToken:];
-[AVCallbackContextRegistry init];
-[AVCallbackContextRegistry registerCallbackContextObject:];
-[AVCallbackContextRegistry dealloc];
-[AVCallbackContextRegistry unregisterCallbackContextForToken:];
```
