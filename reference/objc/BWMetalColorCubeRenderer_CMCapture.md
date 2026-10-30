# `BWMetalColorCubeRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 10 instance variables, 9 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSBundle" _bundle;
[5@"FigColorCubeMetalFilter"] _filters;
[5@"NSData"] _currentForegroundColorLookupTables;
[5@"NSData"] _currentBackgroundColorLookupTables;
[5{BWInterpolatedColorLookupTableEntry="lookupTable"@"NSData""strength"f"interpolatedTable"@"NSData"}] _interpolatedForegroundColorLookupTables;
[5{BWInterpolatedColorLookupTableEntry="lookupTable"@"NSData""strength"f"interpolatedTable"@"NSData"}] _interpolatedBackgroundColorLookupTables;
@"BWColorLookupCache" _colorLookupCache;
@"<MTLCommandQueue>" _mtlCommandQueue;
B _mixingColorCubesInGammaDomain;
f _previousInterpolationFractionComplete;
```

## Properties

```
@property (TB,R,N) mixingColorCubesInGammaDomain;
@property (T@"NSString",R,C,N) displayName;
@property (Ts,R,N) type;
@property (TB,R,N) supportsAnimation;
@property (TB,R,N) adjustsMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWMetalColorCubeRenderer bundle];
+[BWMetalColorCubeRenderer initialize];
```

## Instance methods

```
-[BWMetalColorCubeRenderer displayName];
-[BWMetalColorCubeRenderer dealloc];
-[BWMetalColorCubeRenderer type];
-[BWMetalColorCubeRenderer adjustsMetadata];
-[BWMetalColorCubeRenderer adjustMetadataOfSampleBuffer:];
-[BWMetalColorCubeRenderer initWithMetalCommandQueue:mixInGammaDomain:];
-[BWMetalColorCubeRenderer isPassThroughRenderer];
-[BWMetalColorCubeRenderer mixingColorCubesInGammaDomain];
-[BWMetalColorCubeRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWMetalColorCubeRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWMetalColorCubeRenderer supportsAnimation];
```
