# `SBSwitcherWindowManagementContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
Q _hash;
B _automaticStageCreationEnabled;
B _restoresPreviouslyOpenWindows;
Q _baseStyle;
```

## Properties

```
@property (TQ,R,N,V_baseStyle) baseStyle;
@property (TB,R,N,GisAutomaticStageCreationEnabled,V_automaticStageCreationEnabled) automaticStageCreationEnabled;
@property (TB,R,N,V_restoresPreviouslyOpenWindows) restoresPreviouslyOpenWindows;
@property (TB,R,N,GisFlexibleWindowingEnabled) flexibleWindowingEnabled;
@property (TB,R,N,GisButterflyEnabled) butterflyEnabled;
```

## Class methods

```
+[SBSwitcherWindowManagementContext singleAppContext];
```

## Instance methods

```
-[SBSwitcherWindowManagementContext hash];
-[SBSwitcherWindowManagementContext description];
-[SBSwitcherWindowManagementContext appendDescriptionToStream:];
-[SBSwitcherWindowManagementContext isFlexibleWindowingEnabled];
-[SBSwitcherWindowManagementContext isEqual:];
-[SBSwitcherWindowManagementContext baseStyle];
-[SBSwitcherWindowManagementContext isAutomaticStageCreationEnabled];
-[SBSwitcherWindowManagementContext _multitaskingMode];
-[SBSwitcherWindowManagementContext biomeStageManagerMode];
-[SBSwitcherWindowManagementContext initWithBaseStyle:automaticStageCreationEnabled:restoresPreviouslyOpenWindows:];
-[SBSwitcherWindowManagementContext isButterflyEnabled];
-[SBSwitcherWindowManagementContext restoresPreviouslyOpenWindows];
-[SBSwitcherWindowManagementContext telemetryMultitaskingMode];
```
