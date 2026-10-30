# `TUCallProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 25 instance variables, 31 properties, 78 instance methods, 1 class methods

## Instance variables

```
B _supportsCurrentPlatform;
B _supportsAudioOnly;
B _supportsAudioAndVideo;
B _supportsEmergency;
B _supportsVoicemail;
B _supportsAudioTranslation;
B _supportsRecents;
B _supportsRinging;
B _supportsDynamicSystemUI;
I _audioSessionID;
@"NSString" _identifier;
@"NSString" _localizedName;
@"NSSet" _supportedHandleTypes;
@"NSURL" _bundleURL;
@"NSString" _bundleIdentifier;
@"NSArray" _emergencyHandles;
@"NSArray" _emergencyLabeledHandles;
@"NSArray" _handoffIdentifiers;
@"NSOrderedSet" _prioritizedSenderIdentities;
@"TUSandboxExtendedURL" _sandboxExtendedRingtoneSoundURL;
@"NSURL" _originalRingtoneSoundURL;
@"NSData" _iconTemplateImageData;
Q _maximumCallGroups;
Q _maximumCallsPerCallGroup;
q _sandboxExtensionHandle;
```

## Properties

```
@property (T@"NSObject<OS_tcc_identity>",R,C,N) assumedIdentity;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSURL",C,N,V_bundleURL) bundleURL;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSSet",C,N,V_supportedHandleTypes) supportedHandleTypes;
@property (T@"NSArray",C,N,V_emergencyHandles) emergencyHandles;
@property (T@"NSArray",C,N,V_emergencyLabeledHandles) emergencyLabeledHandles;
@property (T@"NSArray",C,N,V_handoffIdentifiers) handoffIdentifiers;
@property (T@"NSOrderedSet",C,N,V_prioritizedSenderIdentities) prioritizedSenderIdentities;
@property (T@"NSURL",&,N) ringtoneSoundURL;
@property (T@"TUSandboxExtendedURL",&,N,V_sandboxExtendedRingtoneSoundURL) sandboxExtendedRingtoneSoundURL;
@property (T@"NSURL",&,N,V_originalRingtoneSoundURL) originalRingtoneSoundURL;
@property (T@"NSData",C,N,V_iconTemplateImageData) iconTemplateImageData;
@property (T@"NSString",C,N,V_localizedName) localizedName;
@property (TQ,N,V_maximumCallGroups) maximumCallGroups;
@property (TQ,N,V_maximumCallsPerCallGroup) maximumCallsPerCallGroup;
@property (TB,N,V_supportsAudioOnly) supportsAudioOnly;
@property (TB,N,V_supportsAudioAndVideo) supportsAudioAndVideo;
@property (TB,N,V_supportsEmergency) supportsEmergency;
@property (TB,N,V_supportsVoicemail) supportsVoicemail;
@property (TB,N,V_supportsRecents) supportsRecents;
@property (TB,N,V_supportsCurrentPlatform) supportsCurrentPlatform;
@property (TB,N,V_supportsRinging) supportsRinging;
@property (TB,N,V_supportsDynamicSystemUI) supportsDynamicSystemUI;
@property (TB,N,V_supportsAudioTranslation) supportsAudioTranslation;
@property (TI,N,V_audioSessionID) audioSessionID;
@property (Tq,N,V_sandboxExtensionHandle) sandboxExtensionHandle;
@property (TB,R,N,GisTelephonyProvider) telephonyProvider;
@property (TB,R,N,GisFaceTimeProvider) faceTimeProvider;
@property (TB,R,N,GisSuperboxProvider) superboxProvider;
@property (T@"TUCallProvider",R,C,N) base;
```

## Class methods

```
+[TUCallProvider supportsSecureCoding];
```

## Instance methods

