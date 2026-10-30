# `UIHandwritingAssistantView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBKeyView`
- Protocols: `TUIPredictionViewDelegate`
- 7 instance variables, 11 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _isDynamicLayout;
@"TUISystemInputAssistantView" _systemInputAssistantView;
@"UIKBHandwritingCandidateView" _candidateView;
@"UIKeyboardCandidatePocketShadow" _rightBorder;
@"TUISecureInputCandidateContainerView" _secureInputCandidateHostedView;
@"TUIHostingInputCandidateController" _hostingInputCandidateController;
@"UIView" _hostedSceneView;
```

## Properties

```
@property (T@"TUISystemInputAssistantView",&,N,V_systemInputAssistantView) systemInputAssistantView;
@property (T@"UIKBHandwritingCandidateView",&,N,V_candidateView) candidateView;
@property (T@"UIKeyboardCandidatePocketShadow",&,N,V_rightBorder) rightBorder;
@property (TB,V_isDynamicLayout) isDynamicLayout;
@property (T@"TUISecureInputCandidateContainerView",&,N,V_secureInputCandidateHostedView) secureInputCandidateHostedView;
@property (T@"TUIHostingInputCandidateController",&,N,V_hostingInputCandidateController) hostingInputCandidateController;
@property (T@"UIView",&,N,V_hostedSceneView) hostedSceneView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIHandwritingAssistantView candidateList];
-[UIHandwritingAssistantView isDynamicLayout];
-[UIHandwritingAssistantView didMoveToWindow];
-[UIHandwritingAssistantView dimKeys:];
-[UIHandwritingAssistantView initWithFrame:keyplane:key:];
-[UIHandwritingAssistantView displayLayer:];
-[UIHandwritingAssistantView setIsDynamicLayout:];
-[UIHandwritingAssistantView updateForKeyplane:key:];
-[UIHandwritingAssistantView hitTest:withEvent:];
-[UIHandwritingAssistantView systemInputAssistantView];
-[UIHandwritingAssistantView hostedPredictionViewDidSelectCandidate:authenticationMessage:];
-[UIHandwritingAssistantView pointInside:withEvent:];
-[UIHandwritingAssistantView hostingInputCandidateController];
-[UIHandwritingAssistantView hostedSceneView];
-[UIHandwritingAssistantView _setUpSecureHostedCandidateView];
-[UIHandwritingAssistantView setRightBorder:];
-[UIHandwritingAssistantView _attachHostedSceneIfNeeded];
-[UIHandwritingAssistantView _detachHostedScene];
-[UIHandwritingAssistantView _owningViewController];
-[UIHandwritingAssistantView _refreshSecureHostedContent];
-[UIHandwritingAssistantView _secureHostingSupported];
-[UIHandwritingAssistantView assistantFrameForKeyplane:key:];
-[UIHandwritingAssistantView candidateView];
-[UIHandwritingAssistantView rightBorder];
-[UIHandwritingAssistantView secureInputCandidateHostedView];
-[UIHandwritingAssistantView setCandidateView:];
-[UIHandwritingAssistantView setHostedSceneView:];
-[UIHandwritingAssistantView setHostingInputCandidateController:];
-[UIHandwritingAssistantView setSecureInputCandidateHostedView:];
-[UIHandwritingAssistantView setSystemInputAssistantView:];
```
