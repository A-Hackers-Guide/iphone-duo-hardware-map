# `BLSHFlipbookSpecification`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q _softMemoryLimit;
q _frameCapacity;
d _framesPerSecond;
d _minimumGapDuration;
d _coaelscingEpsilon;
d _minimumPrepareInterval;
d _maximumRenderInterval;
d _surfaceAllocationPoolSize;
d _surfaceOverallocationFactor;
```

## Properties

```
@property (TQ,R,N,V_softMemoryLimit) softMemoryLimit;
@property (Tq,R,N,V_frameCapacity) frameCapacity;
@property (Td,R,N,V_framesPerSecond) framesPerSecond;
@property (Td,R,N,V_minimumGapDuration) minimumGapDuration;
@property (Td,R,N,V_coaelscingEpsilon) coaelscingEpsilon;
@property (Td,R,N,V_minimumPrepareInterval) minimumPrepareInterval;
@property (Td,R,N,V_maximumRenderInterval) maximumRenderInterval;
@property (Td,R,N,V_surfaceAllocationPoolSize) surfaceAllocationPoolSize;
@property (Td,R,N,V_surfaceOverallocationFactor) surfaceOverallocationFactor;
```

## Instance methods

```
-[BLSHFlipbookSpecification description];
-[BLSHFlipbookSpecification framesPerSecond];
-[BLSHFlipbookSpecification frameCapacity];
-[BLSHFlipbookSpecification initWithSoftMemoryLimit:frameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:];
-[BLSHFlipbookSpecification maximumRenderInterval];
-[BLSHFlipbookSpecification softMemoryLimit];
-[BLSHFlipbookSpecification coaelscingEpsilon];
-[BLSHFlipbookSpecification initWithFrameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:];
-[BLSHFlipbookSpecification initWithSoftMemoryLimit:frameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:surfacePoolSize:surfaceOverallocationFactor:];
-[BLSHFlipbookSpecification minimumGapDuration];
-[BLSHFlipbookSpecification minimumPrepareInterval];
-[BLSHFlipbookSpecification surfaceAllocationPoolSize];
-[BLSHFlipbookSpecification surfaceOverallocationFactor];
```
