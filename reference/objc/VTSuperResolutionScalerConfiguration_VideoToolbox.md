# `VTSuperResolutionScalerConfiguration`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorConfiguration`
- 11 instance variables, 18 properties, 16 instance methods, 4 class methods

## Instance variables

```
@"VESuperResolutionConfiguration" _veConfiguration;
B _precomputedFlow;
q _frameWidth;
q _frameHeight;
q _inputType;
q _scaleFactor;
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
@property (Tq,R,N,V_inputType) inputType;
@property (TB,R,N,GusesPrecomputedFlow,V_precomputedFlow) precomputedFlow;
@property (Tq,R,N,V_scaleFactor) scaleFactor;
@property (Tq,R,N,V_qualityPrioritization) qualityPrioritization;
@property (Tq,R,N,V_revision) revision;
@property (T@"NSArray",R,N,V_frameSupportedPixelFormats) frameSupportedPixelFormats;
@property (T@"NSDictionary",R,N,V_sourcePixelBufferAttributes) sourcePixelBufferAttributes;
@property (T@"NSDictionary",R,N,V_destinationPixelBufferAttributes) destinationPixelBufferAttributes;
@property (Tq,R,N) configurationModelStatus;
@property (Tf,R,N) configurationModelPercentageAvailable;
@property (Tq,?,R,N) nextFrameCount;
@property (Tq,?,R,N) previousFrameCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTSuperResolutionScalerConfiguration isSupported];
+[VTSuperResolutionScalerConfiguration defaultRevision];
+[VTSuperResolutionScalerConfiguration supportedRevisions];
+[VTSuperResolutionScalerConfiguration supportedScaleFactors];
```

## Instance methods

```
-[VTSuperResolutionScalerConfiguration revision];
-[VTSuperResolutionScalerConfiguration dealloc];
-[VTSuperResolutionScalerConfiguration qualityPrioritization];
-[VTSuperResolutionScalerConfiguration inputType];
-[VTSuperResolutionScalerConfiguration scaleFactor];
-[VTSuperResolutionScalerConfiguration veConfiguration];
-[VTSuperResolutionScalerConfiguration configurationModelPercentageAvailable];
-[VTSuperResolutionScalerConfiguration configurationModelStatus];
-[VTSuperResolutionScalerConfiguration destinationPixelBufferAttributes];
-[VTSuperResolutionScalerConfiguration downloadConfigurationModelWithCompletionHandler:];
-[VTSuperResolutionScalerConfiguration frameHeight];
-[VTSuperResolutionScalerConfiguration frameSupportedPixelFormats];
-[VTSuperResolutionScalerConfiguration frameWidth];
-[VTSuperResolutionScalerConfiguration initWithFrameWidth:frameHeight:scaleFactor:inputType:usePrecomputedFlow:qualityPrioritization:revision:];
-[VTSuperResolutionScalerConfiguration sourcePixelBufferAttributes];
-[VTSuperResolutionScalerConfiguration usesPrecomputedFlow];
```
