# `SBSwitcherWindowReplacementResult`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"SBLayoutElement" _primaryElement;
@"SBLayoutElement" _sideElement;
@"SBWorkspaceEntity" _activatingEntity;
q _requestedUnlockedEnvironmentMode;
```

## Properties

```
@property (T@"SBLayoutElement",R,N,V_primaryElement) primaryElement;
@property (T@"SBLayoutElement",R,N,V_sideElement) sideElement;
@property (T@"SBWorkspaceEntity",R,N,V_activatingEntity) activatingEntity;
@property (Tq,R,N,V_requestedUnlockedEnvironmentMode) requestedUnlockedEnvironmentMode;
```

## Class methods

```
+[SBSwitcherWindowReplacementResult defaultWindowReplacementResult];
+[SBSwitcherWindowReplacementResult windowReplacementResultByRemovingLayoutElements:fromLayoutState:withPrecedingLayoutState:recentAppLayouts:windowManagementContext:];
```

## Instance methods

```
-[SBSwitcherWindowReplacementResult requestedUnlockedEnvironmentMode];
-[SBSwitcherWindowReplacementResult activatingEntity];
-[SBSwitcherWindowReplacementResult primaryElement];
-[SBSwitcherWindowReplacementResult initWithPrimaryElement:sideElement:activatingEntity:requestedUnlockedEnvironmentMode:];
-[SBSwitcherWindowReplacementResult sideElement];
```
