# `MPSCNNLossLabels`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- 10 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
{?="width"Q"height"Q"depth"Q} _lossImageSize;
B _isScalarLoss;
@"NSData" _userData;
Q _userDataLayout;
Q _numFeatureChannels_labels;
Q _numFeatureChannels_loss;
@"MPSImage" _userLabelsImage;
@"MPSImage" _userWeightsImage;
B _hasStateWeights;
B _computeNonZeroWeights;
```

## Instance methods

```
-[MPSCNNLossLabels init];
-[MPSCNNLossLabels dealloc];
-[MPSCNNLossLabels initWithDevice:lossImageSize:labelsImage:weightsImage:];
-[MPSCNNLossLabels lossImage];
-[MPSCNNLossLabels initWithDevice:lossImageSize:labelsDescriptor:weightsDescriptor:];
-[MPSCNNLossLabels initWithDevice:labelsDescriptor:];
-[MPSCNNLossLabels labelsImage];
-[MPSCNNLossLabels weightsImage];
```
