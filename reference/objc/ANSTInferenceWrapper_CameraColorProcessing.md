# `ANSTInferenceWrapper`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
^v _espressoContext;
^v _espressoPlan;
{?="plan"^v"network_index"i} _espressoNetwork;
@"ANSTPixelBufferDescriptor" _inputImageDescriptor;
@"ANSTPixelBufferDescriptor" _outputSkinMapDescriptor;
^{e5rt_execution_stream=} _e5rtExecutionStream;
^{e5rt_execution_stream_operation=} _e5rtExecutionStreamOperation;
@"ANSTISPInferenceDescriptor" _anstInferenceDescriptor;
Q _anstVersion;
^{__CVBuffer=} _anstInputPixelBuffer;
^{__CVBuffer=} _anstOutputPixelBuffer;
^{__CVBuffer=} _anstOutputPixelBuffer8;
@"FigMetalContext" _metalContext;
@"<MTLTexture>" _anstInputTex;
@"<MTLTexture>" _anstOutputTex;
```

## Instance methods

```
-[ANSTInferenceWrapper dealloc];
-[ANSTInferenceWrapper _purgeResources];
-[ANSTInferenceWrapper initWithMetalContext:];
-[ANSTInferenceWrapper loadANSTNetwork];
-[ANSTInferenceWrapper _allocateClientIOPixelBuffers:inputPixelBufferFormat:inputPixelBufferAttributes:outputPixelBufferSize:outputPixelBufferFormat:outputPixelBufferAttributes:allocateOutputPixelBufferForConversion:];
-[ANSTInferenceWrapper _bindANSTEspressoV1ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:];
-[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:];
-[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:];
-[ANSTInferenceWrapper _bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:];
-[ANSTInferenceWrapper _loadANSTEspressoV1NetworkFromURL:anstAssetType:];
-[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:];
-[ANSTInferenceWrapper anstInputTex];
-[ANSTInferenceWrapper anstOutputTex];
-[ANSTInferenceWrapper networkLoaded];
-[ANSTInferenceWrapper processANST];
-[ANSTInferenceWrapper purgeANSTNetwork];
```
