# `FigCaptureSourceBackingsProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _sourceBackings;
@"FigCaptureSourceCommonSettings" _commonSettings;
B _hasMicSource;
@"NSDictionary" _continuityCaptureCameraCapabilities;
```

## Properties

```
@property (T@"NSArray",R,N) sourceBackings;
@property (T@"FigCaptureSourceCommonSettings",R,N,V_commonSettings) commonSettings;
@property (T@"NSDictionary",R,N,V_continuityCaptureCameraCapabilities) continuityCaptureCameraCapabilities;
```

## Class methods

```
+[FigCaptureSourceBackingsProvider initialize];
+[FigCaptureSourceBackingsProvider sharedCaptureSourceBackingsProvider];
```

## Instance methods

```
-[FigCaptureSourceBackingsProvider dealloc];
-[FigCaptureSourceBackingsProvider continuityCaptureCameraCapabilities];
-[FigCaptureSourceBackingsProvider commonSettings];
-[FigCaptureSourceBackingsProvider initWithSourceInfoDictionaries:commonSettings:];
-[FigCaptureSourceBackingsProvider sourceBackings];
```
