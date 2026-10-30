# `CIBayerFPProcessor`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CIImageProcessorKernel`
- 0 instance variables, 0 properties, 0 instance methods, 19 class methods

## Class methods

```
+[CIBayerFPProcessor roiForInput:arguments:outputRect:];
+[CIBayerFPProcessor formatForInputAtIndex:];
+[CIBayerFPProcessor onlyUsesMetal];
+[CIBayerFPProcessor synchronizeInputs];
+[CIBayerFPProcessor processWithInputs:arguments:output:error:];
+[CIBayerFPProcessor outputFormat];
+[CIBayerFPProcessor adjustedFirstPixel:forCIOrigin:tileHeight:imageHeight:isQuadra:];
+[CIBayerFPProcessor computePipelineWithName:library:];
+[CIBayerFPProcessor convert10BitFloatingPointToInt17:commandBuffer:library:scale:offset:error:];
+[CIBayerFPProcessor convertInt17To10BitFloatingPoint:commandBuffer:library:scale:offset:error:];
+[CIBayerFPProcessor dispatchBayerKernelWithCommandBuffer:device:texture:grid:firstPixel:imageSize:patternCount:metadata:];
+[CIBayerFPProcessor dispatchQuadraKernelWithCommandBuffer:device:texture:grid:firstPixel:imageSize:metadata:];
+[CIBayerFPProcessor generateQuadraPDCCoefficientsWithMetadata:onR:onB:];
+[CIBayerFPProcessor getSurfaceFromCache:format:width:height:];
+[CIBayerFPProcessor hasSurfaceCacheSPIs:];
+[CIBayerFPProcessor initializePipelines:];
+[CIBayerFPProcessor processImage:patterns:counts:imageSize:firstPixel:inputBlacks:isQuadra:coordinatesPreDoubled:inputDNGMetadata:];
+[CIBayerFPProcessor returnSurfaceToCache:surface:];
+[CIBayerFPProcessor simpleConversion:commandBuffer:pipelineState:scale:offset:error:];
```
