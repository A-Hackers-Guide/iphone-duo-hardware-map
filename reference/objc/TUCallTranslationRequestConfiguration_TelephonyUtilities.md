# `TUCallTranslationRequestConfiguration`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
i _translationLinks;
i _remoteAudioMode;
i _translationMode;
@"NSLocale" _localLocale;
@"NSLocale" _remoteLocale;
```

## Properties

```
@property (T@"NSLocale",&,N,V_localLocale) localLocale;
@property (T@"NSLocale",&,N,V_remoteLocale) remoteLocale;
@property (Ti,N,V_translationLinks) translationLinks;
@property (Ti,N,V_remoteAudioMode) remoteAudioMode;
@property (Ti,N,V_translationMode) translationMode;
```

## Class methods

```
+[TUCallTranslationRequestConfiguration supportsSecureCoding];
```

## Instance methods

```
-[TUCallTranslationRequestConfiguration encodeWithCoder:];
-[TUCallTranslationRequestConfiguration hash];
-[TUCallTranslationRequestConfiguration description];
-[TUCallTranslationRequestConfiguration initWithCoder:];
-[TUCallTranslationRequestConfiguration copyWithZone:];
-[TUCallTranslationRequestConfiguration isEqual:];
-[TUCallTranslationRequestConfiguration remoteAudioMode];
-[TUCallTranslationRequestConfiguration setLocalLocale:];
-[TUCallTranslationRequestConfiguration translationMode];
-[TUCallTranslationRequestConfiguration initWithlocalLocale:remoteLocale:translationLinks:remoteAudioMode:translationMode:];
-[TUCallTranslationRequestConfiguration isEqualToTUCallTranslationRequestConfiguration:];
-[TUCallTranslationRequestConfiguration localLocale];
-[TUCallTranslationRequestConfiguration remoteLocale];
-[TUCallTranslationRequestConfiguration setRemoteAudioMode:];
-[TUCallTranslationRequestConfiguration setRemoteLocale:];
-[TUCallTranslationRequestConfiguration setTranslationLinks:];
-[TUCallTranslationRequestConfiguration setTranslationMode:];
-[TUCallTranslationRequestConfiguration translationLinks];
```
