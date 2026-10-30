# `BKMesaSecureIntentProvider`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAUIDelegate`
- 17 instance variables, 9 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" authManagerLogs;
B _authParamActive;
B _pushCredentialPresent;
B _hasAttemptedCrossMatch;
B _inBuddy;
B _touchIDMatch;
Q _touchIDMatchAttemptCount;
^{__IOHIDEventSystemClient=} _hidClient;
B _inDemo;
@"UIView<SecureIntentClientView>" _presentingView;
@"UIWindow" _alertWindow;
@"<BKSecureIntentDisplayHost>" _displayHost;
@"NSString" _credential;
@"LAContext" _context;
@"BKUIAlertView" _alertView;
@"BKUIAlertView" _wrongButtonAlertView;
@"BKUIDevice" _currentDevice;
```

## Properties

```
@property (T@"NSString",&,N,V_credential) credential;
@property (T@"LAContext",&,N,V_context) context;
@property (T@"BKUIAlertView",&,V_alertView) alertView;
@property (T@"BKUIAlertView",&,V_wrongButtonAlertView) wrongButtonAlertView;
@property (T@"BKUIDevice",&,V_currentDevice) currentDevice;
@property (T@"UIView<SecureIntentClientView>",&,N,V_presentingView) presentingView;
@property (T@"UIWindow",W,N,V_alertWindow) alertWindow;
@property (TB,N,V_inDemo) inDemo;
@property (T@"<BKSecureIntentDisplayHost>",W,N,V_displayHost) displayHost;
```

## Instance methods

```
-[BKMesaSecureIntentProvider credential];
-[BKMesaSecureIntentProvider currentDevice];
-[BKMesaSecureIntentProvider reset];
-[BKMesaSecureIntentProvider setContext:];
-[BKMesaSecureIntentProvider setAlertWindow:];
-[BKMesaSecureIntentProvider context];
-[BKMesaSecureIntentProvider setCurrentDevice:];
-[BKMesaSecureIntentProvider alertWindow];
-[BKMesaSecureIntentProvider setCredential:];
-[BKMesaSecureIntentProvider presentingView];
-[BKMesaSecureIntentProvider _handleTouchIDEventWithParameters:];
-[BKMesaSecureIntentProvider event:params:reply:];
-[BKMesaSecureIntentProvider alertView];
-[BKMesaSecureIntentProvider setAlertView:];
-[BKMesaSecureIntentProvider setPresentingView:];
-[BKMesaSecureIntentProvider setDisplayHost:];
-[BKMesaSecureIntentProvider _getSecureIntentForAccessory:enrollmentOperation:showErrorToRetry:withCompletionHandler:];
-[BKMesaSecureIntentProvider _isMonitoringPowerButton];
-[BKMesaSecureIntentProvider _startMonitoringPowerButton];
-[BKMesaSecureIntentProvider _stopMonitoringPowerButton];
-[BKMesaSecureIntentProvider configureIntentView];
-[BKMesaSecureIntentProvider dismissSecureIntentViewForUserInteraction];
-[BKMesaSecureIntentProvider displayHost];
-[BKMesaSecureIntentProvider getSecureIntentForAccessory:enrollmentOperation:withCompletionHandler:];
-[BKMesaSecureIntentProvider hasFingergprintsEnrolled];
-[BKMesaSecureIntentProvider inDemo];
-[BKMesaSecureIntentProvider initInBuddy:withBKUIDevice:];
-[BKMesaSecureIntentProvider invalidateAuthContext];
-[BKMesaSecureIntentProvider needsToDisplayUI];
-[BKMesaSecureIntentProvider setInDemo:];
-[BKMesaSecureIntentProvider setWrongButtonAlertView:];
-[BKMesaSecureIntentProvider showAlert:detailedText:withCompletionHandler:];
-[BKMesaSecureIntentProvider wrongButtonAlertView];
```
