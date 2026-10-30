# `VTUIProximityDataSharingOptInView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIProximityView`
- 8 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"VTUIProximityContainerView" _containerView;
@"UILabel" _titleLabel;
@"UILabel" _subtitleLabel;
@"UIScrollView" _scrollView;
@"VTUIButton" _shareButton;
@"VTUIButton" _notNowButton;
@"UIButton" _dismissButton;
@"UIButton" _aboutLink;
```

## Properties

```
@property (T@"VTUIButton",&,N,V_shareButton) shareButton;
@property (T@"VTUIButton",&,N,V_notNowButton) notNowButton;
@property (T@"UIButton",&,N,V_dismissButton) dismissButton;
@property (T@"UIButton",&,N,V_aboutLink) aboutLink;
```

## Instance methods

```
-[VTUIProximityDataSharingOptInView initWithFrame:];
-[VTUIProximityDataSharingOptInView dismissButton];
-[VTUIProximityDataSharingOptInView setDismissButton:];
-[VTUIProximityDataSharingOptInView notNowButton];
-[VTUIProximityDataSharingOptInView setNotNowButton:];
-[VTUIProximityDataSharingOptInView setShareButton:];
-[VTUIProximityDataSharingOptInView shareButton];
-[VTUIProximityDataSharingOptInView _setupContent];
-[VTUIProximityDataSharingOptInView _setupPortraitConstraints];
-[VTUIProximityDataSharingOptInView aboutLink];
-[VTUIProximityDataSharingOptInView setAboutLink:];
```
