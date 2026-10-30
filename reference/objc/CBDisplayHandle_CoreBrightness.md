# `CBDisplayHandle`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBHandle`
- 1 instance variables, 0 properties, 10 instance methods, 6 class methods

## Instance variables

```
@"NSString" _cachedDescription;
```

## Class methods

```
+[CBDisplayHandle handleWithDisplayID:andUUID:];
+[CBDisplayHandle handleForUniqueID:];
+[CBDisplayHandle handleForDisplayID:];
+[CBDisplayHandle handleForUUID:];
+[CBDisplayHandle allDisplays];
+[CBDisplayHandle handleWithDisplayID:andUUID:andUniqueID:];
```

## Instance methods

```
-[CBDisplayHandle initWithUUID:];
-[CBDisplayHandle dealloc];
-[CBDisplayHandle initWithUniqueID:];
-[CBDisplayHandle copyDescription];
-[CBDisplayHandle matchesHandle:];
-[CBDisplayHandle initWithDisplayID:andUUID:andUniqueID:];
-[CBDisplayHandle description];
-[CBDisplayHandle initWithDisplayID:andUUID:];
-[CBDisplayHandle initWithDisplayID:];
-[CBDisplayHandle initForAll];
```
