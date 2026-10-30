# `SBSAElementLayoutTransition`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 11 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _initialElementContexts;
@"NSArray" _targetElementContexts;
{?="interfaceOrientation"q"layoutDirection"q"statusBarAxis"q"sensorVariant"Q} _initialOrientationEnvironment;
{?="interfaceOrientation"q"layoutDirection"q"statusBarAxis"q"sensorVariant"Q} _targetOrientationEnvironment;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_initialElementContexts) initialElementContexts;
@property (T@"NSArray",R,C,N,V_targetElementContexts) targetElementContexts;
@property (T{?=qqqQ},R,N,V_initialOrientationEnvironment) initialOrientationEnvironment;
@property (T{?=qqqQ},R,N,V_targetOrientationEnvironment) targetOrientationEnvironment;
@property (TB,R,N,GisLayoutChange) layoutChange;
@property (TB,R,N,GisOrientationChange) orientationChange;
@property (TB,R,N,GisRotationOnly) rotationOnly;
@property (TB,R,N,GisCollisionRequired) collisionRequired;
@property (TB,R,N,GisSingleElementExpansion) singleElementExpansion;
@property (TB,R,N,GisTransitionFromCustom) transitionFromCustom;
@property (TB,R,N,GisTransitionToSingleCompact) transitionToSingleCompact;
```

## Class methods

```
+[SBSAElementLayoutTransition initialize];
```

## Instance methods

```
-[SBSAElementLayoutTransition hash];
-[SBSAElementLayoutTransition description];
-[SBSAElementLayoutTransition copyWithZone:];
-[SBSAElementLayoutTransition isEqual:];
-[SBSAElementLayoutTransition membersForCoder];
-[SBSAElementLayoutTransition elementWithIdentityWasOrIsSensorAttached:];
-[SBSAElementLayoutTransition initWithInitialElementContexts:initialOrientationEnvironment:targetElementContexts:targetOrientationEnvironment:];
-[SBSAElementLayoutTransition initWithInitialElementContexts:targetElementContexts:orientationEnvironment:];
-[SBSAElementLayoutTransition initialElementContexts];
-[SBSAElementLayoutTransition initialOrientationEnvironment];
-[SBSAElementLayoutTransition isCollisionRequired];
-[SBSAElementLayoutTransition isLayoutChange];
-[SBSAElementLayoutTransition isOrientationChange];
-[SBSAElementLayoutTransition isRotationOnly];
-[SBSAElementLayoutTransition isSingleElementExpansion];
-[SBSAElementLayoutTransition isTransitionFromCustom];
-[SBSAElementLayoutTransition isTransitionToSingleCompact];
-[SBSAElementLayoutTransition targetElementContexts];
-[SBSAElementLayoutTransition targetOrientationEnvironment];
```
