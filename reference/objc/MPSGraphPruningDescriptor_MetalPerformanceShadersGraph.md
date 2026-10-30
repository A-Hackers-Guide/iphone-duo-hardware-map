# `MPSGraphPruningDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
f _sparsity;
q _pruningMetric;
q _pruningStructure;
```

## Properties

```
@property (Tq,N,V_pruningMetric) pruningMetric;
@property (Tq,N,V_pruningStructure) pruningStructure;
@property (Tf,N,V_sparsity) sparsity;
```

## Class methods

```
+[MPSGraphPruningDescriptor descriptorWithPruningMetric:sparsityFormat:sparsity:];
```

## Instance methods

```
-[MPSGraphPruningDescriptor copyWithZone:];
-[MPSGraphPruningDescriptor setSparsity:];
-[MPSGraphPruningDescriptor sparsity];
-[MPSGraphPruningDescriptor pruningMetric];
-[MPSGraphPruningDescriptor pruningStructure];
-[MPSGraphPruningDescriptor setPruningMetric:];
-[MPSGraphPruningDescriptor setPruningStructure:];
```
