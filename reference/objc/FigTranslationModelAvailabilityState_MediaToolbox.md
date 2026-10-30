# `FigTranslationModelAvailabilityState`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _isLanguageObservationComplete;
B _isProcessAllowedToListen;
@"_LTLanguageStatus" _languageStatusListener;
^{__CFDictionary=} _sourceToTargetLanguagesDictionary;
@"NSSet" _installedLocales;
@"NSLock" _stateLock;
q _lastListenerCreationTime_ns;
```

## Properties

```
@property (T@"_LTLanguageStatus",&,N,V_languageStatusListener) languageStatusListener;
@property (T^{__CFDictionary=},N,V_sourceToTargetLanguagesDictionary) sourceToTargetLanguagesDictionary;
@property (T@"NSSet",&,N,V_installedLocales) installedLocales;
@property (T@"NSLock",&,N,V_stateLock) stateLock;
@property (TB,N,V_isLanguageObservationComplete) isLanguageObservationComplete;
@property (TB,N,V_isProcessAllowedToListen) isProcessAllowedToListen;
@property (Tq,R,N,V_lastListenerCreationTime_ns) lastListenerCreationTime_ns;
```

## Class methods

```
+[FigTranslationModelAvailabilityState sharedInstance];
```

## Instance methods

```
-[FigTranslationModelAvailabilityState stateLock];
-[FigTranslationModelAvailabilityState setStateLock:];
-[FigTranslationModelAvailabilityState init];
-[FigTranslationModelAvailabilityState dealloc];
-[FigTranslationModelAvailabilityState copySourceToTargetLanguagesDictionary];
-[FigTranslationModelAvailabilityState installedLocales];
-[FigTranslationModelAvailabilityState isLanguageObservationComplete];
-[FigTranslationModelAvailabilityState isProcessAllowedToListen];
-[FigTranslationModelAvailabilityState languageStatusListener];
-[FigTranslationModelAvailabilityState lastListenerCreationTime_ns];
-[FigTranslationModelAvailabilityState setInstalledLocales:];
-[FigTranslationModelAvailabilityState setIsLanguageObservationComplete:];
-[FigTranslationModelAvailabilityState setIsProcessAllowedToListen:];
-[FigTranslationModelAvailabilityState setLanguageStatusListener:];
-[FigTranslationModelAvailabilityState setSourceToTargetLanguagesDictionary:];
-[FigTranslationModelAvailabilityState sourceToTargetLanguagesDictionary];
```
