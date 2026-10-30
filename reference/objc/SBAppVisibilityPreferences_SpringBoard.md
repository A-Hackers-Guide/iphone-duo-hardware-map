# `SBAppVisibilityPreferences`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleID;
@"NSString" _containerPath;
B _defaultVisible;
B _currentlyVisible;
```

## Properties

```
@property (TB,R,GisDefaultVisible,V_defaultVisible) defaultVisible;
@property (TB,R,GisCurrentlyVisible) currentlyVisible;
```

## Instance methods

```
-[SBAppVisibilityPreferences update];
-[SBAppVisibilityPreferences description];
-[SBAppVisibilityPreferences initWithDefaultVisible:bundleID:containerPath:];
-[SBAppVisibilityPreferences isCurrentlyVisible];
-[SBAppVisibilityPreferences isDefaultVisible];
```
