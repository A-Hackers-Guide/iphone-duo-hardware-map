# `SBPosterBoardModalEditingManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PRUISExternallyHostedPosterEditingServerDelegate`, `SBPosterEditingTransientOverlayViewControllerDelegate`
- 2 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"PRUISExternallyHostedPosterEditingServer" _posterEditingServer;
@"NSMutableArray" _presentedTransientOverlayControllers;
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
-[SBPosterBoardModalEditingManager init];
-[SBPosterBoardModalEditingManager beginExternalPosterEditingSessionWithEditingRequest:completion:];
-[SBPosterBoardModalEditingManager sendRequestDismissalActionWithEditingRequest:];
-[SBPosterBoardModalEditingManager _dismissTransientOverlayViewControllerIfPresenting:animated:completion:];
-[SBPosterBoardModalEditingManager _presentTransientOverlayViewController:animated:completion:];
-[SBPosterBoardModalEditingManager posterEditingTransientOverlayViewController:didDismissWithResponse:];
-[SBPosterBoardModalEditingManager posterEditingTransientOverlayViewController:willDismissWithResponse:];
```
