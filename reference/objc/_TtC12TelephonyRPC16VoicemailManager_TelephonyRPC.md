# `_TtC12TelephonyRPC16VoicemailManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](../userland/System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- Protocols: `_FTMSMessageStoreControllerDelegate`
- 5 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
Combine.Published _$sySa -> FaceTimeMessageStore.Message ? _voicemails;
Combine.Published _$sySa -> TelephonyRPC.VoicemailManager.Account _accounts;
FaceTimeMessageStore.MessageStoreController store;
_$sSh -> Combine.AnyCancellable cancellables;
Swift.Bool needsContent;
```

## Instance methods

```
-[_TtC12TelephonyRPC16VoicemailManager messageStoreAccountInfoDidChange:];
-[_TtC12TelephonyRPC16VoicemailManager messageStoreDidAddMessages:];
-[_TtC12TelephonyRPC16VoicemailManager messageStoreDidDeleteMessages:];
-[_TtC12TelephonyRPC16VoicemailManager messageStoreDidDeleteMessagesWithUUIDs:];
-[_TtC12TelephonyRPC16VoicemailManager messageStoreDidUpdateMessages:];
```
