# `MPSGraphSDPADescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _isCausal;
f _scale;
@"MPSGraphTensor" _maskTensor;
@"MPSGraphTensor" _sinksTensor;
```

## Properties

```
@property (Tf,N,V_scale) scale;
@property (T@"MPSGraphTensor",&,N,V_maskTensor) maskTensor;
@property (TB,N,V_isCausal) isCausal;
@property (T@"MPSGraphTensor",&,N,V_sinksTensor) sinksTensor;
```

## Class methods

```
+[MPSGraphSDPADescriptor descriptorWithScale:];
```

## Instance methods

```
-[MPSGraphSDPADescriptor setScale:];
-[MPSGraphSDPADescriptor scale];
-[MPSGraphSDPADescriptor setSinksTensor:];
-[MPSGraphSDPADescriptor isCausal];
-[MPSGraphSDPADescriptor maskTensor];
-[MPSGraphSDPADescriptor setIsCausal:];
-[MPSGraphSDPADescriptor setMaskTensor:];
-[MPSGraphSDPADescriptor sinksTensor];
```
