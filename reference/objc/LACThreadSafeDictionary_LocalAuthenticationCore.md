# `LACThreadSafeDictionary`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LACThreadSafeObject`
- 1 instance variables, 0 properties, 7 instance methods, 3 class methods

## Instance variables

```
B _hasWeakReferences;
```

## Class methods

```
+[LACThreadSafeDictionary strongToStrongObjectsMapTable];
+[LACThreadSafeDictionary strongToWeakObjectsMapTable];
+[LACThreadSafeDictionary weakToStrongObjectsMapTable];
```

## Instance methods

```
-[LACThreadSafeDictionary count];
-[LACThreadSafeDictionary objectForKey:];
-[LACThreadSafeDictionary setObject:forKey:];
-[LACThreadSafeDictionary removeObjectForKey:];
-[LACThreadSafeDictionary removeAllObjects];
-[LACThreadSafeDictionary forEach:];
-[LACThreadSafeDictionary initWithMapTable:hasWeakReferences:];
```
