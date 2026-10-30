# `SBStatusBarSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSSettingDescriptionProvider`, `BSDescriptionProviding`, `NSCopying`, `NSMutableCopying`
- 1 instance variables, 13 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"BSMutableSettings" _settings;
```

## Properties

```
@property (Tq,R,N,G_uiPreferredAxis) uiPreferredAxis;
@property (T@"BSSettings",R,N,G_BSSettings,V_settings) BSSettings;
@property (T@"NSNumber",R,D,N) alpha;
@property (T@"NSDictionary",R,C,D,N) partAlphas;
@property (Tq,R,D,N) style;
@property (TQ,R,D,N) hiddenParts;
@property (Tq,R,D,N) preferredAxis;
@property (T@"_UILegibilitySettings",R,D,N) legibilitySettings;
@property (T@"NSSet",R,C,D,N) backgroundActivitiesToSuppress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStatusBarSettings hiddenParts];
-[SBStatusBarSettings mutableCopyWithZone:];
-[SBStatusBarSettings _initWithBSSettings:];
-[SBStatusBarSettings succinctDescriptionBuilder];
-[SBStatusBarSettings init];
-[SBStatusBarSettings _uiPreferredAxis];
-[SBStatusBarSettings dealloc];
-[SBStatusBarSettings valueDescriptionForFlag:object:ofSetting:];
-[SBStatusBarSettings partAlphas];
-[SBStatusBarSettings preferredAxis];
-[SBStatusBarSettings keyDescriptionForSetting:];
-[SBStatusBarSettings descriptionWithMultilinePrefix:];
-[SBStatusBarSettings style];
-[SBStatusBarSettings _BSSettings];
-[SBStatusBarSettings succinctDescription];
-[SBStatusBarSettings hash];
-[SBStatusBarSettings backgroundActivitiesToSuppress];
-[SBStatusBarSettings description];
-[SBStatusBarSettings legibilitySettings];
-[SBStatusBarSettings alpha];
-[SBStatusBarSettings copyWithZone:];
-[SBStatusBarSettings isEqual:];
-[SBStatusBarSettings descriptionBuilderWithMultilinePrefix:];
```
