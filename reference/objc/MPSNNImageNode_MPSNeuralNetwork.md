# `MPSNNImageNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 6 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"<MPSHandle>" _handle;
@"MPSNNFilterNode" _parent;
@"<MPSImageAllocator>" _imageAllocator;
Q _clientCount;
Q _format;
B _exportFromGraph;
B _synchronize;
B _stopGradient;
B _initializedWithParent;
```

## Properties

```
@property (T@"<MPSHandle>",&,N,V_handle) handle;
@property (TQ,N,V_format) format;
@property (T@"<MPSImageAllocator>",&,N,V_imageAllocator) imageAllocator;
@property (TB,N,V_exportFromGraph) exportFromGraph;
@property (TB,N,V_synchronize) synchronizeResource;
@property (TB,N,V_stopGradient) stopGradient;
```

## Class methods

```
+[MPSNNImageNode nodeWithHandle:];
+[MPSNNImageNode exportedNodeWithHandle:];
```

## Instance methods

```
-[MPSNNImageNode initWithHandle:];
-[MPSNNImageNode debugDescription];
-[MPSNNImageNode debugQuickLookObject];
-[MPSNNImageNode dealloc];
-[MPSNNImageNode handle];
-[MPSNNImageNode initWithParent:];
-[MPSNNImageNode setHandle:];
-[MPSNNImageNode setFormat:];
-[MPSNNImageNode format];
-[MPSNNImageNode setStopGradient:];
-[MPSNNImageNode stopGradient];
-[MPSNNImageNode exportFromGraph];
-[MPSNNImageNode imageAllocator];
-[MPSNNImageNode setExportFromGraph:];
-[MPSNNImageNode setImageAllocator:];
-[MPSNNImageNode setSynchronizeResource:];
-[MPSNNImageNode synchronizeResource];
```
