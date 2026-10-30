# `BWDeferredPipelineParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 32 instance variables, 32 properties, 72 instance methods, 1 class methods

## Instance variables

```
@"NSString" _deviceModelSpecificName;
{?="width"i"height"i} _rawSensorDimensions;
@"NSDictionary" _dimensionsByResolutionFlavorByPortType;
i _nrfVersion;
i _noiseReductionAndFusionScheme;
i _distortionCorrectionVersion;
B _intelligentDistortionCorrectionEnabled;
B _geometricDistortionCorrectionEnabled;
B _dcProcessingWithDepthSupported;
i _stillImageGDCSourceMode;
i _deepZoomVersion;
i _deepZoomMode;
i _semanticRenderingVersion;
i _smartStyleRenderingVersion;
B _smartStyleRenderingEnabled;
B _smartStyleReversibilityEnabled;
i _textureStyleRenderingVersion;
B _textureStyleCreativeEffectsEnabled;
B _textureStyleBaseLookEnabled;
B _textureStyleFSINCMasksRequired;
@"NSArray" _portTypesWithTextureStyleBaseLookEnabled;
B _generateInferencesForSemanticProcessingIfNeeded;
B _quadraProcessingSupportEnabled;
B _canProcessDeepFusionEnhancedResolution;
B _continuousZoomWithDepthSupported;
i _depthDataType;
{?="width"i"height"i} _depthDataDimensions;
i _pearlModuleType;
i _depthDataToRGBRotationAngle;
I _sfhrMode;
{CGPoint="x"d"y"d} _sensorCenterOffset;
@"NSDictionary" _cameraSensorOrientationCompensationDegreesCWByPortType;
```

## Properties

```
@property (T@"NSString",&,N,V_deviceModelSpecificName) deviceModelSpecificName;
@property (T{?=ii},N,V_rawSensorDimensions) rawSensorDimensions;
@property (T@"NSDictionary",&,N,V_dimensionsByResolutionFlavorByPortType) dimensionsByResolutionFlavorByPortType;
@property (Ti,N,V_nrfVersion) nrfVersion;
@property (Ti,N,V_noiseReductionAndFusionScheme) noiseReductionAndFusionScheme;
@property (TB,N,V_intelligentDistortionCorrectionEnabled) intelligentDistortionCorrectionEnabled;
@property (TB,N,V_geometricDistortionCorrectionEnabled) geometricDistortionCorrectionEnabled;
@property (TB,N,V_dcProcessingWithDepthSupported) dcProcessingWithDepthSupported;
@property (Ti,N,V_distortionCorrectionVersion) distortionCorrectionVersion;
@property (Ti,N,V_stillImageGDCSourceMode) stillImageGDCSourceMode;
@property (Ti,N,V_deepZoomVersion) deepZoomVersion;
@property (Ti,N,V_deepZoomMode) deepZoomMode;
@property (Ti,N,V_semanticRenderingVersion) semanticRenderingVersion;
@property (Ti,N,V_smartStyleRenderingVersion) smartStyleRenderingVersion;
@property (TB,N,V_smartStyleRenderingEnabled) smartStyleRenderingEnabled;
@property (TB,N,V_smartStyleReversibilityEnabled) smartStyleReversibilityEnabled;
@property (Ti,N,V_textureStyleRenderingVersion) textureStyleRenderingVersion;
@property (TB,N,V_textureStyleCreativeEffectsEnabled) textureStyleCreativeEffectsEnabled;
@property (TB,N,V_textureStyleBaseLookEnabled) textureStyleBaseLookEnabled;
@property (TB,N,V_textureStyleFSINCMasksRequired) textureStyleFSINCMasksRequired;
@property (T@"NSArray",&,N,V_portTypesWithTextureStyleBaseLookEnabled) portTypesWithTextureStyleBaseLookEnabled;
@property (TB,N,V_generateInferencesForSemanticProcessingIfNeeded) generateInferencesForSemanticProcessingIfNeeded;
@property (TB,N,V_quadraProcessingSupportEnabled) quadraProcessingSupportEnabled;
@property (TB,N,V_canProcessDeepFusionEnhancedResolution) canProcessDeepFusionEnhancedResolution;
@property (TB,N,V_continuousZoomWithDepthSupported) continuousZoomWithDepthSupported;
@property (Ti,N,V_depthDataType) depthDataType;
@property (T{?=ii},N,V_depthDataDimensions) depthDataDimensions;
@property (Ti,N,V_pearlModuleType) pearlModuleType;
@property (Ti,N,V_depthDataToRGBRotationAngle) depthDataToRGBRotationAngle;
@property (TI,N,V_sfhrMode) sfhrMode;
@property (T{CGPoint=dd},N,V_sensorCenterOffset) sensorCenterOffset;
@property (T@"NSDictionary",&,N,V_cameraSensorOrientationCompensationDegreesCWByPortType) cameraSensorOrientationCompensationDegreesCWByPortType;
```

## Class methods

```
+[BWDeferredPipelineParameters supportsSecureCoding];
```

## Instance methods

