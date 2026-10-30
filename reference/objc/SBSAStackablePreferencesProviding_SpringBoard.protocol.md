# `SBSAStackablePreferencesProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBSAPreferencesProviding`
- 0 instance variables, 2 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"<SBSAStackablePreferencesProviding>",R,W,N) parentProvider;
@property (T@"<SBSAStackablePreferencesProviding>",&,N) childProvider;
```

## Instance methods

```
-[SBSAStackablePreferencesProviding childProvider];
-[SBSAStackablePreferencesProviding descriptionForStackDepiction];
-[SBSAStackablePreferencesProviding initWithParentProvider:];
-[SBSAStackablePreferencesProviding parentProvider];
-[SBSAStackablePreferencesProviding removeFromParentProvider];
-[SBSAStackablePreferencesProviding setChildProvider:];
-[SBSAStackablePreferencesProviding stackDepiction];
```
