# `SBFLockScreenDateViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PTSettingsKeyObserver`
- 15 instance variables, 18 properties, 73 instance methods, 0 class methods

## Instance variables

```
@ _timerToken;
B _isVisible;
@ _minuteHandlerToken;
B _disablesUpdates;
@"SBAlwaysOnDefaults" _alwaysOnDefaults;
@"<BSDefaultObserver>" _alwaysOnDefaultsObserver;
@"CSProminentDisplayViewController" _prominentDisplayViewController;
@"<UITraitChangeRegistration>" _luminanceTraitChangeRegistration;
B _screenOff;
B _showCompactTime;
B _alternateDateEnabled;
B _restrictsVibrancy;
@"_UILegibilitySettings" _legibilitySettings;
@"<SBFDateProviding>" _dateProvider;
d _luminanceChangeAnimationResponse;
```

## Properties

```
@property (Td,N) backgroundAlpha;
@property (T@"UIViewController",&,N) inlineComplicationViewController;
@property (T@"UIViewController",&,N) complicationContainerViewController;
@property (TB,N,V_screenOff) screenOff;
@property (TB,N,GisAlternateDateEnabled,V_alternateDateEnabled) alternateDateEnabled;
@property (TB,N,GisSubtitleHidden) subtitleHidden;
@property (TB,N) shouldApplyVibrancyToComplications;
@property (TB,N,V_restrictsVibrancy) restrictsVibrancy;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
@property (T@"<SBFDateProviding>",&,N,V_dateProvider) dateProvider;
@property (TB,N,V_showCompactTime) showCompactTime;
@property (TB,N) hasSidebarContents;
@property (Td,R,N) adaptiveTextHeight;
@property (Td,N,V_luminanceChangeAnimationResponse) luminanceChangeAnimationResponse;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFLockScreenDateViewController shouldApplyVibrancyToComplications];
-[SBFLockScreenDateViewController setShouldApplyVibrancyToComplications:];
-[SBFLockScreenDateViewController setCustomSubtitleView:];
-[SBFLockScreenDateViewController _updateWithFrameSpecifier:];
-[SBFLockScreenDateViewController _timelinesForDateInterval:];
-[SBFLockScreenDateViewController _addObservers];
-[SBFLockScreenDateViewController screenOff];
-[SBFLockScreenDateViewController _updateView];
-[SBFLockScreenDateViewController setScreenOff:];
-[SBFLockScreenDateViewController _updateState];
-[SBFLockScreenDateViewController dateView];
-[SBFLockScreenDateViewController updateTimerWithText:];
-[SBFLockScreenDateViewController dateProvider];
-[SBFLockScreenDateViewController isSubtitleHidden];
-[SBFLockScreenDateViewController setTimerWithText:];
-[SBFLockScreenDateViewController setAlternateDateEnabled:];
-[SBFLockScreenDateViewController transientSubtitleText];
-[SBFLockScreenDateViewController luminanceChangeAnimationResponse];
-[SBFLockScreenDateViewController setBackgroundAlpha:];
-[SBFLockScreenDateViewController showCompactTime];
-[SBFLockScreenDateViewController _updateFormat];
-[SBFLockScreenDateViewController setDateProvider:];
-[SBFLockScreenDateViewController _updateAlternateCalendar];
-[SBFLockScreenDateViewController dealloc];
-[SBFLockScreenDateViewController _updateLegibilityStrength];
-[SBFLockScreenDateViewController setCustomSubtitle:withPriority:withTimeout:];
-[SBFLockScreenDateViewController willMoveToParentViewController:];
-[SBFLockScreenDateViewController setInlineComplicationViewController:];
-[SBFLockScreenDateViewController setView:];
-[SBFLockScreenDateViewController dateViewIfExists];
-[SBFLockScreenDateViewController setComplicationContainerViewController:];
-[SBFLockScreenDateViewController _timeAnimationIntervalToUse];
-[SBFLockScreenDateViewController initWithNibName:bundle:];
-[SBFLockScreenDateViewController settings:changedValueForKey:];
-[SBFLockScreenDateViewController setShowCompactTime:];
-[SBFLockScreenDateViewController viewWillAppear:];
-[SBFLockScreenDateViewController _updateForLuminanceFromTraitEnvironment:];
-[SBFLockScreenDateViewController _updateAnimatesTimeChanges];
-[SBFLockScreenDateViewController backgroundAlpha];
-[SBFLockScreenDateViewController setDateTimeAlignment:];
-[SBFLockScreenDateViewController _canShowWhileLocked];
-[SBFLockScreenDateViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBFLockScreenDateViewController setRestrictsVibrancy:];
-[SBFLockScreenDateViewController setDimmingViewAlpha:];
-[SBFLockScreenDateViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBFLockScreenDateViewController _updateFormatIfEnabled];
-[SBFLockScreenDateViewController loadView];
-[SBFLockScreenDateViewController setTimeSupportsStretch:];
-[SBFLockScreenDateViewController complicationContainerViewController];
-[SBFLockScreenDateViewController setHasSidebarContents:];
-[SBFLockScreenDateViewController inlineComplicationViewController];
-[SBFLockScreenDateViewController restrictsVibrancy];
-[SBFLockScreenDateViewController _stopUpdateTimer];
-[SBFLockScreenDateViewController isHostingViewController:];
-[SBFLockScreenDateViewController description];
-[SBFLockScreenDateViewController legibilitySettings];
-[SBFLockScreenDateViewController viewDidDisappear:];
-[SBFLockScreenDateViewController _backlightLuminanceChangedForEnvironment:previousTraitCollection:];
-[SBFLockScreenDateViewController adaptiveTextHeight];
-[SBFLockScreenDateViewController hasSidebarContents];
-[SBFLockScreenDateViewController _prominentDisplaySubtitlePriorityForPriority:];
-[SBFLockScreenDateViewController _lowPowerModeDidChange:];
-[SBFLockScreenDateViewController _supportsCoaching];
-[SBFLockScreenDateViewController _handleTimeZoneChange];
-[SBFLockScreenDateViewController setSubtitleHidden:];
-[SBFLockScreenDateViewController updateTimeNow];
-[SBFLockScreenDateViewController setLegibilitySettings:];
-[SBFLockScreenDateViewController isAlternateDateEnabled];
-[SBFLockScreenDateViewController setTimeAlpha:subtitleAlpha:];
-[SBFLockScreenDateViewController setLuminanceChangeAnimationResponse:];
-[SBFLockScreenDateViewController _updateCompactTime];
-[SBFLockScreenDateViewController _startUpdateTimer];
-[SBFLockScreenDateViewController setShowCompactTime:animated:];
```
