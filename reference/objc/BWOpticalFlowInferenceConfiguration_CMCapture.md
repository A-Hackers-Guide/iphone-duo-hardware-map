# `BWOpticalFlowInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 12 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
{?="width"i"height"i} _inputDimensions;
{?="width"i"height"i} _outputDimensions;
{?="width"i"height"i} _forceIntermediateDimensions;
Q _concurrencyWidth;
i _inputRotationAngle;
B _propagateColorInput;
B _colorInputFlipHorizontal;
c _colorInputCropMode;
@"NSString" _attachedMediaCropRectKey;
@"NSString" _attachedMediaKeyForPropagatedColorInput;
@"NSString" _attachedMediaKeyForColorInput;
@"NSString" _portType;
```

## Properties

```
@property (T{?=ii},N,V_inputDimensions) inputDimensions;
@property (T{?=ii},N,V_outputDimensions) outputDimensions;
@property (T@"NSString",N,V_portType) portType;
@property (TQ,N,V_concurrencyWidth) concurrencyWidth;
@property (Ti,N,V_inputRotationAngle) inputRotationAngle;
@property (T@"NSString",N,V_attachedMediaKeyForPropagatedColorInput) attachedMediaKeyForPropagatedColorInput;
@property (Tc,N,V_colorInputCropMode) colorInputCropMode;
@property (T@"NSString",N,V_attachedMediaCropRectKey) attachedMediaCropRectKey;
@property (TB,N,V_colorInputFlipHorizontal) colorInputFlipHorizontal;
@property (T@"NSString",N,V_attachedMediaKeyForColorInput) attachedMediaKeyForColorInput;
@property (T{?=ii},N,V_forceIntermediateDimensions) forceIntermediateDimensions;
```

## Instance methods

```
-[BWOpticalFlowInferenceConfiguration portType];
-[BWOpticalFlowInferenceConfiguration setOutputDimensions:];
-[BWOpticalFlowInferenceConfiguration colorInputFlipHorizontal];
-[BWOpticalFlowInferenceConfiguration colorInputCropMode];
-[BWOpticalFlowInferenceConfiguration concurrencyWidth];
-[BWOpticalFlowInferenceConfiguration outputDimensions];
-[BWOpticalFlowInferenceConfiguration setColorInputCropMode:];
-[BWOpticalFlowInferenceConfiguration attachedMediaKeyForPropagatedColorInput];
-[BWOpticalFlowInferenceConfiguration inputDimensions];
-[BWOpticalFlowInferenceConfiguration setAttachedMediaKeyForColorInput:];
-[BWOpticalFlowInferenceConfiguration attachedMediaKeyForColorInput];
-[BWOpticalFlowInferenceConfiguration forceIntermediateDimensions];
-[BWOpticalFlowInferenceConfiguration setPortType:];
-[BWOpticalFlowInferenceConfiguration setAttachedMediaCropRectKey:];
-[BWOpticalFlowInferenceConfiguration attachedMediaCropRectKey];
-[BWOpticalFlowInferenceConfiguration setConcurrencyWidth:];
-[BWOpticalFlowInferenceConfiguration setForceIntermediateDimensions:];
-[BWOpticalFlowInferenceConfiguration setColorInputFlipHorizontal:];
-[BWOpticalFlowInferenceConfiguration setInputDimensions:];
-[BWOpticalFlowInferenceConfiguration setInputRotationAngle:];
-[BWOpticalFlowInferenceConfiguration setAttachedMediaKeyForPropagatedColorInput:];
-[BWOpticalFlowInferenceConfiguration inputRotationAngle];
```
