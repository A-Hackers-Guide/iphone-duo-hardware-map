# `MTLIOMemoryInfo`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
^v memlist_key;
@"MTLIOAccelResource" fResourceListHead;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _memoryInfoLock;
```

## Class methods

```
+[MTLIOMemoryInfo initialize];
```

## Instance methods

```
-[MTLIOMemoryInfo shutdown];
-[MTLIOMemoryInfo addDataSource:];
-[MTLIOMemoryInfo init];
-[MTLIOMemoryInfo dealloc];
-[MTLIOMemoryInfo lock];
-[MTLIOMemoryInfo annotationList];
-[MTLIOMemoryInfo removeResourceFromList:];
-[MTLIOMemoryInfo unlock];
-[MTLIOMemoryInfo removeDataSource:];
-[MTLIOMemoryInfo addResourceToList:];
```
