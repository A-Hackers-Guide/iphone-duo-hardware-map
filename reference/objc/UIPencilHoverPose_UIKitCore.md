# `UIPencilHoverPose`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 6 instance variables, 10 properties, 11 instance methods, 0 class methods

## Instance variables

```
d _zOffset;
d _azimuthAngle;
d _altitudeAngle;
d _rollAngle;
{CGVector="dx"d"dy"d} _azimuthUnitVector;
{CAPoint3D="x"d"y"d"z"d} _location3D;
```

## Properties

```
@property (T{CGPoint=dd},R,N) location;
@property (Td,R,N) zOffset;
@property (Td,R,N) azimuthAngle;
@property (T{CGVector=dd},R,N) azimuthUnitVector;
@property (Td,R,N) altitudeAngle;
@property (Td,R,N) rollAngle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPencilHoverPose debugDescription];
-[UIPencilHoverPose init];
-[UIPencilHoverPose location];
-[UIPencilHoverPose succinctDescription];
-[UIPencilHoverPose rollAngle];
-[UIPencilHoverPose description];
-[UIPencilHoverPose appendDescriptionToStream:];
-[UIPencilHoverPose zOffset];
-[UIPencilHoverPose altitudeAngle];
-[UIPencilHoverPose azimuthAngle];
-[UIPencilHoverPose azimuthUnitVector];
```