```
-[BWDeferredPipelineParameters pearlModuleType];
-[BWDeferredPipelineParameters setSmartStyleRenderingEnabled:];
-[BWDeferredPipelineParameters stillImageGDCSourceMode];
-[BWDeferredPipelineParameters cameraSensorOrientationCompensationDegreesCWByPortType];
-[BWDeferredPipelineParameters setDimensionsByResolutionFlavorByPortType:];
-[BWDeferredPipelineParameters rawSensorDimensions];
-[BWDeferredPipelineParameters smartStyleReversibilityEnabled];
-[BWDeferredPipelineParameters setQuadraProcessingSupportEnabled:];
-[BWDeferredPipelineParameters distortionCorrectionVersion];
-[BWDeferredPipelineParameters setTextureStyleFSINCMasksRequired:];
-[BWDeferredPipelineParameters setTextureStyleRenderingVersion:];
-[BWDeferredPipelineParameters setSfhrMode:];
-[BWDeferredPipelineParameters setSensorCenterOffset:];
-[BWDeferredPipelineParameters setRawSensorDimensions:];
-[BWDeferredPipelineParameters depthDataType];
-[BWDeferredPipelineParameters setGenerateInferencesForSemanticProcessingIfNeeded:];
-[BWDeferredPipelineParameters sfhrMode];
-[BWDeferredPipelineParameters sensorCenterOffset];
-[BWDeferredPipelineParameters semanticRenderingVersion];
-[BWDeferredPipelineParameters setCameraSensorOrientationCompensationDegreesCWByPortType:];
-[BWDeferredPipelineParameters dcProcessingWithDepthSupported];
-[BWDeferredPipelineParameters smartStyleRenderingEnabled];
-[BWDeferredPipelineParameters textureStyleFSINCMasksRequired];
-[BWDeferredPipelineParameters nrfVersion];
-[BWDeferredPipelineParameters setPortTypesWithTextureStyleBaseLookEnabled:];
-[BWDeferredPipelineParameters setDepthDataToRGBRotationAngle:];
-[BWDeferredPipelineParameters setPearlModuleType:];
-[BWDeferredPipelineParameters depthDataToRGBRotationAngle];
-[BWDeferredPipelineParameters setGeometricDistortionCorrectionEnabled:];
-[BWDeferredPipelineParameters setDeepZoomVersion:];
-[BWDeferredPipelineParameters portTypesWithTextureStyleBaseLookEnabled];
-[BWDeferredPipelineParameters setIntelligentDistortionCorrectionEnabled:];
-[BWDeferredPipelineParameters textureStyleBaseLookEnabled];
-[BWDeferredPipelineParameters setDcProcessingWithDepthSupported:];
-[BWDeferredPipelineParameters setSemanticRenderingVersion:];
-[BWDeferredPipelineParameters quadraProcessingSupportEnabled];
-[BWDeferredPipelineParameters setSmartStyleReversibilityEnabled:];
-[BWDeferredPipelineParameters setStillImageGDCSourceMode:];
-[BWDeferredPipelineParameters setContinuousZoomWithDepthSupported:];
-[BWDeferredPipelineParameters generateInferencesForSemanticProcessingIfNeeded];
-[BWDeferredPipelineParameters textureStyleRenderingVersion];
-[BWDeferredPipelineParameters setTextureStyleBaseLookEnabled:];
-[BWDeferredPipelineParameters noiseReductionAndFusionScheme];
-[BWDeferredPipelineParameters deepZoomMode];
-[BWDeferredPipelineParameters geometricDistortionCorrectionEnabled];
-[BWDeferredPipelineParameters deepZoomVersion];
-[BWDeferredPipelineParameters setDepthDataType:];
-[BWDeferredPipelineParameters smartStyleRenderingVersion];
-[BWDeferredPipelineParameters setDepthDataDimensions:];
-[BWDeferredPipelineParameters continuousZoomWithDepthSupported];
-[BWDeferredPipelineParameters dimensionsByResolutionFlavorByPortType];
-[BWDeferredPipelineParameters setDeepZoomMode:];
-[BWDeferredPipelineParameters setSmartStyleRenderingVersion:];
-[BWDeferredPipelineParameters setTextureStyleCreativeEffectsEnabled:];
-[BWDeferredPipelineParameters init];
-[BWDeferredPipelineParameters textureStyleCreativeEffectsEnabled];
-[BWDeferredPipelineParameters dealloc];
-[BWDeferredPipelineParameters setNoiseReductionAndFusionScheme:];
-[BWDeferredPipelineParameters canProcessDeepFusionEnhancedResolution];
-[BWDeferredPipelineParameters depthDataDimensions];
-[BWDeferredPipelineParameters setDistortionCorrectionVersion:];
-[BWDeferredPipelineParameters setNrfVersion:];
-[BWDeferredPipelineParameters areCompatibleWith:];
-[BWDeferredPipelineParameters encodeWithCoder:];
-[BWDeferredPipelineParameters intelligentDistortionCorrectionEnabled];
-[BWDeferredPipelineParameters deviceModelSpecificName];
-[BWDeferredPipelineParameters setDeviceModelSpecificName:];
-[BWDeferredPipelineParameters description];
-[BWDeferredPipelineParameters initWithCoder:];
-[BWDeferredPipelineParameters copyWithZone:];
-[BWDeferredPipelineParameters setCanProcessDeepFusionEnhancedResolution:];
-[BWDeferredPipelineParameters isEqual:];
```
