# `SRStreamBlockSample`

- Image: [`/System/Library/PrivateFrameworks/SensorKitSupport.framework/SensorKitSupport`](../userland/System__Library__PrivateFrameworks__SensorKitSupport.framework__SensorKitSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `SRSampleExporting`, `SRSampleDirectExporting`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"_TtC16SensorKitSupport13SRStreamBlock" _streamBlock;
@"NSDictionary" _sampleDict;
```

## Properties

```
@property (T@"_TtC16SensorKitSupport13SRStreamBlock",&,N,V_streamBlock) streamBlock;
@property (T@"NSDictionary",&,N,V_sampleDict) sampleDict;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SRStreamBlockSample initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRStreamBlockSample sr_dictionaryRepresentation];
-[SRStreamBlockSample sr_prefersUTF8StringRepresentation];
-[SRStreamBlockSample sr_writeUTF8RepresentationToOutputStream:];
-[SRStreamBlockSample setStreamBlock:];
-[SRStreamBlockSample sampleDict];
-[SRStreamBlockSample setSampleDict:];
-[SRStreamBlockSample streamBlock];
```
