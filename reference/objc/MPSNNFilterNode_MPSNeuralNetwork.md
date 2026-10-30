# `MPSNNFilterNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _sourceImages;
@"NSMutableArray" _sourceStates;
@"MPSNNImageNode" _resultImage;
@"NSMutableArray" _resultStates;
@"<MPSNNPadding>" _paddingPolicy;
@"NSString" _label;
```

## Properties

```
@property (T@"MPSNNImageNode",R,N,V_resultImage) resultImage;
@property (T@"MPSNNStateNode",R,N) resultState;
@property (T@"NSArray",R,N) resultStates;
@property (T@"<MPSNNPadding>",&,N,V_paddingPolicy) paddingPolicy;
@property (T@"NSString",C,V_label) label;
```

## Instance methods

```
-[MPSNNFilterNode debugDescription];
-[MPSNNFilterNode debugQuickLookObject];
-[MPSNNFilterNode label];
-[MPSNNFilterNode setLabel:];
-[MPSNNFilterNode dealloc];
-[MPSNNFilterNode resultState];
-[MPSNNFilterNode resultImage];
-[MPSNNFilterNode paddingPolicy];
-[MPSNNFilterNode setPaddingPolicy:];
-[MPSNNFilterNode gradientClass];
-[MPSNNFilterNode gradientFilterWithSource:];
-[MPSNNFilterNode gradientFilterWithSources:];
-[MPSNNFilterNode gradientFiltersWithSource:];
-[MPSNNFilterNode gradientFiltersWithSources:];
-[MPSNNFilterNode initWithSourceImages:sourceStates:paddingPolicy:];
-[MPSNNFilterNode newFilterNode];
-[MPSNNFilterNode resultStates];
-[MPSNNFilterNode resultStatesNoAllocate];
-[MPSNNFilterNode sourceImages];
-[MPSNNFilterNode sourceStates];
-[MPSNNFilterNode trainingGraphWithSourceGradient:nodeHandler:];
```
