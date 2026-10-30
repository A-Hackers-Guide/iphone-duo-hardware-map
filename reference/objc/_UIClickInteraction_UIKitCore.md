# `_UIClickInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIClickInteractionDriverDelegate`, `UIInteraction_Private`, `UIInteraction_Internal`, `UIInteraction`
- 8 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _hapticsEnabled;
@"UIView" _view;
@"<UIInteractionEffect>" _interactionEffect;
@"<_UIClickInteractionDelegate>" _delegate;
d _allowableMovement;
@"<_UIClickInteractionDriving>" _driver;
@"_UIClickFeedbackGenerator" _feedbackGenerator;
# _overrideDriverClass;
```

## Properties

```
@property (T@"<_UIClickInteractionDriving>",&,N,V_driver) driver;
@property (T@"_UIClickFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (T#,N,S_setOverrideDriverClass:,V_overrideDriverClass) overrideDriverClass;
@property (TB,N,V_hapticsEnabled) hapticsEnabled;
@property (TB,N) driverCancelsTouchesInView;
@property (T@"<_UIClickInteractionDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_allowableMovement) allowableMovement;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIInteractionEffect>",?,&,N,V_interactionEffect) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UIClickInteraction allowableMovement];
-[_UIClickInteraction clickDriver:didUpdateHighlightProgress:];
-[_UIClickInteraction setHapticsEnabled:];
-[_UIClickInteraction clickDriver:didPerformEvent:];
-[_UIClickInteraction _createFeedbackGenerator];
-[_UIClickInteraction setFeedbackGenerator:];
-[_UIClickInteraction feedbackGenerator];
-[_UIClickInteraction _beginInteraction];
-[_UIClickInteraction hapticsEnabled];
-[_UIClickInteraction clickDriver:shouldBegin:];
-[_UIClickInteraction locationInCoordinateSpace:];
-[_UIClickInteraction interactionEffect];
-[_UIClickInteraction cancelInteraction];
-[_UIClickInteraction setAllowableMovement:];
-[_UIClickInteraction driver];
-[_UIClickInteraction init];
-[_UIClickInteraction setInteractionEffect:];
-[_UIClickInteraction _setOverrideDriverClass:];
-[_UIClickInteraction _driverClass];
-[_UIClickInteraction setDriver:];
-[_UIClickInteraction view];
-[_UIClickInteraction setDelegate:];
-[_UIClickInteraction driverCancelsTouchesInView];
-[_UIClickInteraction _updateDriver];
-[_UIClickInteraction willMoveToView:];
-[_UIClickInteraction delegate];
-[_UIClickInteraction setDriverCancelsTouchesInView:];
-[_UIClickInteraction _endInteraction];
-[_UIClickInteraction _viewTraitCollectionDidChange:];
-[_UIClickInteraction didMoveToView:];
-[_UIClickInteraction overrideDriverClass];
```
