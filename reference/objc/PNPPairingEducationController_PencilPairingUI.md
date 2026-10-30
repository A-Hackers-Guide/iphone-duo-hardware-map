# `PNPPairingEducationController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PNPWelcomeController`
- Protocols: `UIPencilInteractionDelegate`, `PNPWizardMovieViewDelegate`
- 12 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 movieView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 hasContinueButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 hasStartTourButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 hasAltFlowButtons;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 didKickOffWelcomeVideo;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isDoubleTapVideoPlaying;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 startTourButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pencilInteraction;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 footerLabel;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pairingEducationDelegate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 mode;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 maxHeightConstraint;
```

## Class methods

```
+[PNPPairingEducationController _controllerWithType:buttonType:deviceType:delegate:];
```

## Instance methods

```
-[PNPPairingEducationController viewDidLoad];
-[PNPPairingEducationController viewWillAppear:];
-[PNPPairingEducationController viewDidAppear:];
-[PNPPairingEducationController initWithTitle:detailText:icon:contentLayout:];
-[PNPPairingEducationController pencilInteractionDidTap:];
-[PNPPairingEducationController closeTapped];
-[PNPPairingEducationController wizardMovieView:willAdvanceTo:];
-[PNPPairingEducationController wizardMovieViewDidFinishQueue:];
```
