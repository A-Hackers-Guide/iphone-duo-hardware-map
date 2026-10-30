# `AVWeaklyObservedObjectClientBlockKVONotifier`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVKVONotifier`
- 8 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"AVCallbackContextRegistry" _callbackContextRegistry;
^v _callbackContextToken;
@"NSObject" _observer;
@"AVWeakReference" _weakReferenceToObject;
@"NSObject<AVWeakObservable>" _unsafeUnretainedObject;
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
```

## Instance methods

```
-[AVWeaklyObservedObjectClientBlockKVONotifier callbackDidFireWithChangeDictionary:];
-[AVWeaklyObservedObjectClientBlockKVONotifier dealloc];
-[AVWeaklyObservedObjectClientBlockKVONotifier start];
-[AVWeaklyObservedObjectClientBlockKVONotifier cancelCallbacks];
-[AVWeaklyObservedObjectClientBlockKVONotifier initWithCallbackContextRegistry:observer:object:keyPath:options:block:];
```
