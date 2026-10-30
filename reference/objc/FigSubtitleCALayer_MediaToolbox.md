# `FigSubtitleCALayer`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigSubtitleBackdropCALayer`
- Protocols: `CALayerDelegate`
- 2 instance variables, 7 properties, 29 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigSubtitleCALayerInternal=^{OpaqueFigPlayer}@{CGRect={CGPoint=dd}{CGSize=dd}}{CGSize=dd}C{CGRect={CGPoint=dd}{CGSize=dd}}{FigGeometryMargins={FigGeometryDimension=dII}{FigGeometryDimension=dII}{FigGeometryDimension=dII}{FigGeometryDimension=dII}}CBCC@I^{__CFString}^{OpaqueFigCaptionRendererSession}^{OpaqueFigSubtitleRenderer}^{__CFDictionary}C^{__CFDictionary}^{__CFArray}^{__CFArray}{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}} layerInternal;
B _hidesAllCaptionDisplay;
```

## Properties

```
@property (TB,N,V_hidesAllCaptionDisplay) hidesAllCaptionDisplay;
@property (TB,N,GisOverscanSubtitleSupportEnabled) overscanSubtitleSupportEnabled;
@property (T@"NSString",C,N) captionRenderingStrategy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigSubtitleCALayer defaultActionForKey:];
```

## Instance methods

```
-[FigSubtitleCALayer addAnimations:forKey:];
-[FigSubtitleCALayer actionForKey:];
-[FigSubtitleCALayer layoutSublayersOfLayer:];
-[FigSubtitleCALayer setCaptionsAvoidanceOptions:];
-[FigSubtitleCALayer clear];
-[FigSubtitleCALayer isOverscanSubtitleSupportEnabled];
-[FigSubtitleCALayer setHidden:];
-[FigSubtitleCALayer init];
-[FigSubtitleCALayer setVideosize:];
-[FigSubtitleCALayer dealloc];
-[FigSubtitleCALayer drawLayer:inContext:];
-[FigSubtitleCALayer initWithLayer:];
-[FigSubtitleCALayer captionRenderingStrategy];
-[FigSubtitleCALayer setPlayer:];
-[FigSubtitleCALayer hidesAllCaptionDisplay];
-[FigSubtitleCALayer setVideoRelativeToViewport:];
-[FigSubtitleCALayer setCaptionsAvoidanceMargins:];
-[FigSubtitleCALayer updateNonForcedSubtitleDisplayEnabled:];
-[FigSubtitleCALayer setOverscanSubtitleSupportEnabled:];
-[FigSubtitleCALayer setHidesAllCaptionDisplay:];
-[FigSubtitleCALayer handleNeedsLayoutNotification];
-[FigSubtitleCALayer setViewport:];
-[FigSubtitleCALayer _addBoundsAnimation:forKey:];
-[FigSubtitleCALayer setCaptionRendererOutputOptions:forKeyPath:];
-[FigSubtitleCALayer _addPositionAnimation:forKey:];
-[FigSubtitleCALayer setCaptionRendererOutputSeparated:];
-[FigSubtitleCALayer setSubtitleGravityNonObscuring:];
-[FigSubtitleCALayer removeAnimationsForKey:];
-[FigSubtitleCALayer setCaptionRenderingStrategy:];
```
