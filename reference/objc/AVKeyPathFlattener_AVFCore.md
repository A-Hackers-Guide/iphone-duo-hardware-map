# `AVKeyPathFlattener`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVKeyPathDependencyHost`, `AVWeakObservable`
- 3 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"AVKeyPathDependencyManager" _dependencyManager;
@"AVTwoPartKeyPath" _dependencyKeyPath;
@"NSObject" _observedObject;
```

## Properties

```
@property (T@,R,N) dependentProperty;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVKeyPathFlattener init];
-[AVKeyPathFlattener dealloc];
-[AVKeyPathFlattener observedObject];
-[AVKeyPathFlattener addCallbackToCancelDuringDeallocation:];
-[AVKeyPathFlattener declareKeyPathDependenciesWithRegistry:];
-[AVKeyPathFlattener dependentProperty];
-[AVKeyPathFlattener initForObservingValueAtKeyPath:onObject:];
-[AVKeyPathFlattener topLevelDependencyProperty];
```
