# `TUCallTranslationStartRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUCallTranslationRequest`
- 5 instance variables, 5 properties, 19 instance methods, 1 class methods

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
+[TUCallTranslationStartRequest supportsSecureCoding];
```

## Instance methods

```
-[TUCallTranslationStartRequest encodeWithCoder:];
-[TUCallTranslationStartRequest hash];
-[TUCallTranslationStartRequest description];
-[TUCallTranslationStartRequest initWithCoder:];
-[TUCallTranslationStartRequest copyWithZone:];
-[TUCallTranslationStartRequest isEqual:];
-[TUCallTranslationStartRequest remoteAudioMode];
-[TUCallTranslationStartRequest setLocalLocale:];
-[TUCallTranslationStartRequest translationMode];
-[TUCallTranslationStartRequest initWithCall:configuration:];
-[TUCallTranslationStartRequest initWithCall:localLocale:remoteLocale:translationLinks:remoteAudioMode:translationMode:];
-[TUCallTranslationStartRequest isEqualToTUCallTranslationStartRequest:];
-[TUCallTranslationStartRequest localLocale];
-[TUCallTranslationStartRequest remoteLocale];
-[TUCallTranslationStartRequest setRemoteAudioMode:];
-[TUCallTranslationStartRequest setRemoteLocale:];
-[TUCallTranslationStartRequest setTranslationLinks:];
-[TUCallTranslationStartRequest setTranslationMode:];
-[TUCallTranslationStartRequest translationLinks];
```
