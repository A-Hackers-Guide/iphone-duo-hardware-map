# `MTLHeapDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 8 properties, 5 instance methods, 2 class methods

## Instance variables

```
q _sparsePageSize;
q _maxCompatiblePlacementSparsePageSize;
```

## Properties

```
@property (TQ,D,N) size;
@property (TQ,D,N) storageMode;
@property (TQ,D,N) cpuCacheMode;
@property (Tq,N,V_sparsePageSize) sparsePageSize;
@property (TQ,D,N) hazardTrackingMode;
@property (TQ,D,N) resourceOptions;
@property (Tq,D,N) type;
@property (Tq,N,V_maxCompatiblePlacementSparsePageSize) maxCompatiblePlacementSparsePageSize;
```

## Class methods

```
+[MTLHeapDescriptor allocWithZone:];
+[MTLHeapDescriptor alloc];
```

## Instance methods

```
-[MTLHeapDescriptor sparsePageSize];
-[MTLHeapDescriptor setSparsePageSize:];
-[MTLHeapDescriptor setMaxCompatiblePlacementSparsePageSize:];
-[MTLHeapDescriptor copyWithZone:];
-[MTLHeapDescriptor maxCompatiblePlacementSparsePageSize];
```
