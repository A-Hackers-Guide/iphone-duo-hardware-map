# `CSCoverSheetContextProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 53 properties, 54 instance methods, 0 class methods

## Properties

```
@property (T@"<SBFAuthenticationAssertionProviding>",R,N) authenticationAssertionProvider;
@property (T@"<SBFAuthenticationStatusProvider>",R,N) authenticationStatusProvider;
@property (T@"<SBFPasscodeFieldChangeObserver>",R,N) passcodeFieldChangeObserver;
@property (T@"<SBFLockOutStatusProvider>",R,N) lockOutStatusProvider;
@property (T@"<SBFDateProviding>",R,N) dateProvider;
@property (T@"<CSLegibilityProviding>",R,N) legibilityProvider;
@property (T@"<CSPowerStatusProviding>",R,N) powerStatusProvider;
@property (T@"NSString",R,C,N) powerStatusChangeNotificationName;
@property (T@"NSString",R,C,N) accessoryAttachedNotificationName;
@property (T@"NSString",R,C,N) accessoryDetachedNotificationName;
@property (T@"NSString",R,C,N) accessoryAnimationStatusChangedNotificationName;
@property (T@"<CSMagSafeAccessoryStatusProviding>",R,N) accessoryStatusProvider;
@property (T@"<CSResetRestoreStatusProviding>",R,N) resetRestoreStatusProvider;
@property (T@"<CSThermalStatusProviding>",R,N) thermalStatusProvider;
@property (T@"<SBUIBiometricResource>",R,N) biometricResource;
@property (T@"<CSBiometricSuppressionProviding>",?,R,N) biometricSuppressionProvider;
@property (T@"<CSScreenStateProviding>",R,N) screenStateProvider;
@property (T@"<SBFScreenWakeAnimationControlling>",R,N) screenWakeAnimationController;
@property (T@"<CSWallpaperProviding>",R,N) wallpaperProvider;
@property (T@"<CSWallpaperSnapshotUpdating>",R,N) wallpaperSnapshotUpdater;
@property (T@"<CSTelephonyStatusProviding>",R,N) telephonyStatusProvider;
@property (T@"<CSAuthenticationManaging>",R,N) authenticationManager;
@property (T@"<CSHomeAffordanceControlling>",R,N) homeAffordanceController;
@property (T@"<CSModalHomeAffordanceControlling>",R,N) modalHomeAffordanceController;
@property (T@"<CSPlatterHomeGestureManaging>",R,N) platterHomeGestureManager;
@property (T@"<CSStatusBarControlling>",R,N) statusBarController;
@property (T@"<CSMediaControlling>",R,N) mediaController;
@property (T@"<CSUnlockRequesting>",R,N) unlockRequester;
@property (T@"<SBFActionProviding>",R,N) contentActionProvider;
@property (T@"<CSApplicationInforming>",R,N) applicationInformer;
@property (T@"<CSNotificationPresenting>",R,N) notificationPresenter;
@property (T@"<CSTouchEnvironmentStatusProviding>",R,N) touchEnvironmentStatusProvider;
@property (T@"<CSUserSessionControlling>",R,N) userSessionController;
@property (T@"<CSReachabilityControlling>",R,N) reachabilityController;
@property (T@"<CSCarPlayStatusProviding>",R,N) carPlayStatusProvider;
@property (T@"<CSOverlayProviding>",R,N) homeScreenOverlayProvider;
@property (T@"<CSAppHostConfiguring>",R,N) appHostConfiguring;
@property (T@"<CSTraitAwareAppHostConfiguring>",R,N) traitsAwareAppHosting;
@property (T@"<CSSystemPointerInteractionManaging>",R,N) systemPointerInteractionManager;
@property (T@"<CSProximitySensorProviding>",R,N) proximitySensorProvider;
@property (T@"<CSDeviceOrientationProviding>",R,N) deviceOrientationProvider;
@property (T@"<CSDevicePoseProviding>",R,N) devicePoseProvider;
@property (T@"<SBFHomeAffordanceInteractionProviding>",R,N) homeAffordanceInteractionProvider;
@property (T@"<CSAssistantControlling>",R,N) assistantController;
@property (T@"<CSCaptureButtonRestrictionControlling>",R,N) captureButtonRestrictionController;
@property (T@"<CSBacklightRegistering>",R,N) backlightRegistrar;
@property (T@"<CSAmbientPresentationProviding>",R,N) ambientPresentationProvider;
@property (T@"<CSPosterSwitcherViewControllerProviding>",R,N) posterSwitcherViewControllerProvider;
@property (T@"<CSWakeLoggerProviding>",R,N) wakeLoggerProvider;
@property (T@"<CSHostedEntityTransferCoordinating>",R,N) hostedEntityTransferCoordinator;
@property (T@"<CSRemoteContentAppearanceCoordinating>",?,R,N) remoteContentAppearanceCoordinator;
@property (T@"<CSActivityMetricsProviding>",R,N) activityMetricsProvider;
@property (T@"<CSActiveDisplayStatusProviding>",R,N) activeDisplayStatusProvider;
```

