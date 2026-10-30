# `JFXThreadSafeDictionary`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _dict;
@"NSObject<OS_dispatch_queue>" _concurrentQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_dict) dict;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_concurrentQueue) concurrentQueue;
@property (TQ,R) count;
@property (T@"NSArray",R) allKeys;
@property (T@"NSArray",R) allValues;
```

## Instance methods

```
-[JFXThreadSafeDictionary setDictionary:];
-[JFXThreadSafeDictionary setConcurrentQueue:];
-[JFXThreadSafeDictionary concurrentQueue];
-[JFXThreadSafeDictionary addEntriesFromDictionary:];
-[JFXThreadSafeDictionary init];
-[JFXThreadSafeDictionary dealloc];
-[JFXThreadSafeDictionary count];
-[JFXThreadSafeDictionary setValue:forKey:];
-[JFXThreadSafeDictionary objectForKey:];
-[JFXThreadSafeDictionary valueForKey:];
-[JFXThreadSafeDictionary allValues];
-[JFXThreadSafeDictionary objectsForKeys:notFoundMarker:];
-[JFXThreadSafeDictionary removeObjectsForKeys:];
-[JFXThreadSafeDictionary description];
-[JFXThreadSafeDictionary setObject:forKey:];
-[JFXThreadSafeDictionary removeObjectForKey:];
-[JFXThreadSafeDictionary allKeys];
-[JFXThreadSafeDictionary removeAllObjects];
-[JFXThreadSafeDictionary dict];
-[JFXThreadSafeDictionary setDict:];
```
