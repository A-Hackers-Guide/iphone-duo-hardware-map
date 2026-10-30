# `SBExternalDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractDefaults`
- 12 instance variables, 11 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"SBExternalGlobalDefaults" _lazy_globalDefaults;
@"SBExternalDuetDefaults" _lazy_duetDefaults;
@"SBExternalDemoDefaults" _lazy_demoDefaults;
@"SBExternalSetupDefaults" _lazy_setupDefaults;
@"SBExternalSettingsDefaults" _lazy_settingsDefaults;
@"SBExternalPhoneDefaults" _lazy_phoneDefaults;
@"SBExternalWifiDefaults" _lazy_networkDefaults;
@"SBExternalSoundsDefaults" _lazy_soundDefaults;
@"SBExternalNotesDefaults" _lazy_notesDefaults;
@"SBBiometricKitDefaults" _lazy_biometricKitDefaults;
@"SBExternalChronoDefaults" _lazy_chronoDefaults;
@"SBExternalChronoDefaults" _chronoDefaults;
```

## Properties

```
@property (T@"SBExternalGlobalDefaults",R,&,N) globalDefaults;
@property (T@"SBExternalDuetDefaults",R,&,N) duetDefaults;
@property (T@"SBExternalDemoDefaults",R,&,N) demoDefaults;
@property (T@"SBExternalSetupDefaults",R,&,N) setupDefaults;
@property (T@"SBExternalSettingsDefaults",R,&,N) settingsDefaults;
@property (T@"SBExternalPhoneDefaults",R,&,N) phoneDefaults;
@property (T@"SBExternalWifiDefaults",R,&,N) networkDefaults;
@property (T@"SBExternalSoundsDefaults",R,&,N) soundDefaults;
@property (T@"SBExternalNotesDefaults",R,&,N) notesDefaults;
@property (T@"SBBiometricKitDefaults",R,&,N) biometricKitDefaults;
@property (T@"SBExternalChronoDefaults",R,&,N,V_chronoDefaults) chronoDefaults;
```

## Class methods

```
+[SBExternalDefaults chronoDefaults];
```

## Instance methods

```
-[SBExternalDefaults setupDefaults];
-[SBExternalDefaults demoDefaults];
-[SBExternalDefaults soundDefaults];
-[SBExternalDefaults networkDefaults];
-[SBExternalDefaults biometricKitDefaults];
-[SBExternalDefaults chronoDefaults];
-[SBExternalDefaults duetDefaults];
-[SBExternalDefaults globalDefaults];
-[SBExternalDefaults notesDefaults];
-[SBExternalDefaults phoneDefaults];
-[SBExternalDefaults settingsDefaults];
```
