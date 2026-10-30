# `BWPhotoEncoderControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- 19 instance variables, 19 properties, 39 instance methods, 0 class methods

## Instance variables

```
B _alwaysAwaitInference;
B _usesHighEncodingPriority;
B _zeroShutterLagEnabled;
@"NSDictionary" _attachedMediaConfigurationByAttachedMediaKey;
B _deferredPhotoProcessorEnabled;
i _portraitRenderQuality;
i _semanticDevelopmentVersion;
@"NSDictionary" _inputColorInfo;
B _cameraSupportsFlash;
{?="width"i"height"i} _constantColorConfidenceMapDimensions;
i _smartStyleRenderingVersion;
B _smartStyleReversibilityEnabled;
{?="width"i"height"i} _stereoPhotoOutputDimensions;
@"NSDictionary" _legacySensorOrientationRotationDegreesByPortType;
B _clientIsCameraOrDerivative;
@"NSDictionary" _rawColorCalibrationsByPortType;
@"NSDictionary" _rawLensShadingCorrectionCoefficientsByPortType;
B _secureSigningPhotoCaptureSupportEnabled;
B _textureStyleCreativeEffectsEnabled;
```

## Properties

```
@property (TB,N,V_alwaysAwaitInference) alwaysAwaitInference;
@property (TB,N,V_usesHighEncodingPriority) usesHighEncodingPriority;
@property (TB,N,V_zeroShutterLagEnabled) zeroShutterLagEnabled;
@property (T@"NSDictionary",&,N,V_attachedMediaConfigurationByAttachedMediaKey) attachedMediaConfigurationByAttachedMediaKey;
@property (TB,N,V_deferredPhotoProcessorEnabled) deferredPhotoProcessorEnabled;
@property (Ti,N,V_portraitRenderQuality) portraitRenderQuality;
@property (Ti,N,V_semanticDevelopmentVersion) semanticDevelopmentVersion;
@property (T@"NSDictionary",C,N,V_inputColorInfo) inputColorInfo;
@property (TB,N,V_cameraSupportsFlash) cameraSupportsFlash;
@property (T{?=ii},N,V_constantColorConfidenceMapDimensions) constantColorConfidenceMapDimensions;
@property (Ti,N,V_smartStyleRenderingVersion) smartStyleRenderingVersion;
@property (TB,N,V_smartStyleReversibilityEnabled) smartStyleReversibilityEnabled;
@property (TB,N,V_textureStyleCreativeEffectsEnabled) textureStyleCreativeEffectsEnabled;
@property (T{?=ii},N,V_stereoPhotoOutputDimensions) stereoPhotoOutputDimensions;
@property (T@"NSDictionary",&,N,V_legacySensorOrientationRotationDegreesByPortType) legacySensorOrientationRotationDegreesByPortType;
@property (TB,N,V_clientIsCameraOrDerivative) clientIsCameraOrDerivative;
@property (T@"NSDictionary",&,N,V_rawColorCalibrationsByPortType) rawColorCalibrationsByPortType;
@property (T@"NSDictionary",&,N,V_rawLensShadingCorrectionCoefficientsByPortType) rawLensShadingCorrectionCoefficientsByPortType;
@property (TB,N,V_secureSigningPhotoCaptureSupportEnabled) secureSigningPhotoCaptureSupportEnabled;
```

## Instance methods

```
-[BWPhotoEncoderControllerConfiguration setSemanticDevelopmentVersion:];
-[BWPhotoEncoderControllerConfiguration smartStyleReversibilityEnabled];
-[BWPhotoEncoderControllerConfiguration usesHighEncodingPriority];
-[BWPhotoEncoderControllerConfiguration setRawColorCalibrationsByPortType:];
-[BWPhotoEncoderControllerConfiguration rawLensShadingCorrectionCoefficientsByPortType];
-[BWPhotoEncoderControllerConfiguration secureSigningPhotoCaptureSupportEnabled];
-[BWPhotoEncoderControllerConfiguration setConstantColorConfidenceMapDimensions:];
-[BWPhotoEncoderControllerConfiguration setStereoPhotoOutputDimensions:];
-[BWPhotoEncoderControllerConfiguration deferredPhotoProcessorEnabled];
-[BWPhotoEncoderControllerConfiguration setCameraSupportsFlash:];
-[BWPhotoEncoderControllerConfiguration setPortraitRenderQuality:];
-[BWPhotoEncoderControllerConfiguration rawColorCalibrationsByPortType];
-[BWPhotoEncoderControllerConfiguration setSmartStyleReversibilityEnabled:];
-[BWPhotoEncoderControllerConfiguration cameraSupportsFlash];
-[BWPhotoEncoderControllerConfiguration smartStyleRenderingVersion];
-[BWPhotoEncoderControllerConfiguration stereoPhotoOutputDimensions];
-[BWPhotoEncoderControllerConfiguration setSmartStyleRenderingVersion:];
-[BWPhotoEncoderControllerConfiguration semanticDevelopmentVersion];
-[BWPhotoEncoderControllerConfiguration portraitRenderQuality];
-[BWPhotoEncoderControllerConfiguration setTextureStyleCreativeEffectsEnabled:];
-[BWPhotoEncoderControllerConfiguration zeroShutterLagEnabled];
-[BWPhotoEncoderControllerConfiguration textureStyleCreativeEffectsEnabled];
-[BWPhotoEncoderControllerConfiguration inputColorInfo];
-[BWPhotoEncoderControllerConfiguration clientIsCameraOrDerivative];
-[BWPhotoEncoderControllerConfiguration alwaysAwaitInference];
-[BWPhotoEncoderControllerConfiguration constantColorConfidenceMapDimensions];
-[BWPhotoEncoderControllerConfiguration setRawLensShadingCorrectionCoefficientsByPortType:];
-[BWPhotoEncoderControllerConfiguration setAlwaysAwaitInference:];
-[BWPhotoEncoderControllerConfiguration setDeferredPhotoProcessorEnabled:];
-[BWPhotoEncoderControllerConfiguration setClientIsCameraOrDerivative:];
-[BWPhotoEncoderControllerConfiguration setSecureSigningPhotoCaptureSupportEnabled:];
-[BWPhotoEncoderControllerConfiguration dealloc];
-[BWPhotoEncoderControllerConfiguration setZeroShutterLagEnabled:];
-[BWPhotoEncoderControllerConfiguration setUsesHighEncodingPriority:];
-[BWPhotoEncoderControllerConfiguration setInputColorInfo:];
-[BWPhotoEncoderControllerConfiguration setAttachedMediaConfigurationByAttachedMediaKey:];
-[BWPhotoEncoderControllerConfiguration legacySensorOrientationRotationDegreesByPortType];
-[BWPhotoEncoderControllerConfiguration setLegacySensorOrientationRotationDegreesByPortType:];
-[BWPhotoEncoderControllerConfiguration attachedMediaConfigurationByAttachedMediaKey];
```
