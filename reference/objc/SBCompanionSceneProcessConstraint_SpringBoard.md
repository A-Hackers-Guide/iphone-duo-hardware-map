# `SBCompanionSceneProcessConstraint`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCompanionSceneConstraint`
- 2 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"RBSProcessIdentity" _processIdentity;
@"NSString" _presentationMode;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCompanionSceneProcessConstraint constraintForProcessIdentity:forPresentationMode:];
```

## Instance methods

```
-[SBCompanionSceneProcessConstraint hash];
-[SBCompanionSceneProcessConstraint description];
-[SBCompanionSceneProcessConstraint copyWithZone:];
-[SBCompanionSceneProcessConstraint isEqual:];
-[SBCompanionSceneProcessConstraint _isProcessIdentity:equalToIdentity:];
-[SBCompanionSceneProcessConstraint isConstrainedByContext:];
-[SBCompanionSceneProcessConstraint shouldEvaluateConstraintForSceneUpdate:];
```
