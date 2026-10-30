# `LACThreadSafeCollection`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LACThreadSafeObject`
- 1 instance variables, 0 properties, 7 instance methods, 2 class methods

## Instance variables

```
B _weakObjects;
```

## Class methods

```
+[LACThreadSafeCollection strongObjectsCollection];
+[LACThreadSafeCollection weakObjectsCollection];
```

## Instance methods

```
-[LACThreadSafeCollection remove:];
-[LACThreadSafeCollection append:];
-[LACThreadSafeCollection count];
-[LACThreadSafeCollection containsObject:];
-[LACThreadSafeCollection removeAllObjects];
-[LACThreadSafeCollection forEach:];
-[LACThreadSafeCollection initWithWeakObjects:];
```
