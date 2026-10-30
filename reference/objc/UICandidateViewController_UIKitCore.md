# `UICandidateViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `TUIPredictionViewDelegate`, `UIPredictiveViewController`
- 5 instance variables, 9 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _hasRequestedExtraLayoutPass;
@"UIView" _candidateView;
@"TUIHostingInputCandidateController" _hostingInputCandidateController;
@"TUISecureInputCandidateContainerView" _secureInputCandidateHostedView;
@"UIView" _hostedSceneView;
```

## Properties

```
@property (T@"UIView",&,N,V_candidateView) candidateView;
@property (T@"TUIHostingInputCandidateController",&,N,V_hostingInputCandidateController) hostingInputCandidateController;
@property (T@"TUISecureInputCandidateContainerView",&,N,V_secureInputCandidateHostedView) secureInputCandidateHostedView;
@property (T@"UIView",&,N,V_hostedSceneView) hostedSceneView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",?,R,N) displayedCandidates;
```

## Class methods

```
+[UICandidateViewController preferredCandidateBarHeightForTraitCollection:];
```

## Instance methods

```
-[UICandidateViewController extendsFromKeyplane];
-[UICandidateViewController hidesExpandableButton];
-[UICandidateViewController displayedCandidates];
-[UICandidateViewController viewDidLayoutSubviews];
-[UICandidateViewController viewWillAppear:];
-[UICandidateViewController _canShowWhileLocked];
-[UICandidateViewController requiresKeyboard];
-[UICandidateViewController loadView];
-[UICandidateViewController preferredHeightForTraitCollection:];
-[UICandidateViewController hostedPredictionViewDidSelectCandidate:authenticationMessage:];
-[UICandidateViewController overrideUserInterfaceStyle];
-[UICandidateViewController hostingInputCandidateController];
-[UICandidateViewController isVisibleForInputDelegate:inputViews:];
-[UICandidateViewController hostedSceneView];
-[UICandidateViewController _legacyViewWillAppear:];
-[UICandidateViewController _secureHostedViewWillAppear:];
-[UICandidateViewController candidateView];
-[UICandidateViewController secureInputCandidateHostedView];
-[UICandidateViewController setCandidateView:];
-[UICandidateViewController setHostedSceneView:];
-[UICandidateViewController setHostingInputCandidateController:];
-[UICandidateViewController setSecureInputCandidateHostedView:];
```
