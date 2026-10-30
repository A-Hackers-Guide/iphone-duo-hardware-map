# `ABPKAlgorithmParams`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"ABPK2DDetectionConfiguration" _config2DDetection;
{CGSize="width"d"height"d} _regImageResolution;
{?="columns"[3]} _regIntrinsics;
```

## Properties

```
@property (T{?=[3]},V_regIntrinsics) regIntrinsics;
@property (T{CGSize=dd},V_regImageResolution) regImageResolution;
@property (T@"ABPK2DDetectionConfiguration",&,V_config2DDetection) config2DDetection;
```

## Instance methods

```
-[ABPKAlgorithmParams toDict];
-[ABPKAlgorithmParams config2DDetection];
-[ABPKAlgorithmParams initWithRegIntrinsics:regImageResolution:];
-[ABPKAlgorithmParams regImageResolution];
-[ABPKAlgorithmParams regIntrinsics];
-[ABPKAlgorithmParams setConfig2DDetection:];
-[ABPKAlgorithmParams setRegImageResolution:];
-[ABPKAlgorithmParams setRegIntrinsics:];
```
