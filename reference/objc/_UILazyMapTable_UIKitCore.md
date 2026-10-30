# `_UILazyMapTable`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@? _mappingBlock;
@"NSMapTable" _keysToClientTables;
@"NSMapTable" _keysToValues;
@"NSMapTable" _valuesToKeys;
```

## Instance methods

```
-[_UILazyMapTable count];
-[_UILazyMapTable cachedObjects];
-[_UILazyMapTable objectForKey:];
-[_UILazyMapTable keys];
-[_UILazyMapTable description];
-[_UILazyMapTable cachedObjectEnumerable];
-[_UILazyMapTable hasCachedObjectForKey:];
-[_UILazyMapTable initWithMappingBlock:];
-[_UILazyMapTable keyEnumerable];
-[_UILazyMapTable registerClient:ofObjectForKey:];
-[_UILazyMapTable unregisterClient:ofObjectForKey:];
```
