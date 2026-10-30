# `VTUIStringsHelper`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSDictionary" _localizedStringTable;
@"NSMutableDictionary" _languageLocalizedStringTables;
@"NSString" _siriLanguageCode;
@"NSString" _heySiriTriggerPhrase;
@"NSString" _justSiriTriggerPhrase;
```

## Properties

```
@property (T@"NSString",R,N,V_heySiriTriggerPhrase) heySiriTriggerPhrase;
@property (T@"NSString",R,N,V_justSiriTriggerPhrase) justSiriTriggerPhrase;
```

## Class methods

```
+[VTUIStringsHelper initialize];
+[VTUIStringsHelper sharedStringsHelper];
```

## Instance methods

```
-[VTUIStringsHelper localeDidChange:];
-[VTUIStringsHelper init];
-[VTUIStringsHelper setSiriLanguage:];
-[VTUIStringsHelper _siriLanguageSubstitutedString:];
-[VTUIStringsHelper _bundleStringTableForAllValidLanguages:inLocalizedStringsFileName:];
-[VTUIStringsHelper _bundleStringTableForLanguages:inLocalizedStringsFileName:];
-[VTUIStringsHelper heySiriTriggerPhrase];
-[VTUIStringsHelper justSiriTriggerPhrase];
-[VTUIStringsHelper localizedAudioStringForKey:];
-[VTUIStringsHelper setupForCurrentLocaleAndSiriLanguage];
-[VTUIStringsHelper siriLanguageStringForKey:];
-[VTUIStringsHelper uiLocalizedStringForKey:];
-[VTUIStringsHelper uiLocalizedStringForKey:languageCode:];
-[VTUIStringsHelper uiLocalizedStringForKey:usesMultipleTriggers:siriVoice:];
```
