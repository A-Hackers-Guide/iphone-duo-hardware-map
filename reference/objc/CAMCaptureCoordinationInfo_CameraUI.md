# `CAMCaptureCoordinationInfo`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 13 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSSet" _allExpectedResultSpecifiers;
Q _resultSpecifiers;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSSet",R,N,V_allExpectedResultSpecifiers) allExpectedResultSpecifiers;
@property (TQ,R,N,V_resultSpecifiers) resultSpecifiers;
@property (TB,R,N,GisHDR) HDR;
@property (TB,R,N,GisFiltered) filtered;
@property (TB,R,N,GisUnfilteredImageForFilteredPair) unfilteredImageForFilteredPair;
@property (TB,R,N,GisFilteredImageForFilteredPair) filteredImageForFilteredPair;
@property (TB,R,N,GisEV0ForHDREV0Pair) EV0ForHDREV0Pair;
@property (TB,R,N,GisHDRForHDREV0Pair) HDRForHDREV0Pair;
@property (TB,R,N,GisFinalExpectedStillImageResult) finalExpectedStillImageResult;
@property (TB,R,N,GisFinalExpectedVideoResult) finalExpectedVideoResult;
@property (TB,R,N) representsFinalProcessedStillImage;
@property (TB,R,N) representsFinalProcessedVideo;
```

## Instance methods

```
-[CAMCaptureCoordinationInfo isFinalExpectedStillImageResult];
-[CAMCaptureCoordinationInfo isHDR];
-[CAMCaptureCoordinationInfo isUnfilteredImageForFilteredPair];
-[CAMCaptureCoordinationInfo identifier];
-[CAMCaptureCoordinationInfo isHDRForHDREV0Pair];
-[CAMCaptureCoordinationInfo isEV0ForHDREV0Pair];
-[CAMCaptureCoordinationInfo initWithIdentifier:allExpectedResultSpecifiers:resultSpecifiers:];
-[CAMCaptureCoordinationInfo isFilteredImageForFilteredPair];
-[CAMCaptureCoordinationInfo representsFinalProcessedStillImage];
-[CAMCaptureCoordinationInfo resultSpecifiers];
-[CAMCaptureCoordinationInfo isFinalExpectedVideoResult];
-[CAMCaptureCoordinationInfo representsFinalProcessedVideo];
-[CAMCaptureCoordinationInfo isFiltered];
-[CAMCaptureCoordinationInfo description];
-[CAMCaptureCoordinationInfo allExpectedResultSpecifiers];
```
