# `SBAffordancePresenceController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyPathObserver`, `SBAttentionAwarenessClientDelegate`, `SBTransientUITapToUnhideParticipant`
- 15 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBAttentionAwarenessClient" _idleTouchAwarenessClient;
q _touchState;
q _presence;
Q _lastActivatingToken;
Q _lastInitialHideToken;
B _edgeProtectEnabled;
B _shouldEnableGestures;
@"NSMutableSet" _hiddenOverrides;
Q _lastVisibilityTransitionToken;
@"NSMutableSet" _outstandingVisibilityTransitionTokens;
@"SBAppSwitcherSettings" _appSwitcherSettings;
@"SBFHomeGrabberSettings" _homeGrabberSettings;
@"SBWindowScene" _windowScene;
B _autoHideAffordance;
@"<SBAffordancePresenceControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBAffordancePresenceControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_autoHideAffordance) autoHideAffordance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAffordancePresenceController clientDidResetForUserAttention:withEvent:];
-[SBAffordancePresenceController _calculatePresence];
-[SBAffordancePresenceController client:attentionLostTimeoutDidExpire:forConfigurationGeneration:withAssociatedObject:];
-[SBAffordancePresenceController _updateIdleTouchAwarenessClient];
-[SBAffordancePresenceController dealloc];
-[SBAffordancePresenceController setDelegate:];
-[SBAffordancePresenceController delegate];
-[SBAffordancePresenceController settings:changedValueForKeyPath:];
-[SBAffordancePresenceController initWithDelegate:windowScene:];
-[SBAffordancePresenceController _updatePresence];
-[SBAffordancePresenceController currentPresence];
-[SBAffordancePresenceController _animationSettingsForTransitionFromPresence:toPresence:];
-[SBAffordancePresenceController _unhideIfAutoHidden];
-[SBAffordancePresenceController _updatePresence:withAnimationSettings:];
-[SBAffordancePresenceController autoHideAffordance];
-[SBAffordancePresenceController setAutoHideAffordance:];
-[SBAffordancePresenceController setHidden:forReason:animated:];
-[SBAffordancePresenceController transientUI:wasIndirectPannedToDismissFromGestureRecognizer:];
-[SBAffordancePresenceController transientUI:wasTappedToUnhideFromGestureRecognizer:];
-[SBAffordancePresenceController transientUIHandledTouch:withSystemGestureRecognizer:];
```
