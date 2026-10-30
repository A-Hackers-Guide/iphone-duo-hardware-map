# `AVMediaFileOutputSettingsValidator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVOutputSettingsValidation`
- 1 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"AVMediaFileType" _fileType;
```

## Properties

```
@property (T@"AVMediaFileType",R,N) fileType;
```

## Class methods

```
+[AVMediaFileOutputSettingsValidator initialize];
+[AVMediaFileOutputSettingsValidator mediaFileOutputSettingsValidatorForFileType:];
```

## Instance methods

```
-[AVMediaFileOutputSettingsValidator init];
-[AVMediaFileOutputSettingsValidator dealloc];
-[AVMediaFileOutputSettingsValidator fileType];
-[AVMediaFileOutputSettingsValidator initWithFileType:];
-[AVMediaFileOutputSettingsValidator validateAudioOutputSettings:reason:];
-[AVMediaFileOutputSettingsValidator validateVideoOutputSettings:reason:];
```
