# `MPSGraphCaptureContext`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 17 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _jsonData;
@"NSMutableArray" _nodes;
@"NSMutableArray" _links;
@"NSMutableArray" _portLinks;
@"NSMutableArray" _data;
@"NSMutableArray" _functions;
@"NSArray" _inputPorts;
@"NSArray" _outputPorts;
^v _context;
@"NSMutableDictionary" _pipelineReflectionDictionary;
@"NSMutableDictionary" _pipelineFunctionNameDictionary;
@"NSMutableDictionary" _pipelineFileNameDictionary;
@"NSMutableDictionary" _constantBuffers;
@"NSMutableDictionary" _lastNodeWrittingToBuffer;
@"NSString" _outputFolderPath;
@"NSString" _graphName;
B _doNotWriteJsonFile;
```

## Instance methods

```
-[MPSGraphCaptureContext dealloc];
-[MPSGraphCaptureContext dataWithBytes:length:];
-[MPSGraphCaptureContext setFeeds:names:];
-[MPSGraphCaptureContext addFunctionWithBitCode:metalFunctionName:reflection:];
-[MPSGraphCaptureContext addPipeline:functionName:withReflection:];
-[MPSGraphCaptureContext constantBufferName:];
-[MPSGraphCaptureContext createNodeWithDispatchInfo:encoderContext:];
-[MPSGraphCaptureContext functionNameForPipeline:];
-[MPSGraphCaptureContext initWithOutputFolderPath:graphName:];
-[MPSGraphCaptureContext reflectionForPipeline:];
-[MPSGraphCaptureContext setConstantBuffer:];
-[MPSGraphCaptureContext setInputBuffers:names:];
-[MPSGraphCaptureContext setOutputBuffers:names:];
-[MPSGraphCaptureContext setResults:names:];
-[MPSGraphCaptureContext wrapComputeEncoder:];
-[MPSGraphCaptureContext writeToJsonFile:];
-[MPSGraphCaptureContext writejsonFile:];
```
