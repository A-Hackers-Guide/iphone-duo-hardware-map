# `VTTestProcessorParameters`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorParameters`
- 4 instance variables, 9 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"VTFrameProcessorFrame" _sourceFrame;
@"VTFrameProcessorFrame" _nextFrame;
@"VTFrameProcessorFrame" _previousFrame;
@"VTFrameProcessorFrame" _destinationFrame;
```

## Properties

```
@property (T@"VTFrameProcessorFrame",R,N,V_sourceFrame) sourceFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_nextFrame) nextFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_previousFrame) previousFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_destinationFrame) destinationFrame;
@property (T@"NSArray",?,R,N) destinationFrames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTTestProcessorParameters dealloc];
-[VTTestProcessorParameters sourceFrame];
-[VTTestProcessorParameters destinationFrame];
-[VTTestProcessorParameters initWithSourceFrame:nextFrame:previousFrame:destinationFrame:];
-[VTTestProcessorParameters nextFrame];
-[VTTestProcessorParameters previousFrame];
```
