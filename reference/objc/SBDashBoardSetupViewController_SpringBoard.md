# `SBDashBoardSetupViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSCoverSheetViewControllerBase`
- Protocols: `SBSolariumCursiveTextAnimationDelegate`, `STTelephonyStateObserver`, `CSEventHandling`, `UIGestureRecognizerDelegate`
- 29 instance variables, 5 properties, 70 instance methods, 0 class methods

## Instance variables

```
@"SBSetupWiFiScanner" _wifiScanner;
@"SBSRemoteAlertHandle" _remoteAlertHandle;
@"SBActivationInfoViewController" _activationInfoViewController;
@"SBSetupRegulatoryInfoViewController" _regulatoryInfoViewController;
@"SBSetupManager" _setupManager;
@"CSCoverSheetViewController" _coverSheetViewController;
@"SBTelephonyManager" _telephonyManager;
@"NSString" _configureKey;
@"NSString" _wifiPrimaryLanguage;
@"NSString" _telephonyPrimaryLanguage;
@"NSTimer" _cycleStartTimer;
@"NSDictionary" _storeRestrictedStrings;
@"NSDictionary" _activationLockStrings;
@"NSString" _maskedAppleID;
@"NSString" _solariumCursiveTextLanguage;
@"NSTimer" _cursiveTextAnimationApproximationTimer;
B _suppressingWallpaperForCursiveTextAnimation;
@"NSArray" _stringsOrdering;
@"NSMutableArray" _currentStringsOrdering;
Q _currentStringsIndex;
B _shouldResetOrderingOnNextCycle;
B _isCyclingComponents;
Q _componentsToCycle;
d _customDelayDuration;
B _isStoreRestricted;
B _isActivationLocked;
@"UITapGestureRecognizer" _pointerClickGestureRecognizer;
@"UIHoverGestureRecognizer" _hoverGestureRecognizer;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"CSCoverSheetViewController",W,N,V_coverSheetViewController) coverSheetViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardSetupViewController coverSheetViewController];
-[SBDashBoardSetupViewController presentationType];
-[SBDashBoardSetupViewController handleEvent:];
-[SBDashBoardSetupViewController _isSecurityResearchDevice];
-[SBDashBoardSetupViewController gestureRecognizer:shouldReceiveTouch:];
-[SBDashBoardSetupViewController aggregateBehavior:];
-[SBDashBoardSetupViewController viewWillDisappear:];
-[SBDashBoardSetupViewController dealloc];
-[SBDashBoardSetupViewController presentationPriority];
-[SBDashBoardSetupViewController viewDidLoad];
-[SBDashBoardSetupViewController subscriptionInfoDidChangeForStateProvider:slot:];
-[SBDashBoardSetupViewController viewWillAppear:];
-[SBDashBoardSetupViewController aggregateAppearance:];
-[SBDashBoardSetupViewController setCoverSheetViewController:];
-[SBDashBoardSetupViewController viewDidAppear:];
-[SBDashBoardSetupViewController setupView];
-[SBDashBoardSetupViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBDashBoardSetupViewController loadView];
-[SBDashBoardSetupViewController viewDidDisappear:];
-[SBDashBoardSetupViewController _startWifiScan];
-[SBDashBoardSetupViewController _infoButtonTapped:];
-[SBDashBoardSetupViewController _regulatoryInfoButtonTapped:];
-[SBDashBoardSetupViewController _cancelWifiScan];
-[SBDashBoardSetupViewController _activateForESIMSetupButtonTapped:];
-[SBDashBoardSetupViewController _alignedMarketingOrdering];
-[SBDashBoardSetupViewController _animateComponentsForNewCycle];
-[SBDashBoardSetupViewController _applicableIdentifierForDictionary:identifier:];
-[SBDashBoardSetupViewController _canCycleAnimationComponents];
-[SBDashBoardSetupViewController _canShowSolariumCursiveAnimation];
-[SBDashBoardSetupViewController _checkIfActivationLocked];
-[SBDashBoardSetupViewController _componentsRelevantToPointerSuppression];
-[SBDashBoardSetupViewController _componentsToStartCycling];
-[SBDashBoardSetupViewController _currentActivationLockStringsDictionary];
-[SBDashBoardSetupViewController _currentLanguageIdentifier];
-[SBDashBoardSetupViewController _currentStoreRestrictedStringsDictionary];
-[SBDashBoardSetupViewController _didClickHomeAffordance:];
-[SBDashBoardSetupViewController _displayStringForLocalizedString:fallbackString:];
-[SBDashBoardSetupViewController _evaluateUpdatingLanguageForImportantLanguageChanges];
-[SBDashBoardSetupViewController _handleHoverEvent:];
-[SBDashBoardSetupViewController _haveImportantLanguagesChangedFrom:];
-[SBDashBoardSetupViewController _importantLanguageIdentifiers];
-[SBDashBoardSetupViewController _incrementLocalizedStringsForNewCycle];
-[SBDashBoardSetupViewController _invalidateWallpaperLoadingTimerAndShowUIIfNeeded];
-[SBDashBoardSetupViewController _isRunningBookendAnimation];
-[SBDashBoardSetupViewController _makeSetupAccessoryViewsVisible:animated:delay:];
-[SBDashBoardSetupViewController _presentSIMSetupFlowWithFlowType:reason:];
-[SBDashBoardSetupViewController _resetDisplayedLocalizedStringsImmediately:];
-[SBDashBoardSetupViewController _retrieveChildIconIfNecessaryWithCompletion:];
-[SBDashBoardSetupViewController _setSuppressingWallpaperForCursiveTextAnimation:];
-[SBDashBoardSetupViewController _shareIdentityButtonTapped:];
-[SBDashBoardSetupViewController _simConfigButtonTapped:];
-[SBDashBoardSetupViewController _startCyclingComponents:withDelay:];
-[SBDashBoardSetupViewController _startWallpaperLoadingTimerWithDuration:];
-[SBDashBoardSetupViewController _stopCyclingComponents:];
-[SBDashBoardSetupViewController _subcriptionDataSourceDescription:];
-[SBDashBoardSetupViewController _subscriptionInfoForSubscriptionDataSource:];
-[SBDashBoardSetupViewController _supportedLanguageIdentifierFromRegionalLanguageIdentifier:countryCode:];
-[SBDashBoardSetupViewController _unlockIfNecessaryAndPresentSIMSetupFlowWithFlowType:reason:unlockName:];
-[SBDashBoardSetupViewController _updateDisplayedStrings];
-[SBDashBoardSetupViewController _updateForLockInfo:];
-[SBDashBoardSetupViewController _updateLanguageFromSubscriptionDataSource:];
-[SBDashBoardSetupViewController _updateLanguageFromTelephony];
-[SBDashBoardSetupViewController _updateStringOrderingForLanguageChange];
-[SBDashBoardSetupViewController _updateWifiPrimaryLanguageFromDiscoveredCountryCodes:];
-[SBDashBoardSetupViewController animationWillBeginForLanguage:animationDuration:];
-[SBDashBoardSetupViewController firstSupportedLanguageIdentifierInRegionalLanguageIdentifiers:countryCode:];
-[SBDashBoardSetupViewController glassCursiveTextLanguages];
-[SBDashBoardSetupViewController initWithCoverSheetViewController:];
-[SBDashBoardSetupViewController initWithCoverSheetViewController:telephonyManager:];
-[SBDashBoardSetupViewController isCyclingComponents:];
```
