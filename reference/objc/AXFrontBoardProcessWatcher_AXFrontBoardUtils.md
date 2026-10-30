# `AXFrontBoardProcessWatcher`

- Image: [`/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils`](../userland/System__Library__PrivateFrameworks__AXFrontBoardUtils.framework__AXFrontBoardUtils.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBProcessManagerObserver`, `FBProcessObserver`
- 3 instance variables, 4 properties, 10 instance methods, 3 class methods

## Instance variables

```
@ _observerToken;
@"AXDispatchTimer" _appTransitionTimer;
@"NSSet" _cachedFocusedAppPIDs;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AXFrontBoardProcessWatcher accessibilitySpokenNameForProcess:];
+[AXFrontBoardProcessWatcher processForBundleIdentifier:];
+[AXFrontBoardProcessWatcher validateFocusedAppsWithEvent:];
```

## Instance methods

```
-[AXFrontBoardProcessWatcher init];
-[AXFrontBoardProcessWatcher processManager:didAddProcess:];
-[AXFrontBoardProcessWatcher process:stateDidChangeFromState:toState:];
-[AXFrontBoardProcessWatcher dealloc];
-[AXFrontBoardProcessWatcher processDidExit:];
-[AXFrontBoardProcessWatcher processManager:didRemoveProcess:];
-[AXFrontBoardProcessWatcher _processDescriptionForPID:];
-[AXFrontBoardProcessWatcher _processStateChangeIsTaskStateChangeFrom:to:];
-[AXFrontBoardProcessWatcher _processStateChangeIsVisibilityStateChangeFrom:to:];
-[AXFrontBoardProcessWatcher _validateFocusedApps:];
```
