# `MLCustomLayerWrapper`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EspressoBrick`
- 3 instance variables, 7 properties, 10 instance methods, 9 class methods

## Instance variables

```
B _ndMode;
@"NSString" _className;
@"NSObject<MLCustomLayer>" _customImpl;
```

## Properties

```
@property (TB,R,N,V_ndMode) ndMode;
@property (T@"NSString",R,N,V_className) className;
@property (T@"NSObject<MLCustomLayer>",&,N,V_customImpl) customImpl;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLCustomLayerWrapper factory];
+[MLCustomLayerWrapper coremlShapeToEspressoShape:ndMode:];
+[MLCustomLayerWrapper coremlShapesToEspressoShapes:ndMode:];
+[MLCustomLayerWrapper espressoShapeToCoremlShape:ndMode:];
+[MLCustomLayerWrapper espressoShapesToCoremlShapes:ndMode:];
+[MLCustomLayerWrapper espressoTensorToCoremlTensor:ndMode:];
+[MLCustomLayerWrapper espressoTensorsToCoremlTensors:ndMode:];
+[MLCustomLayerWrapper espressoTensorsToCoremlTensorsGPU:];
+[MLCustomLayerWrapper getStrides:];
```

## Instance methods

```
-[MLCustomLayerWrapper className];
-[MLCustomLayerWrapper initWithParameters:];
-[MLCustomLayerWrapper computeOnCPUWithInputTensors:outputTensors:];
-[MLCustomLayerWrapper encodeToMetalCommandBuffer:inputTensors:outputTensors:];
-[MLCustomLayerWrapper hasGPUSupport];
-[MLCustomLayerWrapper setMappedWeights:sizeInBytes:];
-[MLCustomLayerWrapper setupForInputShapes:withParameters:];
-[MLCustomLayerWrapper customImpl];
-[MLCustomLayerWrapper ndMode];
-[MLCustomLayerWrapper setCustomImpl:];
```
