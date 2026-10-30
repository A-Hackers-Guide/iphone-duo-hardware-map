# `FBSActiveInterfaceOrientationStateUpdate`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BSXPCSecureCoding`, `NSCopying`
- 4 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"FBSActiveInterfaceOrientationState" _state;
d _animationDuration;
q _rotationDirection;
Q _sequenceNumber;
```

## Properties

```
@property (TQ,R,N,V_sequenceNumber) sequenceNumber;
@property (T@"FBSActiveInterfaceOrientationState",R,N,V_state) state;
@property (Td,R,N,V_animationDuration) animationDuration;
@property (Tq,R,N,V_rotationDirection) rotationDirection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSActiveInterfaceOrientationStateUpdate supportsBSXPCSecureCoding];
```

## Instance methods

```
-[FBSActiveInterfaceOrientationStateUpdate animationDuration];
-[FBSActiveInterfaceOrientationStateUpdate _initWithState:animationDuration:rotationDirection:sequenceNumber:];
-[FBSActiveInterfaceOrientationStateUpdate sequenceNumber];
-[FBSActiveInterfaceOrientationStateUpdate rotationDirection];
-[FBSActiveInterfaceOrientationStateUpdate asLegacyOrientationUpdate];
-[FBSActiveInterfaceOrientationStateUpdate hash];
-[FBSActiveInterfaceOrientationStateUpdate description];
-[FBSActiveInterfaceOrientationStateUpdate appendDescriptionToStream:];
-[FBSActiveInterfaceOrientationStateUpdate encodeWithBSXPCCoder:];
-[FBSActiveInterfaceOrientationStateUpdate initWithBSXPCCoder:];
-[FBSActiveInterfaceOrientationStateUpdate copyWithZone:];
-[FBSActiveInterfaceOrientationStateUpdate isEqual:];
-[FBSActiveInterfaceOrientationStateUpdate state];
```
