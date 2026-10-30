# `SBFHingeRun`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFHingeSamplePlayback`
- 3 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
^{?=dffffiiBB} _samples;
Q _count;
d _modalSampleInterval;
```

## Properties

```
@property (TQ,R,N) sampleCount;
@property (Td,R,N) duration;
@property (Td,R,N) modalSampleInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFHingeRun runWithContentsOfFile:error:];
```

## Instance methods

```
-[SBFHingeRun dealloc];
-[SBFHingeRun duration];
-[SBFHingeRun sampleCount];
-[SBFHingeRun description];
-[SBFHingeRun sampleAtIndex:];
-[SBFHingeRun _interpolatedSampleAtTime:fromIndex:];
-[SBFHingeRun _motionRangeContainingIndex:dwellInterval:];
-[SBFHingeRun initWithSamples:count:];
-[SBFHingeRun modalSampleInterval];
-[SBFHingeRun offsetAtIndex:];
-[SBFHingeRun playbackFromNormalizedOffset:maxDuration:seed:error:];
-[SBFHingeRun windowWithMinimumDuration:landingMinimum:landingMaximum:seed:error:];
```
