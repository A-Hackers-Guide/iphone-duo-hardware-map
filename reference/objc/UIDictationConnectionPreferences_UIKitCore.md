# `UIDictationConnectionPreferences`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"AFPreferences" _afPreferences;
```

## Properties

```
@property (T@"AFPreferences",&,N,V_afPreferences) afPreferences;
```

## Class methods

```
+[UIDictationConnectionPreferences sharedInstance];
```

## Instance methods

```
-[UIDictationConnectionPreferences enableEuclidAlternatives];
-[UIDictationConnectionPreferences manualEndpointingThreshold];
-[UIDictationConnectionPreferences isSmartLanguageSelectionEnabled];
-[UIDictationConnectionPreferences isOnDeviceDictationSupportAvailableForLanguage:];
-[UIDictationConnectionPreferences suppressDataSharingOptIn];
-[UIDictationConnectionPreferences isOnDeviceDictationSupportMissingAssetForLanguage:];
-[UIDictationConnectionPreferences dictationSLSEnabledLanguages];
-[UIDictationConnectionPreferences dataSharingOptInStatus];
-[UIDictationConnectionPreferences initSingleton];
-[UIDictationConnectionPreferences languageCode];
-[UIDictationConnectionPreferences isOnDeviceEmojiRecognitionSupportAvailableForLanguage:];
-[UIDictationConnectionPreferences afPreferences];
-[UIDictationConnectionPreferences afPreferencesChanged:];
-[UIDictationConnectionPreferences suppressDictationOptIn];
-[UIDictationConnectionPreferences getOfflineDictationStatusForLanguage:];
-[UIDictationConnectionPreferences dictationIsEnabled];
-[UIDictationConnectionPreferences setAfPreferences:];
-[UIDictationConnectionPreferences ignoreServerManualEndpointingThreshold];
```
