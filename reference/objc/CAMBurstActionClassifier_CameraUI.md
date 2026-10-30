# `CAMBurstActionClassifier`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 11 properties, 28 instance methods, 0 class methods

## Instance variables

```
B hasBeenScaled;
[7d] testVector;
f testAverageCameraTravelDistance;
f testMaxRegistrationErrorIntegral;
f testMaxPeakRegistrationError;
f testMeanPeakRegistrationError;
f testBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix;
f testInOutRatio;
f testMaxInnerDistance;
f testAverageRegistrationErrorSkewness;
f testMinRegionOfInterestSize;
f testMaxRegistrationErrorSkewness;
^{__SVMParameters=[7{__SVMScaleOffset=ff}]ddii^{CAMBurstSupportVector}^{CAMBurstSupportVector}} _svmParameters;
```

## Properties

```
@property (Tf,VtestMaxInnerDistance) testMaxInnerDistance;
@property (Tf,VtestInOutRatio) testInOutRatio;
@property (Tf,VtestMaxPeakRegistrationError) testMaxPeakRegistrationError;
@property (Tf,VtestMeanPeakRegistrationError) testMeanPeakRegistrationError;
@property (Tf,VtestMinRegionOfInterestSize) testMinRegionOfInterestSize;
@property (Tf,VtestMaxRegistrationErrorSkewness) testMaxRegistrationErrorSkewness;
@property (Tf,VtestMaxRegistrationErrorIntegral) testMaxRegistrationErrorIntegral;
@property (Tf,VtestAverageCameraTravelDistance) testAverageCameraTravelDistance;
@property (Tf,VtestAverageRegistrationErrorSkewness) testAverageRegistrationErrorSkewness;
@property (Tf,VtestBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix) testBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix;
@property (T^{__SVMParameters=[7{__SVMScaleOffset=ff}]ddii^{CAMBurstSupportVector}^{CAMBurstSupportVector}},V_svmParameters) svmParameters;
```

## Instance methods

```
-[CAMBurstActionClassifier init];
-[CAMBurstActionClassifier initWithVersion:];
-[CAMBurstActionClassifier setTestMinRegionOfInterestSize:];
-[CAMBurstActionClassifier testAverageCameraTravelDistance];
-[CAMBurstActionClassifier computeKernelValueWithSupportVector:];
-[CAMBurstActionClassifier isBurstAction];
-[CAMBurstActionClassifier predictResult];
-[CAMBurstActionClassifier scaleVector];
-[CAMBurstActionClassifier setSvmParameters:];
-[CAMBurstActionClassifier setTestAverageCameraTravelDistance:];
-[CAMBurstActionClassifier setTestAverageRegistrationErrorSkewness:];
-[CAMBurstActionClassifier setTestBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix:];
-[CAMBurstActionClassifier setTestInOutRatio:];
-[CAMBurstActionClassifier setTestMaxInnerDistance:];
-[CAMBurstActionClassifier setTestMaxPeakRegistrationError:];
-[CAMBurstActionClassifier setTestMaxRegistrationErrorIntegral:];
-[CAMBurstActionClassifier setTestMaxRegistrationErrorSkewness:];
-[CAMBurstActionClassifier setTestMeanPeakRegistrationError:];
-[CAMBurstActionClassifier svmParameters];
-[CAMBurstActionClassifier testAverageRegistrationErrorSkewness];
-[CAMBurstActionClassifier testBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix];
-[CAMBurstActionClassifier testInOutRatio];
-[CAMBurstActionClassifier testMaxInnerDistance];
-[CAMBurstActionClassifier testMaxPeakRegistrationError];
-[CAMBurstActionClassifier testMaxRegistrationErrorIntegral];
-[CAMBurstActionClassifier testMaxRegistrationErrorSkewness];
-[CAMBurstActionClassifier testMeanPeakRegistrationError];
-[CAMBurstActionClassifier testMinRegionOfInterestSize];
```
