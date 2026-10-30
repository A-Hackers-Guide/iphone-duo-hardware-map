# `AVOutputSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 3 properties, 11 instance methods, 8 class methods

## Instance variables

```
@"NSDictionary" _outputSettingsDictionary;
```

## Properties

```
@property (T@"NSSet",R,N) compatibleMediaTypes;
@property (TB,R,N) willYieldCompressedSamples;
@property (T@"NSDictionary",R,N,V_outputSettingsDictionary) outputSettingsDictionary;
```

## Class methods

```
+[AVOutputSettings registeredOutputSettingsClasses];
+[AVOutputSettings _outputSettingsWithOutputSettingsDictionary:mediaType:exceptionReason:];
+[AVOutputSettings _validateOutputSettingsDictionary:compatibilityDescription:];
+[AVOutputSettings defaultOutputSettingsForMediaType:];
+[AVOutputSettings eligibleOutputSettingsDictionaryKeys];
+[AVOutputSettings outputSettingsWithOutputSettingsDictionary:mediaType:];
+[AVOutputSettings supportsEmptyOutputSettingsDictionary];
+[AVOutputSettings validateOutputSettingsDictionary:];
```

## Instance methods

```
-[AVOutputSettings init];
-[AVOutputSettings dealloc];
-[AVOutputSettings description];
-[AVOutputSettings copyWithZone:];
-[AVOutputSettings canFullySpecifyOutputFormatReturningReason:];
-[AVOutputSettings compatibleMediaTypes];
-[AVOutputSettings encoderIsAvailableOnCurrentSystemReturningError:];
-[AVOutputSettings initWithOutputSettingsDictionary:exceptionReason:];
-[AVOutputSettings outputSettingsDictionary];
-[AVOutputSettings validateUsingOutputSettingsValidator:reason:];
-[AVOutputSettings willYieldCompressedSamples];
```
