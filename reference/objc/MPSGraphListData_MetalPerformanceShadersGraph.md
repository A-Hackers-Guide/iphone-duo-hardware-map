# `MPSGraphListData`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphTensorData`
- 3 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _list;
q _maxSize;
@"MPSGraphType" _elementType;
```

## Instance methods

```
-[MPSGraphListData maxSize];
-[MPSGraphListData elementType];
-[MPSGraphListData list];
-[MPSGraphListData mpsndarray];
-[MPSGraphListData clonedList];
-[MPSGraphListData initEmptyListWithDevice:maxSize:elementType:];
-[MPSGraphListData initWithDevice:list:maxSize:elementType:];
-[MPSGraphListData popBackElement];
-[MPSGraphListData pushBackElement:];
```
