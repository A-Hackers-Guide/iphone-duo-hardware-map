# `_SBHUDModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBHUDHostViewControllerDelegate`, `SBHUDPresenting`, `SBHUDAttachmentDelegate`
- 10 instance variables, 15 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"NSTimer" _dismissalTimer;
B _dismissed;
B _dismissing;
B _presenting;
B _presented;
@"UIViewController<SBHUDViewControlling>" _HUDViewController;
@"SBHUDController" _HUDController;
d _dismissalInterval;
@"NSString" _identifier;
@"<BSInvalidatable>" _dropletLayoutAssertion;
```

## Properties

```
@property (TB,N,SsetPresented:,V_presented) isPresented;
@property (TB,N,SsetPresenting:,V_presenting) isPresenting;
@property (TB,N,SsetDismissing:,V_dismissing) isDismissing;
@property (TB,N,SsetDismissed:,V_dismissed) isDismissed;
@property (T@"SBHUDController",R,N,V_HUDController) HUDController;
@property (T@"UIViewController<SBHUDViewControlling>",R,N,V_HUDViewController) HUDViewController;
@property (Td,R,N,V_dismissalInterval) dismissalInterval;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"<BSInvalidatable>",R,N,V_dropletLayoutAssertion) dropletLayoutAssertion;
@property (TB,R,N,GisDismissalScheduled) dismissalScheduled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) isVisible;
```

## Class methods

```
+[_SBHUDModel HUDModelForController:viewController:identifier:];
```

## Instance methods

```
-[_SBHUDModel dismissAnimated:];
-[_SBHUDModel isPresented];
-[_SBHUDModel dismiss];
-[_SBHUDModel identifier];
-[_SBHUDModel dealloc];
-[_SBHUDModel isVisible];
-[_SBHUDModel dismissalInterval];
-[_SBHUDModel isDismissing];
-[_SBHUDModel description];
-[_SBHUDModel setDismissing:];
-[_SBHUDModel setDismissed:];
-[_SBHUDModel isEqual:];
-[_SBHUDModel isPresenting];
-[_SBHUDModel setPresenting:];
-[_SBHUDModel isDismissed];
-[_SBHUDModel setPresented:];
-[_SBHUDModel HUDController];
-[_SBHUDModel HUDViewController];
-[_SBHUDModel _handleDropletLayoutCallback:];
-[_SBHUDModel _setupDropletLayout];
-[_SBHUDModel _shouldIgnoreDropletAttachment];
-[_SBHUDModel _teardownDropletLayout];
-[_SBHUDModel dropletLayoutAssertion];
-[_SBHUDModel hudViewController:didDismissHUD:];
-[_SBHUDModel hudViewController:didPresentHUD:];
-[_SBHUDModel hudViewController:willDismissHUD:];
-[_SBHUDModel hudViewController:willPresentHUD:];
-[_SBHUDModel invalidateDismissalTimer];
-[_SBHUDModel isDismissalScheduled];
-[_SBHUDModel presentWithDismissalInterval:];
-[_SBHUDModel presentWithDismissalInterval:animated:];
-[_SBHUDModel rescheduleDismissalTimer];
-[_SBHUDModel scheduleDismissalTimer];
-[_SBHUDModel updateAttachmentStateForHUDViewController:];
```
