# `SBSAElementContentProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 4 instance variables, 2 properties, 10 instance methods, 3 class methods

## Instance variables

```
B _sensorObscuringShadowDisappearingIfTransitioning;
@"<SBSAInterfaceElementPropertyIdentifying>" _pendingSensorObscuringShadowProperty;
q _transitionDirection;
@"SBSAElementLayoutTransition" _staticLayoutTransition;
```

## Properties

```
@property (Tq,R,N,V_transitionDirection) transitionDirection;
@property (T@"SBSAElementLayoutTransition",R,C,N,V_staticLayoutTransition) staticLayoutTransition;
```

## Class methods

```
+[SBSAElementContentProvider initialize];
+[SBSAElementContentProvider appearanceTransitionElementContentProviderWithParentProvider:staticLayoutTransition:];
+[SBSAElementContentProvider disappearanceTransitionElementContentProviderWithParentProvider:staticLayoutTransition:];
```

## Instance methods

```
-[SBSAElementContentProvider defaultTransitionSettings];
-[SBSAElementContentProvider description];
-[SBSAElementContentProvider transitionDirection];
-[SBSAElementContentProvider membersForCoder];
-[SBSAElementContentProvider _initWithParentProvider:transitionDirection:staticLayoutTransition:];
-[SBSAElementContentProvider _sensorObscuringShadowApexMilestone];
-[SBSAElementContentProvider _updatedElementDescriptionFromDescription:layoutTransition:transitionDescriptions:context:];
-[SBSAElementContentProvider initWithParentProvider:];
-[SBSAElementContentProvider preferencesFromContext:];
-[SBSAElementContentProvider staticLayoutTransition];
```
