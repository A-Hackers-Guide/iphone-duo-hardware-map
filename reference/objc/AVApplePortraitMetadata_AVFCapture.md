# `AVApplePortraitMetadata`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"AVApplePortraitMetadataInternal" _internal;
```

## Properties

```
@property (Tf,R) apertureFocalRatio;
@property (Tf,R) minimumApertureFocalRatio;
@property (Tf,R) maximumApertureFocalRatio;
@property (Tf,R) portraitLightingEffectStrength;
@property (Tf,R) luminanceNoiseAmplitude;
@property (Ti,R) faceOrientation;
@property (T@"NSData",R) faceObservationsData;
@property (T@"NSIndexSet",R) indexesOfShallowDepthOfFieldObservations;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R) focusRectangle;
@property (TI,R) SDOFRenderingVersion;
```

## Class methods

```
+[AVApplePortraitMetadata supportsSecureCoding];
```

## Instance methods

```
-[AVApplePortraitMetadata portraitLightingEffectStrength];
-[AVApplePortraitMetadata dealloc];
-[AVApplePortraitMetadata encodeWithCoder:];
-[AVApplePortraitMetadata initWithCoder:];
-[AVApplePortraitMetadata initWithInternal:];
-[AVApplePortraitMetadata faceOrientation];
-[AVApplePortraitMetadata SDOFRenderingVersion];
-[AVApplePortraitMetadata apertureFocalRatio];
-[AVApplePortraitMetadata faceObservationsData];
-[AVApplePortraitMetadata focusRectangle];
-[AVApplePortraitMetadata indexesOfShallowDepthOfFieldObservations];
-[AVApplePortraitMetadata initWithPortraitMetadataDictionary:];
-[AVApplePortraitMetadata luminanceNoiseAmplitude];
-[AVApplePortraitMetadata maximumApertureFocalRatio];
-[AVApplePortraitMetadata minimumApertureFocalRatio];
```
