# `FigVideoContainerLayer`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigBaseCALayer`
- 8 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"CALayer" _videoLayer;
@"NSString" _STSLabel;
B _shouldResizeVideoLayer;
B _isForScrubbingOnly;
@"CALayer" _STSLayer;
@"CALayer" _UUIDLayer;
@"NSString" _preferredCADynamicRange;
^{OpaqueFigSimpleMutex=} _HDRPreferDynamicRangeMutex;
```

## Properties

```
@property (T@"CALayer",&,N) videoLayer;
@property (TB,N,V_shouldResizeVideoLayer) shouldResizeVideoLayer;
@property (T@"NSString",&,N,V_STSLabel) STSLabel;
@property (TB,N,GisForScrubbingOnly,V_isForScrubbingOnly) forScrubbingOnly;
```

## Class methods

```
+[FigVideoContainerLayer defaultActionForKey:];
```

## Instance methods

```
-[FigVideoContainerLayer actionForKey:];
-[FigVideoContainerLayer setToneMapToStandardDynamicRange:];
-[FigVideoContainerLayer setPreferredDynamicRange:];
-[FigVideoContainerLayer videoLayer];
-[FigVideoContainerLayer init];
-[FigVideoContainerLayer initWithUUID:];
-[FigVideoContainerLayer dealloc];
-[FigVideoContainerLayer preferredDynamicRange];
-[FigVideoContainerLayer setVideoLayer:];
-[FigVideoContainerLayer setSTSLabel:];
-[FigVideoContainerLayer layoutSublayers];
-[FigVideoContainerLayer STSLabel];
-[FigVideoContainerLayer isForScrubbingOnly];
-[FigVideoContainerLayer setForScrubbingOnly:];
-[FigVideoContainerLayer setShouldResizeVideoLayer:];
-[FigVideoContainerLayer setupVideoLayer:];
-[FigVideoContainerLayer shouldResizeVideoLayer];
```
