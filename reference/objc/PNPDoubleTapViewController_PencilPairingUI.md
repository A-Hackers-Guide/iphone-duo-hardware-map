# `PNPDoubleTapViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PNPWelcomeController`
- Protocols: `PNPWizardScratchpadViewDelegate`, `PNPPencilInteractionEventDestination`, `UIPencilInteractionDelegate`
- 5 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 scratchPadView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pencilInteraction;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 quickSwapEventSource;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pencilView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 animationsCancelled;
```

## Class methods

```
+[PNPDoubleTapViewController _controllerWithType:buttonType:deviceType:delegate:];
```

## Instance methods

```
-[PNPDoubleTapViewController viewWillDisappear:];
-[PNPDoubleTapViewController viewDidLoad];
-[PNPDoubleTapViewController viewWillAppear:];
-[PNPDoubleTapViewController initWithTitle:detailText:icon:contentLayout:];
-[PNPDoubleTapViewController pencilInteractionDidTap:];
-[PNPDoubleTapViewController eventSource:hadPencilDoubleTapped:];
-[PNPDoubleTapViewController scratchPadViewHadInteractionEvent:];
-[PNPDoubleTapViewController scratchPadViewIsPlayingAnimation:];
```
