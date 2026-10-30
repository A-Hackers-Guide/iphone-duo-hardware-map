# `SBHomeAffordanceInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyObserver`, `SBFHomeAffordanceInteraction`
- 8 instance variables, 11 properties, 26 instance methods, 0 class methods

## Instance variables

```
{?="homeAffordanceFrameForHomeAffordanceInteraction"b1"standardHomeAffordanceHitTestRectOutsetsForHomeAffordanceInteraction"b1"expandedHomeAffordanceHitTestRectOutsetsForHomeAffordanceInteraction"b1"homeAffordanceInteractionHomeAffordanceHitTestRectDidChange"b1"homeAffordanceInteractionAllowsUserInteraction"b1"homeAffordanceInteractionDidRecognizeSingleTap"b1"homeAffordanceInteractionDidRecognizeDoubleTap"b1"homeAffordanceInteractionDidFailToRecognizeDoubleTap"b1"homeAffordanceInteractionDidRecognizeSingleClick"b1"homeAffordanceInteractionDidRecognizeTouchThatShouldUnhideViewImmediately"b1} _delegateRespondsTo;
B _enabled;
@"<SBFHomeAffordanceInteractionDelegate>" _delegate;
@"UIView" _view;
@"SBHomeAffordanceInteractionManager" _homeAffordanceInteractionManager;
@"SBFHomeGrabberSettings" _homeGrabberSettings;
@"MTLumaDodgePillSettings" _lumaDodgePillSettings;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _homeAffordanceHitTestRect;
```

## Properties

```
@property (T@"SBHomeAffordanceInteractionManager",R,W,N,V_homeAffordanceInteractionManager) homeAffordanceInteractionManager;
@property (T@"SBFHomeGrabberSettings",R,N,V_homeGrabberSettings) homeGrabberSettings;
@property (T@"MTLumaDodgePillSettings",R,N,V_lumaDodgePillSettings) lumaDodgePillSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBFHomeAffordanceInteractionDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_homeAffordanceHitTestRect) homeAffordanceHitTestRect;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[SBHomeAffordanceInteraction notifyDidRecognizeDoubleTap];
-[SBHomeAffordanceInteraction homeGrabberSettings];
-[SBHomeAffordanceInteraction standardHomeAffordanceHitTestRectOutsets];
-[SBHomeAffordanceInteraction expandedHomeAffordanceHitTestRectOutsets];
-[SBHomeAffordanceInteraction notifyDidRecognizeSingleTap];
-[SBHomeAffordanceInteraction dealloc];
-[SBHomeAffordanceInteraction notifyDidRecognizeTouchThatShouldUnhideViewImmediately:];
-[SBHomeAffordanceInteraction lumaDodgePillSettings];
-[SBHomeAffordanceInteraction settings:changedValueForKey:];
-[SBHomeAffordanceInteraction initWithHomeAffordanceInteractionManager:];
-[SBHomeAffordanceInteraction notifyDidFailToRecognizeDoubleTap];
-[SBHomeAffordanceInteraction isEnabled];
-[SBHomeAffordanceInteraction homeAffordanceInteractionManager];
-[SBHomeAffordanceInteraction setHomeAffordanceHitTestRect:];
-[SBHomeAffordanceInteraction view];
-[SBHomeAffordanceInteraction setDelegate:];
-[SBHomeAffordanceInteraction notifyDidRecognizeSingleClick];
-[SBHomeAffordanceInteraction setEnabled:];
-[SBHomeAffordanceInteraction willMoveToView:];
-[SBHomeAffordanceInteraction delegate];
-[SBHomeAffordanceInteraction homeAffordanceHitTestRect];
-[SBHomeAffordanceInteraction setNeedsUpdate];
-[SBHomeAffordanceInteraction _assistantController];
-[SBHomeAffordanceInteraction homeAffordanceFrame];
-[SBHomeAffordanceInteraction didMoveToView:];
-[SBHomeAffordanceInteraction allowsUserInteraction];
```
