# `MLIndexedBatchProvider`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLBatchProvider`
- 2 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<MLBatchProvider>" _fullBatch;
@"NSArray" _indices;
```

## Properties

```
@property (T@"<MLBatchProvider>",&,N,V_fullBatch) fullBatch;
@property (T@"NSArray",&,N,V_indices) indices;
@property (Tq,R,N) count;
```

## Instance methods

```
-[MLIndexedBatchProvider count];
-[MLIndexedBatchProvider indices];
-[MLIndexedBatchProvider featuresAtIndex:];
-[MLIndexedBatchProvider fullBatch];
-[MLIndexedBatchProvider initWithBatch:indices:error:];
-[MLIndexedBatchProvider setFullBatch:];
-[MLIndexedBatchProvider setIndices:];
```
