# `/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter`

iOS 27.2 dyld shared cache image. Version `764.42.9.0.0`. **[DSC]**

## Linked libraries (11)

- `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`
- `/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`
- `/System/Library/Frameworks/CoreImage.framework/CoreImage`
- `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/Metal.framework/Metal`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 1 classes, 3 protocols, 80 methods, 24 properties

### Class pages

Every class and protocol, with its methods: [`FigColorCubeMetalFilter`](../objc/FigColorCubeMetalFilter_MetalFilter.md), [`ImageBufferProcessor`](../objc/ImageBufferProcessor_MetalFilter.protocol.md), [`MetalImageBufferProcessor`](../objc/MetalImageBufferProcessor_MetalFilter.protocol.md), [`NSObject`](../objc/NSObject_MetalFilter.protocol.md)

### Classes

`FigColorCubeMetalFilter`

### Protocols

`ImageBufferProcessor`, `MetalImageBufferProcessor`, `NSObject`

### Properties

```
@property (T@"NSDictionary",&,N) tuningParameters;
@property (T@"NSDictionary",&,N) cameraInfoByPortType;
@property (T@"<MTLCommandQueue>",&,N) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N) externalMemoryResource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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

## Strings (40)

```
FigColorCubeMetalFilter.m
textureDesc
texture
fullRangeVertexBuf
_colorCubePipelineStateUV[useBgCube][manyFgCubes][colorSpace][mix]
[self allocateResources] == 0 
inputTex
_colorCubePipelineStateY[useBgCube][manyFgCubes][colorSpace][mix]
CVP
colorCubeFragment2D
<<<< FigColorCube >>>>
_metal
inputTexUV
renderPipelineColorAttachmentDescriptor
%s assert: \"%s\" at %s (%s:%d) - %s%s(err=%d)
<<<< FigColorCube >>>> Fig
%s signalled err=%d at <>:%d
cubeData.length == byteTotalSize
FigColorCube::convert
commandBuffer
constantValues
cubeColorConvertFrag
device
sliceIndex == 0
[self createKernels] == 0 
err == 0 
!_bgCubeTexture[_bgCubeToUseIndex] || (cubeDimension == (int)_bgCubeTexture[_bgCubeToUseIndex].width)
Could not create Pixelbuffer
Q
v8@?0
com.apple.cameracapture
FigColorCubeMetalFilter
outputTexUV
matteTex
FigColorCube::run
bail
outputTex
vd
colorCubeVertex
_colorCubePipelineState[useBgCube][manyFgCubes][colorSpace][mix]
```
