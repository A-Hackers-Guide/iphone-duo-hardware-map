# `SBAppClipPlaceholderWorkspaceEntity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWorkspaceEntity`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _needsUpdate;
@"NSString" _bundleIdentifier;
@"NSString" _futureSceneIdentifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,C,N,V_futureSceneIdentifier) futureSceneIdentifier;
@property (TB,R,N,V_needsUpdate) needsUpdate;
```

## Class methods

```
+[SBAppClipPlaceholderWorkspaceEntity isAppClipUpdateAvailableForBundleIdentifier:];
```

## Instance methods

```
-[SBAppClipPlaceholderWorkspaceEntity needsUpdate];
-[SBAppClipPlaceholderWorkspaceEntity wantsExclusiveForeground];
-[SBAppClipPlaceholderWorkspaceEntity bundleIdentifier];
-[SBAppClipPlaceholderWorkspaceEntity supportsPresentationAtAnySize];
-[SBAppClipPlaceholderWorkspaceEntity supportedLayoutRoles];
-[SBAppClipPlaceholderWorkspaceEntity hash];
-[SBAppClipPlaceholderWorkspaceEntity entityGenerator];
-[SBAppClipPlaceholderWorkspaceEntity copyWithZone:];
-[SBAppClipPlaceholderWorkspaceEntity isEqual:];
-[SBAppClipPlaceholderWorkspaceEntity appClipPlaceholderEntity];
-[SBAppClipPlaceholderWorkspaceEntity futureSceneIdentifier];
-[SBAppClipPlaceholderWorkspaceEntity initWithBundleIdentifier:futureSceneIdentifier:needsUpdate:];
-[SBAppClipPlaceholderWorkspaceEntity isAppClipPlaceholderEntity];
```
