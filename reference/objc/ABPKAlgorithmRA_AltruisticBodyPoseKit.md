# `ABPKAlgorithmRA`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"ABPKAlgorithm" _abpkAlgorithm;
q _exitPoint;
{CGSize="width"d"height"d} _inputResolution;
@"ABPKCameraParams" _abpkCameraParams;
@"ABPKAlgorithmParams" _algParams;
@"NSString" _imagePreProcessingType;
@"ABPKCropParams" _cropParameters;
@"ABPKPaddingParams" _paddingParameters;
{CGSize="width"d"height"d} _mlResolution;
@"ABPKImagePreProcessing" _imagePreprocessor;
@"ABPKImagePreProcessingParams" _imagePreProcessingParams;
{CGSize="width"d"height"d} _regImageDimensions;
{?="columns"[3]} _regIntrinsics;
^{__CVBuffer=} _mlImage;
@"NSString" _saveDirectory;
@"ABPKAlgInput" _algorithmInput;
@"ABPKAlgOutput" _algorithmOutput;
```

## Instance methods

```
-[ABPKAlgorithmRA dealloc];
-[ABPKAlgorithmRA runABPKAlgorithmWithInputData:andGetOutput:];
-[ABPKAlgorithmRA preprocessInputImage:];
-[ABPKAlgorithmRA _endABPKAlgoInitSignpost];
-[ABPKAlgorithmRA _endExecuteAlgorithmSignpost];
-[ABPKAlgorithmRA _endImagePreprocessingSignpost];
-[ABPKAlgorithmRA _startABPKAlgoInitSignpost];
-[ABPKAlgorithmRA _startExecuteAlgorithmSignpost];
-[ABPKAlgorithmRA _startImagePreprocessingSignpost];
-[ABPKAlgorithmRA computeRootTransforms:withVioPose:withVioPoseValidity:];
-[ABPKAlgorithmRA initWithCameraParams:];
-[ABPKAlgorithmRA initWithCameraParams:andAlgorithmMode:];
-[ABPKAlgorithmRA saveInputData:andOutputData:ToDir:withFileNamePrefix:];
-[ABPKAlgorithmRA setExitPoint:];
```
