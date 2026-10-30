# `TPInComingCallUISnapshotViewController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 14 instance variables, 14 properties, 55 instance methods, 5 class methods

## Instance variables

```
@"UIView" _overlaysContainerView;
@"PRPosterLabel" _mobileLabel;
@"UIButton" _remindMeButton;
@"UIButton" _messageButton;
@"UIButton" _declineButton;
@"UIButton" _acceptButton;
@"UIButton" _callDetailsViewButton;
@"UILabel" _nameLabel;
@"UIImageView" _avatarView;
@"PRSPosterConfiguration" _configuration;
q _style;
@"UILabel" _fakeLabel;
@"CNContact" _contact;
@"UIImage" _customAvatar;
```

## Properties

```
@property (T@"UIView",&,N,V_overlaysContainerView) overlaysContainerView;
@property (T@"PRPosterLabel",&,N,V_mobileLabel) mobileLabel;
@property (T@"UIButton",&,N,V_remindMeButton) remindMeButton;
@property (T@"UIButton",&,N,V_messageButton) messageButton;
@property (T@"UIButton",&,N,V_declineButton) declineButton;
@property (T@"UIButton",&,N,V_acceptButton) acceptButton;
@property (T@"UIButton",&,N,V_callDetailsViewButton) callDetailsViewButton;
@property (T@"UILabel",&,N,V_nameLabel) nameLabel;
@property (T@"UIImageView",&,N,V_avatarView) avatarView;
@property (T@"PRSPosterConfiguration",&,N,V_configuration) configuration;
@property (Tq,N,V_style) style;
@property (T@"UILabel",&,N,V_fakeLabel) fakeLabel;
@property (T@"CNContact",&,N,V_contact) contact;
@property (T@"UIImage",&,N,V_customAvatar) customAvatar;
```

## Class methods

```
+[TPInComingCallUISnapshotViewController horizontalNameLabelBoundingRectForName:window:];
+[TPInComingCallUISnapshotViewController posterDisplayNameComponentsForContact:];
+[TPInComingCallUISnapshotViewController verticalNameLabelBoundingRectForName:window:];
+[TPInComingCallUISnapshotViewController horizontalNameLabelBoundingRectForName:caption:window:preferredTitleFont:];
+[TPInComingCallUISnapshotViewController verticalNameLabelBoundingRectForName:caption:window:preferredTitleFont:];
```

## Instance methods

```
-[TPInComingCallUISnapshotViewController avatarView];
-[TPInComingCallUISnapshotViewController contact];
-[TPInComingCallUISnapshotViewController setAvatarView:];
-[TPInComingCallUISnapshotViewController setConfiguration:];
-[TPInComingCallUISnapshotViewController viewDidLoad];
-[TPInComingCallUISnapshotViewController style];
-[TPInComingCallUISnapshotViewController setStyle:];
-[TPInComingCallUISnapshotViewController configuration];
-[TPInComingCallUISnapshotViewController nameLabel];
-[TPInComingCallUISnapshotViewController setContact:];
-[TPInComingCallUISnapshotViewController setNameLabel:];
-[TPInComingCallUISnapshotViewController messageButton];
-[TPInComingCallUISnapshotViewController setMessageButton:];
-[TPInComingCallUISnapshotViewController setUpConstraints];
-[TPInComingCallUISnapshotViewController initWithConfiguration:style:contact:avatarImage:];
-[TPInComingCallUISnapshotViewController initWithConfiguration:style:contact:fallbackText:];
-[TPInComingCallUISnapshotViewController initWithConfiguration:style:nameString:avatarImage:];
-[TPInComingCallUISnapshotViewController nameString];
-[TPInComingCallUISnapshotViewController snapshotWithOptions:windowScene:completionBlock:];
-[TPInComingCallUISnapshotViewController acceptButton];
-[TPInComingCallUISnapshotViewController setAcceptButton:];
-[TPInComingCallUISnapshotViewController setLabelsColor:];
-[TPInComingCallUISnapshotViewController setMobileLabel:];
-[TPInComingCallUISnapshotViewController attachmentIdentifiersForStyle];
-[TPInComingCallUISnapshotViewController attachmentsForStyle];
-[TPInComingCallUISnapshotViewController callDetailsViewButton];
-[TPInComingCallUISnapshotViewController capCallDetailsViewButtonSize];
-[TPInComingCallUISnapshotViewController customAvatar];
-[TPInComingCallUISnapshotViewController declineButton];
-[TPInComingCallUISnapshotViewController fakeLabel];
-[TPInComingCallUISnapshotViewController generateOverlaysSnapshot];
-[TPInComingCallUISnapshotViewController hideElementsBasedOn:];
-[TPInComingCallUISnapshotViewController identifierForStyle];
-[TPInComingCallUISnapshotViewController initWithConfiguration:style:contact:];
-[TPInComingCallUISnapshotViewController initWithConfiguration:style:nameString:];
-[TPInComingCallUISnapshotViewController mobileLabel];
-[TPInComingCallUISnapshotViewController moveMobileLabelToBeYAxisCenteredWithInfoButton];
-[TPInComingCallUISnapshotViewController overlaysContainerView];
-[TPInComingCallUISnapshotViewController remindMeButton];
-[TPInComingCallUISnapshotViewController setBackroundColor:];
-[TPInComingCallUISnapshotViewController setCallDetailsViewButton:];
-[TPInComingCallUISnapshotViewController setCustomAvatar:];
-[TPInComingCallUISnapshotViewController setDeclineButton:];
-[TPInComingCallUISnapshotViewController setFakeLabel:];
-[TPInComingCallUISnapshotViewController setNameLabelFont:];
-[TPInComingCallUISnapshotViewController setNameLabelTextColor:];
-[TPInComingCallUISnapshotViewController setOverlaysContainerView:];
-[TPInComingCallUISnapshotViewController setRemindMeButton:];
-[TPInComingCallUISnapshotViewController setUpButton:];
-[TPInComingCallUISnapshotViewController setUpOverlayContentIfNeeded];
-[TPInComingCallUISnapshotViewController setUpOverlaysContainer];
-[TPInComingCallUISnapshotViewController setupAvatarViewIfNeeded];
-[TPInComingCallUISnapshotViewController setupLabels];
-[TPInComingCallUISnapshotViewController snapshotWithOptions:completionBlock:];
-[TPInComingCallUISnapshotViewController snapshotWithOptions:windowScene:useAttachmentConfiguration:completionBlock:];
```
