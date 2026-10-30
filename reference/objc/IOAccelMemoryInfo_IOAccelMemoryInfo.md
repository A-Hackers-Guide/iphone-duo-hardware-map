# `IOAccelMemoryInfo`

- Image: [`/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo`](../userland/System__Library__PrivateFrameworks__IOAccelMemoryInfo.framework__IOAccelMemoryInfo.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 17 properties, 21 instance methods, 6 class methods

## Instance variables

```
@"NSDictionary" dict;
@ _expansionData;
```

## Properties

```
@property (TQ,R) memoryPool;
@property (TQ,R) length;
@property (TQ,R) residentLength;
@property (TQ,R) dirtyLength;
@property (TB,R) wired;
@property (TB,R) cachedCopy;
@property (TB,R) cacheDirty;
@property (TB,R) purgeable;
@property (TB,R) orphaned;
@property (T@"NSArray",R) devices;
@property (TI,R) surfaceID;
@property (T@"NSSet",R) processIDs;
@property (T@"NSSet",R) blamedProcesses;
@property (T@"NSArray",R) mappings;
@property (T@"NSArray",R) openglObjects;
@property (T@"NSArray",R) openclObjects;
@property (T@"NSArray",R) formattedDescriptions;
```

## Class methods

```
+[IOAccelMemoryInfo validateDictionary:];
+[IOAccelMemoryInfo collectAllocationTotalsWithOptions:queue:completionBlock:];
+[IOAccelMemoryInfo collectDataWithCompletionQueue:completionBlock:];
+[IOAccelMemoryInfo newKernelAllocationList:];
+[IOAccelMemoryInfo newKernelAllocationTotals:totalsReturn:errorReturn:];
+[IOAccelMemoryInfo purgeAllVidMem];
```

## Instance methods

```
-[IOAccelMemoryInfo surfaceID];
-[IOAccelMemoryInfo initWithDictionary:];
-[IOAccelMemoryInfo purgeable];
-[IOAccelMemoryInfo dealloc];
-[IOAccelMemoryInfo length];
-[IOAccelMemoryInfo devices];
-[IOAccelMemoryInfo description];
-[IOAccelMemoryInfo memoryPool];
-[IOAccelMemoryInfo mappings];
-[IOAccelMemoryInfo dirtyLength];
-[IOAccelMemoryInfo wired];
-[IOAccelMemoryInfo orphaned];
-[IOAccelMemoryInfo blamedProcesses];
-[IOAccelMemoryInfo blamedProcessesForProcess:];
-[IOAccelMemoryInfo cacheDirty];
-[IOAccelMemoryInfo cachedCopy];
-[IOAccelMemoryInfo formattedDescriptions];
-[IOAccelMemoryInfo openclObjects];
-[IOAccelMemoryInfo openglObjects];
-[IOAccelMemoryInfo processIDs];
-[IOAccelMemoryInfo residentLength];
```
