# `ABPKImagePreProcessingParams`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 1 class methods

## Instance variables

```
i _type;
@"ABPKCropParams" _cropParams;
@"ABPKPaddingParams" _paddingParams;
@"ABPKDirectScalingParams" _scalingParams;
{CGSize="width"d"height"d} _inputResolution;
{CGSize="width"d"height"d} _outputResolution;
```

## Properties

```
@property (T@"ABPKCropParams",R,N,V_cropParams) cropParams;
@property (T@"ABPKPaddingParams",R,N,V_paddingParams) paddingParams;
@property (T@"ABPKDirectScalingParams",R,N,V_scalingParams) scalingParams;
@property (Ti,R,N,V_type) type;
@property (T{CGSize=dd},R,N,V_inputResolution) inputResolution;
@property (T{CGSize=dd},R,N,V_outputResolution) outputResolution;
```

## Class methods

```
+[ABPKImagePreProcessingParams convert2DPoint:toInputSpaceWithParams:];
```

## Instance methods

```
-[ABPKImagePreProcessingParams type];
-[ABPKImagePreProcessingParams inputResolution];
-[ABPKImagePreProcessingParams cropParams];
-[ABPKImagePreProcessingParams initWithType:inputResolution:outputResolution:];
-[ABPKImagePreProcessingParams outputResolution];
-[ABPKImagePreProcessingParams paddingParams];
-[ABPKImagePreProcessingParams printData];
-[ABPKImagePreProcessingParams scalingParams];
```
