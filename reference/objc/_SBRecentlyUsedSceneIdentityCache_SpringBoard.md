# `_SBRecentlyUsedSceneIdentityCache`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSCopying`
- 2 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _recentSceneIdentityTokensByPID;
@"NSMutableOrderedSet" _recentPIDs;
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
-[_SBRecentlyUsedSceneIdentityCache init];
-[_SBRecentlyUsedSceneIdentityCache appendDescriptionToFormatter:];
-[_SBRecentlyUsedSceneIdentityCache description];
-[_SBRecentlyUsedSceneIdentityCache copyWithZone:];
-[_SBRecentlyUsedSceneIdentityCache isEqual:];
-[_SBRecentlyUsedSceneIdentityCache addSceneIdentityToken:forPID:];
-[_SBRecentlyUsedSceneIdentityCache promoteContainedSceneIdentityToken:forPID:];
-[_SBRecentlyUsedSceneIdentityCache removeSceneIdentityToken:forPID:];
```
