# `SBPIPContainerViewControllerAdapterContextProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 23 instance methods, 1 class methods

## Properties

```
@property (TQ,R,N) currentCanonicalPosition;
@property (Tq,R,N) windowInterfaceOrientation;
@property (T@"NSNumber",R,N) overrideResourcesUsageReductionTimeout;
@property (TB,R,N) shouldSuppressAssociatedElementsInSystemAperture;
@property (T{UIEdgeInsets=dddd},R,N) effectiveEdgeInsets;
@property (T{UIEdgeInsets=dddd},R,N) stashedPadding;
```

## Class methods

```
+[SBPIPContainerViewControllerAdapterContextProviding resolvedHomeScreenSafeAreaInsetsForWindowScene:interfaceOrientation:rawSafeAreaInsets:];
```

## Instance methods

```
-[SBPIPContainerViewControllerAdapterContextProviding windowInterfaceOrientation];
-[SBPIPContainerViewControllerAdapterContextProviding stopAnimationWillBeginWithFinalInterfaceOrientation:finalFrame:];
-[SBPIPContainerViewControllerAdapterContextProviding currentCanonicalPosition];
-[SBPIPContainerViewControllerAdapterContextProviding effectiveEdgeInsets];
-[SBPIPContainerViewControllerAdapterContextProviding effectiveEdgeInsetsForWindowScene:];
-[SBPIPContainerViewControllerAdapterContextProviding effectiveEdgeInsetsForWindowScene:interfaceOrientation:];
-[SBPIPContainerViewControllerAdapterContextProviding homeScreenEffectiveEdgeInsetsForWindowScene:interfaceOrientation:];
-[SBPIPContainerViewControllerAdapterContextProviding overrideResourcesUsageReductionTimeout];
-[SBPIPContainerViewControllerAdapterContextProviding rotationAnimationDidBeginToRotation:contentViewFrame:];
-[SBPIPContainerViewControllerAdapterContextProviding rotationAnimationDidCompleteToRotation:contentViewFrame:];
-[SBPIPContainerViewControllerAdapterContextProviding rotationAnimationWillBeginToRotation:contentViewFrame:];
-[SBPIPContainerViewControllerAdapterContextProviding rotationAnimationWillCompleteToRotation:contentViewFrame:];
-[SBPIPContainerViewControllerAdapterContextProviding shouldSuppressAssociatedElementsInSystemAperture];
-[SBPIPContainerViewControllerAdapterContextProviding startAnimationDidBeginWithInitialInterfaceOrientation:];
-[SBPIPContainerViewControllerAdapterContextProviding startAnimationDidCompleteWithInitialInterfaceOrientation:];
-[SBPIPContainerViewControllerAdapterContextProviding startAnimationWillBeginWithInitialInterfaceOrientation:initialFrame:];
-[SBPIPContainerViewControllerAdapterContextProviding stashedOcclusionRectForWindowScene:];
-[SBPIPContainerViewControllerAdapterContextProviding stashedPadding];
-[SBPIPContainerViewControllerAdapterContextProviding stopAnimationDidBeginWithFinalInterfaceOrientation:finalFrame:];
-[SBPIPContainerViewControllerAdapterContextProviding stopAnimationDidCompleteWithFinalInterfaceOrientation:];
-[SBPIPContainerViewControllerAdapterContextProviding toggleUserPreferredScale];
-[SBPIPContainerViewControllerAdapterContextProviding updateEdgeInsetsForLayoutStateTransition];
-[SBPIPContainerViewControllerAdapterContextProviding updatePreferredContentSize:];
```
