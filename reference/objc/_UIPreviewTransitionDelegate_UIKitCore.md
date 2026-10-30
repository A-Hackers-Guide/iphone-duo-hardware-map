# `_UIPreviewTransitionDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIForceTransitioningDelegate`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIInteractionProgress" interactionProgressForPresentation;
@"_UIStatesFeedbackGenerator" _feedbackGenerator;
```

## Properties

```
@property (T@"_UIStatesFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (T@"UIInteractionProgress",&,N,VinteractionProgressForPresentation) interactionProgressForPresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewTransitionDelegate setFeedbackGenerator:];
-[_UIPreviewTransitionDelegate feedbackGenerator];
-[_UIPreviewTransitionDelegate animationControllerForDismissedController:];
-[_UIPreviewTransitionDelegate animationControllerForPresentedController:presentingController:sourceController:];
-[_UIPreviewTransitionDelegate presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIPreviewTransitionDelegate interactionProgressForPresentation];
-[_UIPreviewTransitionDelegate setInteractionProgressForPresentation:];
-[_UIPreviewTransitionDelegate interactionControllerForPresentation:];
```