```
-[TUCallProvider base];
-[TUCallProvider assumedIdentity];
-[TUCallProvider bundleURL];
-[TUCallProvider audioSessionID];
-[TUCallProvider setLocalizedName:];
-[TUCallProvider sandboxExtensionHandle];
-[TUCallProvider setAudioSessionID:];
-[TUCallProvider identifier];
-[TUCallProvider isSuperboxProvider];
-[TUCallProvider init];
-[TUCallProvider maximumCallGroups];
-[TUCallProvider ringtoneSoundURL];
-[TUCallProvider sandboxExtendedRingtoneSoundURL];
-[TUCallProvider senderIdentities];
-[TUCallProvider supportsEmergency];
-[TUCallProvider setSupportedHandleTypes:];
-[TUCallProvider setSandboxExtensionHandle:];
-[TUCallProvider senderIdentityForHandle:];
-[TUCallProvider senderIdentityForAccountUUID:];
-[TUCallProvider bundleIdentifier];
-[TUCallProvider emergencyLabeledHandles];
-[TUCallProvider displayAppBundleIdentifier];
-[TUCallProvider setSenderIdentities:];
-[TUCallProvider localizedName];
-[TUCallProvider setSupportsVoicemail:];
-[TUCallProvider isTelephonyProvider];
-[TUCallProvider setEmergencyLabeledHandles:];
-[TUCallProvider supportsAudioOnly];
-[TUCallProvider setRingtoneSoundURL:];
-[TUCallProvider supportsHandleType:];
-[TUCallProvider setMaximumCallsPerCallGroup:];
-[TUCallProvider setSupportsAudioAndVideo:];
-[TUCallProvider isEqualToCallProvider:];
-[TUCallProvider setPrioritizedSenderIdentities:];
-[TUCallProvider setIdentifier:];
-[TUCallProvider setIconTemplateImageData:];
-[TUCallProvider supportsRinging];
-[TUCallProvider supportsDynamicSystemUI];
-[TUCallProvider inCallUIBundleIdentifier];
-[TUCallProvider setHandoffIdentifiers:];
-[TUCallProvider prioritizedSenderIdentities];
-[TUCallProvider supportsAudioTranslation];
-[TUCallProvider setOriginalRingtoneSoundURL:];
-[TUCallProvider setSupportsCurrentPlatform:];
-[TUCallProvider supportsGuestModeBroadcastToDeviceType:];
-[TUCallProvider isTinCanProvider];
-[TUCallProvider supportsCurrentPlatform];
-[TUCallProvider encodeWithCoder:];
-[TUCallProvider setSandboxExtendedRingtoneSoundURL:];
-[TUCallProvider isSystemProvider];
-[TUCallProvider supportsVoicemail];
-[TUCallProvider hash];
-[TUCallProvider description];
-[TUCallProvider setSupportsAudioOnly:];
-[TUCallProvider setSupportsRecents:];
-[TUCallProvider senderIdentityForUUID:];
-[TUCallProvider initWithCoder:];
-[TUCallProvider supportsRecents];
-[TUCallProvider supportedHandleTypes];
-[TUCallProvider isFaceTimeProvider];
-[TUCallProvider hasRestrictionsInRetailEnvironment];
-[TUCallProvider setBundleIdentifier:];
-[TUCallProvider setSupportsRinging:];
-[TUCallProvider supportsAudioAndVideo];
-[TUCallProvider originalRingtoneSoundURL];
-[TUCallProvider setEmergencyHandles:];
-[TUCallProvider copyWithZone:];
-[TUCallProvider handoffIdentifiers];
-[TUCallProvider isEqual:];
-[TUCallProvider setSupportsDynamicSystemUI:];
-[TUCallProvider setSupportsAudioTranslation:];
-[TUCallProvider maximumCallsPerCallGroup];
-[TUCallProvider initWithIdentifier:];
-[TUCallProvider iconTemplateImageData];
-[TUCallProvider setBundleURL:];
-[TUCallProvider setSupportsEmergency:];
-[TUCallProvider emergencyHandles];
-[TUCallProvider setMaximumCallGroups:];
```
