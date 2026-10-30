# `FBSSetting`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSMutableSetting_Internal`, `FBSSetting`
- 20 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
# _settingsClass;
B _lock_initialized;
B _local;
B _legacy;
c _type;
B _isBSSettings;
B _redacted;
B _volatile;
B _propagating;
B _nullPreserving;
@"NSString" _name;
Q _setting;
Q _legacySetting;
# _extension;
@"NSString" _extensionID;
# _expectedClass;
q _specialCollection;
@ _defaultValue;
@? _descriptionProvider;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSSetting setDefaultValue:];
-[FBSSetting setVolatile:];
-[FBSSetting indirect_name];
-[FBSSetting indirect_legacySetting];
-[FBSSetting indirect_isPropagating];
-[FBSSetting indirect_defaultValue];
-[FBSSetting indirect_isLegacy];
-[FBSSetting setDescriptionProvider:];
-[FBSSetting setPropagating:];
-[FBSSetting matchesProperty:];
-[FBSSetting hash];
-[FBSSetting description];
-[FBSSetting _finishInitializing];
-[FBSSetting setPrivacySensitive:];
-[FBSSetting isEqual:];
-[FBSSetting setNullPreserving:];
-[FBSSetting matchesPropertyName:];
```
