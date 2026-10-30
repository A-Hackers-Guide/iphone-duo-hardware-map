# `UIPanelControllerDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 23 instance methods, 0 class methods

## Properties

```
@property (T@"UIColor",?,R) primaryBackgroundColor;
```

## Instance methods

```
-[UIPanelControllerDelegate primaryBackgroundColor];
-[UIPanelControllerDelegate panelController:adjustLeadingViewController:forKeyboardInfo:];
-[UIPanelControllerDelegate panelController:adjustTrailingViewController:forKeyboardInfo:];
-[UIPanelControllerDelegate panelController:animateTransitionToStateRequest:predictedEndState:predictedDuration:];
-[UIPanelControllerDelegate panelController:collapseOntoPrimaryViewController:];
-[UIPanelControllerDelegate panelController:collapsePrimaryViewController:withFallbackSecondaryViewController:onTopOfSupplementaryViewController:transitionCoordinator:];
-[UIPanelControllerDelegate panelController:collapsePrimaryViewController:withFallbackSecondaryViewController:transitionCoordinator:];
-[UIPanelControllerDelegate panelController:didChangeToState:withSize:];
-[UIPanelControllerDelegate panelController:didEndAnimatedTransitionToStateRequest:];
-[UIPanelControllerDelegate panelController:expectedWidthForColumnForViewController:];
-[UIPanelControllerDelegate panelController:navigationBarForViewController:];
-[UIPanelControllerDelegate panelController:separateSecondaryViewControllerFromPrimaryViewController:];
-[UIPanelControllerDelegate panelController:separateSupplementaryViewControllerFromPrimaryViewController:];
-[UIPanelControllerDelegate panelController:willBeginAnimatedTransitionToStateRequest:predictedEndState:predictedDuration:];
-[UIPanelControllerDelegate panelController:willBeginAnimationToPrimarySize:supplementarySize:secondarySize:];
-[UIPanelControllerDelegate panelController:willChangeToState:];
-[UIPanelControllerDelegate panelControllerDidCollapse:];
-[UIPanelControllerDelegate panelControllerDidExpand:];
-[UIPanelControllerDelegate panelControllerWillUpdate:];
-[UIPanelControllerDelegate primaryViewControllerForCollapsingPanelController:];
-[UIPanelControllerDelegate primaryViewControllerForExpandingPanelController:];
-[UIPanelControllerDelegate topColumnForCollapsingPanelController:];
-[UIPanelControllerDelegate viewClassForPanelController:];
```
