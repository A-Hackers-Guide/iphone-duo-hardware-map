# `SBContinuousFoldCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _activeControllerAssertions;
@"NSHashTable" _foldControllers;
@"BSCompoundAssertion" _suppressionAssertion;
```

## Instance methods

```
-[SBContinuousFoldCoordinator init];
-[SBContinuousFoldCoordinator registerController:];
-[SBContinuousFoldCoordinator unregisterController:];
-[SBContinuousFoldCoordinator _updateAssertionsIfNeeded];
-[SBContinuousFoldCoordinator newContinuousFoldControllerForWindowScene:];
-[SBContinuousFoldCoordinator requestSuppressionAssertionWithReason:];
```
