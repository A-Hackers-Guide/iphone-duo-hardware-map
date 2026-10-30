# `FBSSceneClientSettingsCore`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSCoreSettingsExtension`
- Protocols: `FBSSceneClientSettings`
- 0 instance variables, 5 properties, 10 instance methods, 3 class methods

## Properties

```
@property (T@"BSKeyedSettings",&,N) layers;
@property (Td,N) preferredLevel;
@property (Tq,N) preferredInterfaceOrientation;
@property (T@"NSString",C,N) preferredSceneHostIdentifier;
@property (T@"FBSSceneIdentityToken",C,N) preferredSceneHostIdentity;
```

## Class methods

```
+[FBSSceneClientSettingsCore protocol];
+[FBSSceneClientSettingsCore descriptionOfValue:forSetting:];
+[FBSSceneClientSettingsCore configureSetting:];
```

## Instance methods

```
-[FBSSceneClientSettingsCore layers];
-[FBSSceneClientSettingsCore preferredInterfaceOrientation];
-[FBSSceneClientSettingsCore setPreferredInterfaceOrientation:];
-[FBSSceneClientSettingsCore setLayers:];
-[FBSSceneClientSettingsCore preferredSceneHostIdentity];
-[FBSSceneClientSettingsCore preferredLevel];
-[FBSSceneClientSettingsCore preferredSceneHostIdentifier];
-[FBSSceneClientSettingsCore setPreferredLevel:];
-[FBSSceneClientSettingsCore setPreferredSceneHostIdentifier:];
-[FBSSceneClientSettingsCore setPreferredSceneHostIdentity:];
```
