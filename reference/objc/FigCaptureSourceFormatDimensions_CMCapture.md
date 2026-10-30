# `FigCaptureSourceFormatDimensions`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 8 instance methods, 3 class methods

## Instance variables

```
{?="width"i"height"i} _dimensions;
{?="width"i"height"i} _deferredPhotoProxyDimensions;
{?="width"i"height"i} _maxUpscalingDimensions;
B _isPrivate;
i _flavor;
```

## Properties

```
@property (T{?=ii},R,V_dimensions) dimensions;
@property (T{?=ii},R,V_deferredPhotoProxyDimensions) deferredPhotoProxyDimensions;
@property (TB,R,V_isPrivate) isPrivate;
@property (Ti,R,V_flavor) flavor;
@property (T{?=ii},R,V_maxUpscalingDimensions) maxUpscalingDimensions;
```

## Class methods

```
+[FigCaptureSourceFormatDimensions identifyDimensionsFromFlavor:availableHighResStillImageDimensions:];
+[FigCaptureSourceFormatDimensions identifyResolutionFlavorFromDimensions:availableHighResStillImageDimensions:aspectRatio:];
+[FigCaptureSourceFormatDimensions identifySourceFormatDimensionsFromDimensions:availableHighResStillImageDimensions:aspectRatio:];
```

## Instance methods

```
-[FigCaptureSourceFormatDimensions isPrivate];
-[FigCaptureSourceFormatDimensions dimensions];
-[FigCaptureSourceFormatDimensions deferredPhotoProxyDimensions];
-[FigCaptureSourceFormatDimensions initWithDimensions:deferredPhotoProxyDimensions:isPrivate:flavor:maxUpscalingDimensions:];
-[FigCaptureSourceFormatDimensions description];
-[FigCaptureSourceFormatDimensions dimensionsAreEqualToDimensions:];
-[FigCaptureSourceFormatDimensions flavor];
-[FigCaptureSourceFormatDimensions maxUpscalingDimensions];
```
