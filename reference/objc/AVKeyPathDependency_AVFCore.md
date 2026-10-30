# `AVKeyPathDependency`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _subObjectRegistrationQueue;
@"AVKVODispatcher" _KVODispatcher;
@"AVWeakReference" _weakReferenceToObject;
@"NSString" _dependentKey;
@"AVTwoPartKeyPath" _dependencyKeyPath;
@"<AVCallbackCancellation>" _leafPropertyChangeNotifier;
```

## Class methods

```
+[AVKeyPathDependency initialize];
```

## Instance methods

```
-[AVKeyPathDependency _reactToTopLevelPropertyChange:];
-[AVKeyPathDependency dealloc];
-[AVKeyPathDependency initializationIsCompleteForObject:];
-[AVKeyPathDependency _startObservingSecondLevelPropertyOnNewCurrentValueForTopLevelDependencyProperty:];
-[AVKeyPathDependency _reactToSecondLevelPropertyChange:];
-[AVKeyPathDependency description];
-[AVKeyPathDependency initWithObject:thatHasPropertyWithKey:whoseValueDependsOnValueAtKeyPath:];
```
