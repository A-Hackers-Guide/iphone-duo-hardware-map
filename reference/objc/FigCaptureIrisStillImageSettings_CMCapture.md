# `FigCaptureIrisStillImageSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureStillImageSettings`
- 8 instance variables, 8 properties, 22 instance methods, 1 class methods

## Instance variables

```
i _movieMode;
@"FigCaptureMovieFileRecordingSettings" _movieRecordingSettings;
@"NSURL" _movieURLForOriginalImage;
@"NSArray" _movieLevelMetadataForOriginalImage;
@"NSURL" _spatialOverCaptureMovieURLForOriginalImage;
@"NSArray" _spatialOverCaptureMovieLevelMetadataForOriginalImage;
{CGSize="width"d"height"d} _nonDestructiveCropSize;
@"FigCaptureSemanticStyle" _semanticStyle;
```

## Properties

```
@property (Ti,N,V_movieMode) movieMode;
@property (T@"FigCaptureMovieFileRecordingSettings",C,N,V_movieRecordingSettings) movieRecordingSettings;
@property (T@"NSURL",C,N,V_movieURLForOriginalImage) movieURLForOriginalImage;
@property (T@"NSArray",C,N,V_movieLevelMetadataForOriginalImage) movieLevelMetadataForOriginalImage;
@property (T@"NSURL",C,N,V_spatialOverCaptureMovieURLForOriginalImage) spatialOverCaptureMovieURLForOriginalImage;
@property (T@"NSArray",C,N,V_spatialOverCaptureMovieLevelMetadataForOriginalImage) spatialOverCaptureMovieLevelMetadataForOriginalImage;
@property (T{CGSize=dd},N,V_nonDestructiveCropSize) nonDestructiveCropSize;
@property (T@"FigCaptureSemanticStyle",&,N,V_semanticStyle) semanticStyle;
```

## Class methods

```
+[FigCaptureIrisStillImageSettings supportsSecureCoding];
```

## Instance methods

```
-[FigCaptureIrisStillImageSettings setSemanticStyle:];
-[FigCaptureIrisStillImageSettings copyForPersonalPhotographerWithSettingsID:rotationDegrees:mirrored:];
-[FigCaptureIrisStillImageSettings movieLevelMetadataForOriginalImage];
-[FigCaptureIrisStillImageSettings movieRecordingSettings];
-[FigCaptureIrisStillImageSettings movieURLForOriginalImage];
-[FigCaptureIrisStillImageSettings setSpatialOverCaptureMovieLevelMetadataForOriginalImage:];
-[FigCaptureIrisStillImageSettings dealloc];
-[FigCaptureIrisStillImageSettings setNonDestructiveCropSize:];
-[FigCaptureIrisStillImageSettings setMovieMode:];
-[FigCaptureIrisStillImageSettings movieMode];
-[FigCaptureIrisStillImageSettings setMovieLevelMetadataForOriginalImage:];
-[FigCaptureIrisStillImageSettings semanticStyle];
-[FigCaptureIrisStillImageSettings encodeWithCoder:];
-[FigCaptureIrisStillImageSettings setMovieRecordingSettings:];
-[FigCaptureIrisStillImageSettings description];
-[FigCaptureIrisStillImageSettings spatialOverCaptureMovieLevelMetadataForOriginalImage];
-[FigCaptureIrisStillImageSettings initWithCoder:];
-[FigCaptureIrisStillImageSettings spatialOverCaptureMovieURLForOriginalImage];
-[FigCaptureIrisStillImageSettings nonDestructiveCropSize];
-[FigCaptureIrisStillImageSettings copyWithZone:];
-[FigCaptureIrisStillImageSettings setSpatialOverCaptureMovieURLForOriginalImage:];
-[FigCaptureIrisStillImageSettings setMovieURLForOriginalImage:];
```
