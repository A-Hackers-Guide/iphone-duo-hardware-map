# `AVCurrentMediaSelectionCache`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
@"AVAsset" _asset;
@"AVMediaSelection" _currentMediaSelection;
@"NSMutableDictionary" _mediaOptionsSelectedByClient;
```

## Class methods

```
+[AVCurrentMediaSelectionCache initialize];
```

## Instance methods

```
-[AVCurrentMediaSelectionCache dealloc];
-[AVCurrentMediaSelectionCache initWithAsset:];
-[AVCurrentMediaSelectionCache cachedCurrentMediaSelection];
-[AVCurrentMediaSelectionCache clientSelectedOrEmptyMediaSelection];
-[AVCurrentMediaSelectionCache mediaOptionsSelectedByClient];
-[AVCurrentMediaSelectionCache mediaOptionsSelectedByClientForKey:];
-[AVCurrentMediaSelectionCache propertyListForMediaSelection:forGroup:];
-[AVCurrentMediaSelectionCache removeMediaOptionsSelectedByClient];
-[AVCurrentMediaSelectionCache selectMediaOption:inMediaSelectionGroup:];
-[AVCurrentMediaSelectionCache setMediaOptionsSelectedByClient:forKey:];
-[AVCurrentMediaSelectionCache updateCurrentMediaSelection:];
```
