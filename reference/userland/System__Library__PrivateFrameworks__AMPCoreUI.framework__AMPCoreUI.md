# `/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI`

iOS 27.2 dyld shared cache image. Version `1453.1.1.2.2`. **[DSC]**

## Linked libraries (10)

- `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/System/Library/Frameworks/UserNotifications.framework/UserNotifications`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking`

## Objective-C: 13 classes, 6 protocols, 205 methods, 73 properties

### Class pages

Every class and protocol, with its methods: [`AMPAppleCardArtwork`](../objc/AMPAppleCardArtwork_AMPCoreUI.md), [`AMPButton`](../objc/AMPButton_AMPCoreUI.md), [`AMPCardMetadataRegistration`](../objc/AMPCardMetadataRegistration_AMPCoreUI.md), [`AMPOnboardingFeature`](../objc/AMPOnboardingFeature_AMPCoreUI.md), [`AMPOnboardingFeatureView`](../objc/AMPOnboardingFeatureView_AMPCoreUI.md), [`AMPOnboardingHeaderView`](../objc/AMPOnboardingHeaderView_AMPCoreUI.md), [`AMPOnboardingMultiFeatureHeaderView`](../objc/AMPOnboardingMultiFeatureHeaderView_AMPCoreUI.md), [`AMPOnboardingViewController`](../objc/AMPOnboardingViewController_AMPCoreUI.md), [`AMPPrivacyAnimatedTransitioning`](../objc/AMPPrivacyAnimatedTransitioning_AMPCoreUI.md), [`AMPPrivacyPresentationController`](../objc/AMPPrivacyPresentationController_AMPCoreUI.md), [`AMPTintedBackgroundButton`](../objc/AMPTintedBackgroundButton_AMPCoreUI.md), [`AMPUserNotificationContentDelegate`](../objc/AMPUserNotificationContentDelegate_AMPCoreUI.protocol.md), [`AMPUserNotificationContentViewController`](../objc/AMPUserNotificationContentViewController_AMPCoreUI.md), [`AMPUserNotificationViewController`](../objc/AMPUserNotificationViewController_AMPCoreUI.md), [`NSObject`](../objc/NSObject_AMPCoreUI.protocol.md), [`UIAdaptivePresentationControllerDelegate`](../objc/UIAdaptivePresentationControllerDelegate_AMPCoreUI.protocol.md), [`UIScrollViewDelegate`](../objc/UIScrollViewDelegate_AMPCoreUI.protocol.md), [`UIViewControllerAnimatedTransitioning`](../objc/UIViewControllerAnimatedTransitioning_AMPCoreUI.protocol.md), [`UNNotificationContentExtension`](../objc/UNNotificationContentExtension_AMPCoreUI.protocol.md)

### Classes

`AMPAppleCardArtwork`, `AMPButton`, `AMPCardMetadataRegistration`, `AMPOnboardingFeature`, `AMPOnboardingFeatureView`, `AMPOnboardingHeaderView`, `AMPOnboardingMultiFeatureHeaderView`, `AMPOnboardingViewController`, `AMPPrivacyAnimatedTransitioning`, `AMPPrivacyPresentationController`, `AMPTintedBackgroundButton`, `AMPUserNotificationContentViewController`, `AMPUserNotificationViewController`

### Protocols

`AMPUserNotificationContentDelegate`, `NSObject`, `UIAdaptivePresentationControllerDelegate`, `UIScrollViewDelegate`, `UIViewControllerAnimatedTransitioning`, `UNNotificationContentExtension`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,?,R,N) mediaPlayPauseButtonType;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) mediaPlayPauseButtonFrame;
@property (T@"UIColor",?,R,C,N) mediaPlayPauseButtonTintColor;
@property (T@"UIImage",R,N,V_image) image;
@property (T@"NSString",R,N,V_titleText) titleText;
@property (T@"NSString",R,N,V_descriptionText) descriptionText;
@property (T@"UIImageView",&,N,V_imageView) imageView;
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"UILabel",&,N,V_descriptionLabel) descriptionLabel;
@property (Td,R,N) baselineOffsetFromBottom;
@property (T@"UIImageView",&,N,V_imageView) imageView;
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"UILabel",&,N,V_descriptionLabel) descriptionLabel;
@property (Td,N,V_containerHeight) containerHeight;
@property (TB,N,V_isPresentedInFormSheet) isPresentedInFormSheet;
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"NSArray",&,N,V_featureViews) featureViews;
@property (Td,N,V_containerHeight) containerHeight;
@property (TB,N,V_isPresentedInFormSheet) isPresentedInFormSheet;
@property (T@"AMSUIOnboardingViewController",&,N,V_onboardingController) onboardingController;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"NSString",&,N,V_titleText) titleText;
@property (T@"NSString",&,N,V_descriptionText) descriptionText;
@property (T@"NSString",&,N,V_primaryButtonText) primaryButtonText;
@property (TB,R,N) isPresentedInFormSheet;
@property (T@"UIVisualEffectView",&,N,V_statusBarVisualEffectView) statusBarVisualEffectView;
@property (T@"_UIBackdropView",&,N,V_backdropView) backdropView;
@property (T@"UITraitCollection",R,N) cappedTraitCollection;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_metricsQueue) metricsQueue;
@property (TB,N,V_viewHasAppeared) viewHasAppeared;
@property (T@"UIImage",R,N) headerImage;
@property (T@"OBPrivacyLinkController",R,N,V_privacyLinkController) privacyLinkController;
@property (T@?,C,N,V_primaryButtonCallback) primaryButtonCallback;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,GisPresentation,V_presentation) presentation;
@property (T@"UIViewController",&,N,V_viewController) viewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",&,N,V_dimmingView) dimmingView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",&,N,V_audioSessionCategory) audioSessionCategory;
@property (TQ,N,V_audioSessionCategoryOptions) audioSessionCategoryOptions;
@property (TB,N,V_hasAppeared) hasAppeared;
@property (TB,N,V_hasPlayedVideo) hasPlayedVideo;
@property (T@"UIImageView",R,N,V_imageView) imageView;
@property (T@"AMSMetrics",&,N,V_metrics) metrics;
@property (T@"UILabel",R,N,V_textLabel) textLabel;
@property (T@"UILabel",R,N,V_titleLabel) titleLabel;
@property (T@"AVPlayerViewController",R,N,V_videoPlayerController) videoPlayerController;
@property (T@"AMSUserNotification",R,N,V_userNotification) userNotification;
@property (T@"<AMPUserNotificationContentDelegate>",W,N,V_delegate) delegate;
@property (T{CGSize=dd},R,N) expectedContentSize;
@property (T@"AMPUserNotificationContentViewController",&,N,V_contentViewController) contentViewController;
@property (T@"<AMSURLBagContract>",&,N,V_bagContract) bagContract;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,?,R,N) mediaPlayPauseButtonType;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) mediaPlayPauseButtonFrame;
@property (T@"UIColor",?,R,C,N) mediaPlayPauseButtonTintColor;
```

