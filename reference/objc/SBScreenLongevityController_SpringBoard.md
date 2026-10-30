# `SBScreenLongevityController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyObserver`, `SBSensorActivityObserver`, `SBAttentionAwarenessClientDelegate`, `SBScreenLongevityTimerDelegate`, `MCProfileConnectionObserver`, `SBAttentionAwarenessStreamerClientDelegate`
- 11 instance variables, 4 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"SBScreenLongevitySettings" _settings;
@"<BSDefaultObserver>" _defaultsObserver;
i _attentionAwarenessFeatureMonitoringToken;
B _enabled;
@"AWAttentionAwarenessConfiguration" _faceStreamAwarenessConfiguration;
@"SBAttentionAwarenessStreamerClient" _faceStreamAwarenessClient;
@"AWAttentionAwarenessConfiguration" _idleTouchAwarenessConfiguration;
@"SBAttentionAwarenessClient" _idleTouchAwarenessClient;
@"SBScreenLongevityTimer" _dimTimer;
@"NSTimer" _undimTimer;
@"BrightnessSystemClient" _brightnessSystemClient;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBScreenLongevityController activityDidChangeForSensorActivityDataProvider:];
-[SBScreenLongevityController clientDidResetForUserAttention:withEvent:];
-[SBScreenLongevityController client:attentionLostTimeoutDidExpire:forConfigurationGeneration:withAssociatedObject:];
-[SBScreenLongevityController profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[SBScreenLongevityController init];
-[SBScreenLongevityController dealloc];
-[SBScreenLongevityController settings:changedValueForKey:];
-[SBScreenLongevityController setEnabled:];
-[SBScreenLongevityController _shouldEnable];
-[SBScreenLongevityController _isDimmed];
-[SBScreenLongevityController _beginMonitoringAttentionAwarenessFeaturesEnablement];
-[SBScreenLongevityController _checkFaceAttentionAwareness];
-[SBScreenLongevityController _clientDidResetForUserAttention:];
-[SBScreenLongevityController _dim];
-[SBScreenLongevityController _endMonitoringAttentionAwarenessFeaturesEnablement];
-[SBScreenLongevityController _hasCameraAttributions];
-[SBScreenLongevityController _isAutoLockSetToNever];
-[SBScreenLongevityController _isValidCurrentTimer:];
-[SBScreenLongevityController _mediaNowPlayingChanged];
-[SBScreenLongevityController _observeDefaults];
-[SBScreenLongevityController _screenBacklightStateChanged];
-[SBScreenLongevityController _startDimTimer];
-[SBScreenLongevityController _toggleBacklightAdaptiveDimming:];
-[SBScreenLongevityController _undim];
-[SBScreenLongevityController _updateCachedDefaults];
-[SBScreenLongevityController dimTimerDidExpireForTimer:];
-[SBScreenLongevityController evaluateEnablement];
-[SBScreenLongevityController faceDetectionTimerDidExpire:];
-[SBScreenLongevityController faceStreamAwarenessConfiguration];
-[SBScreenLongevityController isAdaptiveDimmingEnabled];
-[SBScreenLongevityController isUnderAutoDimThreshold];
-[SBScreenLongevityController resetTimerForReason:];
-[SBScreenLongevityController setAdaptiveDimmingEnabled:];
-[SBScreenLongevityController streamerClientDidResetForUserAttention:];
```
