# `FBSOrientationUpdate`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 4 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
q _orientation;
Q _sequenceNumber;
d _duration;
q _rotationDirection;
```

## Properties

```
@property (Tq,N,V_orientation) orientation;
@property (TQ,N,V_sequenceNumber) sequenceNumber;
@property (Td,N,V_duration) duration;
@property (Tq,N,V_rotationDirection) rotationDirection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSOrientationUpdate supportsBSXPCSecureCoding];
```

## Instance methods

```
-[FBSOrientationUpdate setOrientation:];
-[FBSOrientationUpdate init];
-[FBSOrientationUpdate setSequenceNumber:];
-[FBSOrientationUpdate orientation];
-[FBSOrientationUpdate sequenceNumber];
-[FBSOrientationUpdate rotationDirection];
-[FBSOrientationUpdate duration];
-[FBSOrientationUpdate description];
-[FBSOrientationUpdate encodeWithBSXPCCoder:];
-[FBSOrientationUpdate initWithOrientation:sequenceNumber:duration:rotationDirection:];
-[FBSOrientationUpdate setRotationDirection:];
-[FBSOrientationUpdate setDuration:];
-[FBSOrientationUpdate initWithBSXPCCoder:];
```
