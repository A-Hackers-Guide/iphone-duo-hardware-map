# `IOUserNotification`

- Image: [`/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`](../userland/System__Library__PrivateFrameworks__HIDRMUI.framework__HIDRMUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 31 instance variables, 33 properties, 80 instance methods, 4 class methods

## Instance variables

```
B _shouldDisplayOnTop;
B _shouldPresentViaSystemAperture;
B _shouldDismissOnLock;
B _shouldDismissOnUnlock;
B _shouldAllowLockScreenDismissal;
B _shouldIgnoreQuietMode;
B _shouldHideOnMirroredDisplay;
B _noDefaultButton;
B _useRadioOptions;
B _visible;
B _responseReceived;
B _notificationCancelled;
B _notificationDismissed;
@? _responseHandler;
d _timeout;
Q _notificationLevel;
@"NSString" _header;
@"NSString" _message;
@"NSURL" _iconURL;
@"NSDictionary" _iconConfiguration;
@"NSString" _lockScreenHeader;
@"NSString" _lockScreenMessage;
@"NSNumber" _systemSoundID;
@"NSString" _extensionIdentifier;
@"NSArray" _extensionItems;
@"NSDictionary" _additionalConfiguration;
Q _updateCount;
@"NSObject<OS_dispatch_queue>" _queue;
@"IOThread" _thread;
@"NSMutableArray" _buttonsMutable;
@"NSMutableArray" _optionsMutable;
```

## Properties

```
@property (TB,N,GisVisible,V_visible) visible;
@property (TQ,N,V_updateCount) updateCount;
@property (TB,N,V_responseReceived) responseReceived;
@property (TB,N,V_notificationCancelled) notificationCancelled;
@property (TB,N,V_notificationDismissed) notificationDismissed;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"IOThread",&,N,V_thread) thread;
@property (T@"NSMutableArray",&,N,V_buttonsMutable) buttonsMutable;
@property (T@"NSMutableArray",&,N,V_optionsMutable) optionsMutable;
@property (T@?,C,N,V_responseHandler) responseHandler;
@property (Td,N,V_timeout) timeout;
@property (TQ,N,V_notificationLevel) notificationLevel;
@property (TB,N,V_shouldDisplayOnTop) shouldDisplayOnTop;
@property (T@"NSString",C,N,V_header) header;
@property (T@"NSString",C,N,V_message) message;
@property (T@"NSURL",C,N,V_iconURL) iconURL;
@property (T@"NSDictionary",C,N,V_iconConfiguration) iconConfiguration;
@property (T@"NSString",C,N,V_lockScreenHeader) lockScreenHeader;
@property (T@"NSString",C,N,V_lockScreenMessage) lockScreenMessage;
@property (TB,N,V_shouldPresentViaSystemAperture) shouldPresentViaSystemAperture;
@property (TB,N,V_shouldDismissOnLock) shouldDismissOnLock;
@property (TB,N,V_shouldDismissOnUnlock) shouldDismissOnUnlock;
@property (TB,N,V_shouldAllowLockScreenDismissal) shouldAllowLockScreenDismissal;
@property (TB,N,V_shouldIgnoreQuietMode) shouldIgnoreQuietMode;
@property (TB,N,V_shouldHideOnMirroredDisplay) shouldHideOnMirroredDisplay;
@property (T@"NSNumber",C,N,V_systemSoundID) systemSoundID;
@property (T@"NSString",C,N,V_extensionIdentifier) extensionIdentifier;
@property (T@"NSArray",C,N,V_extensionItems) extensionItems;
@property (TB,N,V_noDefaultButton) noDefaultButton;
@property (TB,N,V_useRadioOptions) useRadioOptions;
@property (T@"NSDictionary",C,N,V_additionalConfiguration) additionalConfiguration;
@property (T@"NSArray",R,N) buttons;
@property (T@"NSArray",R,N) options;
```

## Class methods

```
+[IOUserNotification _findCFUserNotificationForUserNotification:];
+[IOUserNotification _notificationMapTable];
+[IOUserNotification _notificationMapTableLock];
+[IOUserNotification notificationWithHeader:andMessage:];
```

## Instance methods

```
-[IOUserNotification buttons];
-[IOUserNotification header];
-[IOUserNotification setSystemSoundID:];
-[IOUserNotification systemSoundID];
-[IOUserNotification setExtensionIdentifier:];
-[IOUserNotification setHeader:];
-[IOUserNotification setMessage:];
-[IOUserNotification setVisible:];
-[IOUserNotification responseHandler];
-[IOUserNotification extensionIdentifier];
-[IOUserNotification init];
-[IOUserNotification message];
-[IOUserNotification setThread:];
-[IOUserNotification setResponseHandler:];
-[IOUserNotification dealloc];
-[IOUserNotification isVisible];
-[IOUserNotification thread];
-[IOUserNotification queue];
-[IOUserNotification updateCount];
-[IOUserNotification timeout];
-[IOUserNotification setIconURL:];
-[IOUserNotification setTimeout:];
-[IOUserNotification iconURL];
-[IOUserNotification description];
-[IOUserNotification updateNotification];
-[IOUserNotification options];
-[IOUserNotification setQueue:];
-[IOUserNotification addButtonWithTitle:];
-[IOUserNotification additionalConfiguration];
-[IOUserNotification responseReceived];
-[IOUserNotification extensionItems];
-[IOUserNotification setResponseReceived:];
-[IOUserNotification dismissNotification];
-[IOUserNotification setUpdateCount:];
-[IOUserNotification setExtensionItems:];
-[IOUserNotification _addButton:];
-[IOUserNotification notificationLevel];
-[IOUserNotification setNotificationLevel:];
-[IOUserNotification noDefaultButton];
-[IOUserNotification setNoDefaultButton:];
-[IOUserNotification iconConfiguration];
-[IOUserNotification lockScreenMessage];
-[IOUserNotification setIconConfiguration:];
-[IOUserNotification setLockScreenMessage:];
-[IOUserNotification setShouldHideOnMirroredDisplay:];
-[IOUserNotification useRadioOptions];
-[IOUserNotification _addOption:];
-[IOUserNotification _userNotificationDictionary];
-[IOUserNotification _userNotificationOptionFlags];
-[IOUserNotification addButtonWithTitle:andIdentifier:];
-[IOUserNotification addOptionWithTitle:selected:];
-[IOUserNotification buttonsMutable];
-[IOUserNotification hasSelectedButtonWithIdentifier:];
-[IOUserNotification initWithHeader:andMessage:];
-[IOUserNotification lockScreenHeader];
-[IOUserNotification notificationCancelled];
-[IOUserNotification notificationDismissed];
-[IOUserNotification optionsMutable];
-[IOUserNotification presentNotification];
-[IOUserNotification presentNotificationWithResponseHandler:];
-[IOUserNotification setAdditionalConfiguration:];
-[IOUserNotification setButtonsMutable:];
-[IOUserNotification setLockScreenHeader:];
-[IOUserNotification setNotificationCancelled:];
-[IOUserNotification setNotificationDismissed:];
-[IOUserNotification setOptionsMutable:];
-[IOUserNotification setShouldAllowLockScreenDismissal:];
-[IOUserNotification setShouldDismissOnLock:];
-[IOUserNotification setShouldDismissOnUnlock:];
-[IOUserNotification setShouldDisplayOnTop:];
-[IOUserNotification setShouldIgnoreQuietMode:];
-[IOUserNotification setShouldPresentViaSystemAperture:];
-[IOUserNotification setUseRadioOptions:];
-[IOUserNotification shouldAllowLockScreenDismissal];
-[IOUserNotification shouldDismissOnLock];
-[IOUserNotification shouldDismissOnUnlock];
-[IOUserNotification shouldDisplayOnTop];
-[IOUserNotification shouldHideOnMirroredDisplay];
-[IOUserNotification shouldIgnoreQuietMode];
-[IOUserNotification shouldPresentViaSystemAperture];
```
