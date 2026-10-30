# `/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`

iOS 27.2 dyld shared cache image. Version `95.0.0.0.0`. **[DSC]**

## Linked libraries (9)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`
- `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices`
- `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`
- `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 7 classes, 3 protocols, 171 methods, 55 properties

### Class pages

Every class and protocol, with its methods: [`AuthRequestWrapper`](../objc/AuthRequestWrapper_HIDRMUI.md), [`HIDRMUIUserAuthorizationManager`](../objc/HIDRMUIUserAuthorizationManager_HIDRMUI.md), [`HIDRMUIUserAuthorizationRequest`](../objc/HIDRMUIUserAuthorizationRequest_HIDRMUI.md), [`IOThread`](../objc/IOThread_HIDRMUI.md), [`IOUserNotification`](../objc/IOUserNotification_HIDRMUI.md), [`IOUserNotificationButton`](../objc/IOUserNotificationButton_HIDRMUI.md), [`IOUserNotificationOption`](../objc/IOUserNotificationOption_HIDRMUI.md), [`NSCoding`](../objc/NSCoding_HIDRMUI.protocol.md), [`NSCopying`](../objc/NSCopying_HIDRMUI.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_HIDRMUI.protocol.md)

### Classes

`AuthRequestWrapper`, `HIDRMUIUserAuthorizationManager`, `HIDRMUIUserAuthorizationRequest`, `IOThread`, `IOUserNotification`, `IOUserNotificationButton`, `IOUserNotificationOption`

### Protocols

`NSCoding`, `NSCopying`, `NSSecureCoding`

### Properties

```
@property (class, TB,R) supportsSecureCoding;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"IOUserNotification",&,N,V_userNotification) userNotification;
@property (Tq,N,V_pairingStatus) pairingStatus;
@property (T@"NSArray",&,N,V_pairingCodeDigits) pairingCodeDigits;
@property (T@"NSMutableArray",&,N,V_pairingCodeDigitsEntered) pairingCodeDigitsEntered;
@property (TQ,N,V_pairingFailureCount) pairingFailureCount;
@property (T@"NSDate",&,N,V_characterLockoutExpirationTimestamp) characterLockoutExpirationTimestamp;
@property (T@"NSObject<OS_os_log>",R,N) log;
@property (T@"NSMutableDictionary",&,N,V_authRequests) authRequests;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_completionQueue) completionQueue;
@property (T@"NSArray",R,N) userAuthorizationRequests;
@property (TB,N,V_requiresPairing) requiresPairing;
@property (TB,N,V_requestedFromSettings) requestedFromSettings;
@property (T@"NSObject<OS_os_log>",R,N) log;
@property (T@"NSString",C,N,V_deviceName) deviceName;
@property (T@"NSRunLoop",R,N) runLoop;
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
@property (TB,N,V_selected) selected;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_title) title;
@property (TB,N,V_selected) selected;
```

## Strings (113)

```
yyyy.MM.dd_HH-mm-ss
all
2129480
v24@?0@\"NSDictionary\"8@\"NSError\"16
Skip Pairing
allow
Authorization request not found.
Pairing Failure
HIDRMUINotificationMessagePairingFailure
IOUserNotificationErrorDomain
v8@?0
ComponentName
ComponentID
IncludeDevicePrefixInTitle
\n\n[INTERNAL ONLY]\nNavigate to Settings -> Privacy & Security -> Wired Accessories to allow this accessory.
v24@?0q8@\"NSError\"16
CFUserNotificationCreate() failed! (error: %d)
settings
Unlock to approve your accessory
NO
com.apple.HIDRMUI.HIDRMUICFUNUIExtension
You can allow this accessory to control your Device in Settings.\n\nSome accessories may appear as another type of device to try to access your data or harm your Device. Only allow accessories you recognize.
View in Settings
yyyy-MM-dd HH:mm:ss
tap-to-radar
new
HID Restricted Mode (HIDRM) Issue Report\nFiled via Tap-to-Radar Button\n\nISSUE DESCRIPTION:\nWhat happened?\n\nEXPECTED BEHAVIOR:\nWhat did you expect to happen?\n\nACTUAL BEHAVIOR:\nWhat actually happened instead?\n\nSTEPS TO REPRODUCE:\
TimeOfIssue
Guidance
deviceName
<%@: %p, header: %@, message: %@, numButtons: %lu, numOptions: %lu, visible: %s>
<%@: %p, title: %@, identifier: %@, selected: %d>
Not found.
Keywords
Title
HIDRMUINotificationPairingCodeViewController
AppleHIDRM
Undefined
file-radar
Allow
1
<%@: %p, deviceName: %@, requiresPairing: %s>
HIDRMUINotificationMessage
<%@: %p, title: %@, selected: %d>
not-a-keyboard
BundleID
Pairing
HIDRMUINotificationPairingCodeDigits
don't-allow
Approve Your Accessory
Done
v24@?0@\"IOUserNotification\"8@\"NSError\"16
v32@?0@\"NSNumber\"8Q16^B24
HIDRMUINotificationMessagePairingDigitCorrect
v32@?0@\"IOUserNotificationOption\"8Q16^B24
Enter this code on the keyboard to allow it to control your Device.
File Radar
YES
HIDRMUIErrorDomain
ComponentVersion
Allow Accessory in Settings
settings-navigation://com.apple.Settings.PrivacyAndSecurity/InputAccessories
Only allow control if you trust this accessory. Malicious accessories may attempt to compromise your privacy or harm your device.
Description
requiresPairing
Invalid parameter.
1684648
[TTR] [HIDRM] 
Launching settings pane...
Starting character input lockout for %lums...
Still an instance of %@ allocated, not releasing thread! (sClassCount: %lu)
CFUserNotificationCancel() returned error (2nd): %d!
Invalid notification type! (notificationType: %ld
Error presenting user notification! (error_int: %@
Invalid character! (character: 0x%02x)
Flushed run loop!
Could not add option - maximum of 8 options allowed!
Error encoding extension items! (error: %@)
Pairing failure! (pairingCodeDigits: %@, pairingCodeDigitsEntered: %@)
Max number of pairing failures!
Not in pairing flow, ignoring input character! (character: 0x%02x)
Starting thread...
Creating CFUserNotification...
Cancelling CFUserNotification...
Error launching radar! (error: %@)
Invalid authorization request! (authorizationRequest.class: %@)
Handling input character 0x%02x... (authorizationRequest: %@)
Starting run loop...
Could not find userNotification! (userNotificationCF: %@)
Error launching settings pane! (error: %@)
Adding user authorization request... (authorizationRequest: %@)
Removing user authorization request... (authorizationRequest: %@)
Incremented class count! (sClassCount: %lu)
Decremented class count! (sClassCount: %lu)
Initializing thread...
Could not add button - maximum of 3 buttons allowed!
CFUserNotificationCancel() returned error (1st): %d!
Launching TTR... (radarURL: %@)
Input character lockout expired, clearing expiration timestamp...
Sending pairing failure notification to extension...
Sending correct digit notification to extension...
CFUserNotification already exists, ignoring...
Updating CFUserNotification...
No instances of %@ allocated, releasing thread...
_userNotificationCallback fired!
Removing all user authorization requests... (authRequests.count: %lu)
userNotification.responseReceived: %d, notificationCancelled: %d, notificationDismissed: %d
userNotification.buttons: %@
Presenting user authorization dialog...
Last instance deallocated! Setting timer for %lu seconds...
CFUserNotificationUpdate() returned error: %d!
Could not dismiss notification!
Error presenting user notification! (error: %@
```
