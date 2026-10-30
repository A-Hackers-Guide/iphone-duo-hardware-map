# `ABPKAlgorithmState`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _image_preprocessing;
B _detection2d;
B _lifting3d;
B _registration;
B _retargeting;
```

## Properties

```
@property (TB,V_image_preprocessing) image_preprocessing;
@property (TB,V_detection2d) detection2d;
@property (TB,V_lifting3d) lifting3d;
@property (TB,V_registration) registration;
@property (TB,V_retargeting) retargeting;
```

## Instance methods

```
-[ABPKAlgorithmState init];
-[ABPKAlgorithmState registration];
-[ABPKAlgorithmState toDict];
-[ABPKAlgorithmState setRegistration:];
-[ABPKAlgorithmState setDetection2d:];
-[ABPKAlgorithmState setRetargeting:];
-[ABPKAlgorithmState detection2d];
-[ABPKAlgorithmState image_preprocessing];
-[ABPKAlgorithmState lifting3d];
-[ABPKAlgorithmState retargeting];
-[ABPKAlgorithmState setImage_preprocessing:];
-[ABPKAlgorithmState setLifting3d:];
```
