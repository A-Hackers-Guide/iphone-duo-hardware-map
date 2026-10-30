# `CMProxPDP`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 10 instance variables, 10 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" fTimestamp;
@"NSNumber" fIntensity;
@"NSNumber" fIntensityCalDelta;
@"NSNumber" fIntensityBaselineDelta;
@"NSNumber" fAmbient;
@"NSNumber" fPocketProbability;
@"NSNumber" fBaselineConfidence;
@"NSNumber" fRxNtcC;
@"NSNumber" fScanFlags;
@"NSNumber" fPocketFlag;
```

## Properties

```
@property (T@"NSNumber",R,N) timestamp;
@property (T@"NSNumber",R,N) intensity;
@property (T@"NSNumber",R,N) intensityCalDelta;
@property (T@"NSNumber",R,N) intensityBaselineDelta;
@property (T@"NSNumber",R,N) ambient;
@property (T@"NSNumber",R,N) pocketProbability;
@property (T@"NSNumber",R,N) baselineConfidence;
@property (T@"NSNumber",R,N) rxNtcC;
@property (T@"NSNumber",R,N) scanFlags;
@property (T@"NSNumber",R,N) pocketFlag;
```

## Class methods

```
+[CMProxPDP supportsSecureCoding];
```

## Instance methods

```
-[CMProxPDP intensity];
-[CMProxPDP dealloc];
-[CMProxPDP timestamp];
-[CMProxPDP encodeWithCoder:];
-[CMProxPDP description];
-[CMProxPDP initWithCoder:];
-[CMProxPDP copyWithZone:];
-[CMProxPDP scanFlags];
-[CMProxPDP ambient];
-[CMProxPDP baselineConfidence];
-[CMProxPDP initWithTimestamp:intensity:intensityCalDelta:intensityBaselineDelta:ambient:pocketProbability:baselineConfidence:rxNtcC:scanFlags:pocketFlag:];
-[CMProxPDP intensityBaselineDelta];
-[CMProxPDP intensityCalDelta];
-[CMProxPDP pocketFlag];
-[CMProxPDP pocketProbability];
-[CMProxPDP rxNtcC];
```
