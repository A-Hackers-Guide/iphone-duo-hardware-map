# `MPSGraphRandomOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
I _dataType;
f _min;
f _max;
f _mean;
f _standardDeviation;
Q _distribution;
q _minInteger;
q _maxInteger;
Q _samplingMethod;
```

## Properties

```
@property (TQ,N,V_distribution) distribution;
@property (TI,N,V_dataType) dataType;
@property (Tf,N,V_min) min;
@property (Tf,N,V_max) max;
@property (Tq,N,V_minInteger) minInteger;
@property (Tq,N,V_maxInteger) maxInteger;
@property (Tf,N,V_mean) mean;
@property (Tf,N,V_standardDeviation) standardDeviation;
@property (TQ,N,V_samplingMethod) samplingMethod;
```

## Class methods

```
+[MPSGraphRandomOpDescriptor descriptorWithDistribution:dataType:];
```

## Instance methods

```
-[MPSGraphRandomOpDescriptor min];
-[MPSGraphRandomOpDescriptor setDataType:];
-[MPSGraphRandomOpDescriptor max];
-[MPSGraphRandomOpDescriptor dataType];
-[MPSGraphRandomOpDescriptor standardDeviation];
-[MPSGraphRandomOpDescriptor distribution];
-[MPSGraphRandomOpDescriptor copyWithZone:];
-[MPSGraphRandomOpDescriptor setMax:];
-[MPSGraphRandomOpDescriptor setDistribution:];
-[MPSGraphRandomOpDescriptor setMin:];
-[MPSGraphRandomOpDescriptor mean];
-[MPSGraphRandomOpDescriptor setMaxInteger:];
-[MPSGraphRandomOpDescriptor setMean:];
-[MPSGraphRandomOpDescriptor setMinInteger:];
-[MPSGraphRandomOpDescriptor setStandardDeviation:];
-[MPSGraphRandomOpDescriptor samplingMethod];
-[MPSGraphRandomOpDescriptor setSamplingMethod:];
-[MPSGraphRandomOpDescriptor maxInteger];
-[MPSGraphRandomOpDescriptor minInteger];
```
