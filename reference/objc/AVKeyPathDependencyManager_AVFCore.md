# `AVKeyPathDependencyManager`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVKeyPathDependencyRegistration`
- 3 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" _weakReferenceToDependencyHost;
@"AVWeakObservableCallbackCancellationHelper" _callbackCancellationHelper;
@"NSMutableSet" _keyPathDependencies;
```

## Instance methods

```
-[AVKeyPathDependencyManager dealloc];
-[AVKeyPathDependencyManager addCallbackToCancel:];
-[AVKeyPathDependencyManager cancelAllCallbacks];
-[AVKeyPathDependencyManager dependencyHostIsFullyInitialized];
-[AVKeyPathDependencyManager initWithDependencyHost:];
-[AVKeyPathDependencyManager valueForKey:dependsOnValueAtKeyPath:];
```
