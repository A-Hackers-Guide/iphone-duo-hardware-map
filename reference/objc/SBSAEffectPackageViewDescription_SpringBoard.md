# `SBSAEffectPackageViewDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSAViewDescription`
- 5 instance variables, 5 properties, 15 instance methods, 2 class methods

## Instance variables

```
B _stateAnimated;
@"NSString" _packageName;
@"NSString" _requestedState;
@"NSString" _reachedState;
d _rotationAngle;
```

## Properties

```
@property (T@"NSString",C,N,S_setPackageName:,V_packageName) packageName;
@property (T@"NSString",C,N,S_setRequestedState:,V_requestedState) requestedState;
@property (T@"NSString",C,N,S_setReachedState:,V_reachedState) reachedState;
@property (Td,N,S_setRotationAngle:,V_rotationAngle) rotationAngle;
@property (TB,N,GisStateAnimated,S_setStateAnimated:,V_stateAnimated) stateAnimated;
```

## Class methods

```
+[SBSAEffectPackageViewDescription initialize];
+[SBSAEffectPackageViewDescription mutatorClass];
```

## Instance methods

```
-[SBSAEffectPackageViewDescription rotationAngle];
-[SBSAEffectPackageViewDescription packageName];
-[SBSAEffectPackageViewDescription hash];
-[SBSAEffectPackageViewDescription description];
-[SBSAEffectPackageViewDescription copyWithZone:];
-[SBSAEffectPackageViewDescription isEqual:];
-[SBSAEffectPackageViewDescription membersForCoder];
-[SBSAEffectPackageViewDescription isStateAnimated];
-[SBSAEffectPackageViewDescription _setPackageName:];
-[SBSAEffectPackageViewDescription _setReachedState:];
-[SBSAEffectPackageViewDescription _setRequestedState:];
-[SBSAEffectPackageViewDescription _setRotationAngle:];
-[SBSAEffectPackageViewDescription _setStateAnimated:];
-[SBSAEffectPackageViewDescription reachedState];
-[SBSAEffectPackageViewDescription requestedState];
```
