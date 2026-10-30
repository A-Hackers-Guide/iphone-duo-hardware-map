# `SBFBarSwipeBehavior`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<UIViewSpringAnimationBehaviorDescribing>" _settleAffordanceAnimationBehaviorDescription;
@"UINotificationFeedbackGenerator" _dismissalFeedbackGenerator;
B _didFireAction;
@"UIView" _grabberView;
d _grabberViewAdditionalEdgeSpacing;
@"<SBFBarSwipeBehaviorDelegate>" _delegate;
q _feedbackType;
```

## Properties

```
@property (T@"UIView",R,N,V_grabberView) grabberView;
@property (Td,R,N,V_grabberViewAdditionalEdgeSpacing) grabberViewAdditionalEdgeSpacing;
@property (T@"<UIViewSpringAnimationBehaviorDescribing>",R,N,V_settleAffordanceAnimationBehaviorDescription) settleAffordanceAnimationBehaviorDescription;
@property (T@"<SBFBarSwipeBehaviorDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_feedbackType) feedbackType;
```

## Instance methods

```
-[SBFBarSwipeBehavior _createFeedbackGenerator];
-[SBFBarSwipeBehavior feedbackType];
-[SBFBarSwipeBehavior setFeedbackType:];
-[SBFBarSwipeBehavior grabberView];
-[SBFBarSwipeBehavior setDelegate:];
-[SBFBarSwipeBehavior delegate];
-[SBFBarSwipeBehavior _fireAction];
-[SBFBarSwipeBehavior _grabberViewContainerView];
-[SBFBarSwipeBehavior _offsetGrabberForProgress:];
-[SBFBarSwipeBehavior _progressWithTranslation:liftoffVelocity:];
-[SBFBarSwipeBehavior _setGrabberAdditionalEdgeSpacing:];
-[SBFBarSwipeBehavior _settleAffordanceAnimationBehaviorDescription];
-[SBFBarSwipeBehavior _settleGrabber];
-[SBFBarSwipeBehavior barSwipeInteractionBegan:];
-[SBFBarSwipeBehavior barSwipeInteractionCancelled:];
-[SBFBarSwipeBehavior barSwipeInteractionChanged:];
-[SBFBarSwipeBehavior barSwipeInteractionEnded:];
-[SBFBarSwipeBehavior grabberViewAdditionalEdgeSpacing];
-[SBFBarSwipeBehavior initWithGrabberView:settleAffordanceAnimationBehaviorDescription:];
-[SBFBarSwipeBehavior settleAffordanceAnimationBehaviorDescription];
```
