# `MPSNNStateNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<MPSHandle>" _handle;
@"MPSNNFilterNode" _parent;
Q _clientCount;
B _synchronize;
B _exportFromGraph;
B _initializedWithParent;
```

## Properties

```
@property (T@"<MPSHandle>",&,N,V_handle) handle;
@property (TB,N,V_exportFromGraph) exportFromGraph;
@property (TB,N,V_synchronize) synchronizeResource;
```

## Instance methods

```
-[MPSNNStateNode debugDescription];
-[MPSNNStateNode debugQuickLookObject];
-[MPSNNStateNode dealloc];
-[MPSNNStateNode handle];
-[MPSNNStateNode initWithParent:];
-[MPSNNStateNode setHandle:];
-[MPSNNStateNode exportFromGraph];
-[MPSNNStateNode setExportFromGraph:];
-[MPSNNStateNode setSynchronizeResource:];
-[MPSNNStateNode synchronizeResource];
```
