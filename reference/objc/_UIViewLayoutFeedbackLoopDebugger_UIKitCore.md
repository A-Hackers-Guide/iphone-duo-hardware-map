# `_UIViewLayoutFeedbackLoopDebugger`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 1 properties, 29 instance methods, 3 class methods

## Instance variables

```
q _debuggingState;
@"UIView" _rootView;
@"NSMutableSet" _viewsWithChangingGeometry;
@"NSMutableSet" _viewsWithVariableChangesTriggeringLayout;
@"NSMutableSet" _turningPointViews;
@"NSMutableSet" _involvedViews;
@"NSMutableArray" _layoutList;
@"NSArray" _reducedLayoutList;
B _rootViewConfirmed;
B _feedbackLoopConfirmed;
q _rootViewLayoutCount;
q _infoCollectionLayoutCount;
@"UIView" _currentLayoutView;
```

## Properties

```
@property (T@"UIView",&,N,V_currentLayoutView) currentLayoutView;
```

## Class methods

```
+[_UIViewLayoutFeedbackLoopDebugger layoutFeedbackLoopDebugger];
+[_UIViewLayoutFeedbackLoopDebugger destroyLayoutFeedbackLoopDebuggerForUnitTests];
+[_UIViewLayoutFeedbackLoopDebugger createLayoutFeedbackLoopDebuggerForUnitTests];
```

## Instance methods

```
-[_UIViewLayoutFeedbackLoopDebugger description];
-[_UIViewLayoutFeedbackLoopDebugger willSendSetFrame:toLayerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger didUpdateSafeAreaInsets:ofView:];
-[_UIViewLayoutFeedbackLoopDebugger _recordSetNeedsLayoutToLayerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger currentLayoutView];
-[_UIViewLayoutFeedbackLoopDebugger didEnterLayoutSublayersOfLayerForView:];
-[_UIViewLayoutFeedbackLoopDebugger didSendLayoutSubviewsToView:];
-[_UIViewLayoutFeedbackLoopDebugger didSendSetNeedsLayoutToLayerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger didSendViewDidLayoutSubviewsToViewControllerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger didSendViewWillLayoutSubviewsToViewControllerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger didUpdateLayoutMargins:ofView:];
-[_UIViewLayoutFeedbackLoopDebugger dumpInfoWithInfoCollectionSuccess:];
-[_UIViewLayoutFeedbackLoopDebugger dumpInfoWithInfoCollectionSuccess:informationBounded:];
-[_UIViewLayoutFeedbackLoopDebugger resumeCounting];
-[_UIViewLayoutFeedbackLoopDebugger setCurrentLayoutView:];
-[_UIViewLayoutFeedbackLoopDebugger topLevelViewHierarchyTrace];
-[_UIViewLayoutFeedbackLoopDebugger turningPointViewsCreateIfNecessary];
-[_UIViewLayoutFeedbackLoopDebugger viewsWithChangingGeometryCreateIfNecessary];
-[_UIViewLayoutFeedbackLoopDebugger viewsWithVariableChangesTriggeringLayoutCreateIfNecessary];
-[_UIViewLayoutFeedbackLoopDebugger willChangeGeometryForLayerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger willExitLayoutSublayersOfLayerForView:];
-[_UIViewLayoutFeedbackLoopDebugger willSendLayoutSubviewsToView:];
-[_UIViewLayoutFeedbackLoopDebugger willSendSetAnchorPoint:toLayerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger willSendSetBounds:toLayerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger willSendSetNeedsLayoutToLayerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger willSendSetNeedsLayoutToView:becauseOfChangeInVariable:inLayoutEngine:];
-[_UIViewLayoutFeedbackLoopDebugger willSendSetPosition:toLayerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger willSendViewDidLayoutSubviewsToViewControllerOfView:];
-[_UIViewLayoutFeedbackLoopDebugger willSendViewWillLayoutSubviewsToViewControllerOfView:];
```
