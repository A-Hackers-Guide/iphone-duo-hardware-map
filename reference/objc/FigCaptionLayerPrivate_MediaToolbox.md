# `FigCaptionLayerPrivate`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigCFCaptionRenderer=} renderer;
@"NSMutableArray" captionElementLayers;
^{OpaqueFigSimpleMutex=} renderMutex;
^{OpaqueFigReentrantMutex=} layoutSublayersMutex;
C shouldDrawGrid;
@"NSMutableArray" captionBackdropLayers;
C enableBackdrop;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} videoRelativeToViewport;
{FigGeometryMargins="left"{FigGeometryDimension="value"d"units"I"flags"I}"right"{FigGeometryDimension="value"d"units"I"flags"I}"top"{FigGeometryDimension="value"d"units"I"flags"I}"bottom"{FigGeometryDimension="value"d"units"I"flags"I}} captionsAvoidanceMargins;
C enableGMSpew;
@"NSMutableDictionary" options;
B separated;
B separatedUpdated;
```
