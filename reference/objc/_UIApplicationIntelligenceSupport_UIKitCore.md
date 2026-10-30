# `_UIApplicationIntelligenceSupport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 6 instance methods, 5 class methods

## Instance variables

```
collector;
exportableDataHandler;
q applicationState;
```

## Properties

```
@property (Tq,N,VapplicationState) applicationState;
@property (TB,N,R) isExcludedApplication;
```

## Class methods

```
+[_UIApplicationIntelligenceSupport sharedInstance];
+[_UIApplicationIntelligenceSupport collectRemoteContentForRootViews:withRemoteContextWrapper:];
+[_UIApplicationIntelligenceSupport collectRemoteContent:inVisibleRect:withRemoteContextWrapper:];
+[_UIApplicationIntelligenceSupport remoteContextWrapperClass];
+[_UIApplicationIntelligenceSupport collectRemoteContentForWindowHostingScene:inVisibleRect:withRemoteContextWrapper:];
```

## Instance methods

```
-[_UIApplicationIntelligenceSupport applicationState];
-[_UIApplicationIntelligenceSupport init];
-[_UIApplicationIntelligenceSupport setApplicationState:];
-[_UIApplicationIntelligenceSupport isExcludedApplication];
-[_UIApplicationIntelligenceSupport sceneProtectionStateChanged];
-[_UIApplicationIntelligenceSupport connectedScenesUpdated];
```
