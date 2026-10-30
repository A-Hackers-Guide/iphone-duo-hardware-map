# `DCLRUCache`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSMapTable" mData;
@"NSMutableArray" mOrderedKeys;
Q mMax;
@"<DCLRUCacheDelegate>" _delegate;
```

## Properties

```
@property (TQ,R,N,VmMax) maxSize;
@property (T@"NSArray",R,N) allKeys;
@property (T@"<DCLRUCacheDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[DCLRUCache cacheCollection];
+[DCLRUCache purgeAllCaches];
```

## Instance methods

```
-[DCLRUCache initWithMaxSize:];
-[DCLRUCache maxSize];
-[DCLRUCache objectForKey:];
-[DCLRUCache setDelegate:];
-[DCLRUCache delegate];
-[DCLRUCache setObject:forKey:];
-[DCLRUCache removeObjectForKey:];
-[DCLRUCache allKeys];
-[DCLRUCache removeAllObjects];
-[DCLRUCache p_removeOldestObject];
```
