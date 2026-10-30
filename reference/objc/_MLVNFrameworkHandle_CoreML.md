# `_MLVNFrameworkHandle`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 21 instance methods, 2 class methods

## Instance variables

```
B _validForSceneprint;
B _validForObjectprint;
^? _scenePrintsFromPixelBuffersImpl;
^? _scenePrintsFromPixelBuffersUsesCPUOnlyImpl;
^? _scenePrintElementCountImpl;
^? _scenePrintLengthImpl;
# _VNImageBufferClass;
^? _detectionPrintsFromPixelBuffersImpl;
^? _detectionPrintsFromPixelBuffersUsesCPUOnlyImpl;
^? _detectionPrintShapesImpl;
^? _detectionPrintSupportedRevisionsImpl;
```

## Properties

```
@property (T^?,R,N,V_scenePrintsFromPixelBuffersImpl) scenePrintsFromPixelBuffersImpl;
@property (T^?,R,N,V_scenePrintsFromPixelBuffersUsesCPUOnlyImpl) scenePrintsFromPixelBuffersUsesCPUOnlyImpl;
@property (T^?,R,N,V_scenePrintElementCountImpl) scenePrintElementCountImpl;
@property (T^?,R,N,V_scenePrintLengthImpl) scenePrintLengthImpl;
@property (T#,R,N,V_VNImageBufferClass) VNImageBufferClass;
@property (T^?,R,N,V_detectionPrintsFromPixelBuffersImpl) detectionPrintsFromPixelBuffersImpl;
@property (T^?,R,N,V_detectionPrintsFromPixelBuffersUsesCPUOnlyImpl) detectionPrintsFromPixelBuffersUsesCPUOnlyImpl;
@property (T^?,R,N,V_detectionPrintShapesImpl) detectionPrintShapesImpl;
@property (T^?,R,N,V_detectionPrintSupportedRevisionsImpl) detectionPrintSupportedRevisionsImpl;
@property (TB,R,N,GisValid,V_validForSceneprint) validForSceneprint;
@property (TB,R,N,GisValid,V_validForObjectprint) validForObjectprint;
```

## Class methods

```
+[_MLVNFrameworkHandle addOrientation:toOptions:];
+[_MLVNFrameworkHandle sharedHandle];
```

## Instance methods

```
-[_MLVNFrameworkHandle init];
-[_MLVNFrameworkHandle isValid];
-[_MLVNFrameworkHandle isValid];
-[_MLVNFrameworkHandle scenePrintsFromPixelBuffersImpl];
-[_MLVNFrameworkHandle VNImageBufferClass];
-[_MLVNFrameworkHandle createPixelBufferFromCGImage:constraint:cropRect:cropAndScaleOption:options:error:];
-[_MLVNFrameworkHandle createPixelBufferFromImageAtURL:constraint:cropRect:cropAndScaleOption:options:error:];
-[_MLVNFrameworkHandle createPixelBufferFromVNImageBuffer:constraint:cropRect:cropAndScaleOption:options:error:];
-[_MLVNFrameworkHandle detectionPrintShapes:];
-[_MLVNFrameworkHandle detectionPrintShapesImpl];
-[_MLVNFrameworkHandle detectionPrintSupportedRevisions];
-[_MLVNFrameworkHandle detectionPrintSupportedRevisionsImpl];
-[_MLVNFrameworkHandle detectionPrintsFromPixelBuffers:version:augmentationOptions:useCPUOnly:error:];
-[_MLVNFrameworkHandle detectionPrintsFromPixelBuffersImpl];
-[_MLVNFrameworkHandle detectionPrintsFromPixelBuffersUsesCPUOnlyImpl];
-[_MLVNFrameworkHandle elementCountForScenePrintRequestRevision:];
-[_MLVNFrameworkHandle lengthInBytesForScenePrintRequestRevision:];
-[_MLVNFrameworkHandle scenePrintElementCountImpl];
-[_MLVNFrameworkHandle scenePrintLengthImpl];
-[_MLVNFrameworkHandle scenePrintsFromPixelBuffers:version:augmentationOptions:useCPUOnly:error:];
-[_MLVNFrameworkHandle scenePrintsFromPixelBuffersUsesCPUOnlyImpl];
```
