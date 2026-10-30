# `FigColorCubeMetalFilter`

- Image: [`/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter`](../userland/System__Library__VideoProcessors__MetalFilter.bundle__MetalFilter.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MetalImageBufferProcessor`
- 27 instance variables, 15 properties, 40 instance methods, 2 class methods

## Instance variables

```
@"FigMetalContext" _metal;
Q _yuvFormat;
[2[2[2[2@"<MTLRenderPipelineState>"]]]] _colorCubePipelineState;
[2[2[2[2@"<MTLRenderPipelineState>"]]]] _colorCubePipelineStateY;
[2[2[2[2@"<MTLRenderPipelineState>"]]]] _colorCubePipelineStateUV;
[2@"<MTLRenderPipelineState>"] _cubeConvert;
[2@"<MTLTexture>"] _fgCubesTexture;
[2@"<MTLTexture>"] _fgCubesTextureTemp;
C _fgCubeToUseIndex;
B _fgCubesHaveBeenUpdated;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _fgCubesHaveBeenUpdatedLock;
[2@"<MTLTexture>"] _bgCubeTexture;
[2@"<MTLTexture>"] _bgCubeTextureTemp;
C _bgCubeToUseIndex;
B _bgCubesHaveBeenUpdated;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bgCubesHaveBeenUpdatedLock;
B _useBgCube;
B _isSingleFgCube;
i _matteToInputPixelBufferRotationDegrees;
@"NSDictionary" _tuningParameters;
@"NSDictionary" _cameraInfoByPortType;
@"<MTLCommandQueue>" _metalCommandQueue;
^{?=iiBiB} _filterDescriptor;
^{__CVBuffer=} _inputPixelBuffer;
^{__CVBuffer=} _outputPixelBuffer;
^{__CVBuffer=} _mattePixelbuffer;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetRectangle;
```

## Properties

```
@property (T^{?=iiBiB},N,V_filterDescriptor) filterDescriptor;
@property (T^{__CVBuffer=},N,V_inputPixelBuffer) inputPixelBuffer;
@property (T^{__CVBuffer=},N,V_outputPixelBuffer) outputPixelBuffer;
@property (T^{__CVBuffer=},N,V_mattePixelbuffer) mattePixelbuffer;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_targetRectangle) targetRectangle;
@property (Ti,N,V_matteToInputPixelBufferRotationDegrees) matteToInputPixelBufferRotationDegrees;
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N) externalMemoryResource;
@property (T@"NSDictionary",&,N,V_tuningParameters) tuningParameters;
@property (T@"NSDictionary",&,N,V_cameraInfoByPortType) cameraInfoByPortType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigColorCubeMetalFilter createCubeTexture:ofSize:cubesCount:textureType:withDevice:];
+[FigColorCubeMetalFilter loadCube:ofSize:intoTexture:toSliceIndex:];
```

## Instance methods

```
-[FigColorCubeMetalFilter resetState];
-[FigColorCubeMetalFilter releaseResources];
-[FigColorCubeMetalFilter tuningParameters];
-[FigColorCubeMetalFilter finishProcessing];
-[FigColorCubeMetalFilter outputPixelBuffer];
-[FigColorCubeMetalFilter setInputPixelBuffer:];
-[FigColorCubeMetalFilter purgeResources];
-[FigColorCubeMetalFilter setMetalCommandQueue:];
-[FigColorCubeMetalFilter setCameraInfoByPortType:];
-[FigColorCubeMetalFilter prewarm];
-[FigColorCubeMetalFilter prepareToProcess:];
-[FigColorCubeMetalFilter setup];
-[FigColorCubeMetalFilter metalCommandQueue];
-[FigColorCubeMetalFilter inputPixelBuffer];
-[FigColorCubeMetalFilter cameraInfoByPortType];
-[FigColorCubeMetalFilter setTuningParameters:];
-[FigColorCubeMetalFilter setOutputPixelBuffer:];
-[FigColorCubeMetalFilter debugDescription];
-[FigColorCubeMetalFilter initWithCommandQueue:];
-[FigColorCubeMetalFilter process];
-[FigColorCubeMetalFilter dealloc];
-[FigColorCubeMetalFilter allocateResources];
-[FigColorCubeMetalFilter setBackgroundCubeWithName:data:];
-[FigColorCubeMetalFilter filterDescriptor];
-[FigColorCubeMetalFilter setForegroundCubesWithNames:data:];
-[FigColorCubeMetalFilter setMattePixelbuffer:];
-[FigColorCubeMetalFilter setMatteToInputPixelBufferRotationDegrees:];
-[FigColorCubeMetalFilter setTargetRectangle:];
-[FigColorCubeMetalFilter createKernels];
-[FigColorCubeMetalFilter targetRectangle];
-[FigColorCubeMetalFilter _prewarmWithTuningParameters:];
-[FigColorCubeMetalFilter convertCubeWithSrcTexture:dstTexture:isP3Cube:];
-[FigColorCubeMetalFilter createPipelineStateWithVertexFunctionName:fragmentName:isLuma:useBgCube:manyFgCubes:colorSpace:mixInGammaDomain:];
-[FigColorCubeMetalFilter createPipelineStatesForCubeConversionWithVertexFunctionName:];
-[FigColorCubeMetalFilter createPipelineStatesWithFragmentName:vertexFunctionName:];
-[FigColorCubeMetalFilter mattePixelbuffer];
-[FigColorCubeMetalFilter matteToInputPixelBufferRotationDegrees];
-[FigColorCubeMetalFilter prewarmMetalInternalShader];
-[FigColorCubeMetalFilter runWithInputPixelBuffer:mattePixelBuffer:outputPixelBuffer:targetRectangle:];
-[FigColorCubeMetalFilter setFilterDescriptor:];
```
