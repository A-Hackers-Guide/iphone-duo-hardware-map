# `MTLDebugFunction`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsFunction`
- 2 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"MTLFunctionConstantValues" _constantValues;
Q _intersectionFunctionSignature;
```

## Properties

```
@property (T@"MTLFunctionConstantValues",&,V_constantValues) constantValues;
@property (TQ,N,V_intersectionFunctionSignature) intersectionFunctionSignature;
```

## Instance methods

```
-[MTLDebugFunction formattedDescription:];
-[MTLDebugFunction importedLibraries];
-[MTLDebugFunction dealloc];
-[MTLDebugFunction newArgumentEncoderWithBufferIndex:reflection:pipelineLibrary:];
-[MTLDebugFunction newArgumentEncoderWithBufferIndex:];
-[MTLDebugFunction newArgumentEncoderWithBufferIndex:reflection:];
-[MTLDebugFunction importedSymbols];
-[MTLDebugFunction constantValues];
-[MTLDebugFunction setConstantValues:];
-[MTLDebugFunction newArgumentEncoderWithBufferIndex:reflection:binaryArchives:];
-[MTLDebugFunction newArgumentEncoderWithBufferIndex:pipelineLibrary:];
-[MTLDebugFunction bitcodeData];
-[MTLDebugFunction getIntersectionFunctionSignature];
-[MTLDebugFunction initWithFunction:library:];
-[MTLDebugFunction intersectionFunctionSignature];
-[MTLDebugFunction setIntersectionFunctionSignature:];
-[MTLDebugFunction validateIsIFBFunction];
```
