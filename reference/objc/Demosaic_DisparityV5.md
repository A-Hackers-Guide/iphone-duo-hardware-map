# `Demosaic`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
[4@"<MTLComputePipelineState>"] _pipelineStates;
@"FigMetalContext" _metalContext;
{?="sensorBlack"I"sensorWhite"I"outputOffsetY"I"outputSizeY"I"sensorAGC"f"noiseE1x8x"[2f]"readnoiseStdE"f"gatScale"f"gatBias"f"gatBlackNormalized"f"gatWhite"f"sensorGain"f"expIspGain"f"expAwbRgb"[3f]"scaleRawTo16bits"I"sensorGainCeilingToFullRange"f"scaleSashimi"f"rawSensorWidth"I"rawSensorHeight"I"lscSampingOffset""lscSampingRatio""bayerFormat"i} _metadataParameters;
@"<MTLTexture>" _lscGainsTex;
I _outputImageHeight;
f _gatNoiseStdInFullResolution;
f _tuningNoiseProcessingScale;
f _maxAnalogGain;
```

## Properties

```
@property (TI,N,V_outputImageHeight) outputImageHeight;
@property (Tf,N,V_gatNoiseStdInFullResolution) gatNoiseStdInFullResolution;
@property (Tf,N,V_tuningNoiseProcessingScale) tuningNoiseProcessingScale;
@property (Tf,N,V_maxAnalogGain) maxAnalogGain;
```

## Instance methods

```
-[Demosaic _compileShaders];
-[Demosaic initWithMetalContext:];
-[Demosaic maxAnalogGain];
-[Demosaic resampleLuma:toLuma:magnification:preShift:];
-[Demosaic setGatNoiseStdInFullResolution:];
-[Demosaic convertLinearRGB:toLuma:];
-[Demosaic demosaic2x:rawImagePixelFormat:toLuma:toRGBA:];
-[Demosaic downscaleRGBA:toRGBA:scalingFactor:commandBuffer:];
-[Demosaic fillLSCGainsTextureFrom:];
-[Demosaic gatNoiseStdInFullResolution];
-[Demosaic outputImageHeight];
-[Demosaic preProcessMetadata:cameraInfoByPortType:];
-[Demosaic setMaxAnalogGain:];
-[Demosaic setOutputImageHeight:];
-[Demosaic setTuningNoiseProcessingScale:];
-[Demosaic tuningNoiseProcessingScale];
```
