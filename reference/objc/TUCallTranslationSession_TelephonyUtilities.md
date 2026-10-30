# `TUCallTranslationSession`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 9 instance variables, 9 properties, 25 instance methods, 1 class methods

## Instance variables

```
i _translationState;
i _translationLinks;
@"NSUUID" _UUID;
@"NSString" _callUUID;
@"NSLocale" _localLocale;
@"NSLocale" _remoteLocale;
@"NSUUID" _uplinkTranslatorIdentifier;
@"NSUUID" _downlinkTranslatorIdentifier;
@"NSUUID" _requestUUID;
```

## Properties

```
@property (Ti,N,V_translationState) translationState;
@property (T@"NSUUID",&,N,V_UUID) UUID;
@property (T@"NSUUID",&,N,V_requestUUID) requestUUID;
@property (T@"NSString",&,N,V_callUUID) callUUID;
@property (T@"NSLocale",&,N,V_localLocale) localLocale;
@property (T@"NSLocale",&,N,V_remoteLocale) remoteLocale;
@property (Ti,N,V_translationLinks) translationLinks;
@property (T@"NSUUID",&,N,V_uplinkTranslatorIdentifier) uplinkTranslatorIdentifier;
@property (T@"NSUUID",&,N,V_downlinkTranslatorIdentifier) downlinkTranslatorIdentifier;
```

## Class methods

```
+[TUCallTranslationSession supportsSecureCoding];
```

## Instance methods

```
-[TUCallTranslationSession requestUUID];
-[TUCallTranslationSession setRequestUUID:];
-[TUCallTranslationSession setUUID:];
-[TUCallTranslationSession UUID];
-[TUCallTranslationSession setCallUUID:];
-[TUCallTranslationSession callUUID];
-[TUCallTranslationSession encodeWithCoder:];
-[TUCallTranslationSession description];
-[TUCallTranslationSession initWithCoder:];
-[TUCallTranslationSession copyWithZone:];
-[TUCallTranslationSession isEqual:];
-[TUCallTranslationSession setLocalLocale:];
-[TUCallTranslationSession downlinkTranslatorIdentifier];
-[TUCallTranslationSession initWithUUID:requestUUID:state:callUUID:localLocale:remoteLocale:translationLinks:uplinkTranslatorIdentifier:downlinkTranslatorIdentifier:];
-[TUCallTranslationSession isEqualToTranslationSession:];
-[TUCallTranslationSession localLocale];
-[TUCallTranslationSession remoteLocale];
-[TUCallTranslationSession setDownlinkTranslatorIdentifier:];
-[TUCallTranslationSession setRemoteLocale:];
-[TUCallTranslationSession setTranslationLinks:];
-[TUCallTranslationSession setTranslationState:];
-[TUCallTranslationSession setUplinkTranslatorIdentifier:];
-[TUCallTranslationSession translationLinks];
-[TUCallTranslationSession translationState];
-[TUCallTranslationSession uplinkTranslatorIdentifier];
```
