# `SBSceneDestructionConfirmationViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 3 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _presented;
@"UISceneClosureConfirmation" _configuration;
@"<SBSceneDestructionConfirmationViewControllerDelegate>" _confirmationDelegate;
```

## Properties

```
@property (T@"UISceneClosureConfirmation",&,N,V_configuration) configuration;
@property (T@"<SBSceneDestructionConfirmationViewControllerDelegate>",W,N,V_confirmationDelegate) confirmationDelegate;
@property (TB,N,GhasPresented,V_presented) presented;
```

## Instance methods

```
-[SBSceneDestructionConfirmationViewController setConfiguration:];
-[SBSceneDestructionConfirmationViewController viewDidAppear:];
-[SBSceneDestructionConfirmationViewController configuration];
-[SBSceneDestructionConfirmationViewController initWithConfiguration:delegate:];
-[SBSceneDestructionConfirmationViewController setPresented:];
-[SBSceneDestructionConfirmationViewController _finishWithResult:chosenAction:];
-[SBSceneDestructionConfirmationViewController _dismissAlertAndFadeDimming];
-[SBSceneDestructionConfirmationViewController _handleDimmingTap:];
-[SBSceneDestructionConfirmationViewController _presentConfirmationAlert];
-[SBSceneDestructionConfirmationViewController confirmationDelegate];
-[SBSceneDestructionConfirmationViewController hasPresented];
-[SBSceneDestructionConfirmationViewController setConfirmationDelegate:];
```
