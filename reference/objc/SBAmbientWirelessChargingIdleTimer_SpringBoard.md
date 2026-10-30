# `SBAmbientWirelessChargingIdleTimer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAmbientPresentationObserver`, `SBBacklightControllerObserver`
- 8 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBChargingController" _chargingController;
@"SBScreenSleepCoordinator" _screenSleepCoordinator;
@"SBBacklightController" _backlightController;
@"AWAttentionAwarenessClient" _attentionClient;
@"SBAmbientDefaults" _ambientTestingDefaults;
B _enabled;
B _ambientPresented;
B _attentionClientActive;
```

## Properties

```
@property (TB,N,G_ambientPresented,S_setAmbientPresented:,V_ambientPresented) ambientPresented;
@property (TB,N,G_isAttentionClientActive,S_setAttentionClientActive:,V_attentionClientActive) attentionClientActive;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAmbientWirelessChargingIdleTimer backlightController:didTransitionToBacklightState:source:];
-[SBAmbientWirelessChargingIdleTimer ambientPresentationController:didUpdatePresented:];
-[SBAmbientWirelessChargingIdleTimer isEnabled];
-[SBAmbientWirelessChargingIdleTimer succinctDescription];
-[SBAmbientWirelessChargingIdleTimer setEnabled:];
-[SBAmbientWirelessChargingIdleTimer _ambientPresented];
-[SBAmbientWirelessChargingIdleTimer _handleAttentionLost:];
-[SBAmbientWirelessChargingIdleTimer _isAttentionClientActive];
-[SBAmbientWirelessChargingIdleTimer _noteQiPowerStatusChanged];
-[SBAmbientWirelessChargingIdleTimer _noteSpringBoardBootComplete];
-[SBAmbientWirelessChargingIdleTimer _reconfigureAttentionClient];
-[SBAmbientWirelessChargingIdleTimer _setAmbientPresented:];
-[SBAmbientWirelessChargingIdleTimer _setAttentionClientActive:];
-[SBAmbientWirelessChargingIdleTimer _updateIdleTimerEnablement];
-[SBAmbientWirelessChargingIdleTimer initWithAmbientPresentationController:screenSleepCoordinator:chargingController:backlightController:];
```
