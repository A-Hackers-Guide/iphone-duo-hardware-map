# `VTFrameRateConversionConfiguration`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorConfiguration`
- 9 instance variables, 14 properties, 11 instance methods, 4 class methods

## Instance variables

```
@"VEFrameRateConversionConfiguration" _veConfiguration;
B _usePrecomputedFlow;
q _frameWidth;
q _frameHeight;
q _qualityPrioritization;
q _revision;
@"NSArray" _frameSupportedPixelFormats;
@"NSDictionary" _sourcePixelBufferAttributes;
@"NSDictionary" _destinationPixelBufferAttributes;
```

## Properties

```
@property (Tq,R,N,V_frameWidth) frameWidth;
@property (Tq,R,N,V_frameHeight) frameHeight;
@property (TB,R,N,V_usePrecomputedFlow) usePrecomputedFlow;
@property (Tq,R,N,V_qualityPrioritization) qualityPrioritization;
@property (Tq,R,N,V_revision) revision;
@property (T@"NSArray",R,N,V_frameSupportedPixelFormats) frameSupportedPixelFormats;
@property (T@"NSDictionary",R,N,V_sourcePixelBufferAttributes) sourcePixelBufferAttributes;
@property (T@"NSDictionary",R,N,V_destinationPixelBufferAttributes) destinationPixelBufferAttributes;
@property (Tq,?,R,N) nextFrameCount;
@property (Tq,?,R,N) previousFrameCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTFrameRateConversionConfiguration isSupported];
+[VTFrameRateConversionConfiguration defaultRevision];
+[VTFrameRateConversionConfiguration processorSupported];
+[VTFrameRateConversionConfiguration supportedRevisions];
```

## Instance methods

```
-[VTFrameRateConversionConfiguration revision];
-[VTFrameRateConversionConfiguration dealloc];
-[VTFrameRateConversionConfiguration qualityPrioritization];
-[VTFrameRateConversionConfiguration veConfiguration];
-[VTFrameRateConversionConfiguration destinationPixelBufferAttributes];
-[VTFrameRateConversionConfiguration frameHeight];
-[VTFrameRateConversionConfiguration frameSupportedPixelFormats];
-[VTFrameRateConversionConfiguration frameWidth];
-[VTFrameRateConversionConfiguration initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:];
-[VTFrameRateConversionConfiguration sourcePixelBufferAttributes];
-[VTFrameRateConversionConfiguration usePrecomputedFlow];
```
