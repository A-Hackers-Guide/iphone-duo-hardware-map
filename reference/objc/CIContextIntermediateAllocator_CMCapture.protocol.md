# `CIContextIntermediateAllocator` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TQ,R) totalSize;
@property (TQ,R) maxAvailableAllocationSize;
```

## Instance methods

```
-[CIContextIntermediateAllocator totalSize];
-[CIContextIntermediateAllocator bufferForContextIntermediateCommitted:];
-[CIContextIntermediateAllocator bufferForContextIntermediateCompleted:];
-[CIContextIntermediateAllocator maxAvailableAllocationSize];
-[CIContextIntermediateAllocator newBufferForContextIntermediate:usingHint:identifier:];
```
