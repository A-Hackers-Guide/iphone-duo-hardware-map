# `UISCrossSceneMorphAnimationToken`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `BSXPCSecureCoding`, `BSDescriptionStreaming`
- 3 instance variables, 7 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"FBSSceneIdentityToken" _sceneIdentityToken;
Q _identifierNumber;
@"RBSProcessHandle" _processHandle;
```

## Properties

```
@property (T@"FBSSceneIdentityToken",R,C,N,V_sceneIdentityToken) sceneIdentityToken;
@property (TQ,R,N,V_identifierNumber) identifierNumber;
@property (T@"RBSProcessHandle",R,N,V_processHandle) processHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISCrossSceneMorphAnimationToken supportsBSXPCSecureCoding];
+[UISCrossSceneMorphAnimationToken supportsSecureCoding];
```

## Instance methods

```
-[UISCrossSceneMorphAnimationToken debugDescription];
-[UISCrossSceneMorphAnimationToken encodeWithCoder:];
-[UISCrossSceneMorphAnimationToken processHandle];
-[UISCrossSceneMorphAnimationToken hash];
-[UISCrossSceneMorphAnimationToken description];
-[UISCrossSceneMorphAnimationToken initWithCoder:];
-[UISCrossSceneMorphAnimationToken appendDescriptionToStream:];
-[UISCrossSceneMorphAnimationToken encodeWithBSXPCCoder:];
-[UISCrossSceneMorphAnimationToken initWithBSXPCCoder:];
-[UISCrossSceneMorphAnimationToken copyWithZone:];
-[UISCrossSceneMorphAnimationToken isEqual:];
-[UISCrossSceneMorphAnimationToken initWithSceneIdentityToken:identifierNumber:];
-[UISCrossSceneMorphAnimationToken sceneIdentityToken];
-[UISCrossSceneMorphAnimationToken identifierNumber];
```
