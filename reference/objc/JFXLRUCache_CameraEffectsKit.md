# `JFXLRUCache`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _capacity;
@"NSMutableDictionary" _dictionary;
@"NSMutableOrderedSet" _keys;
@"NSObject<OS_dispatch_queue>" _cacheQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_dictionary) dictionary;
@property (T@"NSMutableOrderedSet",&,N,V_keys) keys;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_cacheQueue) cacheQueue;
@property (TQ,N,V_capacity) capacity;
@property (TQ,R) count;
```

## Instance methods

```
-[JFXLRUCache setCapacity:];
-[JFXLRUCache addEntriesFromDictionary:];
-[JFXLRUCache capacity];
-[JFXLRUCache dealloc];
-[JFXLRUCache dictionary];
-[JFXLRUCache count];
-[JFXLRUCache setKeys:];
-[JFXLRUCache cacheQueue];
-[JFXLRUCache objectForKey:];
-[JFXLRUCache keys];
-[JFXLRUCache objectsForKeys:notFoundMarker:];
-[JFXLRUCache initWithCapacity:];
-[JFXLRUCache setObject:forKey:];
-[JFXLRUCache removeObjectForKey:];
-[JFXLRUCache removeAllObjects];
-[JFXLRUCache JT_removeLeastRecentlyUsedIfAtCapacity];
-[JFXLRUCache JT_markRecentlyUsed:];
-[JFXLRUCache highMemoryWarning];
```
