# `_UISceneHingeState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSSecureCoding`, `BSXPCCoding`, `BSXPCSecureCoding`
- 7 instance variables, 11 properties, 21 instance methods, 3 class methods

## Instance variables

```
q _magicPose;
q _status;
q _nextStatus;
d _progress;
d _angleDegrees;
Q _identifier;
@"NSString" _sceneRegionIdentifier;
```

## Properties

```
@property (Tq,R,N,V_magicPose) magicPose;
@property (Tq,R,N,V_status) status;
@property (Tq,R,N,V_nextStatus) nextStatus;
@property (Td,R,N,V_progress) progress;
@property (Td,R,N,V_angleDegrees) angleDegrees;
@property (TQ,R,N,V_identifier) identifier;
@property (T@"NSString",R,C,N,V_sceneRegionIdentifier) sceneRegionIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISceneHingeState supportsBSXPCSecureCoding];
+[_UISceneHingeState supportsSecureCoding];
+[_UISceneHingeState hingeStateFromBuilder:];
```

## Instance methods

```
-[_UISceneHingeState debugDescription];
-[_UISceneHingeState identifier];
-[_UISceneHingeState init];
-[_UISceneHingeState initWithXPCDictionary:];
-[_UISceneHingeState status];
-[_UISceneHingeState progress];
-[_UISceneHingeState succinctDescription];
-[_UISceneHingeState encodeWithXPCDictionary:];
-[_UISceneHingeState encodeWithCoder:];
-[_UISceneHingeState hash];
-[_UISceneHingeState description];
-[_UISceneHingeState initWithCoder:];
-[_UISceneHingeState appendDescriptionToStream:];
-[_UISceneHingeState encodeWithBSXPCCoder:];
-[_UISceneHingeState initWithBSXPCCoder:];
-[_UISceneHingeState copyWithZone:];
-[_UISceneHingeState isEqual:];
-[_UISceneHingeState angleDegrees];
-[_UISceneHingeState magicPose];
-[_UISceneHingeState nextStatus];
-[_UISceneHingeState sceneRegionIdentifier];
```
