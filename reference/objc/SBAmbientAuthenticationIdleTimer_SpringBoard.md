# `SBAmbientAuthenticationIdleTimer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFMobileKeyBagObserver`
- 9 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"SBFMobileKeyBag" _keybag;
q _authenticated;
d _lastAuthenticationTime;
@"BSContinuousMachTimer" _authenticationLimitTimer;
@"AWAttentionAwarenessClient" _attentionClient;
B _enabled;
B _attentionClientActive;
d _maximumAuthenticatedInterval;
d _idleTimerDuration;
```

## Properties

```
@property (TB,N,G_isAuthenticated,S_setAuthenticated:) authenticated;
@property (TB,N,G_isAttentionClientActive,S_setAttentionClientActive:,V_attentionClientActive) attentionClientActive;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Td,N,V_maximumAuthenticatedInterval) maximumAuthenticatedInterval;
@property (Td,N,V_idleTimerDuration) idleTimerDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAmbientAuthenticationIdleTimer init];
-[SBAmbientAuthenticationIdleTimer _setAuthenticated:];
-[SBAmbientAuthenticationIdleTimer dealloc];
-[SBAmbientAuthenticationIdleTimer idleTimerDuration];
-[SBAmbientAuthenticationIdleTimer isEnabled];
-[SBAmbientAuthenticationIdleTimer keybag:extendedStateDidChange:];
-[SBAmbientAuthenticationIdleTimer setEnabled:];
-[SBAmbientAuthenticationIdleTimer _isAuthenticated];
-[SBAmbientAuthenticationIdleTimer setIdleTimerDuration:];
-[SBAmbientAuthenticationIdleTimer _handleAttentionLost:];
-[SBAmbientAuthenticationIdleTimer _initWithKeyBag:attentionAwarenessClient:];
-[SBAmbientAuthenticationIdleTimer _isAttentionClientActive];
-[SBAmbientAuthenticationIdleTimer _recomputeAuthenticationLimitTimer];
-[SBAmbientAuthenticationIdleTimer _reconfigureAttentionClient];
-[SBAmbientAuthenticationIdleTimer _setAttentionClientActive:];
-[SBAmbientAuthenticationIdleTimer _updateAttentionClientActive];
-[SBAmbientAuthenticationIdleTimer maximumAuthenticatedInterval];
-[SBAmbientAuthenticationIdleTimer setMaximumAuthenticatedInterval:];
```
