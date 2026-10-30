# `VTTemporalNoiseFilterParameters`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorParameters`
- 6 instance variables, 11 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _hasDiscontinuity;
f _filterStrength;
@"VTFrameProcessorFrame" _sourceFrame;
@"NSArray" _nextFrames;
@"NSArray" _previousFrames;
@"VTFrameProcessorFrame" _destinationFrame;
```

## Properties

```
@property (T@"VTFrameProcessorFrame",R,N,V_sourceFrame) sourceFrame;
@property (T@"NSArray",R,N,V_nextFrames) nextFrames;
@property (T@"NSArray",R,N,V_previousFrames) previousFrames;
@property (Tf,N,V_filterStrength) filterStrength;
@property (TB,N,V_hasDiscontinuity) hasDiscontinuity;
@property (T@"VTFrameProcessorFrame",R,N,V_destinationFrame) destinationFrame;
@property (T@"NSArray",?,R,N) destinationFrames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTTemporalNoiseFilterParameters dealloc];
-[VTTemporalNoiseFilterParameters sourceFrame];
-[VTTemporalNoiseFilterParameters destinationFrame];
-[VTTemporalNoiseFilterParameters filterStrength];
-[VTTemporalNoiseFilterParameters hasDiscontinuity];
-[VTTemporalNoiseFilterParameters initWithSourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:hasDiscontinuity:];
-[VTTemporalNoiseFilterParameters initWithSourceFrame:nextFrames:previousFrames:destinationFrame:hasDiscontinuity:];
-[VTTemporalNoiseFilterParameters nextFrames];
-[VTTemporalNoiseFilterParameters previousFrames];
-[VTTemporalNoiseFilterParameters setFilterStrength:];
-[VTTemporalNoiseFilterParameters setHasDiscontinuity:];
```
