# `AVClientBlockKVONotifier`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVKVONotifier`, `AVKVOIntrospection`
- 7 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"AVCallbackContextRegistry" _callbackContextRegistry;
^v _callbackContextToken;
@"NSObject" _observer;
@"NSObject" _object;
@"NSString" _keyPath;
Q _options;
@? _block;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject",R,N) observedObject;
```

## Instance methods

```
-[AVClientBlockKVONotifier callbackDidFireWithChangeDictionary:];
-[AVClientBlockKVONotifier dealloc];
-[AVClientBlockKVONotifier observedObject];
-[AVClientBlockKVONotifier start];
-[AVClientBlockKVONotifier cancelCallbacks];
-[AVClientBlockKVONotifier initWithCallbackContextRegistry:observer:object:keyPath:options:block:];
```
