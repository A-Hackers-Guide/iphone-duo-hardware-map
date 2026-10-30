# `_SBHUDHostViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughViewController`
- Protocols: `SBViewControllerTransitionContextDelegate`
- 8 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _activeTransitionContexts;
@"NSMutableSet" _presentedHUDs;
@"NSMutableSet" _presentingHUDs;
@"NSMutableSet" _executingDismissalHUDs;
@"NSMutableSet" _presentingHUDsTransitionContexts;
@"NSMutableSet" _dismissingHUDsTransitionContexts;
@"SBHUDController" _HUDController;
@"<_SBHUDHostViewControllerDelegate>" _delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBHUDHostViewController transitionDidFinish:];
-[_SBHUDHostViewController supportedInterfaceOrientations];
-[_SBHUDHostViewController getRotationContentSettings:forWindow:];
-[_SBHUDHostViewController _canShowWhileLocked];
-[_SBHUDHostViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[_SBHUDHostViewController description];
-[_SBHUDHostViewController _buildTransitionContextToPresentHUD:dismissHUD:animated:delegate:containerView:completion:];
-[_SBHUDHostViewController _executeDismissHUD:animated:completion:];
-[_SBHUDHostViewController _executePresentNewHUD:animated:completion:];
-[_SBHUDHostViewController _executeViewControllerTransitionContext:];
-[_SBHUDHostViewController _transitionContextMatchingHUD:withinContainer:];
```
