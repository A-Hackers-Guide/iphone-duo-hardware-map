# `ABDMetadata`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
f _analogGain;
f _hrdRatio;
f _totalGain;
f _luxLevel;
f _noiseAddbackFactor;
Q _bufferWidth;
Q _bufferHeight;
```

## Properties

```
@property (TQ,V_bufferWidth) bufferWidth;
@property (TQ,V_bufferHeight) bufferHeight;
@property (Tf,V_analogGain) analogGain;
@property (Tf,V_hrdRatio) hrdRatio;
@property (Tf,V_totalGain) totalGain;
@property (Tf,V_luxLevel) luxLevel;
@property (Tf,V_noiseAddbackFactor) noiseAddbackFactor;
```

## Instance methods

```
-[ABDMetadata init];
-[ABDMetadata luxLevel];
-[ABDMetadata setLuxLevel:];
-[ABDMetadata bufferHeight];
-[ABDMetadata setBufferHeight:];
-[ABDMetadata setBufferWidth:];
-[ABDMetadata noiseAddbackFactor];
-[ABDMetadata setAnalogGain:];
-[ABDMetadata setHrdRatio:];
-[ABDMetadata setTotalGain:];
-[ABDMetadata bufferWidth];
-[ABDMetadata analogGain];
-[ABDMetadata hrdRatio];
-[ABDMetadata setNoiseAddbackFactor:];
-[ABDMetadata totalGain];
```
