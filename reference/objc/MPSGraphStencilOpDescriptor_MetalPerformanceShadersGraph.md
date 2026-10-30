# `MPSGraphStencilOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 17 instance methods, 4 class methods

## Instance variables

```
f _paddingConstant;
Q _reductionMode;
@"NSArray" _offsets;
@"NSArray" _strides;
@"NSArray" _dilationRates;
@"NSArray" _explicitPadding;
q _boundaryMode;
Q _paddingStyle;
```

## Properties

```
@property (TQ,N,V_reductionMode) reductionMode;
@property (T@"NSArray",C,N,V_offsets) offsets;
@property (T@"NSArray",C,N,V_strides) strides;
@property (T@"NSArray",C,N,V_dilationRates) dilationRates;
@property (T@"NSArray",C,N,V_explicitPadding) explicitPadding;
@property (Tq,N,V_boundaryMode) boundaryMode;
@property (TQ,N,V_paddingStyle) paddingStyle;
@property (Tf,N,V_paddingConstant) paddingConstant;
```

## Class methods

```
+[MPSGraphStencilOpDescriptor descriptorWithExplicitPadding:];
+[MPSGraphStencilOpDescriptor descriptorWithOffsets:explicitPadding:];
+[MPSGraphStencilOpDescriptor descriptorWithPaddingStyle:];
+[MPSGraphStencilOpDescriptor descriptorWithReductionMode:offsets:strides:dilationRates:explicitPadding:boundaryMode:paddingStyle:paddingConstant:];
```

## Instance methods

```
-[MPSGraphStencilOpDescriptor reductionMode];
-[MPSGraphStencilOpDescriptor setOffsets:];
-[MPSGraphStencilOpDescriptor strides];
-[MPSGraphStencilOpDescriptor setReductionMode:];
-[MPSGraphStencilOpDescriptor copyWithZone:];
-[MPSGraphStencilOpDescriptor offsets];
-[MPSGraphStencilOpDescriptor setStrides:];
-[MPSGraphStencilOpDescriptor paddingConstant];
-[MPSGraphStencilOpDescriptor dilationRates];
-[MPSGraphStencilOpDescriptor setDilationRates:];
-[MPSGraphStencilOpDescriptor setPaddingConstant:];
-[MPSGraphStencilOpDescriptor explicitPadding];
-[MPSGraphStencilOpDescriptor boundaryMode];
-[MPSGraphStencilOpDescriptor paddingStyle];
-[MPSGraphStencilOpDescriptor setBoundaryMode:];
-[MPSGraphStencilOpDescriptor setExplicitPadding:];
-[MPSGraphStencilOpDescriptor setPaddingStyle:];
```
