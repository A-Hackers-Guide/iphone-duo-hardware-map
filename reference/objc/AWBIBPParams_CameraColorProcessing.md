# `AWBIBPParams`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AWBIBPParams`
- 26 instance variables, 30 properties, 53 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _metadata;
@"NSDictionary" _moduleConfig;
@"NSDictionary" _secondaryModuleConfig;
@"NSDictionary" _cameraInfo;
@"NSDictionary" _secondaryCameraInfo;
@"<MTLTexture>" _imageTex;
@"<MTLTexture>" _clippedTex;
@"<MTLTexture>" _lscGainsTex;
@"<MTLTexture>" _skinMask;
@"NSNumber" _firstPixel;
@"NSNumber" _cfaLayout;
@"NSNumber" _downsizeFactor;
@"NSNumber" _digitalFlash;
@"NSDictionary" _validRectInSensorReadoutCoords;
@"NSDictionary" _validRectInBufferCoords;
@"NSDictionary" _regionOfInterestRectInBufferCoords;
@"NSNumber" _faceAssistedBehaviorMode;
@"NSDictionary" _faceAssistedSkinGainsToMatch;
@"NSNumber" _skipDemosaic;
@"NSNumber" _lscMaxGain;
@"NSNumber" _lscModulationWeight;
@"NSMutableDictionary" _outputMetadata;
@"<MTLTexture>" _skyMask;
{?="rGain"I"gGain"I"bGain"I} _awbComboGains;
{?="rGain"I"gGain"I"bGain"I} _awbComboGainsNormalized;
{?="rGain"I"gGain"I"bGain"I} _awbGains;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_metadata) metadata;
@property (T@"NSDictionary",&,N,V_moduleConfig) moduleConfig;
@property (T@"NSDictionary",&,N,V_secondaryModuleConfig) secondaryModuleConfig;
@property (T@"NSDictionary",&,N,V_cameraInfo) cameraInfo;
@property (T@"NSDictionary",&,N,V_secondaryCameraInfo) secondaryCameraInfo;
@property (T@"<MTLTexture>",&,N,V_imageTex) imageTex;
@property (T@"<MTLTexture>",&,N,V_clippedTex) clippedTex;
@property (T@"<MTLTexture>",&,N,V_lscGainsTex) lscGainsTex;
@property (T@"<MTLTexture>",&,N,V_skinMask) skinMask;
@property (T@"NSNumber",&,N,V_firstPixel) firstPixel;
@property (T@"NSNumber",&,N,V_cfaLayout) cfaLayout;
@property (T@"NSNumber",&,N,V_downsizeFactor) downsizeFactor;
@property (T@"NSNumber",&,N,V_digitalFlash) digitalFlash;
@property (T@"NSDictionary",&,N,V_validRectInSensorReadoutCoords) validRectInSensorReadoutCoords;
@property (T@"NSDictionary",&,N,V_validRectInBufferCoords) validRectInBufferCoords;
@property (T@"NSDictionary",&,N,V_regionOfInterestRectInBufferCoords) regionOfInterestRectInBufferCoords;
@property (T@"NSNumber",&,N,V_faceAssistedBehaviorMode) faceAssistedBehaviorMode;
@property (T@"NSDictionary",&,N,V_faceAssistedSkinGainsToMatch) faceAssistedSkinGainsToMatch;
@property (T@"NSNumber",&,N,V_skipDemosaic) skipDemosaic;
@property (T@"NSNumber",&,N,V_lscMaxGain) lscMaxGain;
@property (T@"NSNumber",&,N,V_lscModulationWeight) lscModulationWeight;
@property (T@"<MTLTexture>",&,N,V_skyMask) skyMask;
@property (T{?=III},N,V_awbComboGains) awbComboGains;
@property (T{?=III},N,V_awbComboGainsNormalized) awbComboGainsNormalized;
@property (T{?=III},N,V_awbGains) awbGains;
@property (T@"NSMutableDictionary",&,N,V_outputMetadata) outputMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AWBIBPParams faceAssistedBehaviorMode];
-[AWBIBPParams setFaceAssistedSkinGainsToMatch:];
-[AWBIBPParams awbComboGains];
-[AWBIBPParams imageTex];
-[AWBIBPParams setCfaLayout:];
-[AWBIBPParams faceAssistedSkinGainsToMatch];
-[AWBIBPParams setSkinMask:];
-[AWBIBPParams setDigitalFlash:];
-[AWBIBPParams setAwbGains:];
-[AWBIBPParams awbComboGainsNormalized];
-[AWBIBPParams moduleConfig];
-[AWBIBPParams setOutputMetadata:];
-[AWBIBPParams setFirstPixel:];
-[AWBIBPParams setRegionOfInterestRectInBufferCoords:];
-[AWBIBPParams setFaceAssistedBehaviorMode:];
-[AWBIBPParams setLscModulationWeight:];
-[AWBIBPParams setSkipDemosaic:];
-[AWBIBPParams reset];
-[AWBIBPParams validRectInBufferCoords];
-[AWBIBPParams regionOfInterestRectInBufferCoords];
-[AWBIBPParams lscGainsTex];
-[AWBIBPParams metadata];
-[AWBIBPParams setImageTex:];
-[AWBIBPParams setClippedTex:];
-[AWBIBPParams setAwbComboGains:];
-[AWBIBPParams clippedTex];
-[AWBIBPParams skipDemosaic];
-[AWBIBPParams setLscMaxGain:];
-[AWBIBPParams cfaLayout];
-[AWBIBPParams firstPixel];
-[AWBIBPParams awbGains];
-[AWBIBPParams setMetadata:];
-[AWBIBPParams setSecondaryCameraInfo:];
-[AWBIBPParams downsizeFactor];
-[AWBIBPParams validRectInSensorReadoutCoords];
-[AWBIBPParams setModuleConfig:];
-[AWBIBPParams setLscGainsTex:];
-[AWBIBPParams cameraInfo];
-[AWBIBPParams secondaryCameraInfo];
-[AWBIBPParams setDownsizeFactor:];
-[AWBIBPParams setAwbComboGainsNormalized:];
-[AWBIBPParams skyMask];
-[AWBIBPParams setCameraInfo:];
-[AWBIBPParams setSecondaryModuleConfig:];
-[AWBIBPParams secondaryModuleConfig];
-[AWBIBPParams skinMask];
-[AWBIBPParams setSkyMask:];
-[AWBIBPParams outputMetadata];
-[AWBIBPParams lscMaxGain];
-[AWBIBPParams setValidRectInSensorReadoutCoords:];
-[AWBIBPParams digitalFlash];
-[AWBIBPParams lscModulationWeight];
-[AWBIBPParams setValidRectInBufferCoords:];
```
