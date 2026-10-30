# `PKVectorMultiTimestamp`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 1 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _timestamps;
```

## Properties

```
@property (T@"NSArray",R,N,V_timestamps) timestamps;
```

## Instance methods

```
-[PKVectorMultiTimestamp timestamps];
-[PKVectorMultiTimestamp initWithTimestamps:];
-[PKVectorMultiTimestamp mergeWithTimestamp:];
-[PKVectorMultiTimestamp sortedUUIDs];
-[PKVectorMultiTimestamp compareTo:];
-[PKVectorMultiTimestamp initWithData:andCapacity:];
-[PKVectorMultiTimestamp clockElementForUUID:atIndex:];
-[PKVectorMultiTimestamp setClock:subclock:forUUID:atIndex:];
-[PKVectorMultiTimestamp initWithCapacity:];
-[PKVectorMultiTimestamp serialize];
-[PKVectorMultiTimestamp hash];
-[PKVectorMultiTimestamp saveToArchive:];
-[PKVectorMultiTimestamp description];
-[PKVectorMultiTimestamp setClock:forUUID:atIndex:];
-[PKVectorMultiTimestamp copyWithZone:];
-[PKVectorMultiTimestamp isEqual:];
-[PKVectorMultiTimestamp clockForUUID:atIndex:];
-[PKVectorMultiTimestamp initWithArchive:andCapacity:];
```
