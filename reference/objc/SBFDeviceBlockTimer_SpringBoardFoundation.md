# `SBFDeviceBlockTimer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _userRequestedEraseEnabled;
B _enabled;
@? _handler;
@"NSString" _titleText;
@"NSString" _subtitleText;
@"NSString" _timeoutText;
@"NSString" _primaryActionButtonText;
@"<SBFBlockStatusProvider>" _blockStatusProvider;
@"NSTimer" _timer;
```

## Properties

```
@property (T@"NSString",C,N,V_titleText) titleText;
@property (T@"NSString",C,N,V_subtitleText) subtitleText;
@property (T@"NSString",C,N,V_timeoutText) timeoutText;
@property (T@"NSString",C,N,V_primaryActionButtonText) primaryActionButtonText;
@property (TB,N,GisUserRequestedEraseEnabled,V_userRequestedEraseEnabled) userRequestedEraseEnabled;
@property (T@"<SBFBlockStatusProvider>",&,N,S_setBlockStatusProvider:,V_blockStatusProvider) blockStatusProvider;
@property (T@"NSTimer",&,N,S_setTimer:,V_timer) timer;
@property (TB,N,G_isEnabled,S_setEnabled:,V_enabled) enabled;
@property (T@?,C,N,V_handler) handler;
```

## Instance methods

```
-[SBFDeviceBlockTimer _setEnabled:];
-[SBFDeviceBlockTimer _isEnabled];
-[SBFDeviceBlockTimer subtitleText];
-[SBFDeviceBlockTimer timer];
-[SBFDeviceBlockTimer setTitleText:];
-[SBFDeviceBlockTimer dealloc];
-[SBFDeviceBlockTimer start];
-[SBFDeviceBlockTimer setHandler:];
-[SBFDeviceBlockTimer titleText];
-[SBFDeviceBlockTimer invalidate];
-[SBFDeviceBlockTimer setSubtitleText:];
-[SBFDeviceBlockTimer handler];
-[SBFDeviceBlockTimer _clearTimer];
-[SBFDeviceBlockTimer setTimeoutText:];
-[SBFDeviceBlockTimer _scheduleTimerIfNecessaryAndUpdateState];
-[SBFDeviceBlockTimer _setBlockStatusProvider:];
-[SBFDeviceBlockTimer _setTimer:];
-[SBFDeviceBlockTimer blockStatusProvider];
-[SBFDeviceBlockTimer initWithDeviceBlockStatusProvider:];
-[SBFDeviceBlockTimer isUserRequestedEraseEnabled];
-[SBFDeviceBlockTimer primaryActionButtonText];
-[SBFDeviceBlockTimer setPrimaryActionButtonText:];
-[SBFDeviceBlockTimer setUserRequestedEraseEnabled:];
-[SBFDeviceBlockTimer timeoutText];
```
