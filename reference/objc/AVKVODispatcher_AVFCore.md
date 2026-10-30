# `AVKVODispatcher`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"AVCallbackContextRegistry" _callbackContextRegistry;
```

## Class methods

```
+[AVKVODispatcher sharedKVODispatcher];
```

## Instance methods

```
-[AVKVODispatcher observeValueForKeyPath:ofObject:change:context:];
-[AVKVODispatcher startObservingObject:weakObserver:forTwoPartKeyPath:options:context:];
-[AVKVODispatcher dealloc];
-[AVKVODispatcher initWithDescriptionOfHowAllObservedPropertyChangesAreSerializedWithDispatcherDeallocation:];
-[AVKVODispatcher startObservingValueAtTwoPartKeyPath:ofObject:options:usingBlock:];
-[AVKVODispatcher startObservingObject:weakObserver:forKeyPath:options:context:];
-[AVKVODispatcher startObservingValueAtKeyPath:withoutKeepingAliveObservedObject:options:usingBlock:];
-[AVKVODispatcher startObservingValueAtKeyPath:ofObject:options:usingBlock:];
```
