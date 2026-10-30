# `ExplicitZeroPadding`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNDefaultPadding`
- Protocols: `MPSNNPadding`
- 4 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
Q _paddingLeft;
Q _paddingRight;
Q _paddingTop;
Q _paddingBottom;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ExplicitZeroPadding destinationImageDescriptorForSourceImages:sourceStates:forKernel:suggestedDescriptor:];
-[ExplicitZeroPadding paddingMethod];
-[ExplicitZeroPadding initWithPaddingLeft:paddingRight:paddingTop:paddingBottom:];
```
