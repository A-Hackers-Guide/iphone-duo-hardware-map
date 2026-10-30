# `ABPK2D3DLiftingData`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _rawJointsUsedForLifting;
{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>="__begin_"^"__end_"^""{?="__cap_"^}} _rotatedJointsUsedForLifting;
{array<float, 32UL>="__elems_"[32f]} _multiArray;
{array<float, 32UL>="__elems_"[32f]} _unnormalizedMultiArray;
q _rotationNeeded;
```

## Properties

```
@property (Tr^,R,N) joints;
@property (Tr^,R,N) rotatedJoints;
@property (TQ,R,N) jointCount;
@property (Tr^f,R,N) liftingData3D;
@property (Tr^f,R,N) unnormalizedLiftingData3D;
@property (TQ,R,N) liftingData3DElementCount;
```

## Class methods

```
+[ABPK2D3DLiftingData supportsSecureCoding];
```

## Instance methods

```
-[ABPK2D3DLiftingData encodeWithCoder:];
-[ABPK2D3DLiftingData hash];
-[ABPK2D3DLiftingData initWithCoder:];
-[ABPK2D3DLiftingData isEqual:];
-[ABPK2D3DLiftingData jointCount];
-[ABPK2D3DLiftingData joints];
-[ABPK2D3DLiftingData _rotateAndUndoCroppingFromRect:];
-[ABPK2D3DLiftingData initWithHumanForLifting:imageSize:rotation:croppedRect:];
-[ABPK2D3DLiftingData initWithJoints:numberOfJoints:];
-[ABPK2D3DLiftingData initWithJoints:numberOfJoints:imageSize:];
-[ABPK2D3DLiftingData initWithJoints:numberOfJoints:liftingData3D:liftingData3DElementCount:];
-[ABPK2D3DLiftingData initWithJoints:numberOfJoints:rotation:croppedRect:liftingData3D:liftingData3DElementCount:];
-[ABPK2D3DLiftingData liftingData3D];
-[ABPK2D3DLiftingData liftingData3DElementCount];
-[ABPK2D3DLiftingData prepareLiftingInput:imageSize:pUnnormalizedMultiArray:pMultiArray:];
-[ABPK2D3DLiftingData rotatedJoints];
-[ABPK2D3DLiftingData unnormalizedLiftingData3D];
```
