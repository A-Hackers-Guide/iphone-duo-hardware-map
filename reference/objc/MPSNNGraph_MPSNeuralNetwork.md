# `MPSNNGraph`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSKernel`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 9 properties, 29 instance methods, 4 class methods

## Instance variables

```
{Graph="_graphSourceImages"{NodeList<ResourceGraphNode *>="_items"^^{ResourceGraphNode}"_count"Q"_storageSize"Q}"_graphSourceStates"{NodeList<ResourceGraphNode *>="_items"^^{ResourceGraphNode}"_count"Q"_storageSize"Q}"_graphResultImages"{NodeList<ResourceGraphNode *>="_items"^^{ResourceGraphNode}"_count"Q"_storageSize"Q}"_graphIntermediateImages"{NodeList<ResourceGraphNode *>="_items"^^{ResourceGraphNode}"_count"Q"_storageSize"Q}"_graphResultStates"{NodeList<ResourceGraphNode *>="_items"^^{ResourceGraphNode}"_count"Q"_storageSize"Q}"_graph"@"MPSNNGraph""_filters"{NodeList<FilterGraphNode *>="_items"^^{FilterGraphNode}"_count"Q"_storageSize"Q}"_images"{NodeList<ResourceGraphNode *>="_items"^^{ResourceGraphNode}"_count"Q"_storageSize"Q}"_states"{NodeList<ResourceGraphNode *>="_items"^^{ResourceGraphNode}"_count"Q"_storageSize"Q}"_cpuUpdateSem"@"NSObject<OS_dispatch_semaphore>""_graphNull"@"NSNull"} _graph;
@"<MPSImageAllocator>" _destinationImageAllocator;
Q _format;
B _resultIsNeeded;
B _outputStateIsTemporary;
```

## Properties

```
@property (T@"NSArray",R,C,N) sourceImageHandles;
@property (T@"NSArray",R,C,N) sourceStateHandles;
@property (T@"NSArray",R,C,N) intermediateImageHandles;
@property (T@"NSArray",R,C,N) resultStateHandles;
@property (T@"<MPSHandle>",R,N) resultHandle;
@property (TB,N,V_outputStateIsTemporary) outputStateIsTemporary;
@property (T@"<MPSImageAllocator>",&,N,V_destinationImageAllocator) destinationImageAllocator;
@property (TQ,N,V_format) format;
@property (TB,R,N) resultImageIsNeeded;
```

## Class methods

```
+[MPSNNGraph libraryInfo:];
+[MPSNNGraph graphWithDevice:resultImage:];
+[MPSNNGraph graphWithDevice:resultImage:resultImageIsNeeded:];
+[MPSNNGraph graphWithDevice:resultImages:resultsAreNeeded:];
```

## Instance methods

```
-[MPSNNGraph setOptions:];
-[MPSNNGraph debugDescription];
-[MPSNNGraph dealloc];
-[MPSNNGraph copyWithZone:device:];
-[MPSNNGraph initWithCoder:device:];
-[MPSNNGraph encodeWithCoder:];
-[MPSNNGraph setFormat:];
-[MPSNNGraph format];
-[MPSNNGraph destinationImageAllocator];
-[MPSNNGraph setDestinationImageAllocator:];
-[MPSNNGraph readCountForSourceImageAtIndex:];
-[MPSNNGraph readCountForSourceStateAtIndex:];
-[MPSNNGraph encodeBatchToCommandBuffer:sourceImages:sourceStates:];
-[MPSNNGraph encodeBatchToCommandBuffer:sourceImages:sourceStates:intermediateImages:destinationStates:];
-[MPSNNGraph encodeToCommandBuffer:sourceImages:];
-[MPSNNGraph encodeToCommandBuffer:sourceImages:sourceStates:intermediateImages:destinationStates:];
-[MPSNNGraph executeAsyncWithSourceImages:completionHandler:];
-[MPSNNGraph initWithDevice:resultImage:];
-[MPSNNGraph initWithDevice:resultImage:resultImageIsNeeded:];
-[MPSNNGraph initWithDevice:resultImages:resultsAreNeeded:];
-[MPSNNGraph intermediateImageHandles];
-[MPSNNGraph outputStateIsTemporary];
-[MPSNNGraph reloadFromDataSources];
-[MPSNNGraph resultHandle];
-[MPSNNGraph resultImageIsNeeded];
-[MPSNNGraph resultStateHandles];
-[MPSNNGraph setOutputStateIsTemporary:];
-[MPSNNGraph sourceImageHandles];
-[MPSNNGraph sourceStateHandles];
```