## Strings (51)

```
AMSUIOnboardingViewController
OBPrivacyLinkController
AVPlayerItem
AVPlayer
v32@?0@\"PKPass\"8Q16^B24
/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI
PKPassLibrary
Unable to find class %s
AMSUIOnboardingFeature
com.apple.AppleMediaServices
AVPlayerViewController
AVAudioSession
%@
data:image/png;base64,%@
v16@?0@\"AMSUIOnboardingViewController\"8
v8@?0
status
timeControlStatus
!
AVAudioSessionCategoryPlayback
PKPaymentPass
PKVirtualCard
%s
v12@?0B8
com.apple.AppleMediaServicesTests.FaultLogged
softlink:r:path:/System/Library/Frameworks/AVFoundation.framework/AVFoundation
softlink:r:path:/System/Library/Frameworks/AVKit.framework/AVKit
softlink:r:path:/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation
softlink:r:path:/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
softlink:r:path:/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI
softlink:r:path:/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
%{public}@: Failed to find card artwork
%{public}@: Checking for cardIcon
%{public}@: Found associated account
%{public}@: Card metadata failed for no card
%{public}@: [%{public}@] Unable to find artwork at url
%{public}@: [%{public}@] Ready to play rich notification video
%{public}@: Found %{public}@ payment passes
%{public}@: Caller did not specify a valid image size
%{public}@: Failed to obtain card artwork
%{public}@: Failed to fetch virtual card
%{public}@: Failed to fetch card icon
%{public}@: [%{public}@] Loading rich notification video
%{public}@: Found cash payment instrument
%{public}@: Found credit payment instrument
%{public}@: Attempting to search for specific card
%{public}@: Attempting to search for all cards
%{public}@: [%{public}@] Will render notification
%{public}@: didReceiveNotification: received for a notification that did not originate from an AMS
%{public}@: [%{public}@] Unable to load video at url
```
