# `TUPrivacyManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 1 properties, 14 instance methods, 1 class methods

## Properties

```
@property (T@"NSArray",R,C,N) privacyRules;
```

## Class methods

```
+[TUPrivacyManager sharedPrivacyManager];
```

## Instance methods

```
-[TUPrivacyManager init];
-[TUPrivacyManager dealloc];
-[TUPrivacyManager _handleBlockListChanged:];
-[TUPrivacyManager addRule:];
-[TUPrivacyManager allBlacklistRules];
-[TUPrivacyManager isIncomingCommunicationBlockedForBusinessID:];
-[TUPrivacyManager isIncomingCommunicationBlockedForEmailAddress:];
-[TUPrivacyManager isIncomingCommunicationBlockedForHandle:];
-[TUPrivacyManager isIncomingCommunicationBlockedForPhoneNumber:];
-[TUPrivacyManager privacyRules];
-[TUPrivacyManager removeRule:];
-[TUPrivacyManager setBlockIncomingCommunication:forBusinessID:];
-[TUPrivacyManager setBlockIncomingCommunication:forEmailAddress:];
-[TUPrivacyManager setBlockIncomingCommunication:forPhoneNumber:];
```
