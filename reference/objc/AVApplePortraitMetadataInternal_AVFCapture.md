# `AVApplePortraitMetadataInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
i version;
f apertureFocalRatio;
f minimumApertureFocalRatio;
f maximumApertureFocalRatio;
f portraitLightingEffectStrength;
f luminanceNoiseAmplitude;
i faceOrientation;
@"NSData" faceObservationsData;
@"NSIndexSet" indexesOfShallowDepthOfFieldObservations;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} focusRectangle;
I SDOFRenderingVersion;
```

## Properties

```
@property (Ti,N,Vversion) version;
@property (Tf,N,VapertureFocalRatio) apertureFocalRatio;
@property (Tf,N,VminimumApertureFocalRatio) minimumApertureFocalRatio;
@property (Tf,N,VmaximumApertureFocalRatio) maximumApertureFocalRatio;
@property (Tf,N,VportraitLightingEffectStrength) portraitLightingEffectStrength;
@property (Tf,N,VluminanceNoiseAmplitude) luminanceNoiseAmplitude;
@property (Ti,N,VfaceOrientation) faceOrientation;
@property (T@"NSData",&,N,VfaceObservationsData) faceObservationsData;
@property (T@"NSIndexSet",&,N,VindexesOfShallowDepthOfFieldObservations) indexesOfShallowDepthOfFieldObservations;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,VfocusRectangle) focusRectangle;
@property (TI,N,VSDOFRenderingVersion) SDOFRenderingVersion;
```

## Instance methods

```
-[AVApplePortraitMetadataInternal portraitLightingEffectStrength];
-[AVApplePortraitMetadataInternal init];
-[AVApplePortraitMetadataInternal dealloc];
-[AVApplePortraitMetadataInternal version];
-[AVApplePortraitMetadataInternal setVersion:];
-[AVApplePortraitMetadataInternal setPortraitLightingEffectStrength:];
-[AVApplePortraitMetadataInternal faceOrientation];
-[AVApplePortraitMetadataInternal setFaceOrientation:];
-[AVApplePortraitMetadataInternal setSDOFRenderingVersion:];
-[AVApplePortraitMetadataInternal SDOFRenderingVersion];
-[AVApplePortraitMetadataInternal apertureFocalRatio];
-[AVApplePortraitMetadataInternal faceObservationsData];
-[AVApplePortraitMetadataInternal focusRectangle];
-[AVApplePortraitMetadataInternal indexesOfShallowDepthOfFieldObservations];
-[AVApplePortraitMetadataInternal luminanceNoiseAmplitude];
-[AVApplePortraitMetadataInternal maximumApertureFocalRatio];
-[AVApplePortraitMetadataInternal minimumApertureFocalRatio];
-[AVApplePortraitMetadataInternal setApertureFocalRatio:];
-[AVApplePortraitMetadataInternal setFaceObservationsData:];
-[AVApplePortraitMetadataInternal setFocusRectangle:];
-[AVApplePortraitMetadataInternal setIndexesOfShallowDepthOfFieldObservations:];
-[AVApplePortraitMetadataInternal setLuminanceNoiseAmplitude:];
-[AVApplePortraitMetadataInternal setMaximumApertureFocalRatio:];
-[AVApplePortraitMetadataInternal setMinimumApertureFocalRatio:];
```
