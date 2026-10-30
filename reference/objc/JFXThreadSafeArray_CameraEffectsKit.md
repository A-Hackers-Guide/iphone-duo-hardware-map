# `JFXThreadSafeArray`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _array;
@"NSObject<OS_dispatch_queue>" _concurrentQueue;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_array) array;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_concurrentQueue) concurrentQueue;
@property (TQ,R) count;
```

## Instance methods

```
-[JFXThreadSafeArray setConcurrentQueue:];
-[JFXThreadSafeArray concurrentQueue];
-[JFXThreadSafeArray sortUsingSelector:];
-[JFXThreadSafeArray replaceObjectAtIndex:withObject:];
-[JFXThreadSafeArray init];
-[JFXThreadSafeArray setArray:];
-[JFXThreadSafeArray addObject:];
-[JFXThreadSafeArray count];
-[JFXThreadSafeArray insertObject:atIndex:];
-[JFXThreadSafeArray enumerateObjectsUsingBlock:];
-[JFXThreadSafeArray sortedArrayUsingComparator:];
-[JFXThreadSafeArray indexOfObject:];
-[JFXThreadSafeArray removeObjectsInArray:];
-[JFXThreadSafeArray removeObjectAtIndex:];
-[JFXThreadSafeArray objectsAtIndexes:];
-[JFXThreadSafeArray enumerateObjectsWithOptions:usingBlock:];
-[JFXThreadSafeArray description];
-[JFXThreadSafeArray removeObject:];
-[JFXThreadSafeArray containsObject:];
-[JFXThreadSafeArray array];
-[JFXThreadSafeArray objectAtIndex:];
-[JFXThreadSafeArray removeAllObjects];
-[JFXThreadSafeArray moveObjectAtIndex:toIndex:];
-[JFXThreadSafeArray copyOfArray];
```
