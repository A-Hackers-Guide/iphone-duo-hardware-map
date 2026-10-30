# `SBMainScreenActiveInterfaceOrientationWindow`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindow`
- Protocols: `BSDescriptionProviding`, `SBUIActiveOrientationObserver`
- 4 instance variables, 7 properties, 25 instance methods, 4 class methods

## Instance variables

```
@"NSCountedSet" _orientationUpdateDisableReasons;
B _passesTouchesThrough;
@"NSString" _debugName;
@"UIViewController" _contentViewController;
```

## Properties

```
@property (T@"NSString",R,C,N,V_debugName) debugName;
@property (T@"UIViewController",&,N,SsetContentViewController:,V_contentViewController) contentViewController;
@property (TB,N,V_passesTouchesThrough) passesTouchesThrough;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBMainScreenActiveInterfaceOrientationWindow sb_autorotates];
+[SBMainScreenActiveInterfaceOrientationWindow _traitsArbiterOrientationActuationEnabled];
+[SBMainScreenActiveInterfaceOrientationWindow _traitsArbiterOrientationActuationRole];
+[SBMainScreenActiveInterfaceOrientationWindow layoutContentViewControllerWithConstraints];
```

## Instance methods

```
-[SBMainScreenActiveInterfaceOrientationWindow activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBMainScreenActiveInterfaceOrientationWindow rootViewController];
-[SBMainScreenActiveInterfaceOrientationWindow setRootViewController:];
-[SBMainScreenActiveInterfaceOrientationWindow setContentViewController:];
-[SBMainScreenActiveInterfaceOrientationWindow setHidden:];
-[SBMainScreenActiveInterfaceOrientationWindow succinctDescriptionBuilder];
-[SBMainScreenActiveInterfaceOrientationWindow contentViewController];
-[SBMainScreenActiveInterfaceOrientationWindow _canBecomeKeyWindow];
-[SBMainScreenActiveInterfaceOrientationWindow hitTest:withEvent:];
-[SBMainScreenActiveInterfaceOrientationWindow activeInterfaceOrientationWillChangeToOrientation:];
-[SBMainScreenActiveInterfaceOrientationWindow descriptionWithMultilinePrefix:];
-[SBMainScreenActiveInterfaceOrientationWindow setPassesTouchesThrough:];
-[SBMainScreenActiveInterfaceOrientationWindow succinctDescription];
-[SBMainScreenActiveInterfaceOrientationWindow passesTouchesThrough];
-[SBMainScreenActiveInterfaceOrientationWindow debugName];
-[SBMainScreenActiveInterfaceOrientationWindow description];
-[SBMainScreenActiveInterfaceOrientationWindow descriptionBuilderWithMultilinePrefix:];
-[SBMainScreenActiveInterfaceOrientationWindow initWithWindowScene:role:debugName:];
-[SBMainScreenActiveInterfaceOrientationWindow _updateInterfaceOrientationToCurrentActiveInterfaceOrientationWithDuration:];
-[SBMainScreenActiveInterfaceOrientationWindow _updateSupportedInterfaceOrientationsForTraitArbiterActuationIfNeeded];
-[SBMainScreenActiveInterfaceOrientationWindow disableInterfaceOrientationChangesForReason:];
-[SBMainScreenActiveInterfaceOrientationWindow effectiveRootViewControllerSupportedInterfaceOrientations];
-[SBMainScreenActiveInterfaceOrientationWindow enableInterfaceOrientationChangesForReason:];
-[SBMainScreenActiveInterfaceOrientationWindow initWithRole:debugName:];
-[SBMainScreenActiveInterfaceOrientationWindow isDisablingInterfaceOrientationChanges];
```