## Instance methods

```
-[CSCoverSheetContextProviding contentActionProvider];
-[CSCoverSheetContextProviding wakeLoggerProvider];
-[CSCoverSheetContextProviding userSessionController];
-[CSCoverSheetContextProviding platterHomeGestureManager];
-[CSCoverSheetContextProviding deviceOrientationProvider];
-[CSCoverSheetContextProviding hostedEntityTransferCoordinator];
-[CSCoverSheetContextProviding reachabilityController];
-[CSCoverSheetContextProviding notificationPresenter];
-[CSCoverSheetContextProviding powerStatusProvider];
-[CSCoverSheetContextProviding legibilityProvider];
-[CSCoverSheetContextProviding mediaController];
-[CSCoverSheetContextProviding unlockRequester];
-[CSCoverSheetContextProviding biometricResource];
-[CSCoverSheetContextProviding dateProvider];
-[CSCoverSheetContextProviding applicationInformer];
-[CSCoverSheetContextProviding proximitySensorProvider];
-[CSCoverSheetContextProviding homeAffordanceController];
-[CSCoverSheetContextProviding passcodeFieldChangeObserver];
-[CSCoverSheetContextProviding systemPointerInteractionManager];
-[CSCoverSheetContextProviding authenticationStatusProvider];
-[CSCoverSheetContextProviding wallpaperProvider];
-[CSCoverSheetContextProviding thermalStatusProvider];
-[CSCoverSheetContextProviding accessoryAttachedNotificationName];
-[CSCoverSheetContextProviding backlightRegistrar];
-[CSCoverSheetContextProviding resetRestoreStatusProvider];
-[CSCoverSheetContextProviding carPlayStatusProvider];
-[CSCoverSheetContextProviding appHostConfiguring];
-[CSCoverSheetContextProviding ambientPresentationProvider];
-[CSCoverSheetContextProviding touchEnvironmentStatusProvider];
-[CSCoverSheetContextProviding captureButtonRestrictionController];
-[CSCoverSheetContextProviding statusBarController];
-[CSCoverSheetContextProviding assistantController];
-[CSCoverSheetContextProviding traitsAwareAppHosting];
-[CSCoverSheetContextProviding authenticationManager];
-[CSCoverSheetContextProviding accessoryAnimationStatusChangedNotificationName];
-[CSCoverSheetContextProviding modalHomeAffordanceController];
-[CSCoverSheetContextProviding authenticationAssertionProvider];
-[CSCoverSheetContextProviding accessoryDetachedNotificationName];
-[CSCoverSheetContextProviding devicePoseProvider];
-[CSCoverSheetContextProviding telephonyStatusProvider];
-[CSCoverSheetContextProviding dismissableOverlaysOutOf:];
-[CSCoverSheetContextProviding screenStateProvider];
-[CSCoverSheetContextProviding posterSwitcherViewControllerProvider];
-[CSCoverSheetContextProviding accessoryStatusProvider];
-[CSCoverSheetContextProviding screenWakeAnimationController];
-[CSCoverSheetContextProviding lockOutStatusProvider];
-[CSCoverSheetContextProviding wallpaperSnapshotUpdater];
-[CSCoverSheetContextProviding powerStatusChangeNotificationName];
-[CSCoverSheetContextProviding activeDisplayStatusProvider];
-[CSCoverSheetContextProviding activityMetricsProvider];
-[CSCoverSheetContextProviding homeAffordanceInteractionProvider];
-[CSCoverSheetContextProviding homeScreenOverlayProvider];
-[CSCoverSheetContextProviding biometricSuppressionProvider];
-[CSCoverSheetContextProviding remoteContentAppearanceCoordinator];
```
