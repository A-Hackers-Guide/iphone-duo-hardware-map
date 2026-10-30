# `AMPUserNotificationContentViewController`

- Image: [`/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI`](../userland/System__Library__PrivateFrameworks__AMPCoreUI.framework__AMPCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 11 instance variables, 12 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _hasAppeared;
B _hasPlayedVideo;
@"AMSUserNotification" _userNotification;
@"<AMPUserNotificationContentDelegate>" _delegate;
@"NSString" _audioSessionCategory;
Q _audioSessionCategoryOptions;
@"UIImageView" _imageView;
@"AMSMetrics" _metrics;
@"UILabel" _textLabel;
@"UILabel" _titleLabel;
@"AVPlayerViewController" _videoPlayerController;
```

## Properties

```
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
```

## Instance methods

```
-[AMPUserNotificationContentViewController audioSessionCategory];
-[AMPUserNotificationContentViewController setMetrics:];
-[AMPUserNotificationContentViewController setHasAppeared:];
-[AMPUserNotificationContentViewController audioSessionCategoryOptions];
-[AMPUserNotificationContentViewController setPreferredContentSize:];
-[AMPUserNotificationContentViewController observeValueForKeyPath:ofObject:change:context:];
-[AMPUserNotificationContentViewController titleLabel];
-[AMPUserNotificationContentViewController textLabel];
-[AMPUserNotificationContentViewController hasAppeared];
-[AMPUserNotificationContentViewController videoPlayerController];
-[AMPUserNotificationContentViewController setAudioSessionCategory:];
-[AMPUserNotificationContentViewController viewWillAppear:];
-[AMPUserNotificationContentViewController setDelegate:];
-[AMPUserNotificationContentViewController loadView];
-[AMPUserNotificationContentViewController delegate];
-[AMPUserNotificationContentViewController viewWillLayoutSubviews];
-[AMPUserNotificationContentViewController metrics];
-[AMPUserNotificationContentViewController imageView];
-[AMPUserNotificationContentViewController setAudioSessionCategoryOptions:];
-[AMPUserNotificationContentViewController userNotification];
-[AMPUserNotificationContentViewController mediaPause];
-[AMPUserNotificationContentViewController expectedContentSize];
-[AMPUserNotificationContentViewController hasPlayedVideo];
-[AMPUserNotificationContentViewController initWithNotification:delegate:];
-[AMPUserNotificationContentViewController setHasPlayedVideo:];
-[AMPUserNotificationContentViewController imageViewTapped:];
```
