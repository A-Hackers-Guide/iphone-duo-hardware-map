# `SSRVoiceProfileLoader`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 5 class methods

## Instance variables

```
@"NSString" _locale;
@"NSString" _personaId;
@"NSString" _siriSharedUserId;
```

## Properties

```
@property (T@"NSString",&,N,V_locale) locale;
@property (T@"NSString",&,N,V_personaId) personaId;
@property (T@"NSString",&,N,V_siriSharedUserId) siriSharedUserId;
```

## Class methods

```
+[SSRVoiceProfileLoader getActivePersonaIds];
+[SSRVoiceProfileLoader getActiveSiriSharedUserIds];
+[SSRVoiceProfileLoader getVoiceProfileWithLocale:];
+[SSRVoiceProfileLoader getVoiceProfileWithLocale:userSiriProfileId:];
+[SSRVoiceProfileLoader getVoiceProfileWithVoiceProfileId:];
```

## Instance methods

```
-[SSRVoiceProfileLoader initWithLocale:];
-[SSRVoiceProfileLoader setLocale:];
-[SSRVoiceProfileLoader setPersonaId:];
-[SSRVoiceProfileLoader locale];
-[SSRVoiceProfileLoader personaId];
-[SSRVoiceProfileLoader userProfileIdentifier];
-[SSRVoiceProfileLoader getVoiceProfile];
-[SSRVoiceProfileLoader initWithLocale:siriSharedUserId:];
-[SSRVoiceProfileLoader setSiriSharedUserId:];
-[SSRVoiceProfileLoader siriSharedUserId];
```
