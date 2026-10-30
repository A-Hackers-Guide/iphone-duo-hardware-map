# `MPSNNPadGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientState`
- 3 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
{MPSImageCoordinate="x"Q"y"Q"channel"Q} _fwdPadBefore;
{MPSImageCoordinate="x"Q"y"Q"channel"Q} _fwdPadAfter;
Q _srcImgFcCount;
```

## Class methods

```
+[MPSNNPadGradientState temporaryStateWithCommandBuffer:];
```

## Instance methods

```
-[MPSNNPadGradientState debugDescription];
-[MPSNNPadGradientState dealloc];
-[MPSNNPadGradientState initWithResource:];
```
