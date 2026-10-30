# `IOGPUMemoryInfo`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
^v memlist_key;
@"IOGPUMetalResource" fResourceListHead;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _memoryInfoLock;
```

## Class methods

```
+[IOGPUMemoryInfo initialize];
```

## Instance methods

```
-[IOGPUMemoryInfo shutdown];
-[IOGPUMemoryInfo addDataSource:];
-[IOGPUMemoryInfo init];
-[IOGPUMemoryInfo dealloc];
-[IOGPUMemoryInfo getAnnotationListAndEmitResourceInfo];
-[IOGPUMemoryInfo lock];
-[IOGPUMemoryInfo annotationList];
-[IOGPUMemoryInfo removeResourceFromList:];
-[IOGPUMemoryInfo unlock];
-[IOGPUMemoryInfo removeDataSource:];
-[IOGPUMemoryInfo addResourceToList:];
```
