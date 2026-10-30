# `DSErrorDescriptor`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSString" _localizedTitle;
@"NSString" _localizedMessage;
@"NSArray" _errors;
@"NSArray" _localizedAppNames;
```

## Properties

```
@property (T@"NSArray",&,N,V_errors) errors;
@property (T@"NSArray",&,N,V_localizedAppNames) localizedAppNames;
@property (T@"NSString",&,N,V_localizedTitle) localizedTitle;
@property (T@"NSString",&,N,V_localizedMessage) localizedMessage;
```

## Class methods

```
+[DSErrorDescriptor initialize];
```

## Instance methods

```
-[DSErrorDescriptor localizedTitle];
-[DSErrorDescriptor errors];
-[DSErrorDescriptor setErrors:];
-[DSErrorDescriptor localizedMessage];
-[DSErrorDescriptor setLocalizedTitle:];
-[DSErrorDescriptor setLocalizedMessage:];
-[DSErrorDescriptor localizedAppNames];
-[DSErrorDescriptor _describeErrorsWithType:];
-[DSErrorDescriptor customMessageForError:fromSource:descriptorKey:];
-[DSErrorDescriptor customMessageForError:fromSources:descriptorKey:];
-[DSErrorDescriptor descriptorKeyForDSSourceErrorCode:];
-[DSErrorDescriptor errorMessageForType:];
-[DSErrorDescriptor errorOverridesCustomTextFormatting:];
-[DSErrorDescriptor initWithFetchSharingError:];
-[DSErrorDescriptor initWithStopSharingErrors:];
-[DSErrorDescriptor isDSSourceError:];
-[DSErrorDescriptor isHomeStopSharingPINFailed:];
-[DSErrorDescriptor isStopSharingRestrictionsEnabled:];
-[DSErrorDescriptor multipleDSSourceErrorMessageWithType:withCode:];
-[DSErrorDescriptor multipleNameMessageFormatForError:];
-[DSErrorDescriptor namelessTitleForError:];
-[DSErrorDescriptor setLocalizedAppNames:];
-[DSErrorDescriptor singleDSSourceErrorMessageWithType:withCode:];
-[DSErrorDescriptor singleNameMessageFormatForError:];
-[DSErrorDescriptor singleNameTitleFormatForError:];
```
