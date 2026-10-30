# `CAMCoverScreenStateWrapper`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 7 properties, 13 instance methods, 4 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _state;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _shouldLoadAssets;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _$observationRegistrar;
```

## Properties

```
@property (TB,N) shouldLoadAssets;
@property (TB,N,R) isOff;
@property (TB,N,R) isShutterBuddy;
@property (TB,N,R) isPartnerPreview;
@property (TB,N,R) isCoverScreenFeatureActive;
@property (TB,N,R) isCaptureIndicatorsOnly;
@property (TB,N,R) areCaptureIndicatorsActive;
```

## Class methods

```
+[CAMCoverScreenStateWrapper off];
+[CAMCoverScreenStateWrapper captureIndicatorsOnly];
+[CAMCoverScreenStateWrapper partnerPreview];
+[CAMCoverScreenStateWrapper shutterBuddy];
```

## Instance methods

```
-[CAMCoverScreenStateWrapper init];
-[CAMCoverScreenStateWrapper isEqual:];
-[CAMCoverScreenStateWrapper setShouldLoadAssets:];
-[CAMCoverScreenStateWrapper shouldLoadAssets];
-[CAMCoverScreenStateWrapper areCaptureIndicatorsActive];
-[CAMCoverScreenStateWrapper enableAssetLoading];
-[CAMCoverScreenStateWrapper isCaptureIndicatorsOnly];
-[CAMCoverScreenStateWrapper isCoverScreenFeatureActive];
-[CAMCoverScreenStateWrapper isOff];
-[CAMCoverScreenStateWrapper isPartnerPreview];
-[CAMCoverScreenStateWrapper isShutterBuddy];
-[CAMCoverScreenStateWrapper updateFrom:];
-[CAMCoverScreenStateWrapper withCaptureIndicators:];
```
