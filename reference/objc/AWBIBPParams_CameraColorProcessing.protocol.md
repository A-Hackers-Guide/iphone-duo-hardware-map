# `AWBIBPParams` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 26 properties, 53 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",&,N) metadata;
@property (T@"NSDictionary",&,N) moduleConfig;
@property (T@"NSDictionary",&,N) secondaryModuleConfig;
@property (T@"NSDictionary",&,N) cameraInfo;
@property (T@"NSDictionary",&,N) secondaryCameraInfo;
@property (T@"<MTLTexture>",&,N) imageTex;
@property (T@"<MTLTexture>",&,N) clippedTex;
@property (T@"<MTLTexture>",&,N) lscGainsTex;
@property (T@"<MTLTexture>",&,N) skinMask;
@property (T@"NSNumber",&,N) firstPixel;
@property (T@"NSNumber",&,N) cfaLayout;
@property (T@"NSNumber",&,N) downsizeFactor;
@property (T@"NSNumber",&,N) digitalFlash;
@property (T@"NSDictionary",&,N) validRectInSensorReadoutCoords;
@property (T@"NSDictionary",&,N) validRectInBufferCoords;
@property (T@"NSDictionary",&,N) regionOfInterestRectInBufferCoords;
@property (T@"NSNumber",&,N) faceAssistedBehaviorMode;
@property (T@"NSDictionary",&,N) faceAssistedSkinGainsToMatch;
@property (T@"NSNumber",&,N) skipDemosaic;
@property (T@"NSNumber",&,N) lscMaxGain;
@property (T@"NSNumber",&,N) lscModulationWeight;
@property (T@"<MTLTexture>",&,N) skyMask;
@property (T{?=III},N) awbComboGains;
@property (T{?=III},N) awbComboGainsNormalized;
@property (T{?=III},N) awbGains;
@property (T@"NSMutableDictionary",&,N) outputMetadata;
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
