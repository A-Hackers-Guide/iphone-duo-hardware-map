# `SBAppInteractionEventSourceManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAppInteractionEventSourceObserving`, `SBAppInteractionEventSourceProviding`, `SBWindowSceneAttachmentObserving`
- 3 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"NSMapTable" _windowScenesToEventSources;
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"NSMapTable",R,N,V_windowScenesToEventSources) windowScenesToEventSources;
@property (T@"NSHashTable",R,N,V_observers) observers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAppInteractionEventSourceManager sharedInstance];
```

## Instance methods

```
-[SBAppInteractionEventSourceManager eventSource:userTouchedApplication:];
-[SBAppInteractionEventSourceManager removeObserver:];
-[SBAppInteractionEventSourceManager windowSceneDidDisconnect:];
-[SBAppInteractionEventSourceManager initWithApplicationController:];
-[SBAppInteractionEventSourceManager addObserver:];
-[SBAppInteractionEventSourceManager observers];
-[SBAppInteractionEventSourceManager windowSceneDidConnect:];
-[SBAppInteractionEventSourceManager eventSource:userDeletedWebBookmark:];
-[SBAppInteractionEventSourceManager eventSource:applicationsBecameHidden:];
-[SBAppInteractionEventSourceManager eventSource:applicationsBecameVisible:];
-[SBAppInteractionEventSourceManager eventSource:didBeginTransitionToMode:withLayoutState:activatingElement:triggeredBy:];
-[SBAppInteractionEventSourceManager eventSource:didFinishTransitionToMode:withLayoutState:activatingElement:triggeredBy:];
-[SBAppInteractionEventSourceManager eventSource:keyboardFocusChangedToApplication:];
-[SBAppInteractionEventSourceManager eventSource:userDeletedApplications:];
-[SBAppInteractionEventSourceManager eventSource:userQuitApplicationInSwitcher:];
-[SBAppInteractionEventSourceManager eventSource:userRemovedSuggestions:];
-[SBAppInteractionEventSourceManager eventSource:userTouchedApplication:pid:inContext:];
-[SBAppInteractionEventSourceManager eventSourceForWindowScene:];
-[SBAppInteractionEventSourceManager windowScenesToEventSources];
```
