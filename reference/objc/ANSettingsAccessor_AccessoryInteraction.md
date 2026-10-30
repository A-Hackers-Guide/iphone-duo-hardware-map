# `ANSettingsAccessor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ANSettingsAccessorProtocol`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{__CFString=} _applicationId;
@"NSString" _userName;
@"<ANSystemUtilsProtocol>" _systemUtils;
@"NSDictionary" _profileSettings;
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
-[ANSettingsAccessor synchronize];
-[ANSettingsAccessor initialize];
-[ANSettingsAccessor dealloc];
-[ANSettingsAccessor objectForKey:];
-[ANSettingsAccessor setObject:forKey:];
-[ANSettingsAccessor initWithSystemUtils:userName:];
```
