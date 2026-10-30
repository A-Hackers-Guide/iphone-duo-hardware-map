# `MPSGraphTensorData`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 14 instance variables, 7 properties, 44 instance methods, 0 class methods

## Instance variables

```
Q _rowBytes;
Q _numElements;
_shapeValues;
Q _rank;
B _createdInCoreAIUsingRawSpanInputs;
@"MPSNDArray" _mpsndarray;
@"NSArray" _mpsimagebatch;
^{__IOSurface=} _iosurface;
@"NSData" _data;
q _tensorDataType;
@"NSString" _typeString;
I _dataType;
@"MPSGraphDevice" _device;
@"NSString" _label;
```

## Properties

```
@property (T^{__IOSurface=},R,N) iosurface;
@property (Tq,R,N,V_tensorDataType) tensorDataType;
@property (T@"NSString",&,N,V_label) label;
@property (TB,N,V_createdInCoreAIUsingRawSpanInputs) createdInCoreAIUsingRawSpanInputs;
@property (T@"NSArray",R,C,N) shape;
@property (TI,R,N,V_dataType) dataType;
@property (T@"MPSGraphDevice",R,N,V_device) device;
```

## Instance methods

```
-[MPSGraphTensorData iosurface];
-[MPSGraphTensorData debugDescription];
-[MPSGraphTensorData shape];
-[MPSGraphTensorData device];
-[MPSGraphTensorData label];
-[MPSGraphTensorData setLabel:];
-[MPSGraphTensorData dealloc];
-[MPSGraphTensorData dataType];
-[MPSGraphTensorData print];
-[MPSGraphTensorData initWithMPSNDArray:];
-[MPSGraphTensorData initWithMTLBuffer:shape:strides:interleaves:dataType:];
-[MPSGraphTensorData mpsndarray];
-[MPSGraphTensorData initWithDevice:IOSurface:rowBytesAlignment:shape:dataType:];
-[MPSGraphTensorData initWithDevice:data:shape:dataType:];
-[MPSGraphTensorData initWithMTLBuffer:shape:dataType:];
-[MPSGraphTensorData initWithMTLBuffer:shape:dataType:rowBytes:];
-[MPSGraphTensorData tensorDataType];
-[MPSGraphTensorData getShapeVector];
-[MPSGraphTensorData allocateIOSurfaceWithByteCount:];
-[MPSGraphTensorData getRank];
-[MPSGraphTensorData checkTensorData:nativeUlps:absoluteErr:];
-[MPSGraphTensorData checkTensorData:nativeUlps:absoluteErr:PSNR:];
-[MPSGraphTensorData checkWithReferenceTensorData:nativeUlps:absoluteError:PSNR:];
-[MPSGraphTensorData commonInitialize];
-[MPSGraphTensorData copyDataFromNDArrayToImageBatchWithCommandBuffer:];
-[MPSGraphTensorData copyToIOSurface:fromSource:dataSize:];
-[MPSGraphTensorData createdInCoreAIUsingRawSpanInputs];
-[MPSGraphTensorData initEmptyWithShape:dataType:device:];
-[MPSGraphTensorData initWithDevice:IOSurface:offset:rowBytesAlignment:shape:dataType:];
-[MPSGraphTensorData initWithDevice:rowBytesAlignment:shape:dataType:];
-[MPSGraphTensorData initWithMPSImageBatch:];
-[MPSGraphTensorData initWithMPSMatrix:];
-[MPSGraphTensorData initWithMPSMatrix:rank:];
-[MPSGraphTensorData initWithMPSNDArray:device:];
-[MPSGraphTensorData initWithMPSVector:];
-[MPSGraphTensorData initWithMPSVector:rank:];
-[MPSGraphTensorData initWithMTLBuffer:offset:shape:strides:interleaves:dataType:];
-[MPSGraphTensorData initWithMTLBuffer:shape:strideBytes:dataType:];
-[MPSGraphTensorData initWithMTLBuffer:shape:strides:dataType:];
-[MPSGraphTensorData initWithMTLTensor:];
-[MPSGraphTensorData mpsndarrayWithCommandBuffer:];
-[MPSGraphTensorData printIOSurface];
-[MPSGraphTensorData printNDArray];
-[MPSGraphTensorData setCreatedInCoreAIUsingRawSpanInputs:];
```
