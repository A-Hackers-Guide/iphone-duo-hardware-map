# `VTUISiriDataSharingOptInPresenter`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTUISiriDataSharingOptInViewControllerDelegate`
- 8 instance variables, 3 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"AFSettingsConnection" _settings;
@"NSObject<OS_dispatch_queue>" _settingsQueue;
q _dataSharingOptInStatus;
@"VTUISiriDataSharingOptInViewController" _currentWelcomeController;
@"VTUIProximityDataSharingOptInView" _currentProxView;
@"<VTUISiriDataSharingOptInPresentationDelegate>" _presentationDelegate;
q _sourceOfChange;
@"NSString" _reasonForChange;
```

## Properties

```
@property (T@"<VTUISiriDataSharingOptInPresentationDelegate>",W,N,V_presentationDelegate) presentationDelegate;
@property (Tq,V_sourceOfChange) sourceOfChange;
@property (T@"NSString",C,V_reasonForChange) reasonForChange;
```

## Class methods

```
+[VTUISiriDataSharingOptInPresenter siriDataSharingOptInViewFeatureFlagEnabled];
```

## Instance methods

```
-[VTUISiriDataSharingOptInPresenter presentationDelegate];
-[VTUISiriDataSharingOptInPresenter setPresentationDelegate:];
-[VTUISiriDataSharingOptInPresenter init];
-[VTUISiriDataSharingOptInPresenter _requestDismissal];
-[VTUISiriDataSharingOptInPresenter dataSharingOptInTextWelcomeControllerForViewStyle:];
-[VTUISiriDataSharingOptInPresenter setSourceOfChange:];
-[VTUISiriDataSharingOptInPresenter shouldShowSiriDataSharingOptInView];
-[VTUISiriDataSharingOptInPresenter reasonForChange];
-[VTUISiriDataSharingOptInPresenter _fetchSiriDataSharingEnabled];
-[VTUISiriDataSharingOptInPresenter _modalViewControllerForViewStyle:];
-[VTUISiriDataSharingOptInPresenter _proximityViewForFrame:];
-[VTUISiriDataSharingOptInPresenter _setSiriDataSharingStatus:forceDismissal:];
-[VTUISiriDataSharingOptInPresenter _userTappedDetailLinkText];
-[VTUISiriDataSharingOptInPresenter _userTappedDismissButtonFromProxCard];
-[VTUISiriDataSharingOptInPresenter _userTappedOptInToDataSharing];
-[VTUISiriDataSharingOptInPresenter _userTappedOptOutOfDataSharing];
-[VTUISiriDataSharingOptInPresenter dataSharingOptInViewForFrame:viewStyle:];
-[VTUISiriDataSharingOptInPresenter didDismissFromViewController:];
-[VTUISiriDataSharingOptInPresenter setReasonForChange:];
-[VTUISiriDataSharingOptInPresenter sourceOfChange];
-[VTUISiriDataSharingOptInPresenter tearDownPresentedViews];
```
