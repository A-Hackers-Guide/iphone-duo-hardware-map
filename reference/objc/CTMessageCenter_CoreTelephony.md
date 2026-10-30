# `CTMessageCenter`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 38 instance methods, 1 class methods

## Class methods

```
+[CTMessageCenter sharedMessageCenter];
```

## Instance methods

```
-[CTMessageCenter isMmsEnabled];
-[CTMessageCenter send:withMoreToFollow:];
-[CTMessageCenter init];
-[CTMessageCenter send:];
-[CTMessageCenter allIncomingMessages];
-[CTMessageCenter emergencySessionIntentEnd:];
-[CTMessageCenter dealloc];
-[CTMessageCenter sendSMSWithText:serviceCenter:toAddress:trackingID:];
-[CTMessageCenter sendSMSWithText:text:serviceCenter:toAddress:withID:];
-[CTMessageCenter setDeliveryReportsEnabled:];
-[CTMessageCenter simulateSmsReceived:];
-[CTMessageCenter isDeliveryReportsEnabled:];
-[CTMessageCenter sendSMSWithText:serviceCenter:toAddress:];
-[CTMessageCenter addMessageOfType:toArray:withIdsFromArray:];
-[CTMessageCenter sendSMSWithText:serviceCenter:toAddress:withMoreToFollow:withID:];
-[CTMessageCenter encodeMessage:];
-[CTMessageCenter sendSMSWithText:text:serviceCenter:toAddress:withMoreToFollow:withID:];
-[CTMessageCenter decodeMessage:];
-[CTMessageCenter sendSMSWithText:text:serviceCenter:toAddress:trackingID:];
-[CTMessageCenter isMmsEnabledForSub:];
-[CTMessageCenter isMmsConfiguredForSub:];
-[CTMessageCenter incomingMessageWithId:];
-[CTMessageCenter emergencySessionIntentStart:];
-[CTMessageCenter getCharacterCountForSub:count:andMessageSplitThreshold:forSmsText:];
-[CTMessageCenter sendSMSWithText:text:serviceCenter:toAddress:];
-[CTMessageCenter isMmsConfigured];
-[CTMessageCenter sendSMSWithText:serviceCenter:toAddress:withID:];
-[CTMessageCenter incomingMessageCount];
-[CTMessageCenter isMmsEnabledForSub:enabled:];
-[CTMessageCenter sendMMSFromData:messageId:subSlot:];
-[CTMessageCenter sendMMS:];
-[CTMessageCenter acknowledgeOutgoingMessageWithId:];
-[CTMessageCenter sendMessageAsSmsToShortCodeRecipients:andReplaceData:];
-[CTMessageCenter sendSMS:withMoreToFollow:trackingID:];
-[CTMessageCenter simulateDeferredMessage];
-[CTMessageCenter acknowledgeIncomingMessageWithId:];
-[CTMessageCenter sendBinarySMS:trackingID:];
-[CTMessageCenter getCharacterCount:andMessageSplitThreshold:forSmsText:];
```
