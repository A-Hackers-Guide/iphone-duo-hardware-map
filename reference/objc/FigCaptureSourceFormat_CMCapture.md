# `FigCaptureSourceFormat`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 13 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _formatDictionary;
@"NSString" _uniqueID;
I _pixelFormatOverride;
@"NSArray" _highResStillImageDimensions;
```

## Properties

```
@property (TI,R) mediaType;
@property (T^{opaqueCMFormatDescription=},R) formatDescription;
@property (T@"NSString",R) uniqueID;
@property (TI,R) format;
@property (T{?=ii},R) dimensions;
@property (Tf,R) minSupportedFrameRate;
@property (Tf,R) maxSupportedFrameRate;
@property (Ti,R) maxPoints;
@property (TB,R,GisDefaultActiveFormat) defaultActiveFormat;
@property (TB,R,GisExperimental) experimental;
@property (T@"NSArray",R,V_highResStillImageDimensions) highResStillImageDimensions;
@property (T{?=ii},R) soleHighResStillImageDimensions;
@property (T{?=ii},R) defaultHighResStillImageDimensions;
```

## Instance methods

```
-[FigCaptureSourceFormat formatDescription];
-[FigCaptureSourceFormat dimensions];
-[FigCaptureSourceFormat dealloc];
-[FigCaptureSourceFormat uniqueID];
-[FigCaptureSourceFormat highResStillImageDimensions];
-[FigCaptureSourceFormat initWithFigCaptureStreamFormatDictionary:];
-[FigCaptureSourceFormat initWithFigCaptureStreamFormatDictionary:pixelFormatOverride:];
-[FigCaptureSourceFormat description];
-[FigCaptureSourceFormat mediaType];
-[FigCaptureSourceFormat isEqual:];
-[FigCaptureSourceFormat format];
-[FigCaptureSourceFormat defaultHighResStillImageDimensions];
-[FigCaptureSourceFormat isDefaultActiveFormat];
-[FigCaptureSourceFormat isExperimental];
-[FigCaptureSourceFormat maxSupportedFrameRate];
-[FigCaptureSourceFormat minSupportedFrameRate];
-[FigCaptureSourceFormat soleHighResStillImageDimensions];
-[FigCaptureSourceFormat formatDictionary];
-[FigCaptureSourceFormat maxPoints];
```
