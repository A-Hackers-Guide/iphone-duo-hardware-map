# `IOAccelMemoryPoolTotals`

- Image: [`/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo`](../userland/System__Library__PrivateFrameworks__IOAccelMemoryInfo.framework__IOAccelMemoryInfo.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" device_name;
@"NSString" pool;
Q allocatedSize;
Q residentSize;
Q wiredSize;
Q dirtySize;
Q purgeableSize;
Q nonpurgeableSize;
Q orphanedSize;
```

## Properties

```
@property (T@"NSString",&,Vdevice_name) device_name;
@property (T@"NSString",&,Vpool) pool;
@property (TQ,VallocatedSize) allocatedSize;
@property (TQ,VresidentSize) residentSize;
@property (TQ,VwiredSize) wiredSize;
@property (TQ,VdirtySize) dirtySize;
@property (TQ,VpurgeableSize) purgeableSize;
@property (TQ,VnonpurgeableSize) nonpurgeableSize;
@property (TQ,VorphanedSize) orphanedSize;
```

## Instance methods

```
-[IOAccelMemoryPoolTotals pool];
-[IOAccelMemoryPoolTotals allocatedSize];
-[IOAccelMemoryPoolTotals dealloc];
-[IOAccelMemoryPoolTotals device_name];
-[IOAccelMemoryPoolTotals setPool:];
-[IOAccelMemoryPoolTotals setAllocatedSize:];
-[IOAccelMemoryPoolTotals dirtySize];
-[IOAccelMemoryPoolTotals residentSize];
-[IOAccelMemoryPoolTotals purgeableSize];
-[IOAccelMemoryPoolTotals setDevice_name:];
-[IOAccelMemoryPoolTotals nonpurgeableSize];
-[IOAccelMemoryPoolTotals orphanedSize];
-[IOAccelMemoryPoolTotals setDirtySize:];
-[IOAccelMemoryPoolTotals setNonpurgeableSize:];
-[IOAccelMemoryPoolTotals setOrphanedSize:];
-[IOAccelMemoryPoolTotals setPurgeableSize:];
-[IOAccelMemoryPoolTotals setResidentSize:];
-[IOAccelMemoryPoolTotals setWiredSize:];
-[IOAccelMemoryPoolTotals wiredSize];
```
